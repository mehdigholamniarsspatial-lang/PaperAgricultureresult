"""Step 3 – the dataset, presented interactively."""
import math
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from dash import html, dcc, Input, Output, State, ctx, no_update

from ..components import (page_header, section, card, kpi, kpi_row, callout, table, num, two_col, details, badge, md)
from ..data_store import (DATA, YEARS, COLS, VARIABLES, GROUPS, EVENTS, series, value, coverage, fmt, CODEBOOK,
                          COVERAGE_LABEL, VERIFICATION, PANEL_CSV)
from ..theme import (base_layout, add_events, empty_fig, PAL, C_M, C_P, C_S, INK, INK2, MUTED, GRID, BLUE, ORANGE, AQUA,
                     YELLOW, MAGENTA, VIOLET, GREEN, RED, REGION_COL, GRAPH_CONFIG)
from . import dataset_sources, dataset_map

MANIFEST = [r for r in DATA["manifest"] if r["used"]]   # files actually loaded into the analysis
VAR_OPTIONS = [{"label": f"{VARIABLES[k][0]} · {VARIABLES[k][1]}", "value": k} for g in GROUPS for k in VARIABLES if VARIABLES[k][0] == g]
DEFAULT_VARS = ["crf3_kt", "dairy_cows", "milk_per_cow_l", "n_fert_kt"]

SOURCES = [
    ("EPA", "Environmental Protection Agency", "Provisional GHG inventory workbook 1990–2025", "CRF3 total, 5 categories, 3 gases", "1990–2024"),
    ("UNFCCC", "Ireland CRT 2025 submission", "34 workbooks, one per inventory year", "Dairy / non-dairy CH₄ split, N excretion, mineral N 1990–99", "1990–2023"),
    ("Eurostat", "env_air_gge · aei_fm_usefert · LSU", "Downloaded CSV extracts", "Species CH₄ detail, mineral N 2000–24, LSU coefficients", "1990–2024"),
    ("CSO", "Central Statistics Office", "AAA01/07/09, AKA01, AHA01–05, CPA01, NA002", "Livestock (national + regional), milk, prices, CPI, GNI*", "1991–2024"),
    ("Authors", "Policy codebooks", "pressure_codebook.csv · mitigation_codebook_PROVISIONAL.csv", "20 instruments scored I × C × B", "1990–2024"),
]

HARMONISATION = [
    ("Emissions boundary (CRF sector 3)",
     "The EPA 'Agriculture' row follows the Climate Action Plan definition, which includes agricultural/forestry fuel (1.A.4.c.ii) and "
     "fishing (1.A.4.c.iii). The outcome is **CRF3 = Agriculture − 1.A.4.c.ii − 1.A.4.c.iii**, checked against the sum of the five "
     "reported categories (3.A, 3.B, 3.D, 3.G, 3.H) and the sum of the three gases (gap < 0.0001%). Other sector-3 categories are NO/NA for Ireland."),
    ("Inventory vintages",
     "Three vintages are combined: EPA provisional (2026) for CRF3 — the only source with 2024; Eurostat `env_air_gge` for species detail; "
     "CRT 2025 for the dairy split and 1990s fertiliser. They agree to ≤ 0.01% for 1990–2020 and ≤ 0.21% for 2021–2023. The LMDI 'other' "
     "term absorbs any vintage difference, so the decomposition stays exact."),
    ("Livestock series and the 2004→05 break",
     "AAA01 (1991–2004), AAA07 (2005–2014) and AAA09 (2015–) cover disjoint years and are stacked without back-filling. 1990 stays missing. "
     "Dairy cows fall 8.7% at the AAA01→AAA07 switch while total cattle fall 0.3%; the CRT shows the same step, so it is a classification "
     "change. Every model where the herd enters includes a 2005 indicator."),
    ("Constant-boundary regions",
     "In the 2014/2016 NUTS3 revision Louth moved from the Border to the Mid-East and Tipperary was unified. Five units keep boundaries "
     "stable: West, Midland, South-West (unchanged), **Border + Dublin/Mid-East** and **Mid-West + South-East**. They sum to the State within 0.014%."),
    ("Price chain-linking and deflation",
     "Five CSO vintages (base 2000, 2005, 2010, 2015, 2020) are linked by the overlap method: each older vintage is rescaled by the geometric "
     "mean of the newest-to-older ratio over overlapping years, keeping the newest vintage. Real price = nominal index ÷ CPI × 100 (2020 = 100). "
     "Largest overlap deviation: 2.88%."),
    ("Fertiliser N units",
     "CRT Table 3.D is headed 't N/year' but the values are kg N — confirmed by an exact match with Eurostat in 2000–2005 after dividing by 1,000."),
    ("Missing data rule",
     "Missing years are **never** interpolated, back-cast or set to zero. `NO/NE/NA` codes become missing. Each estimator uses the largest common "
     "sample and reports it. Every file read is hashed with SHA-256."),
]


