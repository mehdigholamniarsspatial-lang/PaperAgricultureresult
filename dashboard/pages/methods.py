"""Step 4 – implementation and methodology, step by step, with the mathematics."""
import math
import plotly.graph_objects as go
from dash import html, dcc, Input, Output

from ..components import (page_header, section, card, callout, maths, md, table, num, two_col, steps_list, details, kpi, kpi_row)
from ..data_store import DATA, KEY, YEARS, COLS, series, value, fmt, pfmt, CODEBOOK, COVERAGE_LABEL, PHASES, EVENTS
from ..theme import (base_layout, add_events, empty_fig, PAL, C_M, C_P, C_S, INK, INK2, MUTED, GRID, BLUE, ORANGE, AQUA, YELLOW,
                     RED, GREEN, FACTOR_COL, FACTOR_LAB, COMP_LAB, GRAPH_CONFIG)

# ------------------------------------------------------------------ helpers


def block(title, *kids):
    return html.Div(className="m-block", children=[html.H3(title), *kids])


def settings(rows):
    return table([{"p": a, "v": b, "w": c} for a, b, c in rows], [("p", "Setting"), ("v", "Value"), ("w", "Why / basis")], page_size=30, sort=False)


def ardl_coefs():
    return {r["index"]: r["coef"] for r in DATA["ardl_coef"]}


# ------------------------------------------------------------------ workflow diagram
WORKFLOW = [
    ("1", "Load & hash", "Files located by name; SHA-256 recorded; duplicates detected"),
    ("2", "Harmonise", "CRF3 boundary · livestock stacking · regions · price chain-link"),
    ("3", "Panels", "Annual panel 1990–2024 · regional panel 5 × 1991–2024"),
    ("4", "Policy indices", "M, P, S = M − P from I × C × B codebooks"),
    ("5", "Models", "Breaks · LMDI · ARDL + bootstrap · counterfactuals · power · DiD · 2030"),
    ("6", "Export & verify", "34 result sheets · 7 figures · 30 independent checks"),
]


def workflow():
    out = []
    for i, (n, t, s) in enumerate(WORKFLOW):
        out.append(html.Div(className="wf-step", children=[html.Div(n, className="wf-num"), html.Div(t, className="wf-t"), html.Div(s, className="wf-s")]))
        if i < len(WORKFLOW) - 1:
            out.append(html.Div("→", className="wf-arrow"))
    return html.Div(className="workflow", children=out)


DESIGNS = html.Div(className="grid-3", children=[
    html.Div(className="card card-accent-blue", children=[html.Div("Design A · descriptive", className="eyebrow"), html.H3("Trends, breaks & decomposition"),
                                                         html.P("Mann–Kendall, Theil–Sen, Bai–Perron with bootstrap UDmax, exact LMDI-I. Answers RQ1, RQ2.")]),
    html.Div(className="card card-accent-orange", children=[html.Div("Design B · policy-mix time series", className="eyebrow"), html.H3("ARDL with block bootstrap"),
                                                           html.P("ARDL(1,0,2), 1997–2024, n = 28; restricted bootstrap p-values; counterfactuals; power/MDE. Answers RQ3.")]),
    html.Div(className="card card-accent-aqua", children=[html.Div("Design C · within-Ireland comparison", className="eyebrow"), html.H3("Regional DiD"),
                                                         html.P("Five constant-boundary regions; exposure = pre-2015 dairy share; randomisation inference. Answers RQ4.")]),
])


# ------------------------------------------------------------------ step contents
def step_data():
    return html.Div([
        callout("plain", "Purpose", "Turn 58 raw files from four agencies into one consistent annual panel without changing any source value and without "
                "inventing missing years."),
        block("1.1 The outcome: CRF sector 3",
              maths(r"E_t^{\text{CRF3}} = E_t^{\text{Agriculture}} - E_t^{1.A.4.c.ii} - E_t^{1.A.4.c.iii}"
                    r"\;=\;\sum_{c\in\{3A,3B,3D,3G,3H\}} E_{c,t}\;=\;E^{CO_2}_t+28\,E^{CH_4}_t+265\,E^{N_2O}_t"),
              md("Emissions are in kt CO₂-equivalent using AR5 100-year GWPs (CH₄ = 28, N₂O = 265), the metric of Ireland's inventory. "
                 "The two identities on the right are checked every run (gap < 0.0001%).")),
        block("1.2 Livestock, livestock units and nitrogen",
              maths(r"\text{LU}_t = 1.0\cdot D_t + \sum_{k} \lambda_k N_{k,t} + 0.1\cdot Sh_t,\qquad \lambda_k\in\{0.4,0.7,0.8,1.0\}"),
              maths(r"N^{\text{manure}}_t=\frac{\text{nex}^{D}_t D_t+\text{nex}^{O}_t O_t+\text{nex}^{Sh}_t Sh_t}{10^3},\qquad "
                    r"\text{yield}_t=\frac{\text{milk}_t\,(10^6\,\text{L})\times 10^3}{D_t\,(10^3\ \text{head})}"),
              md("$D$ = dairy cows, $O$ = other cattle, $Sh$ = sheep, $N_{k}$ = CSO non-dairy cattle categories with Eurostat LSU coefficients "
                 "$\\lambda_k$; nex = N excretion (kg N/head/yr) from CRT Table 3.B(b).", math=True)),
        block("1.3 Price indices: chain-linking and deflation",
              maths(r"\tilde I^{\,old}_{t}=I^{old}_t\cdot\exp\!\Big(\frac{1}{|\mathcal O|}\sum_{s\in\mathcal O}\ln\frac{I^{new}_s}{I^{old}_s}\Big),"
                    r"\qquad p^{real}_t=\frac{\tilde I_t}{CPI_t}\times 100\quad(2020=100)"),
              md("$\\mathcal O$ = overlapping years between an older and a newer vintage. The newest vintage is kept in overlaps; "
                 "the geometric mean treats ratios symmetrically (Eurostat, 2016).", math=True)),
        block("Step by step", steps_list([
            "Locate each table by its file-name stem (newest download wins); hash with SHA-256; report byte-identical duplicates.",
            "Compute CRF3 from the EPA workbook; verify against the category and gas sums.",
            "Read the 34 CRT 2025 workbooks for the dairy/non-dairy CH₄ split, N excretion and 1990–99 mineral N (kg → t).",
            "Stack CSO livestock tables (disjoint years); aggregate regions to five constant-boundary units; flag the 2004→05 break.",
            "Chain-link five price vintages; deflate by CPI; take logs of the controls.",
            "Join everything on Year into a 35-row panel; never interpolate; record first/last year and n for each column.",
        ])),
        block("Settings", settings([
            ("Analysis window", "1990–2024", "UNFCCC base year to the last full inventory year"),
            ("GWP100", "CH₄ 28, N₂O 265", "AR5 (Myhre et al., 2013), as used by Ireland's inventory"),
            ("Price base", "2020 = 100", "Newest CSO vintage, so recent data are not rescaled"),
            ("2005 break indicator", "dummy / region × post-2005", "CSO table switch: dairy −8.7% vs cattle −0.3%"),
            ("Missing values", "left missing", "No interpolation, back-casting or zero-filling"),
        ])),
    ])


