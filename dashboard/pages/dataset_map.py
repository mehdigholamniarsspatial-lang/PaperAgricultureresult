"""Step 3 – 'Regional map' tab: CSO datasets that carry a region code, drawn on a map of Ireland.

Data and boundaries come from data/cso_regions.json, written by tools/build_cso_regions.py.
"""
import csv
import io
import json
import math
from pathlib import Path

import plotly.graph_objects as go
from dash import html, dcc, Input, Output, State, ctx, no_update

from ..components import card, callout, table, num
from ..data_store import DATA
from ..theme import base_layout, empty_fig, BLUE, INK, INK2, MUTED, GRAPH_CONFIG, FONT

HERE = Path(__file__).resolve().parents[1] / "data"
CSO = json.loads((HERE / "cso_regions.json").read_text(encoding="utf-8"))
GEO = CSO["geo"]
STATE = "-"

PANEL_VARS = {"dairy_cows": ("Dairy cows", "000 Head"), "other_cows": ("Other cows", "000 Head"),
              "cattle_total": ("Total cattle", "000 Head"), "other_cattle": ("Non-dairy cattle", "000 Head"),
              "sheep_total": ("Total sheep", "000 Head"), "livestock_units": ("Livestock units", "000 LU"),
              "emis_imputed_kt": ("Imputed livestock CH₄ emissions", "kt CO₂e"), "dairy_share": ("Dairy share of all cows", "%")}
SEQ = [[0, "#eef4fc"], [0.5, "#78a8e6"], [1, "#16447f"]]


def _panel():
    """The study's constant-boundary regional panel (results.json) in the same shape as a CSO table."""
    rows = DATA["regional"]
    years = sorted({r["Year"] for r in rows})
    regions = list(dict.fromkeys(r["unit"] for r in rows))
    values = {}
    for k in PANEL_VARS:
        for reg in regions:
            by = {}
            for r in rows:
                if r["unit"] == reg:
                    v = (100 * r["dairy_cows"] / (r["dairy_cows"] + r["other_cows"])) if k == "dairy_share" else r.get(k)
                    by[r["Year"]] = v
            values.setdefault(PANEL_VARS[k][0], {})[reg] = [by.get(y) for y in years]
    return dict(title="Study panel · 5 constant-boundary regions, 1991–2024", geo="constant",
                boundary="constant-boundary units (NUTS 2016 outlines)", source="data/results.json (regional)",
                years=years, stats=[v[0] for v in PANEL_VARS.values()], regions={r: r for r in regions}, values=values,
                units={v[0]: v[1] for v in PANEL_VARS.values()})


DATASETS = {"panel": _panel(), **CSO["tables"]}


def _area_km2(geom):
    """Approximate area from lon/lat rings (local equirectangular projection, adequate at Ireland's scale)."""
    tot = 0.0
    for poly in geom["coordinates"]:
        for i, ring in enumerate(poly):
            lat0 = math.radians(sum(p[1] for p in ring) / len(ring))
            xs = [p[0] * 111.32 * math.cos(lat0) for p in ring]
            ys = [p[1] * 110.57 for p in ring]
            a = abs(sum(xs[j] * ys[j + 1] - xs[j + 1] * ys[j] for j in range(len(ring) - 1))) / 2
            tot += a if i == 0 else -a
    return tot


AREA = {key: {f["id"]: _area_km2(f["geometry"]) for f in fc["features"]} for key, fc in GEO.items()}


def geo_key(ds, level):
    d = DATASETS[ds]
    return d["geo_l2"] if level == "l2" and "geo_l2" in d else d["geo"]


def unit_of(ds, stat):
    d = DATASETS[ds]
    return d.get("units", {}).get(stat, d.get("unit", ""))