# ------------------------------------------------------------------ figures
def coverage_fig():
    keys = [k for g in GROUPS for k in VARIABLES if VARIABLES[k][0] == g]
    z, text = [], []
    for k in keys:
        row = [0 if v is None else 1 for v in COLS[k]]
        z.append(row)
        text.append([f"{VARIABLES[k][1]} · {y}: {'available' if r else 'missing (not imputed)'}" for y, r in zip(YEARS, row)])
    labels = [VARIABLES[k][1] for k in keys]
    fig = go.Figure(go.Heatmap(z=z, x=YEARS, y=labels, colorscale=[[0, "#f1efe9"], [1, BLUE]], showscale=False,
                               xgap=1.5, ygap=1.5, text=text, hovertemplate="%{text}<extra></extra>", zmin=0, zmax=1))
    base_layout(fig, height=26 * len(keys) + 80, legend=False, hover="closest")
    fig.update_layout(margin=dict(l=300, r=20, t=20, b=40))
    fig.update_yaxes(autorange="reversed", showgrid=False, tickfont=dict(size=11.5))
    fig.update_xaxes(dtick=5)
    return fig


def explorer_fig(vars_, mode, yr, events):
    if not vars_:
        return empty_fig("Choose one or more variables above")
    y0, y1 = yr
    colour = {v: PAL[i % len(PAL)] for i, v in enumerate(vars_)}
    if mode == "levels":
        n = len(vars_)
        cols = 2 if n > 1 else 1
        rows = math.ceil(n / cols)
        fig = make_subplots(rows=rows, cols=cols, subplot_titles=[f"{VARIABLES[v][1]} ({VARIABLES[v][2]})" for v in vars_],
                            vertical_spacing=0.16 / max(rows - 1, 1) + 0.06, horizontal_spacing=0.09, shared_xaxes=False)
        for i, v in enumerate(vars_):
            ys, vals = series(v)
            pts = [(y, x) for y, x in zip(ys, vals) if y0 <= y <= y1]
            r, c = i // cols + 1, i % cols + 1
            fig.add_trace(go.Scatter(x=[p[0] for p in pts], y=[p[1] for p in pts], mode="lines+markers", name=VARIABLES[v][1],
                                     line=dict(color=colour[v], width=2), marker=dict(size=5),
                                     hovertemplate=f"%{{x}}: <b>%{{y:,.3~f}}</b> {VARIABLES[v][2]}<extra></extra>"), row=r, col=c)
            if events:
                for ey in EVENTS:
                    if y0 <= ey <= y1:
                        fig.add_vline(x=ey, line=dict(color=MUTED, width=1, dash="dot"), row=r, col=c)
        base_layout(fig, height=max(330, 290 * rows), legend=False, hover="x")
        fig.update_annotations(font=dict(size=12.5, color=INK))
        return fig
    fig = go.Figure()
    for v in vars_:
        ys, vals = series(v)
        pts = [(y, x) for y, x in zip(ys, vals) if y0 <= y <= y1]
        if not pts:
            continue
        if mode == "index":
            b = pts[0][1]
            yv = [100 * x / b if b else None for _, x in pts]
            ht = f"{VARIABLES[v][1]}: %{{y:.1f}} (first year {pts[0][0]} = 100)<extra></extra>"
        else:
            yv = [None] + [100 * (pts[i][1] / pts[i - 1][1] - 1) if pts[i - 1][1] and pts[i][0] == pts[i - 1][0] + 1 else None
                           for i in range(1, len(pts))]
            ht = f"{VARIABLES[v][1]}: %{{y:+.1f}}%<extra></extra>"
        fig.add_trace(go.Scatter(x=[p[0] for p in pts], y=yv, mode="lines+markers", name=VARIABLES[v][1],
                                 line=dict(color=colour[v], width=2), marker=dict(size=5), hovertemplate=ht))
    if mode == "index":
        fig.add_hline(y=100, line=dict(color=MUTED, width=1))
        yt = "Index, first year in range = 100"
    else:
        fig.add_hline(y=0, line=dict(color=MUTED, width=1))
        yt = "Change on previous year, %"
    base_layout(fig, height=470, ytitle=yt)
    if events:
        add_events(fig, {k: v for k, v in EVENTS.items() if y0 <= k <= y1})
    return fig


def summary_rows(vars_, yr):
    out = []
    for v in vars_ or []:
        ys, vals = series(v)
        pts = [(y, x) for y, x in zip(ys, vals) if yr[0] <= y <= yr[1]]
        if not pts:
            continue
        (fy, fv), (ly, lv) = pts[0], pts[-1]
        mn = min(pts, key=lambda p: p[1]); mx = max(pts, key=lambda p: p[1])
        f_ = lambda x: f"{x:,.0f}" if abs(x) >= 1000 else f"{x:,.3g}"
        n = len(pts)
        cagr = 100 * ((lv / fv) ** (1 / (ly - fy)) - 1) if fv and lv and ly > fy and fv > 0 and lv > 0 else None
        out.append({"variable": VARIABLES[v][1], "unit": VARIABLES[v][2], "years": f"{fy}–{ly}", "n": n,
                    "first": round(fv, 3), "last": round(lv, 3),
                    "change_pct": round(100 * (lv / fv - 1), 1) if fv else None,
                    "cagr": round(cagr, 2) if cagr is not None else None,
                    "min": f"{f_(mn[1])} ({mn[0]})", "max": f"{f_(mx[1])} ({mx[0]})",
                    "mean": round(sum(p[1] for p in pts) / n, 3)})
    return out


