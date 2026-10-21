"""Step 2 – research questions, hypotheses, policy context and conceptual framework."""
import plotly.graph_objects as go
from dash import html, dcc, Input, Output

from ..components import page_header, section, card, callout, maths, two_col, badge
from ..data_store import DATA
from ..theme import base_layout, C_M, C_P, INK2, MUTED

RQS = [
    ("RQ1", "Do breaks in the emission path coincide with policy changes?",
     "H1: an endogenous break lies within ±1 year of 2010 (Food Harvest 2020) or 2015 (quota abolition)",
     "Bai–Perron structural breaks with bootstrap UDmax", "UDmax p < 0.10 and a break date within ±1 year"),
    ("RQ2", "Did intensity gains keep pace with scale growth?",
     "H2: intensity offset IO < 1 after 2015 (efficiency did not keep pace)",
     "Exact LMDI decomposition; decomposition–regression link", "IO < 1 across the dairy emission-factor range"),
    ("RQ3", "Did production pressure offset mitigation?",
     "H3a: θ_M < 0 (mitigation lowers emissions) · H3b: θ_P > 0 (pressure raises them) · H3c: offset ratio ≥ 0.5",
     "ARDL long-run multipliers, restricted block bootstrap, dynamic counterfactuals",
     "One-sided bootstrap p < 0.10; for H3c the pressure effect's 90% interval excludes zero"),
    ("RQ4", "Do effects differ by instrument type and by regional exposure?",
     "H4a: mandatory instruments have the largest negative effect · H4b: more dairy-exposed regions expanded more after 2015",
     "Sub-index ARDL; within-Ireland regional difference-in-differences",
     "p < 0.10 with the predicted sign; placebo not significant"),
]

CONTEXT = [
    ("1990–2004", "Coupled suckler-cow, special-beef and ewe premia", "REPS agri-environment scheme (from 1994)"),
    ("2005–2009", "CAP decoupling (2005) ends coupled premia; nitrates derogation from 2007; quota increments from 2006 and +2% in 2008",
     "Nitrates Action Programme (S.I. 378/2006); Farm Waste Management Scheme"),
    ("2010–2014", "Food Harvest 2020 (+50% milk volume target); +1% a year quota increases",
     "REPS run-off; AEOS; Carbon Navigator; Sustainable Dairy Assurance Scheme (2014)"),
    ("2015–2021", "EU milk-quota abolition (31 March 2015); Food Wise 2025; TAMS II dairy equipment grants",
     "GLAS; Beef Data and Genomics Programme; BEEP-S"),
    ("2021–2024", "Food Vision 2030 (mixed goals); derogation renewed and tightened from 2024",
     "5th NAP chemical-N limits and protected urea (S.I. 113/2022); ACRES; SCEP. Climate Act 2021 and the 2022 ceiling are event markers"),
]


def parse_impl(s):
    out = {}
    for part in str(s).split(";"):
        if ":" not in part:
            continue
        span, v = part.split(":")
        a, b = (span.split("-") + [span])[:2]
        for y in range(int(a), int(b) + 1):
            out[y] = float(v)
    return out


def timeline_fig(which="both"):
    rows = [r for r in DATA["codebook"] if r["direction"] != 0 and (which == "both" or r["policy_set"] == which)]
    rows = sorted(rows, key=lambda r: (r["policy_set"] != "P", -int(r["start"])))
    fig = go.Figure()
    shown = set()
    for r in rows:
        impl = parse_impl(r["implementation"])
        yrs = sorted(impl)
        runs, cur = [], None
        for y in yrs:
            if cur and y == cur[1] + 1 and impl[y] == cur[2]:
                cur[1] = y
            else:
                if cur: runs.append(cur)
                cur = [y, y, impl[y]]
        if cur: runs.append(cur)
        col = C_P if r["policy_set"] == "P" else C_M
        setname = "Production pressure (P)" if r["policy_set"] == "P" else "Mitigation (M)"
        lab = f"{r['policy_id']} · {r['name'][:38]}{'…' if len(r['name']) > 38 else ''}"
        for a, b, v in runs:
            fig.add_trace(go.Bar(
                y=[lab], x=[b - a + 1], base=[a - 0.45], orientation="h", width=0.7,
                marker=dict(color=col, opacity=0.25 + 0.75 * v, line=dict(width=0)),
                name=setname, legendgroup=setname, showlegend=setname not in shown,
                customdata=[[r["name"], a, b, v, r["bindingness"], r["instrument_type"], r["coverage_key"], r["eligibility"]]],
                hovertemplate="<b>%{customdata[0]}</b><br>%{customdata[1]}–%{customdata[2]} · implementation I = %{customdata[3]}"
                              "<br>bindingness B = %{customdata[4]} (%{customdata[5]})<br>coverage key: %{customdata[6]}, eligible share e = %{customdata[7]}<extra></extra>"))
            shown.add(setname)
    base_layout(fig, height=max(320, 30 * len(rows) + 90), hover="closest")
    fig.update_layout(barmode="overlay", margin=dict(l=330, r=20, t=40, b=40))
    fig.update_xaxes(range=[1989.5, 2024.9], dtick=5, showgrid=True, gridcolor="#efeee9")
    fig.update_yaxes(showgrid=False, tickfont=dict(size=12))
    for y in (2005, 2015):
        fig.add_vline(x=y - 0.5, line=dict(color=MUTED, dash="dot", width=1))
    return fig