def contrib_fig(which):
    sc = DATA["scoreM" if which == "M" else "scoreP"]
    fig = go.Figure()
    pids = [p for p in sc["cols"] if max(sc["cols"][p]) > 0]
    for i, p in enumerate(pids):
        col = PAL[i % 8]
        fig.add_trace(go.Bar(x=sc["years"], y=sc["cols"][p], name=f"{p}", marker=dict(color=col, line=dict(color="#fcfcfb", width=0.6)),
                             hovertemplate=f"{p} · {CODEBOOK[p]['name'][:50]}<br>%{{x}}: %{{y:.4f}}<extra></extra>"))
    tot = DATA["key"]["policy"]
    ys, idx = series(which)
    fig.add_trace(go.Scatter(x=ys, y=idx, name=f"{which} (sum)", mode="lines", line=dict(color=INK, width=2),
                             hovertemplate=f"{which} %{{x}}: <b>%{{y:.3f}}</b><extra></extra>"))
    base_layout(fig, height=420, ytitle=f"contribution to {which}")
    fig.update_layout(barmode="stack", bargap=0.15)
    return fig


def step_indices():
    return html.Div([
        callout("plain", "Purpose", "Put expansion and mitigation policy on one common, comparable scale, year by year."),
        block("2.1 Policy score",
              maths(r"x_{pt}=I_{pt}\;C_p\;B_p,\qquad C_p=s_{a(p),\,t^0_p-1}\;e_p", "Equation (1)"),
              md("**I** implementation (0, 0.25, 0.5, 0.75, 1) · **C** coverage = $s$ (share of CRF3 in the targeted activity *a(p)* in the year "
                 "**before** the policy starts, $t^0_p-1$) × $e$ (eligible fraction) · **B** bindingness. The product is non-compensatory: a "
                 "policy only counts if it is in force, covers emissions and carries a signal (OECD et al., 2008).", math=True)),
        block("2.2 Indices",
              maths(r"M_t=\sum_{p\in\mathcal M}x_{pt},\qquad P_t=\sum_{q\in\mathcal P}x_{qt},\qquad S_t=M_t-P_t", "Equation (2)"),
              md("Framework laws (Climate Act 2021, sectoral ceiling 2022) are **event markers**, not index terms, to avoid double counting.")),
        two_col(block("Bindingness scale", table([
            {"b": "0.25", "m": "Information, voluntary scheme, strategy target"}, {"b": "0.5", "m": "Incentive payment"},
            {"b": "0.75", "m": "Conditional relaxation of a legal limit"}, {"b": "1.0", "m": "Mandatory rule, or removal of a legal cap"}],
            [("b", "B"), ("m", "Meaning")], sort=False)),
            block("Coverage keys", table([{"k": k, "m": v} for k, v in COVERAGE_LABEL.items()], [("k", "Key"), ("m", "Share of CRF3 in…")], sort=False))),
        block("Interactive: how the index is built from its parts",
              card(dcc.RadioItems(id="mt-ix", value="P", inline=True, className="seg",
                                  options=[{"label": "Pressure index P", "value": "P"}, {"label": "Mitigation index M", "value": "M"}]),
                   dcc.Graph(id="mt-ix-fig", figure=contrib_fig("P"), config=GRAPH_CONFIG, className="graph"),
                   html.P("Each coloured block is one policy's score x in that year; the black line is their sum. Hover for policy names.", className="fig-note"))),
        callout("read", "Why coverage is fixed before adoption",
                "If coverage were measured each year, a policy that expanded dairy would raise the dairy share and thus its own weight. Fixing exposure "
                "weights before treatment is standard in shift-share designs (Goldsmith-Pinkham, Sorkin & Swift, 2020)."),
        block("Inter-coder reliability",
              maths(r"\kappa_w=1-\frac{\sum_{ij}w_{ij}O_{ij}}{\sum_{ij}w_{ij}E_{ij}},\qquad w_{ij}=\frac{|i-j|}{k-1}"),
              md("Linearly weighted Cohen's kappa on the 5-point grid (Cohen, 1968). Two coders score every policy-year independently, and "
                 "$\\kappa_w$ measures how far their agreement exceeds what chance alone would produce. $O_{ij}$ is the observed share of "
                 "policy-years that coder 1 placed in category $i$ and coder 2 in category $j$, and $E_{ij}$ is the share expected if the two "
                 "coders scored independently. The weights $w_{ij}$ grow with the distance between categories, so a one-step disagreement "
                 "(0.5 vs 0.75) counts less than a large one (0 vs 1). $\\kappa_w = 1$ is perfect agreement and $0$ is chance level. It is "
                 "computed separately for implementation and bindingness. The second coding is currently a provisional placeholder, pending "
                 "independent blind coding.", math=True)),
    ])


def bic_fig():
    rows = DATA["bp"]
    fig = go.Figure(go.Bar(x=[f"m = {r['m']}" for r in rows], y=[r["BIC"] for r in rows],
                           marker=dict(color=[ORANGE if r["selected"] else "#c9d9f0" for r in rows], cornerradius=4),
                           text=[r["break_years"] if r["m"] else "no break" for r in rows], textposition="outside",
                           hovertemplate="%{x}: BIC = %{y:.1f}<extra></extra>"))
    base_layout(fig, height=300, legend=False, ytitle="BIC (lower is better)", hover="closest", title="Number of breaks chosen by BIC")
    return fig