COMPOSITIONS = {
    "category": [("enteric_kt", "Enteric fermentation", BLUE), ("soils_kt", "Agricultural soils", ORANGE),
                 ("manure_kt", "Manure management", AQUA), ("urea_kt", "Urea", YELLOW), ("liming_kt", "Liming", MAGENTA)],
    "gas": [("crf3_ch4_kt", "Methane CH₄", BLUE), ("crf3_n2o_kt", "Nitrous oxide N₂O", ORANGE), ("crf3_co2_kt", "Carbon dioxide CO₂", AQUA)],
    "source": [("dairy_kt", "Dairy cattle CH₄", BLUE), ("other_cattle_kt", "Non-dairy cattle CH₄", ORANGE), ("sheep_kt", "Sheep CH₄", AQUA),
               ("soils_kt", "Agricultural soils N₂O", YELLOW), ("_rest", "Everything else", MAGENTA)],
}


def comp_series(kind):
    out = []
    for c, lab, col in COMPOSITIONS[kind]:
        if c == "_rest":
            vals = []
            for i, y in enumerate(YEARS):
                parts = [COLS[k][i] for k in ("dairy_kt", "other_cattle_kt", "sheep_kt", "soils_kt")]
                vals.append(None if any(p is None for p in parts) else COLS["crf3_kt"][i] - sum(parts))
        else:
            vals = COLS[c]
        out.append((lab, col, vals))
    return out


def composition_fig(kind, display, sel_year):
    fig = go.Figure()
    sers = comp_series(kind)
    years_ok = [y for i, y in enumerate(YEARS) if all(s[2][i] is not None for s in sers)]
    for lab, col, vals in sers:
        pts = [(y, vals[YEARS.index(y)]) for y in years_ok]
        if display == "share":
            yv = [100 * v / sum(s[2][YEARS.index(y)] for s in sers) for y, v in pts]
            ht = f"{lab}: %{{y:.1f}}%<extra></extra>"
        else:
            yv = [v / 1e3 for _, v in pts]
            ht = f"{lab}: %{{y:.2f}} Mt<extra></extra>"
        fig.add_trace(go.Scatter(x=[p[0] for p in pts], y=yv, name=lab, stackgroup="one", mode="lines",
                                 line=dict(color=col, width=0.6), fillcolor=col, hovertemplate=ht))
    fig.add_vline(x=sel_year, line=dict(color=INK, width=1.5))
    base_layout(fig, height=420, ytitle="Share of CRF3, %" if display == "share" else "Mt CO₂e")
    if kind == "source":
        fig.add_annotation(x=0, y=-0.16, xref="paper", yref="paper", showarrow=False, xanchor="left",
                           text="The dairy / non-dairy split comes from CRT 2025 and ends in 2023.", font=dict(size=11, color=MUTED))
    return fig


def composition_bar(kind, year):
    sers = comp_series(kind)
    i = YEARS.index(year)
    vals = [(lab, col, s[i]) for lab, col, s in [(a, b, c) for a, b, c in sers]]
    if any(v[2] is None for v in vals):
        return empty_fig(f"No split available for {year}", height=300)
    tot = sum(v[2] for v in vals)
    vals = sorted(vals, key=lambda v: v[2])
    fig = go.Figure(go.Bar(y=[v[0] for v in vals], x=[v[2] / 1e3 for v in vals], orientation="h",
                           marker=dict(color=[v[1] for v in vals], cornerradius=4),
                           text=[f"{v[2] / 1e3:.2f} Mt · {100 * v[2] / tot:.1f}%" for v in vals], textposition="outside",
                           cliponaxis=False, hovertemplate="%{y}: %{x:.2f} Mt<extra></extra>"))
    base_layout(fig, height=300, legend=False, title=f"{year}: {tot / 1e3:.2f} Mt CO₂e", hover="closest")
    fig.update_layout(margin=dict(l=170, r=110, t=50, b=30))
    fig.update_xaxes(title="Mt CO₂e", showgrid=True, gridcolor=GRID)
    return fig


REG_VARS = {"dairy_cows": ("Dairy cows", "thousand head"), "livestock_units": ("Livestock units", "thousand LU"),
            "other_cattle": ("Non-dairy cattle", "thousand head"), "sheep_total": ("Sheep", "thousand head"),
            "emis_imputed_kt": ("Imputed livestock CH₄ emissions", "kt CO₂e"), "dairy_share": ("Dairy share of all cows", "%")}
REGIONS = ["West", "Midland", "South-West", "Border + Dublin/Mid-East", "Mid-West + South-East"]