def year_values(ds, stat, level, year, measure):
    """[(code, name, value)] for every mapped region in one year, plus the State total used for shares."""
    d = DATASETS[ds]
    gk = geo_key(ds, level)
    codes = [f["id"] for f in GEO[gk]["features"]]
    i = d["years"].index(year)
    vals = d["values"][stat]
    raw = {c: vals.get(c, [None] * len(d["years"]))[i] for c in codes}
    state = vals[STATE][i] if STATE in vals else (sum(v for v in raw.values() if v is not None) or None)
    out = []
    for c in codes:
        v = raw[c]
        if v is not None and measure == "share":
            v = 100 * v / state if state else None
        elif v is not None and measure == "density":
            v = v * (1000 if unit_of(ds, stat).startswith("000") else 1) / AREA[gk][c]
        out.append((c, d["regions"][c], v))
    return out, state


def measure_label(ds, stat, measure):
    u = unit_of(ds, stat)
    if measure == "share":
        return "% of State"
    if measure == "density":
        base = {"000 Head": "head", "000 LU": "LU"}.get(u, u)
        return f"{base} per km²"
    return u


def map_fig(ds, stat, level, year, measure, selected):
    rows, _ = year_values(ds, stat, level, year, measure)
    if all(v is None for _, _, v in rows):
        return empty_fig(f"No data for {stat} in {year}", height=520)
    codes, names, z = zip(*rows)
    unit = measure_label(ds, stat, measure)
    fc = GEO[geo_key(ds, level)]
    fig = go.Figure(go.Choroplethmap(
        geojson=fc, locations=list(codes), z=[v if v is not None else float("nan") for v in z], customdata=list(names),
        colorscale=SEQ, marker=dict(line=dict(color="white", width=1.2), opacity=0.88),
        colorbar=dict(title=dict(text=unit, side="right", font=dict(size=12)), thickness=12, len=0.75, outlinewidth=0),
        hovertemplate="<b>%{customdata}</b><br>" + f"{stat}, {year}: " + "%{z:,.1f} " + unit + "<extra></extra>"))
    if selected in codes:
        sel = {"type": "FeatureCollection", "features": [f for f in fc["features"] if f["id"] == selected]}
        fig.add_trace(go.Choroplethmap(geojson=sel, locations=[selected], z=[1], colorscale=[[0, "rgba(0,0,0,0)"], [1, "rgba(0,0,0,0)"]],
                                       showscale=False, marker=dict(line=dict(color=INK, width=3)), hoverinfo="skip"))
    fig.update_layout(map=dict(style="carto-positron", center=dict(lat=53.45, lon=-8.1), zoom=5.35),
                      height=560, margin=dict(l=0, r=0, t=0, b=0), font=dict(family=FONT, color=INK2),
                      hoverlabel=dict(bgcolor="white", font=dict(family=FONT, color=INK, size=12)), uirevision=f"{ds}-{level}")
    return fig


def rank_fig(ds, stat, level, year, measure, selected):
    rows, _ = year_values(ds, stat, level, year, measure)
    rows = sorted([r for r in rows if r[2] is not None], key=lambda r: r[2])
    if not rows:
        return empty_fig("No data", height=300)
    fig = go.Figure(go.Bar(x=[r[2] for r in rows], y=[r[1] for r in rows], orientation="h", customdata=[r[0] for r in rows],
                           marker=dict(color=[INK if r[0] == selected else BLUE for r in rows], cornerradius=4),
                           text=[f"{r[2]:,.1f}" for r in rows], textposition="outside", cliponaxis=False,
                           hovertemplate="%{y}: <b>%{x:,.1f}</b><extra></extra>"))
    base_layout(fig, height=60 + 38 * len(rows), legend=False, hover="closest", xtitle=measure_label(ds, stat, measure))
    fig.update_layout(margin=dict(l=8, r=56, t=10, b=44))
    fig.update_yaxes(gridcolor="rgba(0,0,0,0)", automargin=True)
    return fig


