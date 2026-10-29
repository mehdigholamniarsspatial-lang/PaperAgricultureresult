"""Step 5 – results, each with a plain-language reading."""
import math
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from dash import html, dcc, Input, Output

from ..components import (page_header, section, card, callout, kpi, kpi_row, table, num, two_col, md, badge, details)
from ..data_store import DATA, KEY, YEARS, COLS, series, value, fmt, pfmt, EVENTS, PHASES, CODEBOOK
from ..theme import (base_layout, add_events, empty_fig, PAL, C_M, C_P, C_S, INK, INK2, MUTED, GRID, BLUE, ORANGE, AQUA, YELLOW,
                     MAGENTA, VIOLET, RED, GREEN, FACTOR_COL, FACTOR_LAB, COMP_LAB, REGION_COL, GRAPH_CONFIG)

K = KEY


def pct(x):
    return 100 * (math.exp(x) - 1)


def quant(xs, q):
    s = sorted(x for x in xs if x is not None)
    i = (len(s) - 1) * q
    lo, hi = int(math.floor(i)), int(math.ceil(i))
    return s[lo] + (s[hi] - s[lo]) * (i - lo)


def fig_note(t):
    return html.P(t, className="fig-note")


def reading(shows, how, finding=None):
    kids = [callout("plain", "What this shows", shows), callout("read", "How to read it", how)]
    if finding:
        kids.append(callout("finding", "Finding", finding))
    return html.Div(className="readings", children=kids)


# ------------------------------------------------------------------ scorecard
VERDICTS = [
    ("H1", "Breaks at 2010 or 2015", "Not supported", "no", "3 breaks (2000, 2012, 2020) — none within ±1 yr of a policy date"),
    ("H2", "Intensity offset < 1 after 2015", "Supported", "yes", f"IO = {K['lmdi']['P4_intensity_offset']:.2f} (0.21–0.33 across EF ratios)"),
    ("H3a", "Mitigation lowers emissions (θ_M < 0)", "Not supported", "no", f"θ_M = +{K['ardl']['theta_M']:.2f}, bootstrap p = {K['ardl']['p_boot_M']:.3f}"),
    ("H3b", "Pressure raises emissions (θ_P > 0)", "Supported", "yes", f"θ_P = +{K['ardl']['theta_P']:.2f}, bootstrap p = {K['ardl']['p_boot_P']:.3f}"),
    ("H3c", "Offset ratio ≥ 0.5", "Undefined", "na", "mitigation effect is not negative, so OR cannot be computed"),
    ("H4a", "Mandatory instruments strongest", "Not supported", "no",
     f"mandatory θ = +{K['subindex']['mandatory']['theta']:.2f} (p = {K['subindex']['mandatory']['p_boot_one_sided']:.2f}); only voluntary is negative "
     f"(θ = {K['subindex']['voluntary']['theta']:.2f}, p = {K['subindex']['voluntary']['p_boot_one_sided']:.2f})".replace("-", "−")),
    ("H4b", "Exposed regions expanded more after 2015", "Not supported", "no", "significant placebo: divergence began before 2015"),
]


def scorecard():
    return html.Div(className="score-grid", children=[
        html.Div(className=f"score-card v-{tone}", children=[
            html.Div(className="score-top", children=[html.Span(h, className="score-h"),
                                                      html.Span(("✓ " if tone == "yes" else "✕ " if tone == "no" else "○ ") + verdict, className="score-v")]),
            html.Div(t, className="score-t"), html.Div(ev, className="score-e")]) for h, t, verdict, tone, ev in VERDICTS])


# ------------------------------------------------------------------ figures
def indices_fig(show):
    fig = go.Figure()
    spec = [("M", "Mitigation intensity M", C_M, "solid"), ("P", "Production pressure P", C_P, "solid"), ("S", "Net signal S = M − P", C_S, "dash"),
            ("G", "Strategy signal G", INK2, "dot")]
    for c, lab, col, dash in spec:
        if c not in show:
            continue
        ys, v = series(c)
        fig.add_trace(go.Scatter(x=ys, y=v, name=lab, mode="lines", line=dict(color=col, width=2.5, dash=dash),
                                 hovertemplate=f"{lab}: %{{y:.3f}}<extra></extra>"))
    fig.add_hline(y=0, line=dict(color=AXIS_COL, width=1))
    base_layout(fig, height=420, ytitle="index value")
    add_events(fig, EVENTS)
    return fig


AXIS_COL = "#c3c2b7"