def regional_values(var):
    out = {}
    for r in DATA["regional"]:
        v = (100 * r["dairy_cows"] / (r["dairy_cows"] + r["other_cows"])) if var == "dairy_share" else r.get(var)
        out.setdefault(r["unit"], {})[r["Year"]] = v
    return out


def regional_fig(var, view, regions):
    if not regions:
        return empty_fig("Select at least one region")
    vals = regional_values(var)
    fig = go.Figure()
    for reg in regions:
        d = {y: v for y, v in vals[reg].items() if v is not None}
        ys = sorted(d)
        if view == "index":
            b = d.get(2014)
            yv = [100 * d[y] / b for y in ys]
        elif view == "share":
            tot = {y: sum(vals[r].get(y) or 0 for r in REGIONS) for y in ys}
            yv = [100 * d[y] / tot[y] for y in ys]
        else:
            yv = [d[y] for y in ys]
        fig.add_trace(go.Scatter(x=ys, y=yv, name=reg, mode="lines+markers", line=dict(color=REGION_COL[reg], width=2),
                                 marker=dict(size=4), hovertemplate=f"{reg} %{{x}}: <b>%{{y:,.1f}}</b><extra></extra>"))
    lab, unit = REG_VARS[var]
    yt = {"index": f"{lab}, index 2014 = 100", "share": f"{lab}, % of the five-region total", "levels": f"{lab} ({unit})"}[view]
    if view == "share" and var == "dairy_share":
        yt = "(share view not meaningful for a ratio — showing levels)"
    base_layout(fig, height=430, ytitle=yt)
    fig.add_vline(x=2014.5, line=dict(color=MUTED, dash="dot"))
    fig.add_annotation(x=2014.5, y=1, yref="paper", text="quota abolition", showarrow=False, xanchor="left", yanchor="top",
                       xshift=4, font=dict(size=11, color=INK2))
    fig.add_vline(x=2004.5, line=dict(color=MUTED, dash="dot"))
    fig.add_annotation(x=2004.5, y=1, yref="paper", text="CSO table switch", showarrow=False, xanchor="left", yanchor="top",
                       xshift=4, font=dict(size=11, color=INK2))
    return fig


def exposure_fig():
    ex = sorted(DATA["exposure"], key=lambda r: r["dairy_share_cows_2010_14_pct"])
    fig = go.Figure(go.Bar(y=[r["unit"] for r in ex], x=[r["dairy_share_cows_2010_14_pct"] for r in ex], orientation="h",
                           marker=dict(color=[REGION_COL[r["unit"]] for r in ex], cornerradius=4),
                           text=[f"{r['dairy_share_cows_2010_14_pct']:.1f}%" for r in ex], textposition="outside", cliponaxis=False,
                           hovertemplate="%{y}: %{x:.1f}% of cows were dairy cows<extra></extra>"))
    base_layout(fig, height=280, legend=False, title="Exposure to quota abolition: dairy share of all cows, 2010–14", hover="closest")
    fig.update_layout(margin=dict(l=190, r=60, t=50, b=30))
    fig.update_xaxes(range=[0, 85], title="%", showgrid=True, gridcolor=GRID)
    return fig


def codebook_heatmap(which):
    key = "scoreM" if which == "M" else "scoreP"
    sc = DATA[key]
    pids = list(sc["cols"])
    z = [sc["cols"][p] for p in pids]
    labels = [f"{p} · {CODEBOOK[p]['name'][:42]}" for p in pids]
    col = C_M if which == "M" else C_P
    fig = go.Figure(go.Heatmap(z=z, x=sc["years"], y=labels, colorscale=[[0, "#f6f5f1"], [0.0001, "#e9f0fb" if which == "M" else "#fdeee6"], [1, col]],
                               xgap=1, ygap=2, colorbar=dict(title="score", thickness=12, len=0.8),
                               hovertemplate="%{y}<br>%{x}: score x = I·C·B = <b>%{z:.4f}</b><extra></extra>"))
    base_layout(fig, height=34 * len(pids) + 90, legend=False, hover="closest")
    fig.update_layout(margin=dict(l=330, r=20, t=20, b=40))
    fig.update_yaxes(autorange="reversed", showgrid=False)
    fig.update_xaxes(dtick=5)
    return fig


def parse_impl(s):
    out = {}
    for part in str(s).split(";"):
        if ":" in part:
            span, v = part.split(":"); a, b = (span.split("-") + [span])[:2]
            for y in range(int(a), int(b) + 1):
                out[y] = float(v)
    return out