def trend_fig(ds, stat, level, measure, selected, year):
    d = DATASETS[ds]
    if selected not in [f["id"] for f in GEO[geo_key(ds, level)]["features"]]:
        return empty_fig("Click a region on the map to see its trend", height=300)
    ys, vs = [], []
    for y in d["years"]:
        rows, _ = year_values(ds, stat, level, y, measure)
        v = next(r[2] for r in rows if r[0] == selected)
        if v is not None:
            ys.append(y); vs.append(v)
    fig = go.Figure(go.Scatter(x=ys, y=vs, mode="lines+markers", line=dict(color=BLUE, width=2.4), marker=dict(size=5),
                               hovertemplate="%{x}: <b>%{y:,.1f}</b><extra></extra>"))
    if year in ys:
        fig.add_trace(go.Scatter(x=[year], y=[vs[ys.index(year)]], mode="markers", marker=dict(color=INK, size=11), hoverinfo="skip"))
    base_layout(fig, height=300, legend=False, hover="x", title=d["regions"][selected], ytitle=measure_label(ds, stat, measure))
    return fig


def info_line(ds):
    d = DATASETS[ds]
    n = len([f for f in GEO[d["geo"]]["features"]])
    return [html.B(d["title"]), f" · {n} regions on {d['boundary']} · {d['years'][0]}–{d['years'][-1]} · ",
            html.A("source", href=d["source"], target="_blank") if d["source"].startswith("http") else d["source"]]


def tab_map():
    first = "AAA09"
    d = DATASETS[first]
    return html.Div([
        callout("plain", "Regional CSO data on a map",
                "Pick any dataset that carries a CSO region code. The map colours each region by the selected statistic and year; "
                "click a region to see its trend. CSO changed its regional breakdown twice, so each table is drawn on the boundaries "
                "it was published for, and the study's five constant-boundary units bridge the breaks."),
        card(
            html.Div(className="control-grid", children=[
                html.Div([html.Label("Dataset", className="ctl-label"),
                          dcc.Dropdown(id="mp-ds", value=first, clearable=False,
                                       options=[{"label": v["title"], "value": k} for k, v in DATASETS.items()])], className="span-2"),
                html.Div([html.Label("Statistic", className="ctl-label"),
                          dcc.Dropdown(id="mp-stat", value="Dairy cows", clearable=False,
                                       options=[{"label": s, "value": s} for s in d["stats"]])], className="span-2"),
                html.Div([html.Label("Year", className="ctl-label"),
                          dcc.Slider(id="mp-year", min=d["years"][0], max=d["years"][-1], step=1, value=d["years"][-1],
                                     marks={y: str(y) for y in d["years"][::2]}, tooltip={"placement": "bottom"})], className="span-2"),
                html.Div([html.Label("Measure", className="ctl-label"),
                          dcc.RadioItems(id="mp-measure", value="level", className="seg", inline=True,
                                         options=[{"label": "Level", "value": "level"}, {"label": "% of State", "value": "share"},
                                                  {"label": "Per km²", "value": "density"}])]),
                html.Div([html.Label("Regional level", className="ctl-label"),
                          dcc.RadioItems(id="mp-level", value="l3", className="seg", inline=True,
                                         options=[{"label": "NUTS 3", "value": "l3"}, {"label": "NUTS 2", "value": "l2"}])]),
            ]),
            html.P(id="mp-info", className="fig-note"),
            dcc.Store(id="mp-sel", data="IE053"),
            html.Div(className="map-grid", children=[
                dcc.Graph(id="mp-map", config=GRAPH_CONFIG, className="graph", style={"height": "560px"}),
                html.Div([dcc.Graph(id="mp-rank", config=GRAPH_CONFIG, className="graph", style={"height": "326px"}),
                          dcc.Graph(id="mp-trend", config=GRAPH_CONFIG, className="graph", style={"height": "300px"})])]),
            html.P("Per km² uses approximate region areas from the Eurostat GISCO 1:1 million boundaries. "
                   "CSO publishes Dublin and Mid-East as one unit, so they are drawn together.",
                   className="fig-note"),
        ),
        card(html.Div(className="control-row", children=[
                html.H3("Values for the selected year"),
                html.Button("⬇ This dataset & statistic (CSV)", id="mp-dl-btn", className="btn")]),
             dcc.Download(id="mp-dl"),
             html.Div(id="mp-table")),
    ])