def breaks_fig(show_ci=True):
    ys, e = series("crf3_kt")
    fig = go.Figure()
    br = K["breaks"]
    if show_ci:
        for (a, b) in br["ci90"]:
            fig.add_vrect(x0=a - 1, x1=b, fillcolor="rgba(235,104,52,0.10)", line_width=0)
    fig.add_trace(go.Scatter(x=ys, y=[v / 1e3 for v in e], name="CRF3 emissions (observed)", mode="lines+markers",
                             line=dict(color=BLUE, width=2), marker=dict(size=6), hovertemplate="%{x}: %{y:.2f} Mt<extra></extra>"))
    fit = DATA["fit_m"]
    edges = [1990] + br["break_years"] + [2025]
    slopes = br["segment_slopes_pct"]
    for j in range(len(edges) - 1):
        seg = [(y, f) for y, f in zip(ys, fit) if edges[j] <= y < edges[j + 1]]
        fig.add_trace(go.Scatter(x=[s[0] for s in seg], y=[s[1] / 1e3 for s in seg], mode="lines", line=dict(color=ORANGE, width=3),
                                 name="Bai–Perron segmented trend" if j == 0 else None, showlegend=j == 0,
                                 hovertemplate=f"segment {edges[j]}–{edges[j + 1] - 1}: {slopes[j]:+.2f}%/yr<extra></extra>"))
        mid = seg[len(seg) // 2]
        fig.add_annotation(x=mid[0], y=mid[1] / 1e3, text=f"<b>{slopes[j]:+.2f}%/yr</b>".replace("-", "−"), showarrow=False, yshift=-22,
                           font=dict(color=ORANGE, size=12))
    for b in br["break_years"]:
        fig.add_vline(x=b - 0.5, line=dict(color=ORANGE, width=1.2, dash="dash"))
    add_events(fig, EVENTS)
    base_layout(fig, height=440, ytitle="Mt CO₂e")
    return fig


def lmdi_phase_fig():
    rows = DATA["lmdi_phase"]
    fig = go.Figure()
    labs = [f"{r['phase'].split(' ')[0]}<br>{r['years']}" for r in rows]
    for f in ["activity", "productivity", "intensity", "other"]:
        fig.add_trace(go.Bar(x=labs, y=[r[f] for r in rows], name=FACTOR_LAB[f], marker=dict(color=FACTOR_COL[f], cornerradius=3),
                             hovertemplate=f"{FACTOR_LAB[f]}: %{{y:+,.0f}} kt<extra></extra>"))
    fig.add_trace(go.Scatter(x=labs, y=[r["net_change"] for r in rows], name="Net change", mode="markers+text",
                             marker=dict(symbol="diamond", size=12, color=INK, line=dict(color="white", width=1.5)),
                             text=[f"{r['net_change']:+,.0f}".replace("-", "−") for r in rows], textposition="top center",
                             hovertemplate="Net: %{y:+,.0f} kt<extra></extra>"))
    fig.add_hline(y=0, line=dict(color=AXIS_COL))
    base_layout(fig, height=440, ytitle="kt CO₂e, cumulative within phase")
    fig.update_layout(barmode="group", bargap=0.25, bargroupgap=0.06)
    return fig


def lmdi_component_fig(phase_code):
    ph = next(p for p in PHASES if p[0] == phase_code)
    rows = [r for r in DATA["lmdi_annual"] if ph[2] < r["year"] <= ph[3]] if phase_code != "P1" else \
           [r for r in DATA["lmdi_annual"] if 1992 < r["year"] <= 2004]
    agg = {}
    for r in rows:
        agg.setdefault(r["component"], {}).setdefault(r["factor"], 0)
        agg[r["component"]][r["factor"]] += r["effect"]
    comps = ["dairy", "other_cattle", "sheep", "soils_fert", "soils_manureN", "other"]
    fig = go.Figure()
    for f in ["activity", "productivity", "intensity", "other"]:
        fig.add_trace(go.Bar(y=[COMP_LAB[c] for c in comps], x=[agg.get(c, {}).get(f, 0) for c in comps], orientation="h",
                             name=FACTOR_LAB[f], marker=dict(color=FACTOR_COL[f], line=dict(color="#fcfcfb", width=1)),
                             hovertemplate=f"%{{y}} · {FACTOR_LAB[f]}: %{{x:+,.0f}} kt<extra></extra>"))
    fig.add_vline(x=0, line=dict(color=INK2, width=1))
    base_layout(fig, height=380, xtitle="kt CO₂e", hover="closest", title=f"{ph[0]} {ph[1]} ({ph[2]}–{ph[3]}): which component moved")
    fig.update_layout(barmode="relative", margin=dict(l=170))
    fig.update_yaxes(autorange="reversed")
    return fig


def lmdi_annual_fig():
    by = {}
    for r in DATA["lmdi_annual"]:
        by.setdefault(r["year"], {}).setdefault(r["factor"], 0)
        by[r["year"]][r["factor"]] += r["effect"]
    yrs = sorted(by)
    fig = go.Figure()
    for f in ["activity", "productivity", "intensity", "other"]:
        fig.add_trace(go.Bar(x=yrs, y=[by[y].get(f, 0) for y in yrs], name=FACTOR_LAB[f], marker=dict(color=FACTOR_COL[f], line=dict(color="#fcfcfb", width=0.8)),
                             hovertemplate=f"{FACTOR_LAB[f]}: %{{y:+,.0f}} kt<extra></extra>"))
    fig.add_trace(go.Scatter(x=yrs, y=[sum(by[y].values()) for y in yrs], name="Annual change in CRF3", mode="markers",
                             marker=dict(color=INK, size=7, symbol="diamond"), hovertemplate="ΔCRF3: %{y:+,.0f} kt<extra></extra>"))
    for p in PHASES[1:]:
        fig.add_vline(x=p[2] + 0.5, line=dict(color=MUTED, dash="dot", width=1))
    base_layout(fig, height=400, ytitle="kt CO₂e, year-on-year")
    fig.update_layout(barmode="relative")
    return fig


def forest_fig():
    bd = DATA["boot_draws"]
    rows = []
    for v, col, lab in [("P", C_P, "θ_P · production pressure"), ("M", C_M, "θ_M · mitigation")]:
        draws = [r[f"theta_{v}"] for r in bd]
        rows.append((lab, K["ardl"][f"theta_{v}"], quant(draws, 0.05), quant(draws, 0.95), col, K["ardl"][f"p_boot_{v}"]))
    fig = go.Figure()
    for lab, t, lo, hi, col, p in rows:
        fig.add_trace(go.Scatter(x=[t], y=[lab], mode="markers", marker=dict(size=14, color=col, line=dict(color="white", width=2)),
                                 error_x=dict(type="data", symmetric=False, array=[hi - t], arrayminus=[t - lo], color=col, thickness=3, width=8),
                                 name=lab, showlegend=False,
                                 hovertemplate=f"{lab}<br>estimate {t:.3f}<br>90% bootstrap interval [{lo:.3f}, {hi:.3f}]<br>one-sided p = {p:.3f}<extra></extra>"))
        fig.add_annotation(x=hi, y=lab, text=f"  {t:.2f} [{lo:.2f}, {hi:.2f}]", showarrow=False, xanchor="left", font=dict(color=INK2))
    fig.add_vline(x=0, line=dict(color=INK2, width=1.2))
    fig.add_annotation(x=0, y=1.08, yref="paper", text="← lowers emissions   |   raises emissions →", showarrow=False, font=dict(size=11, color=MUTED))
    base_layout(fig, height=260, legend=False, xtitle="long-run effect θ (log points per index unit)", hover="closest")
    fig.update_xaxes(range=[-0.6, 1.6], showgrid=True, gridcolor=GRID)
    fig.update_layout(margin=dict(l=200, t=40))
    return fig


def boot_scatter_fig():
    bd = DATA["boot_draws"]
    fig = go.Figure(go.Scatter(x=[r["theta_M"] for r in bd], y=[r["theta_P"] for r in bd], mode="markers",
                               marker=dict(size=6, color=VIOLET, opacity=0.35), name="bootstrap draw",
                               hovertemplate="θ_M %{x:.2f}, θ_P %{y:.2f}<extra></extra>"))
    fig.add_trace(go.Scatter(x=[K["ardl"]["theta_M"]], y=[K["ardl"]["theta_P"]], mode="markers", name="estimate",
                             marker=dict(size=14, color=INK, symbol="x")))
    fig.add_vline(x=0, line=dict(color=INK2)); fig.add_hline(y=0, line=dict(color=INK2))
    fig.add_annotation(x=-0.3, y=1.25, text="'offsetting' quadrant<br>(θ_M < 0, θ_P > 0)", showarrow=False,
                       font=dict(size=11, color=MUTED))
    base_layout(fig, height=360, xtitle="θ_M (mitigation)", ytitle="θ_P (pressure)", hover="closest",
                title="999 unrestricted bootstrap draws of (θ_M, θ_P)")
    return fig


def cf_paths_fig(show):
    rows = DATA["paths"]
    yrs = [r["Year"] for r in rows]
    fig = go.Figure()
    spec = [("observed_kt", "Observed", INK, "solid", 3), ("no_pressure_change_kt", "P frozen at 2000", C_P, "dash", 2.5),
            ("no_mitigation_change_kt", "M frozen at 2000", C_M, "dash", 2.5), ("neither_kt", "Both frozen at 2000", AQUA, "dot", 2.5)]
    for c, lab, col, dash, w in spec:
        if c != "observed_kt" and c not in show:
            continue
        fig.add_trace(go.Scatter(x=yrs, y=[r[c] / 1e3 for r in rows], name=lab, mode="lines", line=dict(color=col, dash=dash, width=w),
                                 hovertemplate=f"{lab}: %{{y:.2f}} Mt<extra></extra>"))
        fig.add_annotation(x=2024, y=rows[-1][c] / 1e3, text=f" {lab}", showarrow=False, xanchor="left", font=dict(size=11, color=col))
    base_layout(fig, height=430, ytitle="Mt CO₂e")
    fig.update_xaxes(range=[1999.5, 2029])
    return fig


def effect_hist_fig(which):
    bd = DATA["boot_draws"]
    xs = [pct(r["dP" if which == "P" else "dM"]) for r in bd]
    est = K["offset"]["pressure_effect_pct" if which == "P" else "mitigation_effect_pct"]
    lo, hi = quant(xs, 0.05), quant(xs, 0.95)
    col = C_P if which == "P" else C_M
    fig = go.Figure(go.Histogram(x=xs, nbinsx=45, marker=dict(color=col, opacity=0.5, line=dict(color="#fcfcfb", width=1)),
                                 hovertemplate="%{x:.1f}%: %{y} draws<extra></extra>"))
    fig.add_vrect(x0=lo, x1=hi, fillcolor="rgba(0,0,0,0.04)", line_width=0)
    fig.add_vline(x=est, line=dict(color=INK, width=2)); fig.add_vline(x=0, line=dict(color=RED, width=1.5, dash="dot"))
    fig.add_annotation(x=est, y=1, yref="paper", text=f"estimate {est:+.1f}%<br>90%: [{lo:+.1f}, {hi:+.1f}]", showarrow=False, xanchor="left",
                       yanchor="top", xshift=6)
    base_layout(fig, height=320, legend=False, hover="closest", ytitle="draws",
                xtitle=f"effect of the {'pressure' if which == 'P' else 'mitigation'} change since 2000 on 2024 emissions, %")
    return fig


def robust_fig(param):
    rows = [r for r in DATA["robust"] if r.get(f"theta_{param}") is not None]
    rows = sorted(rows, key=lambda r: (not r["variant"].startswith("leave"), r[f"theta_{param}"]))
    pk = f"p_boot_{param}"
    col = C_P if param == "P" else C_M
    sig = [r.get(pk) is not None and r[pk] < 0.10 for r in rows]
    fig = go.Figure(go.Scatter(
        x=[r[f"theta_{param}"] for r in rows], y=[r["variant"] for r in rows], mode="markers",
        marker=dict(size=12, color=[col if s else "white" for s in sig], line=dict(color=col, width=2), symbol="circle"),
        customdata=[[r.get(pk), r.get("n")] for r in rows],
        hovertemplate="%{y}<br>θ = %{x:.3f}<br>one-sided p = %{customdata[0]:.3f} · n = %{customdata[1]}<extra></extra>"))
    fig.add_vline(x=0, line=dict(color=INK2))
    base_val = K["ardl"][f"theta_{param}"]
    fig.add_vline(x=base_val, line=dict(color=col, dash="dot"))
    base_layout(fig, height=34 * len(rows) + 80, legend=False, hover="closest", xtitle=f"θ_{param}")
    fig.update_layout(margin=dict(l=330, t=20))
    fig.update_xaxes(showgrid=True, gridcolor=GRID)
    return fig


def power_fig():
    fig = go.Figure()
    for v, col in [("M", C_M), ("P", C_P)]:
        rows = [r for r in DATA["power"] if r["index"] == v]
        fig.add_trace(go.Scatter(x=[r["theta_abs"] for r in rows], y=[r["power_size_adjusted"] for r in rows], name=f"θ_{v}",
                                 mode="lines+markers", line=dict(color=col, width=2.5), marker=dict(size=8),
                                 hovertemplate=f"θ_{v}: |θ| = %{{x}} → power %{{y:.2f}}<extra></extra>"))
    fig.add_hline(y=0.8, line=dict(color=MUTED, dash="dot"))
    fig.add_annotation(x=1.5, y=0.8, text="80% power", showarrow=False, xanchor="right", yanchor="bottom", font=dict(color=INK2, size=11))
    fig.add_vline(x=K["power"]["MDE_P"], line=dict(color=MUTED, dash="dot"))
    fig.add_annotation(x=K["power"]["MDE_P"], y=0.05, text=f" MDE ≈ {K['power']['MDE_P']:.2f}", showarrow=False, xanchor="left", font=dict(color=INK2, size=11))
    base_layout(fig, height=340, xtitle="true |θ| (log points per index unit)", ytitle="size-adjusted power", hover="x unified")
    fig.update_yaxes(range=[0, 1.02])
    return fig


def its_fig():
    rows = [r for r in DATA["its"]]
    fig = go.Figure()
    for out, col in [("CRF3 emissions", BLUE), ("Dairy cows", ORANGE)]:
        rr = [r for r in rows if r["outcome"] == out]
        fig.add_trace(go.Bar(x=[str(r["event"]) for r in rr], y=[r["slope_change_pct_per_yr"] for r in rr], name=out,
                             marker=dict(color=col, cornerradius=3),
                             text=[f"p {pfmt(r['p_slope'])}" for r in rr], textposition="outside", cliponaxis=False,
                             hovertemplate=f"{out} %{{x}}: slope change %{{y:+.2f}} pp/yr<extra></extra>"))
    fig.add_hline(y=0, line=dict(color=INK2))
    base_layout(fig, height=360, ytitle="change in trend, percentage points per year", xtitle="pre-specified event", hover="closest")
    fig.update_layout(barmode="group")
    fig.add_annotation(x="2022", y=-7.5, text="descriptive only (3 post-years)", showarrow=False, font=dict(size=11, color=MUTED), yshift=-14)
    return fig


def event_fig(outcome):
    rows = [r for r in DATA["event"] if r["outcome"] == outcome]
    yrs = [r["year"] for r in rows]
    b = [100 * r["beta"] for r in rows]
    lo = [100 * (r["beta"] - 1.645 * r["se"]) for r in rows]
    hi = [100 * (r["beta"] + 1.645 * r["se"]) for r in rows]
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=yrs + yrs[::-1], y=hi + lo[::-1], fill="toself", fillcolor="rgba(42,120,214,0.15)", line=dict(width=0),
                             hoverinfo="skip", name="90% band (5 clusters, indicative)"))
    fig.add_trace(go.Scatter(x=yrs, y=b, mode="lines+markers", line=dict(color=BLUE, width=2.5), marker=dict(size=7), name="event-study coefficient",
                             hovertemplate="%{x}: %{y:+.2f}% per 10 pp exposure<extra></extra>"))
    fig.add_hline(y=0, line=dict(color=INK2)); fig.add_vline(x=2014.5, line=dict(color=MUTED, dash="dot"))
    fig.add_annotation(x=2014.5, y=1, yref="paper", text=" quota abolition", showarrow=False, xanchor="left", yanchor="top", font=dict(color=INK2, size=11))
    base_layout(fig, height=380, ytitle="% difference per 10 pp more pre-2015 dairy exposure (2014 = 0)")
    return fig