def udmax_fig():
    d = DATA["ud_boot"]; obs = KEY["breaks"]["UDmax"]
    fig = go.Figure(go.Histogram(x=d, nbinsx=40, marker=dict(color="#9ec5f4", line=dict(color="#fcfcfb", width=1)),
                                 hovertemplate="UDmax %{x}: %{y} draws<extra></extra>", name="bootstrap null"))
    fig.add_vline(x=obs, line=dict(color=RED, width=2))
    fig.add_annotation(x=obs, y=1, yref="paper", text=f"observed {obs:.1f}<br>p = {KEY['breaks']['p_UDmax']:.3f}", showarrow=False,
                       xanchor="right", yanchor="top", xshift=-6, font=dict(color=RED))
    base_layout(fig, height=300, legend=False, xtitle="UDmax under H0 (single trend + AR(1) errors)", ytitle="draws", hover="closest",
                title="Bootstrap null distribution of UDmax (999 draws)")
    return fig


def step_breaks():
    return html.Div([
        callout("plain", "Purpose", "Ask whether emissions follow one trend or several regimes, and whether regime changes line up with 2010 or 2015 (RQ1)."),
        block("3.1 Monotonic trend: Mann–Kendall with Hamed–Rao correction",
              maths(r"S=\sum_{i<j}\operatorname{sgn}(y_j-y_i),\qquad Z=\frac{S-\operatorname{sgn}(S)}{\sqrt{\operatorname{Var}^*(S)}},\qquad "
                    r"\operatorname{Var}^*(S)=\operatorname{Var}(S)\cdot\frac{n}{n^*_s}"),
              maths(r"\hat\beta_{\text{Sen}}=\operatorname{median}_{i<j}\frac{y_j-y_i}{j-i}\quad\Rightarrow\quad \%\,\text{per year}=100\,(e^{\hat\beta}-1)"),
              md("$y_t=\\ln E_t$. The Hamed–Rao factor $n/n^*_s$ inflates the variance for positive autocorrelation, which otherwise "
                 "overstates significance (Hamed & Rao, 1998; Yue et al., 2002).", math=True)),
        block("3.2 Structural breaks: Bai–Perron segmented trend",
              maths(r"\ln E_t=\alpha_j+\delta_j t+u_t,\qquad T_{j-1}<t\le T_j,\; j=1,\dots,m+1", "Equation (3)"),
              maths(r"(\hat T_1,\dots,\hat T_m)=\arg\min_{T_1,\dots,T_m}\sum_{j=1}^{m+1}\;\sum_{t=T_{j-1}+1}^{T_j}\big(y_t-\hat\alpha_j-\hat\delta_j t\big)^2"),
              maths(r"\text{BIC}(m)=n\ln\frac{SSR_m}{n}+\big[2(m+1)+m\big]\ln n"),
              maths(r"\text{UDmax}=\max_{1\le m\le 4}F(m),\qquad F(m)=\frac{(SSR_0-SSR_m)/2m}{SSR_m/\big(n-2(m+1)\big)}", "Equation (4)")),
        block("Step by step", steps_list([
            "Compute the SSR of a linear trend for every possible segment [i, j] (closed form).",
            "Dynamic programming finds the global minimum SSR for m = 1…4 breaks with a minimum segment of h = 5 years.",
            "BIC selects the number of breaks m; segment slopes are converted to % per year.",
            "Fit H0 (one trend + AR(1) errors); simulate 999 series under H0, recompute UDmax each time; p = (1 + #{UDmax* ≥ UDmax}) / (B + 1).",
            "Break-date 90% intervals: residual bootstrap of the selected model (499 draws).",
            "Known-date Chow tests at 2010 and 2015 complement the search.",
        ])),
        two_col(card(dcc.Graph(figure=bic_fig(), config=GRAPH_CONFIG, className="graph")),
                card(dcc.Graph(figure=udmax_fig(), config=GRAPH_CONFIG, className="graph"))),
        block("Settings", settings([
            ("Minimum segment h", "5 years", "Trimming ε ≈ 0.15 of n = 35 (Bai & Perron, 2003)"),
            ("Maximum breaks", "4", "Feasible with h = 5; BIC selects m"),
            ("UDmax p-value", "AR(1) parametric bootstrap, B = 999", "Asymptotic critical values unreliable at n = 35 (Diebold & Chen, 1996)"),
            ("Decision rule H1", "p < 0.10 and a break within ±1 year of 2010 or 2015", "Pre-specified"),
        ])),
    ])


def waterfall(y0, y1):
    rows = [r for r in DATA["lmdi_annual"] if y0 < r["year"] <= y1]
    by_f = {}
    for r in rows:
        by_f[r["factor"]] = by_f.get(r["factor"], 0) + r["effect"]
    e0, e1 = value("crf3_kt", y0), value("crf3_kt", y1)
    order = ["activity", "productivity", "intensity", "other"]
    fig = go.Figure(go.Waterfall(
        x=[f"CRF3 {y0}"] + [FACTOR_LAB[f] for f in order] + [f"CRF3 {y1}"],
        measure=["absolute"] + ["relative"] * 4 + ["total"],
        y=[e0] + [by_f.get(f, 0) for f in order] + [e1],
        text=[f"{e0:,.0f}"] + [f"{by_f.get(f, 0):+,.0f}".replace("-", "−") for f in order] + [f"{e1:,.0f}"],
        textposition="outside", cliponaxis=False,
        increasing=dict(marker=dict(color=ORANGE)), decreasing=dict(marker=dict(color=AQUA)), totals=dict(marker=dict(color=BLUE)),
        connector=dict(line=dict(color=MUTED, width=1, dash="dot")),
        hovertemplate="%{x}: %{y:,.1f} kt<extra></extra>"))
    lo = min(e0, e1) - abs(sum(by_f.get(f, 0) for f in order if by_f.get(f, 0) < 0)) - 600
    base_layout(fig, height=400, legend=False, ytitle="kt CO₂e", hover="closest")
    fig.update_yaxes(range=[max(0, lo), max(e0, e1) + sum(v for v in by_f.values() if v > 0) + 600])
    by_c = {}
    for r in rows:
        by_c.setdefault(r["component"], {}).setdefault(r["factor"], 0)
        by_c[r["component"]][r["factor"]] += r["effect"]
    trows = [{"component": COMP_LAB[c], **{f: round(v.get(f, 0), 1) for f in order}, "total": round(sum(v.values()), 1)} for c, v in by_c.items()]
    A, Pr, I = by_f.get("activity", 0), by_f.get("productivity", 0), by_f.get("intensity", 0)
    io = (-I / (A + Pr)) if (A + Pr) > 0 else None
    return fig, trows, io, e1 - e0, sum(by_f.values())