def framework():
    box = lambda t, s, cls="": html.Div(className=f"fw-box {cls}", children=[html.Div(t, className="fw-t"), html.Div(s, className="fw-s")])
    return html.Div(className="fw", children=[
        html.Div(className="fw-col", children=[
            box("Production pressure  P", "derogation · quota increases & abolition · growth strategies · TAMS", "fw-p"),
            box("Mitigation  M", "nitrates rules · agri-environment schemes · genetics · advisory", "fw-m")]),
        html.Div(className="fw-col fw-arrows", children=[html.Div("raises (+) →", className="fw-arrow up"),
                                                          html.Div("lowers (−) →", className="fw-arrow down")]),
        html.Div(className="fw-col", children=[
            box("Activity", "herd size, N use, milk volume"),
            box("Intensity", "emissions per litre, per head, per kg N")]),
        html.Div(className="fw-col fw-arrows", children=[html.Div("×", className="fw-times")]),
        html.Div(className="fw-col", children=[box("CRF3 emissions", "E = Activity × Intensity", "fw-e")]),
    ])


def layout():
    return html.Div([
        page_header("Step 2 · Research questions", "Four questions, each with a pre-specified test",
                    "Hypotheses and decision rules were fixed in the analysis code before estimation. With about 28 usable annual "
                    "observations, every test uses α = 0.10."),
        section("Research questions and hypotheses",
                html.Div(className="rq-grid", children=[
                    html.Div(className="rq-card", children=[
                        html.Div(rq, className="rq-tag"), html.H3(q),
                        html.Div([html.Span("Hypothesis", className="rq-lab"), html.P(h)]),
                        html.Div([html.Span("Primary test", className="rq-lab"), html.P(t)]),
                        html.Div([html.Span("Supported if", className="rq-lab"), html.P(d)]),
                    ]) for rq, q, h, t, d in RQS]),
                callout("caution", "Decision rule", "Rules are applied mechanically: a hypothesis is 'supported' only if its pre-registered "
                        "condition holds. The Results page reports each verdict next to its evidence.")),
        section("Conceptual framework: emissions = scale × intensity",
                card(framework()),
                html.Div(className="grid-2", children=[
                    card(html.H3("Intensity offset"),
                         maths(r"IO=\frac{-\Delta E^{\text{intensity}}}{\Delta E^{\text{activity}}+\Delta E^{\text{productivity}}}"),
                         html.P("The share of scale growth cancelled by lower emissions per unit. IO < 1 means efficiency gains did not keep "
                                "pace with expansion — the agricultural analogue of the rebound effect in energy economics (Greening et al., 2000).")),
                    card(html.H3("Policy incoherence"),
                         maths(r"S_t = M_t - P_t"),
                         html.P("If P and M rise in the same period, the net signal S understates mitigation effort. This makes measurable the "
                                "sector–environment incoherence of Nilsson et al. (2012) and the 'layering' of Howlett & Rayner (2013).")),
                ]),
                callout("plain", "In plain words",
                        "Expansion policies act on how much is produced (more cows, more milk). Irish mitigation policy has mostly acted on how "
                        "it is produced (emissions per litre). Total emissions only fall if intensity falls faster than activity grows.")),
        section("Policy context: two policy sets pulled in opposite directions",
                card(
                    html.Div(className="control-row", children=[
                        html.Span("Show:", className="ctl-label"),
                        dcc.RadioItems(id="q-set", value="both", inline=True, className="seg",
                                       options=[{"label": "Both sets", "value": "both"}, {"label": "Pressure (P)", "value": "P"},
                                                {"label": "Mitigation (M)", "value": "M"}])]),
                    dcc.Graph(id="q-timeline", figure=timeline_fig(), config={"displaylogo": False}, className="graph"),
                    html.P("Each bar shows when an instrument was in force; darker shading = higher implementation level I (0.25 → 1). "
                           "Hover a bar to see its bindingness, coverage and eligibility scores.", className="fig-note")),
                html.Div(className="table-like", children=[
                    html.Div(className="tl-row tl-head", children=[html.Div("Period"), html.Div("Production pressure (expansion)"), html.Div("Mitigation")]),
                    *[html.Div(className="tl-row", children=[html.Div(p, className="tl-period"), html.Div(a), html.Div(b)]) for p, a, b in CONTEXT],
                ]),
                callout("read", "Contrast", "Expansion instruments acted on how much was produced and several relaxed binding legal limits. "
                        "Mitigation instruments acted mainly on how it was produced, most were voluntary contractual schemes, and the main "
                        "binding instrument (the Nitrates Action Programme) was designed for water quality, not climate.")),
        section("Dimensions of policy success",
                html.Div(className="grid-3", children=[
                    card(html.H3("Programme"), html.P("Did instruments change outcomes? → tested by RQ1–RQ4.")),
                    card(html.H3("Process"), html.P("Were they implemented as designed? → captured by the implementation score I.")),
                    card(html.H3("Political"), html.P("Did they survive competing priorities? → discussed against five stakeholder-identified barriers "
                                                      "(Augustenborg et al., 2026).")),
                ]), sub="Interpretive lens from Marsh & McConnell (2010)."),
    ])


def register_callbacks(app):
    @app.callback(Output("q-timeline", "figure"), Input("q-set", "value"))
    def _t(which):
        return timeline_fig(which)