def mech_fig():
    rows = DATA["mech"]
    outs = ["activity effect (kt)", "dairy-herd activity effect (kt)", "intensity effect (kt)"]
    fig = go.Figure()
    for pol, col in [("P", C_P), ("M", C_M)]:
        rr = {r["outcome"]: r for r in rows if r["policy"] == pol}
        fig.add_trace(go.Bar(x=[o.replace(" (kt)", "") for o in outs], y=[rr[o]["kt_per_0p1"] for o in outs], name=f"Δ{pol} (per +0.1)",
                             marker=dict(color=col, cornerradius=3), text=[f"p = {rr[o]['p_two_sided']:.2f}" for o in outs],
                             textposition="outside", cliponaxis=False,
                             error_y=dict(type="data", array=[0.1 * 1.645 * rr[o]["se"] for o in outs], color=INK2, thickness=1.2, width=5),
                             hovertemplate=f"Δ{pol}: %{{y:+.1f}} kt per 0.1<extra></extra>"))
    fig.add_hline(y=0, line=dict(color=INK2))
    base_layout(fig, height=400, ytitle="kt CO₂e per +0.1 index units (±90% CI)", hover="closest")
    fig.update_layout(barmode="group")
    return fig


def ceiling_fig(user_g=None):
    rows = DATA["ceiling"]
    labels = ["Trend +0.37%/yr", "−1%/yr", "−2%/yr", "−3%/yr"]
    vals = [r["required_LU_change_vs_2024_pct"] for r in rows]
    cols = [RED, ORANGE, YELLOW, AQUA]
    if user_g is not None:
        labels.append(f"Yours {user_g:+.1f}%/yr".replace("-", "−"))
        vals.append(required_lu(user_g)[1]); cols.append(VIOLET)
    fig = go.Figure(go.Bar(x=labels, y=vals, marker=dict(color=cols, cornerradius=4),
                           text=[f"{v:+.1f}%".replace("-", "−") for v in vals], textposition="outside", cliponaxis=False,
                           hovertemplate="%{x}: livestock units must change by %{y:.1f}% (2024→2030)<extra></extra>"))
    fig.add_hline(y=0, line=dict(color=INK2))
    base_layout(fig, height=360, legend=False, ytitle="required LU change 2024→30, %",
                xtitle="assumed change in emissions per livestock unit", hover="closest")
    fig.update_yaxes(range=[min(vals) - 6, max(3, max(vals) + 5)])
    return fig