def step_lmdi():
    fig, rows, io, d, s = waterfall(2014, 2021)
    return html.Div([
        callout("plain", "Purpose", "Split each year's change in emissions exactly into: more animals / more N (activity), more milk per cow "
                "(productivity), and emissions per unit (intensity) — RQ2."),
        block("4.1 Components as exact products of factors",
              maths(r"\begin{aligned}E^{dairy}&=\underbrace{D}_{\text{herd}}\times\underbrace{\tfrac{\text{milk}}{D}}_{\text{yield}}\times\underbrace{\tfrac{E^{dairy}}{\text{milk}}}_{\text{per litre}}"
                    r"\qquad E^{other}=O\times\tfrac{E^{other}}{O}\qquad E^{sheep}=Sh\times\tfrac{E^{sheep}}{Sh}\\"
                    r"E^{soils}&=N^{fert}\cdot\tfrac{E^{soils}}{N^{fert}+N^{man}}+N^{man}\cdot\tfrac{E^{soils}}{N^{fert}+N^{man}},\qquad E^{other\ cat.}=E^{CRF3}-\textstyle\sum_i E_i\end{aligned}")),
        block("4.2 Additive LMDI-I",
              maths(r"\Delta E^{k}=\sum_i L\big(E_i^T,E_i^0\big)\,\ln\frac{x_{ik}^T}{x_{ik}^0},\qquad L(a,b)=\frac{a-b}{\ln a-\ln b},\;L(a,a)=a", "Equation (5)"),
              maths(r"\sum_k\Delta E^k=\sum_i L(E_i^T,E_i^0)\ln\frac{E_i^T}{E_i^0}=\sum_i\big(E_i^T-E_i^0\big)=E^T-E^0\quad\text{(no residual)}"),
              maths(r"IO=\frac{-\Delta E^{\text{intensity}}}{\Delta E^{\text{activity}}+\Delta E^{\text{productivity}}}\quad(\text{only when scale grew})"),
              md("Because $\\ln\\prod_k x_k=\\sum_k\\ln x_k$, the factor effects add up exactly to the change. Effects are **chained year by year** "
                 "from 1992 (first year with milk data) to 2023 (last year of the CRT dairy split) and summed within each policy phase. "
                 "Verified residual: 1.9 × 10⁻¹¹ kt.", math=True)),
        block("Interactive: decompose any period",
              card(html.Div(className="control-row", children=[
                  html.Span("Period", className="ctl-label"),
                  html.Div(dcc.RangeSlider(id="mt-lmdi-yr", min=1992, max=2023, step=1, value=[2014, 2021],
                                           marks={y: str(y) for y in [1992, 2000, 2004, 2009, 2014, 2021, 2023]},
                                           tooltip={"placement": "bottom"}), className="grow"),
                  html.Div([html.Span("Phase presets:", className="ctl-label")] +
                           [html.Button(p[0], id=f"mt-ph-{p[0]}", className="btn btn-sm") for p in PHASES], className="btn-row"),
              ]),
                   html.Div(id="mt-lmdi-kpi"),
                   dcc.Graph(id="mt-lmdi-fig", figure=fig, config=GRAPH_CONFIG, className="graph"),
                   html.Div(id="mt-lmdi-tab"),
                   html.P("Orange = factor pushed emissions up, aqua = pushed them down. The start bar plus all factor bars lands exactly on the end bar.",
                          className="fig-note"))),
        callout("caution", "Interpretation", "The decomposition is an accounting identity: it shows what moved emissions, not which policy caused the movement. "
                "Inventory methodology changes appear as intensity change even when farm practice is unchanged."),
        block("Settings", settings([
            ("Form", "additive LMDI-I, chained yearly", "Exact and consistent in aggregation (Ang & Liu, 2001; Ang, 2015)"),
            ("Phases", "P1 1992–04 · P2 04–09 · P3 09–14 · P4 14–21 · P5 21–23", "Decoupling, Food Harvest 2020, quota abolition, sectoral ceiling"),
            ("Soils split", "one implied N₂O intensity per kt N", "Allocates soils N₂O to mineral vs manure N in proportion to inputs"),
            ("EF-ratio sensitivity", "dairy/non-dairy ratio 1.8, 2.2, 2.6", "Brackets the real CRT ratio 2.2–2.85"),
        ])),
    ])


def lag_table():
    rows = sorted(DATA["lag_grid"], key=lambda r: r["AICc"])
    best = rows[0]
    return table([{**r, "sel": "✓ selected" if r is best else ""} for r in rows],
                 [("p", "p"), ("qM", "q_M"), ("qP", "q_P"), ("n", "n"), ("k", "parameters"), ("AICc", "AICc", num(2)), ("sel", "")],
                 page_size=18, style_cond=[{"if": {"filter_query": '{sel} = "✓ selected"'}, "backgroundColor": "#fff1e9", "fontWeight": 700}])


def ardl_fit_fig():
    f = DATA["ardl_fit"]
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=f["years"], y=[v / 1e3 for v in f["observed"]], name="Observed", mode="lines+markers",
                             line=dict(color=INK, width=2), marker=dict(size=5)))
    fig.add_trace(go.Scatter(x=f["years"], y=[v / 1e3 for v in f["fitted"]], name="ARDL fitted (one step ahead)", mode="lines",
                             line=dict(color=ORANGE, width=2, dash="dash")))
    base_layout(fig, height=330, ytitle="Mt CO₂e", title="Model fit, 1997–2024")
    return fig