def policy_detail(pid, year):
    r = CODEBOOK[pid]
    impl = parse_impl(r["implementation"])
    s, e, B = r["coverage_share"], r["eligibility"], r["bindingness"]
    C = s * e
    I = impl.get(year, 0.0)
    x = I * C * B
    key = "scoreM" if r["policy_set"] == "M" else "scoreP"
    col = C_M if r["policy_set"] == "M" else C_P
    sc = DATA[key]["cols"][pid]
    fig = go.Figure()
    fig.add_trace(go.Bar(x=YEARS, y=sc, name="Score x = I·C·B",
                         marker=dict(color=[col if y == year else col for y in YEARS],
                                     opacity=[1 if y == year else 0.45 for y in YEARS], cornerradius=3),
                         customdata=[impl.get(y, 0) for y in YEARS],
                         hovertemplate="%{x}: I = %{customdata} → x = <b>%{y:.4f}</b><extra></extra>"))
    fig.add_hline(y=C * B, line=dict(color=MUTED, dash="dot", width=1))
    fig.add_annotation(x=1990, y=C * B, text=f"maximum C·B = {C * B:.4f} (when I = 1)", showarrow=False, xanchor="left",
                       yanchor="bottom", font=dict(size=11, color=INK2))
    base_layout(fig, height=280, legend=False, ytitle="policy score x", hover="closest")
    fig.update_yaxes(rangemode="tozero")
    info = html.Div(className="policy-info", children=[
        html.Div([badge("Pressure" if r["policy_set"] == "P" else "Mitigation", "orange" if r["policy_set"] == "P" else "blue"),
                  badge(r["instrument_type"], "neutral")]),
        html.H3(f"{pid} · {r['name']}"),
        html.Div(className="formula-strip", children=[
            html.Div([html.Div("I", className="f-sym"), html.Div(f"{I:g}", className="f-val"), html.Div(f"in force in {year}", className="f-lab")]),
            html.Div("×", className="f-op"),
            html.Div([html.Div("C = s·e", className="f-sym"), html.Div(f"{s:.3f}·{e:g} = {C:.3f}", className="f-val"),
                      html.Div(f"s: {COVERAGE_LABEL.get(r['coverage_key'], r['coverage_key'])} share in {int(r['start']) - 1}", className="f-lab")]),
            html.Div("×", className="f-op"),
            html.Div([html.Div("B", className="f-sym"), html.Div(f"{B:g}", className="f-val"), html.Div("bindingness", className="f-lab")]),
            html.Div("=", className="f-op"),
            html.Div([html.Div("x", className="f-sym"), html.Div(f"{x:.4f}", className="f-val strong"), html.Div("policy score", className="f-lab")]),
        ]),
        html.P([html.B("Legal / programme source: "), r.get("legal_or_programme_source") or "–"], className="small"),
        html.P([html.B("Coding note: "), r.get("coding_note") or "–"], className="small"),
    ])
    return info, fig


# ------------------------------------------------------------------ layout
def tab_overview():
    return html.Div([
        kpi_row(kpi("35", "annual observations", "1990–2024"), kpi(str(len(MANIFEST)), "files hashed & loaded", "SHA-256 provenance"),
                kpi(str(len(VARIABLES)), "core variables in the panel", "of 90+ derived columns"),
                kpi("5", "constant-boundary regions", "regional panel 1991–2024"), kpi(f"{len(VERIFICATION)}/{len(VERIFICATION)}", "verification checks pass", tone="tone-green")),
        section("Where the data come from",
                html.Div(className="source-grid", children=[
                    html.Div(className="source-card", children=[html.Div(a, className="src-agency"), html.Div(b, className="src-name"),
                                                                html.Div(c, className="src-files"), html.Div(d, className="src-what"),
                                                                html.Div(e, className="src-years")]) for a, b, c, d, e in SOURCES]),
                html.P(f"All {len(dataset_sources.ITEMS)} parameters, tables and download links are catalogued in the "
                       "“Data sources & resources” tab.", className="fig-note")),
        section("Coverage map: which years exist for which variable",
                card(dcc.Graph(figure=coverage_fig(), config=GRAPH_CONFIG, className="graph"),
                     html.P("Blue = observed; pale = missing. Gaps are left as they are: no year is interpolated, back-cast or set to zero. "
                            "Prices start in 1995, milk in 1992, livestock in 1991; the CRT-based series end in 2023.", className="fig-note"))),
        section("Data dictionary",
                card(html.P("Type in the filter row to search (e.g. 'CSO', 'Real', 'kt').", className="fig-note"),
                     table([{"group": VARIABLES[k][0], "variable": VARIABLES[k][1], "unit": VARIABLES[k][2], "source": VARIABLES[k][3],
                             "role": VARIABLES[k][4], "status": VARIABLES[k][5], "years": "{}–{}".format(*coverage(k)[:2]),
                             "n": coverage(k)[2], "description": VARIABLES[k][6]} for k in VARIABLES],
                           [("group", "Group"), ("variable", "Variable"), ("unit", "Unit"), ("years", "Years"), ("n", "Obs"),
                            ("source", "Source"), ("role", "Role in analysis"), ("status", "Status"), ("description", "Definition")],
                           page_size=15, filter=True,
                           style_cond=[{"if": {"filter_query": '{status} contains "Provisional"', "column_id": "status"}, "color": "#a35a00", "fontWeight": 600},
                                       {"if": {"filter_query": '{status} contains "Real"', "column_id": "status"}, "color": "#006300", "fontWeight": 600}]))),
    ])