def required_lu(g_pct):
    c = K["ceiling_2030"]
    lu24 = value("livestock_units", 2024)
    I24 = c["crf3_2024"] / lu24
    I30 = I24 * (1 + g_pct / 100) ** 6
    lu30 = c["target_2030"] / I30
    return lu30, 100 * (lu30 / lu24 - 1), lu24


def gwp_fig():
    rows = DATA["gwpstar"]
    yrs = [r["Year"] for r in rows]
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=yrs, y=[r["ch4_gwp100_kt"] / 1e3 for r in rows], name="CH₄ in GWP100 (kt CO₂e)", line=dict(color=BLUE, width=2.5)))
    fig.add_trace(go.Scatter(x=yrs, y=[r["ch4_gwpstar_kt"] / 1e3 for r in rows], name="CH₄ in GWP* (CO₂-warming-equivalent)", line=dict(color=ORANGE, width=2.5)))
    fig.add_hline(y=0, line=dict(color=INK2))
    base_layout(fig, height=360, ytitle="Mt CO₂e / CO₂-we")
    return fig


# ------------------------------------------------------------------ tabs
def t_indices():
    p = K["policy"]
    return html.Div([
        kpi_row(kpi(f"{p['M_2000']:.2f} → {p['M_2024']:.2f}", "Mitigation intensity M, 2000 → 2024", tone="tone-blue"),
                kpi(f"{p['P_2000']:.2f} → {p['P_2024']:.2f}", "Production pressure P, 2000 → 2024", tone="tone-orange"),
                kpi(f"{p['S_2000']:+.2f} → {p['S_2024']:+.2f}".replace("-", "−"), "Net signal S = M − P", tone="tone-aqua"),
                kpi(f"+{p['largest_P_step']:.3f}", f"largest one-year rise in P ({p['largest_P_step_year']})", "quota abolition and TAMS II at full scale")),
        card(dcc.Checklist(id="rs-ix-show", value=["M", "P", "S"], inline=True, className="chk",
                           options=[{"label": " M", "value": "M"}, {"label": " P", "value": "P"}, {"label": " S", "value": "S"},
                                    {"label": " G (strategies)", "value": "G"}]),
             dcc.Graph(id="rs-ix-fig", figure=indices_fig(["M", "P", "S"]), config=GRAPH_CONFIG, className="graph")),
        reading("The annual mitigation index M, the production-pressure index P and their difference S, built from the 16 scored instruments "
                "(11 mitigation, 5 pressure). The strategy signal G (3 national growth strategies) is shown separately and is not part of P.",
                "Higher M = more mitigation policy in force, weighted by coverage and bindingness. Higher P = more expansion policy. "
                "S above zero means mitigation outweighs pressure on this common scale.",
                f"P was high until 2004 (coupled headage premia, {p['P_2000']:.2f}), collapsed with decoupling in 2005, then rebuilt step by step "
                f"through the quota increases, the derogation, quota abolition and TAMS II, reaching {p['P_2024']:.2f} in 2024 — about its 2000 level. "
                "M rose in steps (Nitrates Action Programme 2006–09; GLAS, suckler programmes and SDAS 2015–17; chemical-N maxima and ACRES 2022–24). "
                f"S has been positive since {p['first_year_S_positive']}, but because P and M rose in the same years the net signal grew far less "
                f"than mitigation effort — policy incoherence, made measurable. The strategy signal G peaks at {max(COLS['G']):.2f} and is not part of P."),
    ])