def step_ardl():
    c = ardl_coefs()
    coef_rows = [{"term": r["index"], "coef": r["coef"], "se": r["se_HAC"], "p": r["p_HAC"]} for r in DATA["ardl_coef"]]
    names = {"const": "constant α", "trend": "trend τ", "y_L1": "ln E(t−1)  φ", "M_L0": "M(t)  β₀", "P_L0": "P(t)  γ₀", "P_L1": "P(t−1)  γ₁",
             "P_L2": "P(t−2)  γ₂", "ln_milk_real": "ln real milk price", "ln_fert_real": "ln real fertiliser price"}
    for r in coef_rows:
        r["term"] = names.get(r["term"], r["term"])
    phi = c["y_L1"]; sg = c["P_L0"] + c["P_L1"] + c["P_L2"]
    return html.Div([
        callout("plain", "Purpose", "Estimate how emissions respond, in the long run, to sustained changes in the mitigation index M and the "
                "pressure index P, holding prices and a trend constant (RQ3)."),
        block("5.1 The autoregressive distributed-lag model",
              maths(r"\ln E_t=\alpha+\tau t+\sum_{i=1}^{p}\phi_i\ln E_{t-i}+\sum_{j=0}^{q_M}\beta_jM_{t-j}+\sum_{j=0}^{q_P}\gamma_jP_{t-j}+\lambda'X_t+\varepsilon_t", "Equation (6)"),
              md("$X_t$ = log real milk price and log real fertiliser price. The trend stops the two rising indices from absorbing smooth drift; "
                 "the lagged dependent variable captures slow adjustment of herds and soil-N pools. The ARDL is valid whether regressors are "
                 "I(0), I(1) or cointegrated (Pesaran et al., 2001).", math=True)),
        block("5.2 Lag selection by small-sample AIC",
              maths(r"\text{AICc}=\text{AIC}+\frac{2k(k+1)}{n-k-1},\qquad p\in\{0,1\},\;q_M,q_P\in\{0,1,2\}"),
              two_col(lag_table(), html.Div([
                  md(f"All 18 candidates use the **same sample** (1997–2024, n = 28), because prices start in 1995 and up to two lags are allowed. "
                     f"AICc selects **ARDL(1, 0, 2)**: one lag of emissions, M enters contemporaneously, P with lags 0–2."),
                  maths(r"\ln E_t=\alpha+\tau t+\phi\ln E_{t-1}+\beta_0M_t+\gamma_0P_t+\gamma_1P_{t-1}+\gamma_2P_{t-2}+\lambda'X_t+\varepsilon_t")]))),
        block("5.3 Long-run multipliers and the delta method",
              maths(r"\theta_M=\frac{\sum_j\beta_j}{1-\sum_i\phi_i},\qquad \theta_P=\frac{\sum_j\gamma_j}{1-\sum_i\phi_i}", "Equation (7)"),
              maths(r"\operatorname{Var}(\hat\theta)\approx\nabla\theta'\,\hat V_{HAC}\,\nabla\theta,\qquad \frac{\partial\theta_P}{\partial\gamma_j}=\frac{1}{1-\phi},\;\;"
                    r"\frac{\partial\theta_P}{\partial\phi}=\frac{\sum_j\gamma_j}{(1-\phi)^2}"),
              md(f"With the estimates: $\\hat\\phi$ = {phi:.3f}, $\\sum\\hat\\gamma_j$ = {sg:.3f}, so "
                 f"$\\hat\\theta_P$ = {sg:.3f} / (1 − {phi:.3f}) = **{KEY['ardl']['theta_P']:.3f}**; "
                 f"$\\hat\\theta_M$ = {c['M_L0']:.3f} / (1 − {phi:.3f}) = **{KEY['ardl']['theta_M']:.3f}**. "
                 f"A sustained +0.1 in P raises long-run emissions by $100(e^{{0.1\\theta_P}}-1)$ = **{KEY['ardl']['pct_per_0p1_P']:.1f}%**.", math=True),
              md("$\\hat V_{HAC}$: Newey–West covariance with 2 lags and small-sample correction (rule of thumb $0.75\\,T^{1/3}\\approx2.3$).", math=True)),
        block("5.4 Estimated short-run coefficients",
              two_col(table(coef_rows, [("term", "Term"), ("coef", "Coefficient", num(4)), ("se", "HAC s.e.", num(4)), ("p", "HAC p", num(3))], sort=False),
                      card(dcc.Graph(figure=ardl_fit_fig(), config=GRAPH_CONFIG, className="graph")))),
        block("5.5 Diagnostics and the bounds test",
              maths(r"\Delta y_t=c+\tau t+\pi_y y_{t-1}+\pi_M M_{t-1}+\pi_P P_{t-1}+\pi_X'X_{t-1}+\textstyle\sum\psi\,\Delta(\cdot)+u_t,\qquad "
                    r"H_0:\pi_y=\pi_M=\pi_P=\pi_X=0"),
              md("Bounds test, Pesaran–Shin–Smith case V (unrestricted intercept and trend), k = 4. F above the I(1) bound ⇒ a level relationship."),
              two_col(table([{"test": r["test"], "p": r["p"], "ok": "pass" if r["pass_10pct"] else "fail"} for r in DATA["diag"]],
                            [("test", "Diagnostic"), ("p", "p-value", num(3)), ("ok", "at 10%")], sort=False),
                      table([{"level": r["level"], "F": r["F"], "I0": r["I0"], "I1": r["I1"], "verdict": r["verdict"]} for r in DATA["bounds"]],
                            [("level", "Level"), ("F", "F", num(2)), ("I0", "I(0) bound", num(2)), ("I1", "I(1) bound", num(2)), ("verdict", "Verdict")], sort=False))),
        block("Settings", settings([
            ("Sample", "1997–2024, n = 28", "Prices from 1995 + two lags; common sample for every candidate"),
            ("Controls", "ln real milk price, ln real fertiliser price, linear trend", "Main output and input market drivers; no weather control"),
            ("HAC lag", "2, small-sample corrected", "Newey & West (1987); Stock & Watson (2020)"),
            ("α", "0.10", "Short series; power reported alongside"),
        ])),
    ])


