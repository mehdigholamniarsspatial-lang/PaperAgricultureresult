"""Export the supplementary dataset: every manuscript figure as a numbered 300-dpi PNG and the data behind every figure
and table as CSV.

Figure and table numbers are read from paper/paper_src.md in document order (the same order build_paper.py uses), so the
files always match the manuscript. Figure data come from dashboard/data/results.json; table data are the manuscript tables.

Usage:  python tools/export_supplementary.py
"""
import csv
import importlib.util
import json
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "paper" / "paper_src.md"
FIG_DIR = ROOT / "paper" / "figures"
RES = ROOT / "dashboard" / "data" / "results.json"
OUT_FIG = ROOT / "supplementary_figures"
OUT_DAT = ROOT / "supplementary_data"

D = json.loads(RES.read_text(encoding="utf-8"))
K = D["key"]
YEARS = D["panel"]["years"]
COLS = D["panel"]["cols"]

SLUG = {  # figure key in paper_src.md -> file slug
    "emissions": "crf3_emissions_by_category", "drivers": "emissions_and_activity_drivers", "regional": "regional_exposure_and_dairy_herd",
    "scores": "policy_scores_by_instrument", "framework": "conceptual_framework", "indices": "policy_indices_M_P_S_G",
    "breaks": "bai_perron_segmented_trend", "lmdiphase": "lmdi_by_policy_phase", "lmdiannual": "lmdi_annual_effects",
    "ardl": "ardl_long_run_multipliers", "cf": "counterfactual_paths", "robust": "robustness_grid", "power": "power_curves",
    "its": "interrupted_time_series", "event": "regional_event_study", "mech": "lmdi_policy_link", "ceiling": "ceiling_2030_scenarios",
    "gwp": "methane_gwp100_vs_gwpstar",
}


def panel_rows(cols):
    return [dict(Year=y, **{c: COLS[c][i] for c in cols}) for i, y in enumerate(YEARS)]


def score_rows():
    out = []
    for key, pset in (("scoreP", "P"), ("scoreG", "G"), ("scoreM", "M")):
        sc = D[key]
        for pid, vals in sc["cols"].items():
            for y, v in zip(sc["years"], vals):
                out.append({"policy_set": pset, "policy_id": pid, "Year": y, "score": v})
    return out


def fig_data(key):
    """Return {suffix: rows} with the data plotted in each figure."""
    if key == "emissions":
        return {"": panel_rows(["enteric_kt", "soils_kt", "manure_kt", "liming_kt", "urea_kt", "crf3_kt"]),
                "_ceiling_path": [{"Year": 2024, "kt_co2e": K["ceiling_2030"]["crf3_2024"]}, {"Year": 2030, "kt_co2e": K["ceiling_2030"]["target_2030"]}]}
    if key == "drivers":
        return {"": panel_rows(["crf3_kt", "dairy_cows", "other_cattle", "sheep_total", "milk_per_cow_l", "n_fert_kt"])}
    if key == "regional":
        return {"_exposure": [{"region": r, "dairy_share_of_cows_2010_2014_pct": v} for r, v in K["regional_exposure_pct"].items()],
                "_dairy_cows": [{"region": r["unit"], "Year": r["Year"], "dairy_cows_thousand": r["dairy_cows"]} for r in D["regional"]]}
    if key == "scores":
        return {"": score_rows()}
    if key == "framework":
        return {}
    if key == "indices":
        return {"": panel_rows(["M", "P", "S", "G", "M_mandatory", "M_incentive", "M_voluntary"])}
    if key == "breaks":
        rows = panel_rows(["crf3_kt"])
        for r, f in zip(rows, D["fit_m"]):
            r["segmented_trend_fit_kt"] = f
        return {"": rows, "_break_selection": D["bp"]}
    if key == "lmdiphase":
        return {"": D["lmdi_phase"]}
    if key == "lmdiannual":
        return {"": D["lmdi_annual"]}
    if key == "ardl":
        return {"_long_run": D["long_run"], "_bootstrap_draws": D["boot_draws"]}
    if key == "cf":
        return {"_paths": D["paths"], "_bootstrap_draws": D["boot_draws"]}
    if key == "robust":
        return {"": D["robust"]}
    if key == "power":
        return {"": D["power"]}
    if key == "its":
        return {"": D["its"]}
    if key == "event":
        return {"": D["event"]}
    if key == "mech":
        return {"": D["mech"]}
    if key == "ceiling":
        return {"": D["ceiling"]}
    if key == "gwp":
        return {"": D["gwpstar"]}
    raise KeyError(key)