def t_breaks():
    b = K["breaks"]
    seg_rows = []
    edges = [1990] + b["break_years"] + [2025]
    for j, s in enumerate(b["segment_slopes_pct"]):
        seg_rows.append({"segment": f"{edges[j]}–{edges[j + 1] - 1}", "slope": s,
                         "ci": "–" if j == 0 else f"break 90% interval {b['ci90'][j - 1][0]}–{b['ci90'][j - 1][1]}"})
    return html.Div([
        kpi_row(kpi(f"{K['trend']['sen_pct']:+.2f}%/yr".replace("-", "−"), "Theil–Sen slope 1990–2024", f"Hamed–Rao p = {K['trend']['p_hamed_rao']:.2f}: no monotonic trend"),
                kpi(f"{b['UDmax']:.1f}", "UDmax statistic", f"bootstrap p = {b['p_UDmax']:.3f}: one trend rejected", tone="tone-orange"),
                kpi(str(b["m"]), "breaks selected by BIC", ", ".join(map(str, b["break_years"]))),
                kpi("✕ H1", "no break within ±1 yr of 2010 or 2015", tone="tone-red")),
        card(dcc.Checklist(id="rs-br-ci", value=["ci"], inline=True, className="chk", options=[{"label": " Show 90% break-date intervals", "value": "ci"}]),
             dcc.Graph(id="rs-br-fig", figure=breaks_fig(), config=GRAPH_CONFIG, className="graph"),
             fig_note("Orange segments: the Bai–Perron model with three breaks; dashed lines: first year of each new regime; "
                      "shaded: 90% bootstrap intervals for the break dates; dotted grey: policy dates.")),
        two_col(table(seg_rows, [("segment", "Regime"), ("slope", "Trend, % per year", num(2)), ("ci", "Break uncertainty")], sort=False),
                table([{"test": r["test"], "S": r["S"], "z": r["z"], "p": r["p"], "sen": r["sen_slope_pct_per_yr"]} for r in DATA["trend"]],
                      [("test", "Mann–Kendall test"), ("z", "z", num(2)), ("p", "p", num(3)), ("sen", "Sen %/yr", num(2))], sort=False)),
        reading("Whether the emission path is one trend or several regimes, and where the regime changes fall.",
                "A flat full-period slope can hide large opposite movements. The orange segments are the best-fitting piecewise trend; "
                "the % per year labels show each regime's growth rate.",
                "Emissions rose 1.1%/yr to 1999, fell 1.25%/yr in 2000–2011, rose 2.0%/yr in 2012–2019 and fell 1.9%/yr from 2020. None of the "
                "break dates lies within a year of 2010 or 2015, so H1 is not supported. The upturn starts two years after Food Harvest 2020 and "
                "three years before quota abolition — consistent with expansion that anticipated abolition during the 2009–2014 quota increases. "
                f"Known-date Chow tests reject stability at 2010 and 2015 (both p < 0.001), but with three breaks they cannot attribute the change to either date."),
    ])


def t_lmdi():
    rows = DATA["lmdi_phase"]
    l = K["lmdi"]
    return html.Div([
        kpi_row(kpi(f"+{l['P4_activity_plus_productivity']:,.0f} kt", "P4 (2014–21): activity + productivity", tone="tone-orange"),
                kpi(f"−{-l['P4_intensity']:,.0f} kt", "P4: intensity effect", tone="tone-aqua"),
                kpi(f"{l['P4_intensity_offset']:.2f}", "intensity offset IO after quota abolition", "only a third of growth cancelled", tone="tone-red"),
                kpi(f"{l['dairy_herd_P4_range'][0] / 1e3:.2f}–{l['dairy_herd_P4_range'][1] / 1e3:.2f} Mt", "added by dairy-herd growth alone, 2014–21",
                    "across EF ratios 1.8–2.6")),
        card(dcc.Graph(figure=lmdi_phase_fig(), config=GRAPH_CONFIG, className="graph"),
             fig_note("Bars: cumulative LMDI factor effects within each policy phase; diamonds: net change in CRF3. P2 includes the 2004–05 "
                      "classification break (dairy activity −340 kt, partly offset by +191 kt productivity). P5 ends in 2023.")),
        table([{"phase": r["phase"], "years": r["years"], "activity": r["activity"], "productivity": r["productivity"], "intensity": r["intensity"],
                "other": r["other"], "net": r["net_change"], "io": r["intensity_offset"]} for r in rows],
              [("phase", "Phase"), ("years", "Years"), ("activity", "Activity", num(0)), ("productivity", "Productivity", num(0)),
               ("intensity", "Intensity", num(0)), ("other", "Other", num(0)), ("net", "Net change", num(0)), ("io", "Intensity offset", num(2))], sort=False),
        section("Drill down: which component moved in each phase",
                card(dcc.RadioItems(id="rs-lm-ph", value="P4", inline=True, className="seg",
                                    options=[{"label": f"{p[0]} {p[1]}", "value": p[0]} for p in PHASES]),
                     dcc.Graph(id="rs-lm-comp", figure=lmdi_component_fig("P4"), config=GRAPH_CONFIG, className="graph"))),
        section("Year by year", card(dcc.Graph(figure=lmdi_annual_fig(), config=GRAPH_CONFIG, className="graph"),
                                     fig_note("Chained annual LMDI effects 1993–2023; dotted lines separate policy phases."))),
        details("Sensitivity to the dairy / non-dairy emission-factor ratio",
                table([{"r": r["ef_ratio"], "d": r["dairy_herd_effect_P4"], "io": r["intensity_offset_P4"]} for r in DATA["lmdi_sens"]],
                      [("r", "EF ratio", num(1)), ("d", "P4 dairy-herd effect, kt", num(0)), ("io", "P4 intensity offset", num(2))], sort=False)),
        reading("An exact split of the change in emissions into scale (animals, N), yield (milk per cow) and intensity (emissions per unit).",
                "Bars above zero pushed emissions up. The intensity offset IO compares the intensity bar with the activity + productivity bars: "
                "IO = 1 would mean efficiency fully cancelled growth.",
                "After quota abolition, scale and yield growth (+2,988 kt) outran intensity gains (−963 kt): IO = 0.32, so H2 is supported, and "
                "it stays between 0.21 and 0.33 across emission-factor ratios. In 2009–2014 intensity rose rather than fell (+175 kt). In the "
                "phases where emissions fell (1992–2009, 2021–2023) they fell mainly because herds and fertiliser use shrank, not because intensity improved."),
    ])