def null_fig(which):
    obs = KEY["ardl"]["theta_P" if which == "P" else "theta_M"]
    d = DATA["nullP" if which == "P" else "nullM"]
    p = KEY["ardl"]["p_boot_P" if which == "P" else "p_boot_M"]
    col = C_P if which == "P" else C_M
    fig = go.Figure(go.Histogram(x=d, nbinsx=45, marker=dict(color=col, opacity=0.45, line=dict(color="#fcfcfb", width=1)),
                                 hovertemplate="θ* %{x}: %{y} draws<extra></extra>"))
    fig.add_vline(x=obs, line=dict(color=INK, width=2))
    side = "≥" if which == "P" else "≤"
    fig.add_annotation(x=obs, y=1, yref="paper", text=f"estimated θ_{which} = {obs:.3f}<br>one-sided p = {p:.3f}", showarrow=False,
                       xanchor="left", yanchor="top", xshift=6, font=dict(color=INK))
    base_layout(fig, height=340, legend=False, hover="closest", xtitle=f"θ_{which} re-estimated on series generated with {which} removed (H0)",
                ytitle="draws", title=f"Restricted bootstrap null distribution of θ_{which} (B = 999)")
    fig.add_annotation(x=0, y=-0.28, xref="paper", yref="paper", showarrow=False, xanchor="left", font=dict(size=11, color=MUTED),
                       text=("p = share of null draws at least as large as the estimate (test of θ_P > 0)" if which == "P"
                             else "p = share of null draws at least as small as the estimate (test of θ_M < 0)"))
    fig.update_layout(margin=dict(b=80))
    return fig


def step_boot():
    return html.Div([
        callout("plain", "Purpose", "With 28 observations, textbook HAC t-tests reject too often. The decisive p-values therefore come from "
                "re-creating many artificial histories in which the tested policy index has no effect, and asking how unusual the real estimate is."),
        block("6.1 Restricted recursive moving-block bootstrap",
              steps_list([
                  "Re-estimate the model without the tested index v (the null model, H0: θ_v = 0).",
                  "Take its residuals, centre them, and cut them into overlapping blocks of length 3 (preserves serial dependence).",
                  "Draw blocks at random with replacement and glue them into a new residual series ε*.",
                  "Generate pseudo-emissions recursively from the null model: y*_t = X_t b̂₀ with y_{t−1} replaced by y*_{t−1}, plus ε*_t.",
                  "Re-estimate the full ARDL (with v) on y*; record θ*_v.",
                  "Repeat B = 999 times; compute the one-sided p-value below.",
              ]),
              maths(r"y^*_t=\hat\alpha+\hat\tau t+\hat\phi\,y^*_{t-1}+\sum_{w\neq v}\hat b_w'w_t+\hat\lambda'X_t+\varepsilon^*_t,\qquad "
                    r"p^{*}_v=\frac{1+\#\{\theta_v^{*(b)}\ \text{beyond}\ \hat\theta_v\}}{B+1}")),
        block("Interactive: see the null distribution",
              card(dcc.RadioItems(id="mt-null", value="P", inline=True, className="seg",
                                  options=[{"label": "θ_P (pressure)", "value": "P"}, {"label": "θ_M (mitigation)", "value": "M"}]),
                   dcc.Graph(id="mt-null-fig", figure=null_fig("P"), config=GRAPH_CONFIG, className="graph"))),
        callout("read", "Why not just use HAC p-values?",
                f"In Monte Carlo simulation a nominal 10% HAC test actually rejects {100 * KEY['power']['size_nominal_M']:.0f}% of the time for θ_M and "
                f"{100 * KEY['power']['size_nominal_P']:.0f}% for θ_P when the true effect is zero (Kiefer & Vogelsang, 2005). The bootstrap imposes the "
                "null and gives correct size (Davidson & MacKinnon, 2000; Li & Maddala, 1996)."),
        block("Settings", settings([
            ("Block length", "3", "≈ T^(1/3) (Hall, Horowitz & Jing, 1995)"),
            ("Replications", "999 (299 robustness, 499 sub-indices)", "α(B + 1) is an integer"),
            ("Direction", "one-sided", "θ_M < 0 for H3a; θ_P > 0 for H3b"),
            ("Seed", "20261019", "One generator; every draw is reproducible"),
        ])),
    ])


def cf_compute(which, start):
    c = ardl_coefs(); phi = c["y_L1"]
    b = {int(k.split("_L")[1]): v for k, v in c.items() if k.startswith(f"{which}_L")}
    ys, vals = YEARS, COLS[which]
    v = dict(zip(ys, vals)); vstart = v[start]
    gap = {y: (v[y] - vstart) if y >= start else 0.0 for y in ys}
    delta, path = 0.0, {}
    for t in range(start, 2025):
        delta = phi * delta + sum(bj * gap.get(t - j, 0.0) for j, bj in b.items())
        path[t] = delta
    obs = {y: value("crf3_kt", y) for y in path}
    cf = {y: obs[y] * math.exp(-path[y]) for y in path}
    cum = sum(obs[y] - cf[y] for y in path)
    return path, obs, cf, cum


def cf_fig(which, start):
    path, obs, cf, cum = cf_compute(which, start)
    yrs = sorted(path)
    col = C_P if which == "P" else C_M
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=yrs, y=[obs[y] / 1e3 for y in yrs], name="Observed", line=dict(color=INK, width=2.5)))
    fig.add_trace(go.Scatter(x=yrs, y=[cf[y] / 1e3 for y in yrs], name=f"{which} frozen at its {start} level", line=dict(color=col, width=2.5, dash="dash"),
                             fill="tonexty", fillcolor="rgba(235,104,52,0.12)" if which == "P" else "rgba(42,120,214,0.12)"))
    base_layout(fig, height=380, ytitle="Mt CO₂e")
    eff = 100 * (math.exp(path[2024]) - 1)
    return fig, eff, cum