def write_csv(path, rows):
    if not rows:
        return
    keys = []
    for r in rows:
        for k in r:
            if k not in keys:
                keys.append(k)
    with open(path, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=keys)
        w.writeheader()
        for r in rows:
            w.writerow({k: ("" if v is None else v) for k, v in r.items()})


MD_FMT = re.compile(r"\*\*|\*|~|\^|\\")


def md_table_rows(lines):
    rows = []
    for ln in lines:
        if re.match(r"^\|[:\- |]+\|$", ln):
            continue
        cells = [MD_FMT.sub("", c).strip() for c in ln.strip().strip("|").split("|")]
        rows.append(cells)
    return rows


def dictionary_table():
    spec = importlib.util.spec_from_file_location("build_paper", ROOT / "paper" / "build_paper.py")
    bp = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(bp)
    return bp.dictionary_table()


def slugify(caption):
    s = re.sub(r"[^a-z0-9]+", "_", caption.lower()).strip("_")
    return s[:60].rstrip("_")


def main():
    for d in (OUT_FIG, OUT_DAT):
        if d.exists():
            shutil.rmtree(d)
        d.mkdir()
    text = SRC.read_text(encoding="utf-8").replace("TABLEINCLUDE dictionary", dictionary_table())
    lines = text.split("\n")

    fig_index, tab_index = [], []
    n_fig = n_tab = 0
    for i, ln in enumerate(lines):
        m = re.match(r"^FIG (\w+) \| (.+?) \| (\S+) \| ([\d.]+)$", ln)
        if m:
            n_fig += 1
            fig_index.append((f"{n_fig:02d}", m.group(1), m.group(2), m.group(3)))
            continue
        m = re.match(r"^TAB (\w+)(?:=(\w+))? \| (.+)$", ln)
        if m:
            num = m.group(2)
            if not num:
                n_tab += 1
                num = f"{n_tab:02d}"
            j = i + 1
            while j < len(lines) and not lines[j].startswith("|"):
                j += 1
            body = []
            while j < len(lines) and lines[j].startswith("|"):
                body.append(lines[j]); j += 1
            tab_index.append((num, m.group(1), m.group(3), md_table_rows(body)))

    readme_f = ["# Supplementary figures", "", "All figures are 300-dpi PNG files regenerated from `dashboard/data/results.json` by `paper/make_figures.py` "
                "(Okabe–Ito colour-blind-safe palette, Arial). Numbers follow the manuscript.", "", "| File | Manuscript figure | Caption |", "|---|---|---|"]
    readme_d = ["# Supplementary data", "", "CSV files with the data behind every manuscript figure (`FigNN_*`) and table (`TabNN_*`). Figure data are taken "
                "directly from `dashboard/data/results.json`; table files reproduce the manuscript tables. Encoding UTF-8 with BOM; missing values are blank.",
                "", "| File | Belongs to | Content |", "|---|---|---|"]
    for num, key, cap, fn in fig_index:
        slug = SLUG.get(key, slugify(cap))
        dst = OUT_FIG / f"Fig{num}_{slug}.png"
        shutil.copyfile(FIG_DIR / fn, dst)
        readme_f.append(f"| `{dst.name}` | Figure {int(num)} | {cap} |")
        data = fig_data(key)
        if not data:
            readme_d.append(f"| – | Figure {int(num)} | Schematic; no underlying data |")
        for suf, rows in data.items():
            p = OUT_DAT / f"Fig{num}_{slug}{suf}.csv"
            write_csv(p, rows)
            readme_d.append(f"| `{p.name}` | Figure {int(num)} | {cap}{' (' + suf.strip('_').replace('_', ' ') + ')' if suf else ''} |")
    for num, key, cap, rows in tab_index:
        p = OUT_DAT / f"Tab{num}_{slugify(cap)}.csv"
        with open(p, "w", newline="", encoding="utf-8-sig") as f:
            csv.writer(f).writerows(rows)
        readme_d.append(f"| `{p.name}` | Table {num} | {cap} |")
    meta = K["meta"]
    stamp = f"\n\nAnalysis run: {meta['run_utc']} (seed {meta['seed']}, {meta['n_boot']} bootstrap draws); revised policy codebook of 29 October 2026.\n"
    (OUT_FIG / "README.md").write_text("\n".join(readme_f) + stamp, encoding="utf-8")
    (OUT_DAT / "README.md").write_text("\n".join(readme_d) + stamp, encoding="utf-8")
    print(f"{len(fig_index)} figures -> {OUT_FIG}")
    print(f"{sum(len(fig_data(k)) for _, k, _, _ in fig_index)} figure CSVs + {len(tab_index)} table CSVs -> {OUT_DAT}")


if __name__ == "__main__":
    main()