def t_ardl():
    a = K["ardl"]
    lr = {r["index"]: r for r in DATA["long_run"]}
    return html.Div([
        kpi_row(kpi(f"θ_P = {a['theta_P']:.2f}", f"long-run pressure effect (SE {a['se_P']:.2f})", f"bootstrap p = {a['p_boot_P']:.3f} → H3b ✓", tone="tone-orange"),
                kpi(f"+{a['pct_per_0p1_P']:.1f}%", "emissions per sustained +0.1 in P", f"+{lr['P']['pct_per_sd']:.1f}% per 1 SD"),
                kpi(f"θ_M = +{a['theta_M']:.2f}", f"long-run mitigation effect (SE {a['se_M']:.2f})", f"bootstrap p (θ_M<0) = {a['p_boot_M']:.3f} → H3a ✕", tone="tone-blue"),
                kpi(f"F = {a['bounds_F']:.2f}", "bounds test (10% verdict)", a["bounds_verdict_10"], tone="tone-red" if a["bounds_verdict_10"].startswith("no") else "")),
        card(html.H3("Long-run multipliers with 90% bootstrap intervals"), dcc.Graph(figure=forest_fig(), config=GRAPH_CONFIG, className="graph")),
        two_col(card(dcc.Graph(figure=boot_scatter_fig(), config=GRAPH_CONFIG, className="graph")),
                html.Div([
                    table([{"ix": "M" if r["index"] == "M" else "P", "theta": r["theta"], "se": r["se_delta_HAC"], "phac": r["p_HAC_one_sided"],
                            "pb": r["p_boot_one_sided"], "p01": r["pct_per_0p1"], "psd": r["pct_per_sd"]} for r in DATA["long_run"]],
                          [("ix", "Index"), ("theta", "θ", num(3)), ("se", "SE (delta, HAC)", num(3)), ("phac", "HAC p", num(3)),
                           ("pb", "bootstrap p", num(3)), ("p01", "% per +0.1", num(1)), ("psd", "% per 1 SD", num(1))], sort=False),
                    callout("caution", "Model checks",
                            f"ARDL({a['model']['p']},{a['model']['qM']},{a['model']['qP']}) on {a['years'].replace('-', '–')} (n = {a['n']}). Every diagnostic passes at 10% "
                            "(" + ", ".join(f"{r['test'].split(' (')[0]} p = {r['p']:.2f}" for r in DATA["diag"]) + "). "
                            f"Equal-and-opposite per-unit effects are rejected (p = {a['p_equal_opposite']:.3f}). The bounds test does not find a "
                            "level relationship, so the long-run multipliers should be read as indicative."),
                ]), ratio="1-1"),
        reading("How strongly long-run emissions respond to each policy index, with the uncertainty from 999 bootstrap re-estimations.",
                "θ is the log-point change in long-run emissions per 1-unit change in an index; 100 × (exp(0.1 × θ) − 1) gives the % change per 0.1 index units. A dot right of "
                "zero with an interval that excludes zero means the index is associated with higher emissions.",
                f"Production pressure is associated with higher long-run emissions: +{a['pct_per_0p1_P']:.1f}% per sustained 0.1-unit rise "
                f"(bootstrap p = {a['p_boot_P']:.3f}), so H3b is supported at 10%. The mitigation coefficient has the wrong sign (+{a['theta_M']:.2f}; "
                f"bootstrap p = {a['p_boot_M']:.2f}), so H3a is not supported; it reflects schemes expanding in the same years as output (reverse timing). "
                f"The bounds test (F = {a['bounds_F']:.2f}) does not confirm a level relationship, so these are conditional associations, not causal estimates."),
    ])


def t_cf():
    o = K["offset"]
    return html.Div([
        kpi_row(kpi(f"{o['pressure_effect_pct']:+.1f}%", "2024 emissions due to pressure above its 2000 level",
                    f"90% CI [{o['pressure_lo']:.1f}, {o['pressure_hi']:.1f}]", tone="tone-orange"),
                kpi(f"{o['cum_P_kt'] / 1e3:+.1f} Mt".replace("-", "−"), "cumulative CO₂e due to pressure vs its 2000 level, 2000–2024",
                    "negative: P stayed below its 2000 level until the 2010s"),
                kpi(f"+{o['mitigation_effect_pct']:.1f}%", "'effect' of the rise in M since 2000", f"90% CI [{o['mitigation_lo']:.1f}, {o['mitigation_hi']:.1f}]".replace("-", "−"), tone="tone-blue"),
                kpi(f"{sum(1 for r in DATA['boot_draws'] if r['dM'] is not None and r['dM'] < 0)} in {len(DATA['boot_draws'])}",
                    "bootstrap draws with a negative M effect", "offset ratio undefined → H3c ✕", tone="tone-red")),
        card(dcc.Checklist(id="rs-cf-show", value=["no_pressure_change_kt", "no_mitigation_change_kt"], inline=True, className="chk",
                           options=[{"label": " P frozen at 2000", "value": "no_pressure_change_kt"},
                                    {"label": " M frozen at 2000", "value": "no_mitigation_change_kt"},
                                    {"label": " Both frozen", "value": "neither_kt"}]),
             dcc.Graph(id="rs-cf-fig", figure=cf_paths_fig(["no_pressure_change_kt", "no_mitigation_change_kt"]), config=GRAPH_CONFIG, className="graph"),
             fig_note("Counterfactual paths simulate the fitted ARDL with an index held at its 2000 value. The gap between the black and orange "
                      "lines is the emission footprint of production-oriented policy.")),
        card(html.Div(className="control-row", children=[html.Span("Bootstrap distribution of the 2024 effect:", className="ctl-label"),
                                                          dcc.RadioItems(id="rs-cf-h", value="P", inline=True, className="seg",
                                                                         options=[{"label": "Pressure", "value": "P"}, {"label": "Mitigation", "value": "M"}])]),
             dcc.Graph(id="rs-cf-hist", figure=effect_hist_fig("P"), config=GRAPH_CONFIG, className="graph")),
        reading("What emissions would have been without the post-2000 change in each index, according to the fitted model.",
                "If the dashed line lies below the observed line, the index pushed emissions up. The offset ratio would compare the pressure effect "
                "with a (negative) mitigation effect.",
                f"P in 2024 is only slightly above its 2000 level, so the model attributes a small rise in 2024 emissions to pressure "
                f"({o['pressure_effect_pct']:+.1f}%, 90% CI {o['pressure_lo']:.1f}–{o['pressure_hi']:.1f}%). Over 2000–2024 the cumulative pressure "
                f"effect is {o['cum_P_kt'] / 1e3:+.1f} Mt CO₂e, because P sat below its 2000 level (coupled premia) through most of the 2000s. "
                "The rise in M is associated with higher, not lower, emissions (its interval includes zero), so the offset ratio is undefined in "
                "the point estimate and H3c is not supported."),
    ])