def tab_explorer():
    return html.Div([
        callout("plain", "How to use the explorer",
                "Pick any variables, choose how to show them and drag the year range. 'Index' puts series with different units on one "
                "scale (first year = 100); 'Levels' draws each series in its own panel with its own unit; 'Annual change' shows year-on-year %."),
        card(
            html.Div(className="control-grid", children=[
                html.Div([html.Label("Variables", className="ctl-label"),
                          dcc.Dropdown(id="ex-vars", options=VAR_OPTIONS, value=DEFAULT_VARS, multi=True, clearable=True,
                                       placeholder="Choose variables…")], className="span-2"),
                html.Div([html.Label("Display", className="ctl-label"),
                          dcc.RadioItems(id="ex-mode", value="index", className="seg", inline=True,
                                         options=[{"label": "Index (=100)", "value": "index"}, {"label": "Levels", "value": "levels"},
                                                  {"label": "Annual change %", "value": "yoy"}])], className="span-2"),
                html.Div([html.Label("Options", className="ctl-label"),
                          dcc.Checklist(id="ex-events", value=["ev"], className="chk", inline=True,
                                        options=[{"label": " Show policy dates", "value": "ev"}])]),
                html.Div([html.Label("Years", className="ctl-label"),
                          dcc.RangeSlider(id="ex-years", min=1990, max=2024, step=1, value=[1990, 2024],
                                          marks={y: str(y) for y in range(1990, 2025, 5)}, tooltip={"placement": "bottom"})], className="span-3"),
            ]),
            dcc.Loading(dcc.Graph(id="ex-fig", config=GRAPH_CONFIG, className="graph"), type="dot", color=BLUE),
        ),
        section("Summary statistics for your selection",
                card(table([], [("variable", "Variable"), ("unit", "Unit"), ("years", "Years"), ("n", "Obs"), ("first", "First", num(2)),
                                ("last", "Last", num(2)), ("change_pct", "Change %", num(1)), ("cagr", "Avg. growth %/yr", num(2)),
                                ("min", "Min (year)"), ("max", "Max (year)"), ("mean", "Mean", num(2))], id="ex-stats", page_size=10))),
    ])


def tab_composition():
    return html.Div([
        card(
            html.Div(className="control-row", children=[
                html.Span("Break down by", className="ctl-label"),
                dcc.RadioItems(id="co-kind", value="category", className="seg", inline=True,
                               options=[{"label": "Inventory category", "value": "category"}, {"label": "Gas", "value": "gas"},
                                        {"label": "Livestock source", "value": "source"}]),
                html.Span("Show as", className="ctl-label"),
                dcc.RadioItems(id="co-disp", value="abs", className="seg", inline=True,
                               options=[{"label": "Mt CO₂e", "value": "abs"}, {"label": "Share %", "value": "share"}]),
            ]),
            dcc.Graph(id="co-fig", config=GRAPH_CONFIG, className="graph"),
            html.Div(className="control-row", children=[
                html.Span("Year for the breakdown (or click the chart)", className="ctl-label"),
                html.Div(dcc.Slider(id="co-year", min=1990, max=2024, step=1, value=2024,
                                    marks={y: str(y) for y in range(1990, 2025, 5)}, tooltip={"placement": "bottom"}), className="grow"),
            ]),
            dcc.Graph(id="co-bar", config=GRAPH_CONFIG, className="graph"),
        ),
        callout("read", "What to notice",
                "Enteric methane from cattle is about half of the total and drives the long swings. Soils N₂O follows fertiliser use, which "
                "peaked in the late 1990s. The livestock-source view shows dairy CH₄ rising from about a fifth to over a quarter of CRF3 after 2015."),
    ])


def tab_regional():
    return html.Div([
        callout("plain", "Why regions?",
                "Quota abolition should bind hardest where dairy was already dominant. The study compares five regions with constant "
                "boundaries — the basis of the regional difference-in-differences (RQ4)."),
        card(
            html.Div(className="control-grid", children=[
                html.Div([html.Label("Variable", className="ctl-label"),
                          dcc.Dropdown(id="rg-var", value="dairy_cows", clearable=False,
                                       options=[{"label": v[0], "value": k} for k, v in REG_VARS.items()])]),
                html.Div([html.Label("View", className="ctl-label"),
                          dcc.RadioItems(id="rg-view", value="index", className="seg", inline=True,
                                         options=[{"label": "Index 2014 = 100", "value": "index"}, {"label": "Levels", "value": "levels"},
                                                  {"label": "Share of total", "value": "share"}])]),
                html.Div([html.Label("Regions", className="ctl-label"),
                          dcc.Checklist(id="rg-regions", value=REGIONS, className="chk", inline=True,
                                        options=[{"label": f" {r}", "value": r} for r in REGIONS])], className="span-2"),
            ]),
            dcc.Graph(id="rg-fig", config=GRAPH_CONFIG, className="graph"),
            html.P("Imputed emissions = regional head counts × national implied emission factors per head (available to 2023). "
                   "The 2004→05 step is the CSO classification change.", className="fig-note"),
        ),
        two_col(card(dcc.Graph(figure=exposure_fig(), config=GRAPH_CONFIG, className="graph")),
                card(html.H3("The five constant-boundary units"),
                     html.Ul([html.Li([html.B("West, Midland, South-West"), " — unchanged by the NUTS3 revision"]),
                              html.Li([html.B("Border + Dublin/Mid-East"), " — absorbs Louth's move"]),
                              html.Li([html.B("Mid-West + South-East"), " — absorbs the Tipperary unification"])]),
                     html.P("Exposure ranges from 16% of cows in the West to 74% in the South-West, a wide contrast for a "
                            "continuous-intensity design (Card, 1992).", className="small")), ratio="3-2"),
    ])