def step_cf():
    fig, eff, cum = cf_fig("P", 2000)
    return html.Div([
        callout("plain", "Purpose", "Translate the coefficients into tonnes: how different would emissions have been if an index had stayed at its 2000 level?"),
        block("7.1 Dynamic counterfactual recursion",
              maths(r"\Delta_{v,t}=\sum_i\phi_i\Delta_{v,t-i}+\sum_j b_{v,j}\,\big(v_{t-j}-v_{t_0}\big),\qquad "
                    r"E^{cf}_t=E_t\,e^{-\Delta_{v,t}},\qquad OR_T=\frac{\Delta_{P,T}}{-\Delta_{M,T}}", "Equation (8)"),
              md("$\\Delta_{v,t}$ is the log-point effect of index $v$ in year $t$; $b_{v,j}$ are its lag coefficients; $t_0$ = freeze year. "
                 "The **offset ratio** OR is defined only when the mitigation effect is negative (by analogy with the rebound effect). "
                 "90% intervals come from an *unrestricted* block bootstrap (999 draws).", math=True)),
        block("Interactive counterfactual calculator (uses the estimated ARDL coefficients)",
              card(html.Div(className="control-grid", children=[
                  html.Div([html.Label("Index frozen", className="ctl-label"),
                            dcc.RadioItems(id="mt-cf-ix", value="P", inline=True, className="seg",
                                           options=[{"label": "Pressure P", "value": "P"}, {"label": "Mitigation M", "value": "M"}])]),
                  html.Div([html.Label("Freeze year t₀", className="ctl-label"),
                            dcc.Slider(id="mt-cf-yr", min=1997, max=2020, step=1, value=2000,
                                       marks={y: str(y) for y in range(1997, 2021, 3)}, tooltip={"placement": "bottom"})], className="span-2"),
              ]),
                   html.Div(id="mt-cf-kpi"),
                   dcc.Graph(id="mt-cf-fig", figure=fig, config=GRAPH_CONFIG, className="graph"),
                   html.P("t₀ = 2000 reproduces the paper (pressure: +11.2% in 2024, 12.5 Mt cumulative). Point estimates only; intervals are in Results.",
                          className="fig-note"))),
        block("7.2 Power and minimum detectable effect",
              steps_list([
                  "Set a known long-run effect |θ| on a grid {0, 0.1, 0.2, 0.3, 0.5, 0.75, 1, 1.5}.",
                  "Simulate 500 emission series from the fitted model with that θ, using the observed paths of M, P and X and block-resampled residuals.",
                  "Re-estimate the full model on each; record the t-statistic.",
                  "θ = 0 gives the empirical size; its 90th percentile is the size-adjusted critical value.",
                  "Power(θ) = share of t-statistics above that critical value; MDE = smallest |θ| with 80% power (linear interpolation).",
              ]),
              md(f"Result: MDE ≈ **{KEY['power']['MDE_M']:.2f}** for M and **{KEY['power']['MDE_P']:.2f}** for P — about 4% per 0.1 index units "
                 "(Bloom, 1995; Gelman & Carlin, 2014).")),
    ])


def step_other():
    return html.Div([
        callout("plain", "Purpose", "Check that the headline result is not an artefact of one modelling choice, and test timing and instrument type (RQ4a)."),
        block("8.1 Robustness grid (14 pre-specified variants + leave-one-policy-out)",
              table([{"v": v} for v in ["baseline", "no deterministic trend", "fixed lags ARDL(1,1,1)", "equal bindingness (B = 1)",
                                        "drop Nitrates Action Programme from M", "NAP weighted by climate relevance 0.5",
                                        "Food Vision 2030 coded as zero pressure", "extended controls (GNI*, 2018, 2022 dummies)",
                                        "milk-to-feed price ratio as control", "static model (p = 0)", "pre-ceiling sample (to 2021)",
                                        "CH₄-only outcome", "N₂O-only outcome", "first differences (static)",
                                        "leave out each of P01–P08 in turn"]], [("v", "Variant")], page_size=20, sort=False),
              md("Rule fixed in advance: a sign is **robust** if it holds in ≥ 80% of estimable variants. Variants use B = 299 bootstrap draws.")),
        block("8.2 Mitigation sub-indices by instrument type",
              maths(r"\ln E_t=\dots+\beta^{s}M^{s}_t+\beta^{rest}\big(M_t-M^{s}_t\big)+\sum_j\gamma_jP_{t-j}+\dots,\quad s\in\{\text{mandatory, incentive, voluntary}\}"),
              md("Each sub-index is estimated in turn while the rest of M and P are held as controls; bootstrap B = 499.")),
        block("8.3 Interrupted time series at pre-specified dates",
              maths(r"y_t=\beta_0+\beta_1t+\sum_{e\in\{2010,2015,2022\}}\Big[\lambda_e\mathbb 1(t\ge e)+\delta_e\,(t-e+1)\,\mathbb 1(t\ge e)\Big]+\lambda'X_t+u_t"),
              md("$\\lambda_e$ = level change, $\\delta_e$ = slope change at event $e$ (segmented regression; Bernal et al., 2017). Outcomes: ln CRF3 and "
                 "ln dairy cows (with a post-2005 dummy). Sample 1995–2024, HAC errors. 2022 has only three post-years and is descriptive.", math=True)),
    ])


def step_did():
    return html.Div([
        callout("plain", "Purpose", "Use differences inside Ireland: if quota abolition drove expansion, regions where dairy was already dominant should "
                "have expanded more after 2015 (RQ4b)."),
        block("9.1 Continuous-exposure difference-in-differences",
              maths(r"y_{rt}=\alpha_r+\gamma_t+\beta\,\big(\text{Exp}_r-\overline{\text{Exp}}\big)\,\mathbb 1[t\ge2015]+\mu_r\,\mathbb 1[t\ge2005]+\kappa_r t+u_{rt}", "Equation (9)"),
              md("$\\alpha_r$ region effects; $\\gamma_t$ year effects absorb everything national (policy, prices, weather); $\\mu_r$ absorb the CSO "
                 "classification break; $\\kappa_r t$ region trends (second specification). Exposure = region's dairy share of all cows, 2010–2014; "
                 "β is scaled per 10 percentage points. Outcomes: log dairy cows, log livestock units, log imputed livestock emissions.", math=True)),
        block("9.2 Inference with five clusters",
              maths(r"p_{RI}=\frac{1}{120}\sum_{\pi\in S_5}\mathbb 1\big(|\hat\beta_\pi|\ge|\hat\beta|\big),\qquad "
                    r"y^*_{rt}=\hat y^{(0)}_{rt}+\hat u^{(0)}_{rt}\,w_r,\;\;w_r\in\{\pm\sqrt{1.5},\pm1,\pm\sqrt{0.5}\}"),
              md("**Randomisation inference** re-assigns the five exposure values over regions in all 5! = 120 ways (Fisher, 1935; Young, 2019). "
                 "The **wild cluster bootstrap** imposes β = 0 and flips residuals by region with Webb's six-point weights (Webb, 2023; B = 999). "
                 "Conventional cluster-robust errors are unreliable with five clusters (Cameron et al., 2008).")),
        block("9.3 Placebo and event study",
              maths(r"y_{rt}=\alpha_r+\gamma_t+\sum_{k\neq2014}\beta_k\,\frac{\text{Exp}_r-\overline{\text{Exp}}}{0.10}\,\mathbb 1[t=k]+u_{rt},\qquad 2005\le t\le2024"),
              md("The placebo dates 'abolition' to 2010 using pre-2015 data only: a significant placebo signals differential pre-trends (Rambachan & Roth, 2023).")),
    ])


