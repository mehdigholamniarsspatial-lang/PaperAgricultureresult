"""Download the CSO regional livestock tables and the matching NUTS boundaries into dashboard/data/cso_regions.json.

    python tools/build_cso_regions.py

Needs internet access and pandas at build time only; the dashboard itself reads the JSON.
Sources: CSO PxStat (AAA01, AAA07, AAA09) and Eurostat GISCO NUTS boundaries (1:1 million, EPSG:4326).
"""
import io
import json
import urllib.request
from pathlib import Path

import pandas as pd

OUT = Path(__file__).resolve().parents[1] / "dashboard" / "data" / "cso_regions.json"
CSO = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/{}/CSV/1.0/en"
GISCO = "https://gisco-services.ec.europa.eu/distribution/v2/nuts/geojson/NUTS_RG_01M_{}_4326_LEVL_{}.geojson"

# CSO region code -> NUTS polygons that make it up (CSO merges Dublin and Mid-East into one unit).
GEOMS = {
    "nuts2003": ((2003, 3), {"IE11": ["IE011"], "IE12": ["IE012"], "IE13": ["IE013"], "5000": ["IE021", "IE022"],
                             "IE23": ["IE023"], "IE24": ["IE024"], "IE25": ["IE025"]}),
    "nuts2016": ((2016, 3), {"IE041": ["IE041"], "IE042": ["IE042"], "IE051": ["IE051"], "IE052": ["IE052"],
                             "IE053": ["IE053"], "IE06106": ["IE061", "IE062"], "IE063": ["IE063"]}),
    "nuts2016_l2": ((2016, 2), {"IE04": ["IE04"], "IE05": ["IE05"], "IE06": ["IE06"]}),
    # Study's constant-boundary units (sum to the State in every year, across the 2004/05 and 2014/15 table switches).
    "constant": ((2016, 3), {"West": ["IE042"], "Midland": ["IE063"], "South-West": ["IE053"],
                             "Border + Dublin/Mid-East": ["IE041", "IE061", "IE062"],
                             "Mid-West + South-East": ["IE051", "IE052"]}),
}

TABLES = {
    "AAA01": dict(title="AAA01 · Livestock in June, 1991–2004", geo="nuts2003", boundary="NUTS 2003 regions"),
    "AAA07": dict(title="AAA07 · Livestock in June, 2005–2014", geo="nuts2003", boundary="NUTS 2003 regions"),
    "AAA09": dict(title="AAA09 · Livestock in June, 2015 onward", geo="nuts2016", geo_l2="nuts2016_l2",
                  boundary="NUTS 2016 regions"),
}


def get(url):
    with urllib.request.urlopen(url, timeout=300) as r:
        return r.read()


def thin(ring, nd=3):
    """Round to ~100 m and drop repeated points: plenty for a national choropleth, ~20x smaller."""
    out = []
    for x, y in ring:
        p = [round(x, nd), round(y, nd)]
        if not out or p != out[-1]:
            out.append(p)
    return out if len(out) >= 4 else None


def polygons(geom):
    polys = geom["coordinates"] if geom["type"] == "MultiPolygon" else [geom["coordinates"]]
    out = []
    for poly in polys:
        rings = [r for r in (thin(r) for r in poly) if r]
        if rings:
            out.append(rings)
    return out


def build_geo():
    cache, geo = {}, {}
    for key, ((year, level), units) in GEOMS.items():
        if (year, level) not in cache:
            fc = json.loads(get(GISCO.format(year, level)))
            cache[(year, level)] = {f["properties"]["NUTS_ID"]: f for f in fc["features"] if f["properties"]["CNTR_CODE"] == "IE"}
        nuts = cache[(year, level)]
        feats = []
        for code, parts in units.items():
            coords = [p for n in parts for p in polygons(nuts[n]["geometry"])]
            feats.append({"type": "Feature", "id": code, "properties": {"code": code, "nuts": parts},
                          "geometry": {"type": "MultiPolygon", "coordinates": coords}})
        geo[key] = {"type": "FeatureCollection", "features": feats}
    return geo


def build_table(stem):
    d = pd.read_csv(io.BytesIO(get(CSO.format(stem))), encoding="utf-8-sig", dtype=str)
    rcode = next(c for c in d.columns if c.startswith("C02196"))
    d["VALUE"] = pd.to_numeric(d["VALUE"], errors="coerce")
    d["Year"] = d["Year"].astype(int)
    years = sorted(d["Year"].unique().tolist())
    stats = d["Type of Animal"].drop_duplicates().tolist()
    regions = d[[rcode, "Region"]].drop_duplicates()
    values = {}
    for (stat, code), g in d.groupby(["Type of Animal", rcode], sort=False):
        s = g.set_index("Year")["VALUE"].reindex(years)
        values.setdefault(stat, {})[code] = [None if pd.isna(v) else float(v) for v in s]
    return dict(**TABLES[stem], source=CSO.format(stem), unit=d["UNIT"].iloc[0], years=years, stats=stats,
                regions={c: n for c, n in zip(regions[rcode], regions["Region"])}, values=values)


def main():
    out = {"geo": build_geo(), "tables": {stem: build_table(stem) for stem in TABLES}}
    OUT.write_text(json.dumps(out, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    print(f"wrote {OUT} ({OUT.stat().st_size / 1e6:.2f} MB)")


if __name__ == "__main__":
    main()