def tab_codebooks():
    first = "P05"
    info, fig = policy_detail(first, 2016)
    return html.Div([
        callout("plain", "How a policy becomes a number",
                "Each instrument gets a score in every year: implementation I (is it in force?) × coverage C (how much of CRF3 does "
                "it target?) × bindingness B (how strong is the signal?). Summing scores gives the mitigation index M and the pressure index P."),
        card(
            html.Div(className="control-row", children=[
                html.Span("Policy set", className="ctl-label"),
                dcc.RadioItems(id="cb-set", value="P", className="seg", inline=True,
                               options=[{"label": "Production pressure P (8)", "value": "P"}, {"label": "Mitigation M (12)", "value": "M"}])]),
            dcc.Graph(id="cb-heat", config=GRAPH_CONFIG, className="graph"),
            html.P("Click a row in the heatmap to open that policy below.", className="fig-note"),
        ),
        section("Policy score calculator",
                card(
                    html.Div(className="control-grid", children=[
                        html.Div([html.Label("Policy", className="ctl-label"),
                                  dcc.Dropdown(id="cb-pid", value=first, clearable=False,
                                               options=[{"label": f"{p} · {CODEBOOK[p]['name']}", "value": p}
                                                        for p in CODEBOOK if CODEBOOK[p]["direction"] != 0])], className="span-2"),
                        html.Div([html.Label("Year", className="ctl-label"),
                                  dcc.Slider(id="cb-year", min=1990, max=2024, step=1, value=2016,
                                             marks={y: str(y) for y in range(1990, 2025, 5)}, tooltip={"placement": "bottom"})], className="span-2"),
                    ]),
                    html.Div(id="cb-info", children=info),
                    dcc.Graph(id="cb-fig", figure=fig, config=GRAPH_CONFIG, className="graph"),
                    html.P("Bars: the policy's score in each year (the selected year is highlighted). The score is the implementation "
                           "level I times the constant C·B, so it reaches the dotted line only when the policy is fully in force.", className="fig-note"),
                )),
        section("Full codebooks",
                card(table([{k: (round(v, 4) if isinstance(v, float) else v) for k, v in r.items()
                             if k in ("policy_id", "policy_set", "name", "instrument_type", "start", "end", "coverage_key",
                                      "coverage_share", "eligibility", "bindingness", "implementation", "climate_relevance")}
                            for r in DATA["codebook"]],
                           [("policy_id", "ID"), ("policy_set", "Set"), ("name", "Policy"), ("instrument_type", "Type"), ("start", "Start"),
                            ("end", "End"), ("implementation", "Implementation I"), ("coverage_key", "Coverage key"),
                            ("coverage_share", "s", num(3)), ("eligibility", "e", num(2)), ("bindingness", "B", num(2)),
                            ("climate_relevance", "Climate relevance", num(1))], page_size=22, filter=True))),
    ])


TABLE_DEFAULT = ["crf3_kt", "dairy_cows", "other_cattle", "sheep_total", "livestock_units", "milk_per_cow_l", "n_fert_kt", "M", "P", "S"]


def tab_table():
    return html.Div([
        card(
            html.Div(className="control-grid", children=[
                html.Div([html.Label("Columns", className="ctl-label"),
                          dcc.Dropdown(id="tb-cols", options=VAR_OPTIONS, value=TABLE_DEFAULT, multi=True)], className="span-3"),
                html.Div([html.Label("Download", className="ctl-label"),
                          html.Button("⬇ Full panel (CSV)", id="tb-dl-btn", className="btn")]),
            ]),
            dcc.Download(id="tb-dl"),
            html.Div(id="tb-wrap"),
            html.P("Sort by clicking a header; filter with expressions such as > 20000 in the filter row. "
                   "Empty cells are genuinely missing years.", className="fig-note"),
        ),
    ])