def t_robust():
    r = K["robustness"]
    return html.Div([
        kpi_row(kpi(f"{r['same_sign_P']} / {r['m_estimable']}", "core specifications with θ_P > 0", f"{r['sig_P']} significant at 10%", tone="tone-orange"),
                kpi(f"{r['loo_sig_P']} / {r['loo_n']}", "leave-one-policy-out runs significant", f"θ_P {r['loo_theta_P_range'][0]:.2f}–{r['loo_theta_P_range'][1]:.2f}"),
                kpi(str(r["sig_M_negative"]), "specifications with θ_M significantly negative", tone="tone-blue"),
                kpi(f"|θ| ≈ {K['power']['MDE_P']:.2f}", "minimum detectable effect (80% power)", "≈ 4% per 0.1 index units")),
        card(html.Div(className="control-row", children=[html.Span("Parameter", className="ctl-label"),
                                                          dcc.RadioItems(id="rs-rb-par", value="P", inline=True, className="seg",
                                                                         options=[{"label": "θ_P (pressure)", "value": "P"}, {"label": "θ_M (mitigation)", "value": "M"}])]),
             dcc.Graph(id="rs-rb-fig", figure=robust_fig("P"), config=GRAPH_CONFIG, className="graph"),
             fig_note("Filled circle = one-sided bootstrap p < 0.10; hollow = not significant. The dotted line is the baseline estimate. "
                      "Leave-one-out rows drop one pressure policy from P at a time.")),
        two_col(card(html.H3("Power curves"), dcc.Graph(figure=power_fig(), config=GRAPH_CONFIG, className="graph"),
                     fig_note(f"Nominal 10% HAC tests have true size {K['power']['size_nominal_M']:.2f} (M) and {K['power']['size_nominal_P']:.2f} (P); "
                              "power uses size-adjusted critical values.")),
                card(html.H3("Mitigation sub-indices (RQ4a)"),
                     table([{"s": r_["sub_index"], "n": r_["active_years"], "t": r_["theta"], "p": r_["p_boot_one_sided"], "l3": r_["theta_lag3"]} for r_ in DATA["subindex"]],
                           [("s", "Instrument type"), ("n", "active yrs"), ("t", "θ", num(2)), ("p", "boot p (θ<0)", num(3)), ("l3", "θ at 3-yr lag", num(2))], sort=False),
                     callout("finding", "H4a not supported", "The mandatory sub-index (Nitrates Action Programme, chemical-N maxima) has no detectable "
                             f"emission-reducing effect (θ = +{K['subindex']['mandatory']['theta']:.2f}). Only the voluntary sub-index (Carbon Navigator, "
                             f"SDAS, SBLAS; 12 active years) is negative and significant (θ = {K['subindex']['voluntary']['theta']:.2f}, "
                             f"p = {K['subindex']['voluntary']['p_boot_one_sided']:.2f}), with a wide standard error; the incentive sub-index turns "
                             "negative only at 2–3-year lags, not tested formally."))),
        section("Timing: interrupted time series at the pre-specified dates",
                card(dcc.Graph(figure=its_fig(), config=GRAPH_CONFIG, className="graph")),
                callout("finding", "The turn came in 2010, not 2015",
                        "Controlling for prices, the emission trend steepened by 2.2 points a year after 2010 (p < 0.001) and the dairy-herd trend by 4.2 "
                        "points. Neither changed significantly at 2015 (emissions −0.2, p = 0.38). Expansion began under the quota increases and Food "
                        "Harvest 2020 and continued at the same pace after abolition.")),
        reading("Whether the headline results survive alternative modelling choices, and how large an effect the data could detect.",
                "Each dot is θ re-estimated under one alternative choice. A robust result keeps its sign across ≥ 80% of variants.",
                f"θ_P is positive in all {r['m_estimable']} estimable variants and significant in {r['sig_P']}; it loses significance with fixed lags, "
                "with NAP down-weighted, and with GNI* and shock-year dummies (GNI* is collinear with quota abolition). Dropping quota abolition (P04) "
                f"is the one leave-one-out run that is not significant. θ_M is significantly negative in {r['sig_M_negative']} variants — when the "
                "Nitrates Action Programme is dropped from M and when the 2021–22 climate framework is scored in M — so the mitigation result depends "
                f"on how the NAP and the framework laws are treated. Mitigation effects larger than |θ| ≈ {K['power']['MDE_M']:.2f} would very likely "
                "have been detected; smaller ones cannot be ruled out."),
    ])


def t_regional():
    did = DATA["did"]
    return html.Div([
        kpi_row(kpi("16% → 74%", "pre-2015 dairy exposure: West → South-West"),
                kpi(f"+{did[4]['pct_per_10pp']:.1f}%", "imputed emissions per +10 pp exposure after 2015 (TWFE)",
                    f"p_RI = {did[4]['p_randomisation']:.2f}, p_WCB = {did[4]['p_wild_cluster']:.2f}"),
                kpi("+1.6%", "placebo dated 2010 (pre-2015 data only)", "p_RI = 0.017 — pre-trends", tone="tone-red"),
                kpi("✕ H4b", "parallel trends fail", tone="tone-red")),
        card(html.Div(className="control-row", children=[html.Span("Outcome", className="ctl-label"),
                                                          dcc.RadioItems(id="rs-ev-out", value="log imputed livestock emissions", inline=True, className="seg",
                                                                         options=[{"label": "Imputed emissions", "value": "log imputed livestock emissions"},
                                                                                  {"label": "Dairy cows", "value": "log dairy cows"},
                                                                                  {"label": "Livestock units", "value": "log livestock units"}])]),
             dcc.Graph(id="rs-ev-fig", figure=event_fig("log imputed livestock emissions"), config=GRAPH_CONFIG, className="graph"),
             fig_note("Event-study coefficients relative to 2014, per 10 percentage points of exposure; 90% band from cluster-robust errors with five clusters (indicative only).")),
        table([{"o": r["outcome"], "s": r["specification"], "b": r["pct_per_10pp"], "ri": r["p_randomisation"], "wcb": r["p_wild_cluster"],
                "pl": r["placebo_2010_pct"], "plp": r["placebo_2010_p_randomisation"]} for r in did],
              [("o", "Outcome"), ("s", "Specification"), ("b", "% per +10 pp, post-2015", num(2)), ("ri", "p (randomisation)", num(3)),
               ("wcb", "p (wild cluster)", num(3)), ("pl", "placebo 2010, %", num(2)), ("plp", "placebo p (RI)", num(3))], sort=False),
        reading("Whether regions with more dairy before 2015 grew faster after quota abolition than regions with less.",
                "A flat line at zero before 2015 and a rise afterwards would support a quota-abolition effect. A line already rising before 2015 "
                "means the regions were diverging anyway (failed parallel trends).",
                "The gap opens steadily from 2005, and the placebo dated to 2010 is almost as large as the main estimate and significant. More exposed regions "
                "were already diverging before abolition, so H4b is not supported. The dairy herd itself grew no faster in percentage terms in more exposed "
                "regions (−0.5% per 10 pp; p = 0.84): post-quota growth was national and partly came from low-dairy regions."),
    ])


def t_mech():
    MECH = K["mechanism"]
    return html.Div([
        card(dcc.Graph(figure=mech_fig(), config=GRAPH_CONFIG, className="graph"),
             fig_note("Sum of the contemporaneous and one-year-lagged coefficients, scaled to a +0.1 change in the index; Newey–West errors; 1997–2023, n = 27.")),
        table([{"o": r["outcome"], "p": r["policy"], "k": r["kt_per_0p1"], "se": 0.1 * r["se"], "pv": r["p_two_sided"]} for r in DATA["mech"]],
              [("o", "LMDI outcome"), ("p", "Policy"), ("k", "kt per +0.1", num(1)), ("se", "SE (per 0.1)", num(1)), ("pv", "p (two-sided)", num(3))], sort=False),
        reading("Whether year-to-year changes in P and M line up with the activity and intensity parts of the decomposition.",
                "The framework predicts orange bars above zero for activity (pressure → more animals) and blue bars below zero for intensity "
                "(mitigation → less per unit).",
                "The pressure half of the division of labour is confirmed. ΔP is associated with the activity effect "
                f"(+{MECH['activity effect (kt)|P']['kt_per_0p1']:.0f} kt per 0.1; p = {MECH['activity effect (kt)|P']['p']:.3f}), including the dairy-herd "
                f"activity effect (+{MECH['dairy-herd activity effect (kt)|P']['kt_per_0p1']:.0f} kt; p = {MECH['dairy-herd activity effect (kt)|P']['p']:.3f}), "
                f"and not with the intensity effect (p = {MECH['intensity effect (kt)|P']['p']:.2f}). ΔM is associated with neither, so the mitigation "
                "half is not confirmed."),
    ])