def register_callbacks(app):
    @app.callback(Output("mp-stat", "options"), Output("mp-stat", "value"),
                  Output("mp-year", "min"), Output("mp-year", "max"), Output("mp-year", "marks"), Output("mp-year", "value"),
                  Output("mp-level", "options"), Output("mp-level", "value"), Output("mp-info", "children"),
                  Input("mp-ds", "value"), State("mp-stat", "value"), State("mp-year", "value"))
    def _ds(ds, stat, year):
        d = DATASETS[ds]
        ys = d["years"]
        stat = stat if stat in d["stats"] else next((s for s in ("Dairy cows", "Total cattle") if s in d["stats"]), d["stats"][0])
        year = year if year in ys else ys[-1]
        has_l2 = "geo_l2" in d
        levels = [{"label": "NUTS 3", "value": "l3"}, {"label": "NUTS 2", "value": "l2", "disabled": not has_l2}]
        return ([{"label": s, "value": s} for s in d["stats"]], stat, ys[0], ys[-1], {y: str(y) for y in ys[::2]}, year,
                levels, "l3", info_line(ds))

    @app.callback(Output("mp-sel", "data"), Input("mp-map", "clickData"), Input("mp-rank", "clickData"), prevent_initial_call=True)
    def _pick(map_cd, rank_cd):
        cd = map_cd if ctx.triggered_id == "mp-map" else rank_cd
        if not cd:
            return no_update
        p = cd["points"][0]
        return p.get("location") or p.get("customdata")

    @app.callback(Output("mp-map", "figure"), Output("mp-rank", "figure"), Output("mp-rank", "style"), Output("mp-trend", "figure"),
                  Output("mp-table", "children"),
                  Input("mp-ds", "value"), Input("mp-stat", "value"), Input("mp-level", "value"), Input("mp-year", "value"),
                  Input("mp-measure", "value"), Input("mp-sel", "data"))
    def _draw(ds, stat, level, year, measure, sel):
        d = DATASETS[ds]
        if stat not in d["stats"] or year not in d["years"]:
            return no_update, no_update, no_update, no_update, no_update
        if measure != "level" and unit_of(ds, stat) == "%":
            measure = "level"
        rows, state = year_values(ds, stat, level, year, "level")
        if sel not in [c for c, _, _ in rows]:  # switched to other boundaries: start from the largest region
            sel = max(rows, key=lambda r: r[2] if r[2] is not None else -math.inf)[0]
        share = dict((c, v) for c, _, v in year_values(ds, stat, level, year, "share")[0])
        dens = dict((c, v) for c, _, v in year_values(ds, stat, level, year, "density")[0])
        recs = [{"code": c, "region": n, "value": v, "share": share[c], "density": dens[c]} for c, n, v in rows]
        unit = unit_of(ds, stat)
        tbl = table(recs, [("code", "CSO code"), ("region", "Region"), ("value", f"{stat} ({unit})", num(1)),
                           ("share", "% of State", num(1)), ("density", measure_label(ds, stat, "density"), num(1))],
                    page_size=12)
        # Graphs fill their container, so the bar chart's height (one row per region) is set on the component too.
        return (map_fig(ds, stat, level, year, measure, sel), rank_fig(ds, stat, level, year, measure, sel),
                {"height": f"{60 + 38 * len(rows)}px"},
                trend_fig(ds, stat, level, measure, sel, year), tbl)

    @app.callback(Output("mp-dl", "data"), Input("mp-dl-btn", "n_clicks"),
                  State("mp-ds", "value"), State("mp-stat", "value"), prevent_initial_call=True)
    def _dl(n, ds, stat):
        d = DATASETS[ds]
        buf = io.StringIO()
        w = csv.writer(buf)
        w.writerow(["dataset", "statistic", "unit", "region_code", "region", "year", "value"])
        for code, vals in d["values"][stat].items():
            for y, v in zip(d["years"], vals):
                w.writerow([ds, stat, unit_of(ds, stat), code, d["regions"].get(code, code), y, v])
        return dict(content=buf.getvalue(), filename=f"{ds}_{stat.replace(' ', '_').replace(':', '')}_by_region.csv")