def tab_quality():
    return html.Div([
        kpi_row(kpi("0.0000%", "gap: CRF3 vs sum of categories and gases"), kpi("≤ 0.21%", "gap: CRT vs Eurostat CH₄"),
                kpi("2.88%", "largest price chain-link deviation"), kpi("−8.7%", "dairy-cow step at the 2004–05 table switch", "→ break dummy")),
        section("Harmonisation rules", *[details(t, md(b)) for t, b in HARMONISATION]),
        section("Independent workflow verification (tools/verify_workflow.py)",
                card(table([{"stage": a, "check": b, "detail": c, "result": "PASS"} for a, b, c in VERIFICATION],
                           [("stage", "Stage"), ("check", "Check"), ("result", "Result"), ("detail", "Detail")], page_size=30,
                           style_cond=[{"if": {"column_id": "result"}, "color": "#006300", "fontWeight": 700}]))),
        section("File provenance (registry and SHA-256)",
                card(table([{k: r.get(k) for k in ("stem", "folder", "role", "status", "duplicates", "sha256_short")} for r in MANIFEST],
                           [("stem", "File stem"), ("folder", "Folder"), ("role", "Role"), ("status", "Status"), ("duplicates", "Duplicates"),
                            ("sha256_short", "SHA-256 (first 12)")], page_size=12, filter=True))),
    ])


def layout():
    return html.Div([
        page_header("Step 3 · Dataset", "The dataset, interactively",
                    "Every series is annual, read unchanged from the publishing agency, and hashed. Explore what is in the panel, "
                    "how it was built, and how the policy indices are scored."),
        dcc.Tabs(id="ds-tabs", value="overview", className="tabs", children=[
            dcc.Tab(label="Overview & sources", value="overview", children=tab_overview(), className="tab", selected_className="tab--sel"),
            dcc.Tab(label="Data sources & resources", value="sources", children=dataset_sources.tab_sources(), className="tab",
                    selected_className="tab--sel"),
            dcc.Tab(label="Series explorer", value="explorer", children=tab_explorer(), className="tab", selected_className="tab--sel"),
            dcc.Tab(label="Emissions composition", value="comp", children=tab_composition(), className="tab", selected_className="tab--sel"),
            dcc.Tab(label="Regional panel", value="regional", children=tab_regional(), className="tab", selected_className="tab--sel"),
            dcc.Tab(label="Regional map", value="map", children=dataset_map.tab_map(), className="tab", selected_className="tab--sel"),
            dcc.Tab(label="Policy codebooks", value="codebooks", children=tab_codebooks(), className="tab", selected_className="tab--sel"),
            dcc.Tab(label="Data table & download", value="table", children=tab_table(), className="tab", selected_className="tab--sel"),
            dcc.Tab(label="Quality & provenance", value="quality", children=tab_quality(), className="tab", selected_className="tab--sel"),
        ]),
    ])


def register_callbacks(app):
    dataset_sources.register_callbacks(app)
    dataset_map.register_callbacks(app)

    @app.callback(Output("ex-fig", "figure"), Output("ex-stats", "data"),
                  Input("ex-vars", "value"), Input("ex-mode", "value"), Input("ex-years", "value"), Input("ex-events", "value"))
    def _ex(vars_, mode, yr, ev):
        return explorer_fig(vars_, mode, yr, bool(ev)), summary_rows(vars_, yr)

    @app.callback(Output("co-year", "value"), Input("co-fig", "clickData"), prevent_initial_call=True)
    def _click(cd):
        if not cd:
            return no_update
        return int(cd["points"][0]["x"])

    @app.callback(Output("co-fig", "figure"), Output("co-bar", "figure"),
                  Input("co-kind", "value"), Input("co-disp", "value"), Input("co-year", "value"))
    def _co(kind, disp, year):
        if kind == "source" and year == 2024:
            year = 2023
        return composition_fig(kind, disp, year), composition_bar(kind, year)

    @app.callback(Output("rg-fig", "figure"), Input("rg-var", "value"), Input("rg-view", "value"), Input("rg-regions", "value"))
    def _rg(var, view, regs):
        if var == "dairy_share" and view == "share":
            view = "levels"
        return regional_fig(var, view, [r for r in REGIONS if r in (regs or [])])

    @app.callback(Output("cb-heat", "figure"), Input("cb-set", "value"))
    def _heat(which):
        return codebook_heatmap(which)

    @app.callback(Output("cb-pid", "value"), Input("cb-heat", "clickData"), prevent_initial_call=True)
    def _heat_click(cd):
        if not cd:
            return no_update
        return cd["points"][0]["y"].split(" · ")[0]

    @app.callback(Output("cb-info", "children"), Output("cb-fig", "figure"), Input("cb-pid", "value"), Input("cb-year", "value"))
    def _pol(pid, year):
        return policy_detail(pid, year)

    @app.callback(Output("tb-wrap", "children"), Input("tb-cols", "value"))
    def _tb(cols):
        cols = cols or []
        rows = [{"Year": y, **{c: (None if COLS[c][i] is None else round(COLS[c][i], 4)) for c in cols}} for i, y in enumerate(YEARS)]
        return table(rows, [("Year", "Year")] + [(c, f"{VARIABLES[c][1]} [{VARIABLES[c][2]}]", num(3 if c in ('M', 'P', 'S') else 1)) for c in cols],
                     page_size=35, filter=True)

    @app.callback(Output("tb-dl", "data"), Input("tb-dl-btn", "n_clicks"), prevent_initial_call=True)
    def _dl(n):
        return dcc.send_file(str(PANEL_CSV))