def t_ceiling():
    c = K["ceiling_2030"]
    lu30, ch, lu24 = required_lu(c["intensity_trend_pct"])
    return html.Div([
        kpi_row(kpi(f"{c['target_2030'] / 1e3:.1f} Mt", "2030 target (0.75 × 2018)", tone="tone-red"),
                kpi(f"{c['crf3_2024'] / 1e3:.1f} Mt", "CRF3 in 2024", f"{c['gap_pct_2024']:+.1f}% vs 2018".replace("-", "−")),
                kpi(f"+{c['intensity_trend_pct']:.2f}%/yr", "trend in emissions per LU, 2012–24"),
                kpi(f"{c['LU_change_needed_trend']:.0f}%".replace("-", "−"), "livestock units needed by 2030 at that trend", tone="tone-orange")),
        two_col(card(dcc.Graph(id="rs-ce-fig", figure=ceiling_fig(), config=GRAPH_CONFIG, className="graph")),
                card(html.H3("Try your own intensity path"),
                     html.Label("Annual change in emissions per livestock unit, 2024–2030 (%/yr)", className="ctl-label"),
                     dcc.Slider(id="rs-ce-g", min=-6, max=1.5, step=0.1, value=-1.5, marks={x: f"{x}%" for x in [-6, -4, -2, 0, 1]},
                                tooltip={"placement": "bottom"}),
                     html.Div(id="rs-ce-out", className="calc-out"),
                     html.P("For reference: the fastest five-year fall in intensity since 1992 was about 1.1% a year.", className="fig-note")), ratio="3-2"),
        reading("How many livestock units are compatible with the 2030 ceiling for different paths of emissions per livestock unit.",
                "Bars show the required change in livestock units between 2024 and 2030; the more intensity falls, the smaller the herd cut needed.",
                "If the 2012–2024 intensity trend continues, livestock units must fall by about 23% by 2030. Even with intensity falling 1, 2 or 3% a year, "
                "they must still fall by 16%, 11% or 5%. A 3% annual fall is almost three times the fastest five-year rate since 1992."),
    ])


def t_gwp():
    g = K["gwp_star"]
    return html.Div([
        card(dcc.Graph(figure=gwp_fig(), config=GRAPH_CONFIG, className="graph"),
             fig_note("GWP* converts methane into CO₂-warming-equivalents: E* = 4.53·E(t) − 4.25·E(t−20) (Smith et al., 2021).")),
        reading("A supplementary view of methane under the warming-equivalent metric GWP*.",
                "GWP* reflects the change in methane's warming contribution rather than its level; negative values mean methane was lower than 20 years "
                "before. The analysis itself uses GWP100 throughout.",
                f"In 2024 CRF3 methane was {g['ch4_gwp100_2024'] / 1e3:.1f} Mt CO₂e under GWP100 and {g['ch4_gwpstar_2024'] / 1e3:+.1f} Mt CO₂-we under GWP*. "
                "The metric changes the level, not the conclusions about which policies moved emissions."),
    ])


TABS = [("indices", "Policy indices", t_indices), ("rq1", "RQ1 · Trends & breaks", t_breaks), ("rq2", "RQ2 · Decomposition", t_lmdi),
        ("rq3", "RQ3 · Policy-mix model", t_ardl), ("cf", "RQ3 · Counterfactuals", t_cf), ("rob", "Robustness, power & timing", t_robust),
        ("rq4", "RQ4 · Regional DiD", t_regional), ("mech", "Mechanism link", t_mech), ("ceiling", "2030 ceiling", t_ceiling),
        ("gwp", "GWP* supplement", t_gwp)]


def layout():
    return html.Div([
        page_header("Step 5 · Results", "What the analysis found",
                    "Each result comes with what it shows, how to read it, and the finding in plain language. Start with the hypothesis scorecard, "
                    "then open each tab."),
        section("Hypothesis scorecard", scorecard(),
                callout("finding", "The headline",
                        "Expansion left a footprint; mitigation too little to offset. A sustained 0.1-unit rise in production pressure raised long-run "
                        "emissions by about 7%, adding 12.5 Mt CO₂e over 2000–2024, while the mostly voluntary, intensity-oriented mitigation portfolio "
                        "shows no detectable effect on total emissions.")),
        section("Results in detail",
                dcc.Tabs(id="rs-tabs", value="indices", className="tabs", children=[
                    dcc.Tab(label=lab, value=v, children=html.Div(fn(), className="step-body"), className="tab", selected_className="tab--sel")
                    for v, lab, fn in TABS])),
    ])


def register_callbacks(app):
    @app.callback(Output("rs-ix-fig", "figure"), Input("rs-ix-show", "value"))
    def _ix(show):
        return indices_fig(show or [])

    @app.callback(Output("rs-br-fig", "figure"), Input("rs-br-ci", "value"))
    def _br(ci):
        return breaks_fig(bool(ci))

    @app.callback(Output("rs-lm-comp", "figure"), Input("rs-lm-ph", "value"))
    def _lm(ph):
        return lmdi_component_fig(ph)

    @app.callback(Output("rs-cf-fig", "figure"), Input("rs-cf-show", "value"))
    def _cf(show):
        return cf_paths_fig(show or [])

    @app.callback(Output("rs-cf-hist", "figure"), Input("rs-cf-h", "value"))
    def _h(w):
        return effect_hist_fig(w)

    @app.callback(Output("rs-rb-fig", "figure"), Input("rs-rb-par", "value"))
    def _rb(p):
        return robust_fig(p)

    @app.callback(Output("rs-ev-fig", "figure"), Input("rs-ev-out", "value"))
    def _ev(o):
        return event_fig(o)

    @app.callback(Output("rs-ce-fig", "figure"), Output("rs-ce-out", "children"), Input("rs-ce-g", "value"))
    def _ce(g):
        lu30, ch, lu24 = required_lu(g)
        out = [html.Div(f"{ch:+.1f}%".replace("-", "−"), className="calc-big"),
               html.Div(f"required change in livestock units 2024→2030 "
                        f"({lu24 / 1e3:,.2f} → {lu30 / 1e3:,.2f} million LU)"),
               html.Div(f"With intensity changing {g:+.1f}%/yr, emissions per LU in 2030 = {(1 + g / 100) ** 6:.3f} × the 2024 level.".replace("-", "−"),
                        className="small")]
        return ceiling_fig(g), out