def step_link():
    return html.Div([
        callout("plain", "Purpose", "Connect the accounting to the policy: do years of rising pressure show up as more activity, and years of rising mitigation as lower intensity?"),
        block("10.1 Decomposition–regression link",
              maths(r"\Delta E^{k}_t=c+\sum_{j=0}^{1}\pi^{k}_{j}\Delta P_{t-j}+\sum_{j=0}^{1}\rho^{k}_{j}\Delta M_{t-j}+\psi'\Delta X_t+\omega\,d_{2005}+\nu_t", "Equation (10)"),
              md("$k$ ∈ {activity, dairy-herd activity, intensity}; outcomes are the annual LMDI effects (kt). The framework predicts $\\sum\\pi>0$ for "
                 "activity and $\\sum\\rho<0$ for intensity. Newey–West errors, 1997–2023 (n = 27). Reported per 0.1 index units.", math=True)),
        block("10.2 What the 2030 ceiling implies",
              maths(r"E^{*}_{2030}=0.75\,E_{2018},\qquad I_{2030}=\frac{E_{2024}}{LU_{2024}}\,e^{6g},\qquad LU^{*}_{2030}=\frac{E^{*}_{2030}}{I_{2030}}"),
              md("$g$ = annual log change in emissions per livestock unit: the 2012–2024 Theil–Sen trend, or −1%, −2%, −3% a year. The ceiling also "
                 "covers agricultural fuel, so applying it to CRF3 is an approximation. Try it in the calculator on the Results page.", math=True)),
        block("10.3 Supplement: warming-equivalent methane (GWP*)",
              maths(r"E^{*}_t=4.53\,E^{CH_4}_t-4.25\,E^{CH_4}_{t-20}"),
              md("Smith, Cain & Allen (2021). Reported only as a supplementary perspective; the outcome throughout is GWP100.")),
    ])


STEPS = [("data", "1 · Data & harmonisation", step_data), ("indices", "2 · Policy indices", step_indices),
         ("breaks", "3 · Trends & breaks", step_breaks), ("lmdi", "4 · LMDI decomposition", step_lmdi),
         ("ardl", "5 · ARDL policy-mix model", step_ardl), ("boot", "6 · Bootstrap inference", step_boot),
         ("cf", "7 · Counterfactuals & power", step_cf), ("other", "8 · Robustness, sub-indices, ITS", step_other),
         ("did", "9 · Regional DiD", step_did), ("link", "10 · Mechanism link & 2030", step_link)]


def layout():
    return html.Div([
        page_header("Step 4 · Implementation & methodology", "How the analysis was done, step by step",
                    "No single method can identify a causal policy effect from one national series of about 28 usable observations. The study "
                    "combines three designs whose identifying assumptions fail in different ways, so that their agreement — not any single "
                    "estimate — carries the inference (Lawlor et al., 2016; Munafò & Davey Smith, 2018)."),
        section("The pipeline", card(workflow()), DESIGNS,
                callout("read", "Reproducibility", "One notebook runs everything from raw files to every table and figure, with a fixed seed (20261019). "
                        "A full run takes about five minutes; an independent script re-derives every stage (30 / 30 checks pass).")),
        section("Each step in detail",
                html.P("Every step shows its purpose in plain words, the mathematics, the algorithm and the settings with their justification. "
                       "Several steps include live calculators.", className="section-sub"),
                dcc.Tabs(id="mt-tabs", value="data", className="tabs tabs-steps", children=[
                    dcc.Tab(label=lab, value=v, children=html.Div(fn(), className="step-body"), className="tab", selected_className="tab--sel")
                    for v, lab, fn in STEPS])),
    ])


def register_callbacks(app):
    @app.callback(Output("mt-ix-fig", "figure"), Input("mt-ix", "value"))
    def _ix(w):
        return contrib_fig(w)

    from dash import ctx

    @app.callback(Output("mt-lmdi-yr", "value"), [Input(f"mt-ph-{p[0]}", "n_clicks") for p in PHASES], prevent_initial_call=True)
    def _preset(*_):
        t = ctx.triggered_id
        for p in PHASES:
            if t == f"mt-ph-{p[0]}":
                return [p[2], p[3]]
        return [2014, 2021]

    @app.callback(Output("mt-lmdi-fig", "figure"), Output("mt-lmdi-tab", "children"), Output("mt-lmdi-kpi", "children"),
                  Input("mt-lmdi-yr", "value"))
    def _lm(yr):
        y0, y1 = yr
        if y1 <= y0:
            return empty_fig("Choose a period of at least one year"), None, None
        fig, rows, io, d, s = waterfall(y0, y1)
        tab = table(rows, [("component", "Component"), ("activity", "Activity", num(1)), ("productivity", "Productivity", num(1)),
                           ("intensity", "Intensity", num(1)), ("other", "Other", num(1)), ("total", "Total", num(1))], sort=False)
        k = kpi_row(kpi(f"{d:+,.0f} kt".replace("-", "−"), f"change in CRF3, {y0}→{y1}"),
                    kpi(f"{abs(s - d):.0e} kt", "residual: exact by construction (up to rounding)"),
                    kpi("–" if io is None else f"{io:.2f}", "intensity offset IO", "defined only when activity + productivity > 0",
                        tone="tone-orange" if io is not None and io < 1 else ""))
        return fig, tab, k

    @app.callback(Output("mt-null-fig", "figure"), Input("mt-null", "value"))
    def _null(w):
        return null_fig(w)

    @app.callback(Output("mt-cf-fig", "figure"), Output("mt-cf-kpi", "children"), Input("mt-cf-ix", "value"), Input("mt-cf-yr", "value"))
    def _cf(w, y):
        fig, eff, cum = cf_fig(w, y)
        lab = "pressure" if w == "P" else "mitigation"
        return fig, kpi_row(
            kpi(f"{eff:+.1f}%".replace("-", "−"), f"effect of the {lab} change since {y} on 2024 emissions",
                tone="tone-orange" if w == "P" else "tone-blue"),
            kpi(f"{cum / 1e3:+,.1f} Mt".replace("-", "−"), f"cumulative CO₂e, {y}–2024"),
            kpi(f"{value(w, 2024) - value(w, y):+.3f}".replace("-", "−"), f"change in {w}, {y}→2024"))
