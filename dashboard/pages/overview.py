"""Step 1 – defining the problem."""
import plotly.graph_objects as go
from dash import html, dcc, Input, Output

from ..components import page_header, section, card, kpi, kpi_row, callout, graph, two_col, md
from ..data_store import series, value, KEY, EVENTS
from ..theme import base_layout, add_events, PAL, INK, INK2, MUTED, ORANGE, AQUA, BLUE, YELLOW, MAGENTA, RED


def emissions_fig(mode="total"):
    ys, e = series("crf3_kt")
    fig = go.Figure()
    if mode == "total":
        fig.add_trace(go.Scatter(x=ys, y=[v / 1e3 for v in e], name="CRF3 emissions", mode="lines+markers",
                                 line=dict(color=BLUE, width=2.5), marker=dict(size=6),
                                 hovertemplate="%{x}: <b>%{y:.2f} Mt CO₂e</b><extra></extra>"))
    else:
        cats = [("enteric_kt", "Enteric fermentation", BLUE), ("soils_kt", "Agricultural soils", ORANGE),
                ("manure_kt", "Manure management", AQUA), ("urea_kt", "Urea", YELLOW), ("liming_kt", "Liming", MAGENTA)]
        for c, lab, col in cats:
            yy, v = series(c)
            fig.add_trace(go.Scatter(x=yy, y=[x / 1e3 for x in v], name=lab, stackgroup="one", mode="lines",
                                     line=dict(color=col, width=0.5), fillcolor=col,
                                     hovertemplate=f"{lab}: %{{y:.2f}} Mt<extra></extra>"))
    tgt = KEY["ceiling_2030"]["target_2030"] / 1e3
    e24, e18 = value("crf3_kt", 2024) / 1e3, value("crf3_kt", 2018) / 1e3
    fig.add_trace(go.Scatter(x=[2024, 2030], y=[e24, tgt], name="Path to 2030 ceiling", mode="lines+markers",
                             line=dict(color=RED, width=2, dash="dash"), marker=dict(size=[0, 10], symbol="star"),
                             hovertemplate="%{x}: %{y:.2f} Mt<extra>required</extra>"))
    fig.add_annotation(x=2030, y=tgt, text=f"2030 ceiling<br><b>{tgt:.1f} Mt</b> (−25% vs 2018)", showarrow=False,
                       xanchor="right", yanchor="top", yshift=-10, font=dict(color=RED, size=12))
    fig.add_annotation(x=2018, y=e18, text=f"2018 baseline {e18:.1f} Mt", showarrow=True, arrowhead=0, ax=-60, ay=-30,
                       font=dict(size=11, color=INK2), arrowcolor=MUTED)
    base_layout(fig, height=430, ytitle="Mt CO₂e (AR5 GWP100)")
    fig.update_xaxes(range=[1989, 2031])
    fig.update_yaxes(rangemode="tozero" if mode != "total" else None, range=None if mode != "total" else [14, 22.5])
    add_events(fig, EVENTS)
    return fig


def layout():
    k = KEY
    return html.Div([
        page_header("Step 1 · Defining the problem", "Expansion versus mitigation",
                    "Production-oriented policy and agricultural greenhouse-gas emissions in Ireland, 1990–2024. "
                    "Why did three decades of climate-related farm policy leave emissions almost exactly where they started?"),
        kpi_row(
            kpi("37.9%", "of Ireland's national GHG emissions came from agriculture in 2024", "EPA, 2026b"),
            kpi(f"{k['trend']['change_pct_1990_2024']:+.1f}%".replace("-", "−"), "CRF3 emissions, 2024 vs 1990",
                "19.6 vs 19.8 Mt CO₂e", tone="tone-blue"),
            kpi(f"{k['ceiling_2030']['gap_pct_2024']:+.1f}%".replace("-", "−"), "2024 vs the 2018 baseline", "progress so far"),
            kpi("−25%", "required by the 2030 sectoral emissions ceiling", "relative to 2018", tone="tone-red"),
        ),
        section("The puzzle: 35 years of policy, a flat emission path",
                card(
                    dcc.RadioItems(id="ov-mode", value="total", inline=True, className="seg",
                                   options=[{"label": "Total emissions", "value": "total"},
                                            {"label": "By inventory category", "value": "cat"}]),
                    dcc.Graph(id="ov-fig", figure=emissions_fig(), config={"displaylogo": False}, className="graph"),
                    html.P("CRF3 = IPCC agriculture sector. Dotted lines mark the policy dates tested in the study. "
                           "Hover for values; switch to the category view to see what the total is made of.", className="fig-note"),
                ),
                two_col(
                    callout("plain", "In plain words",
                            "Ireland has run agri-environment schemes, nitrates rules and, since 2021, legally binding "
                            "carbon budgets. Yet farm emissions in 2024 were within 1% of 1990. Underneath the flat line "
                            "emissions fell in the 2000s and rose sharply after 2011 — something pushed them back up. "
                            "Agricultural methane and nitrous oxide are hard to abate: the economic potential of livestock measures is a small "
                            "fraction of their technical potential (Herrero et al., 2016), no country prices farm emissions (Leahy et al., 2020), "
                            "and EU agricultural non-CO₂ emissions fell by only 6–7% over 2005–2023 (EEA, 2025)."),
                    callout("finding", "Why it matters",
                            "If mitigation instruments simply do not work, the remedy is better instruments. If they work but are "
                            "cancelled by policies that expand output, adding more instruments will not close the gap while the "
                            "expansion incentives remain."),
                )),
        section("Two competing explanations",
                html.Div(className="grid-2", children=[
                    card(html.Div("Explanation A", className="eyebrow"), html.H3("Mitigation was weak"),
                         html.P("Instruments were voluntary, under-resourced or slow to deliver. This fits stakeholder accounts of "
                                "capacity and coordination constraints (Augustenborg et al., 2026) and Ireland's record as a "
                                "climate-policy laggard (Torney & O'Gorman, 2019)."), cls="card-accent-blue"),
                    card(html.Div("Explanation B", className="eyebrow"), html.H3("Mitigation was offset by expansion"),
                         html.P("From 2007 the nitrates derogation allowed higher stocking rates; milk quotas were raised from 2008 "
                                "and abolished in 2015; Food Harvest 2020 and Food Wise 2025 set quantified growth targets."),
                         cls="card-accent-orange"),
                ]),
                callout("read", "Central research question",
                        html.B("Is the flat emission path failed mitigation, or mitigation offset by policies that expanded output?"))),
        section("What is known — and the gap",
                html.Div(className="grid-3", children=[
                    card(html.H3("Ex post evaluation and attribution"),
                         html.P("Evaluation asks how emissions would have evolved without a policy, which matters under binding carbon budgets "
                                "(Climate Act 2021; CCAC, 2025). Cross-country studies link climate laws to lower CO₂ intensity (Eskander & Fankhauser, 2020) "
                                "and screen about 1,500 policies for large reductions (Stechemesser et al., 2024), but they define treatment as climate-labelled "
                                "policy and exclude agriculture, so quotas, coupled payments, derogations and growth strategies enter only as background."),
                         html.P("Synthetic controls and DiD need credible comparators (Abadie, 2021; Rambachan & Roth, 2023); quota abolition and CAP "
                                "reform hit every EU state at once, so this study uses within-Ireland exposure, interrupted time series and "
                                "structural breaks (Lopez Bernal et al., 2017; Bai & Perron, 2003).")),
                    card(html.H3("Mechanisms and dynamics"),
                         html.P("LMDI decomposition splits emission change into activity, structure and intensity without a residual (Ang & Liu, 2001; "
                                "Ang, 2015) but does not say which policy caused each part. ARDL models separate short- and long-run responses "
                                "(Pesaran et al., 2001), yet a long-run relation is not causal direction, and with about 28 observations correlated "
                                "indices make mitigation effects hard to detect — hence bootstrap inference and an explicit power analysis."),
                         html.P("Sector models (Donnellan et al., 2013; Fellmann et al., 2018; Jansson et al., 2021) show growth–emissions tensions and "
                                "leakage, but as conditional projections, not realised effects. Inference is most credible when designs with "
                                "different biases agree (Lawlor et al., 2016; Munafò & Davey Smith, 2018).")),
                    card(html.H3("Agriculture is a distinct case"),
                         html.P("Over €100 billion of 2014–2020 CAP spending was attributed to climate action, yet farm emissions had not fallen since 2010 "
                                "and the CAP never sought to limit livestock numbers (European Court of Auditors, 2021; Pe'er et al., 2020). "
                                "Commodity-linked support is a production incentive and many mitigation targets are non-binding (OECD, 2022; "
                                "Henderson & Lankoski, 2021). Voluntary agri-environment schemes show limited outcome evidence (Hasler et al., 2022; "
                                "Finn & Ó hUallacháin, 2012; Cullen et al., 2021), and intensity targets lower totals only if output does not grow "
                                "(Ellerman & Wing, 2003; Leahy et al., 2020).")),
                    card(html.H3("Expansion, intensity and coherence"),
                         html.P("Higher yields cut emissions per kg of milk while raising emissions per cow (Gerber et al., 2011) — an agricultural "
                                "analogue of the energy-efficiency rebound (Greening et al., 2000; Sorrell, 2009). Post-quota EU milk supply was "
                                "price-inelastic and few member states expanded herds (Jongeneel & Gonzalez-Martinez, 2022), whereas Ireland's dairy "
                                "herd grew by about 38% over 2010–2018. Policy-coherence frameworks explain why opposing incentives persist "
                                "(Nilsson et al., 2012; Rogge & Reichardt, 2016; Howlett & Rayner, 2013; Daugbjerg & Swinbank, 2016), but they "
                                "measure declared priorities or diagnose conflict qualitatively (von Lüpke et al., 2026).")),
                    card(html.H3("Evidence for Ireland"),
                         html.P("Food Harvest 2020 targeted +50% milk, Food Wise 2025 +65% output value, and Food Vision 2030 pairs growth with "
                                "methane cuts; the 2022 ceiling requires −25% by 2030. Donnellan et al. (2013) anticipated the conflict; "
                                "Balaine et al. (2022) find efficiency-led development did not contain expansion; at farm level emissions per kg fell "
                                "while total farm emissions rose (Läpple et al., 2022; Balaine et al., 2020). Stakeholders report incoherence, "
                                "capacity and finance barriers (Augustenborg et al., 2026; Torney & O'Gorman, 2019).")),
                    card(html.H3("The gap"),
                         html.P("The literature establishes the direction of the mechanisms more securely than their combined magnitude."),
                         html.P(html.B("No study jointly measures Ireland's annual expansion and mitigation portfolios on a common scale and "
                                       "relates their balance to observed emissions, so an undetectable mitigation effect cannot be told apart "
                                       "from demonstrated cancellation.")),
                         html.P("The manuscript's Appendix F tabulates all 73 sources reviewed against the research questions.", className="small")),
                ])),
        section("Contribution of this study",
                html.Div(className="grid-3", children=[
                    card(html.Div("1", className="big-num"), html.H3("Measurement"),
                         html.P("A new annual production-pressure index P, scored on the same implementation × coverage × eligibility × "
                                "bindingness scale as the mitigation index M; non-binding growth strategies are tracked separately as G. "
                                "The two policy sets become commensurable and incoherence becomes measurable (S = M − P).")),
                    card(html.Div("2", className="big-num"), html.H3("Attribution with a short series"),
                         html.P("Three designs whose assumptions fail in different ways — breaks & exact decomposition, an ARDL "
                                "policy-mix model with block bootstrap, and a within-Ireland regional DiD — plus explicit power analysis.")),
                    card(html.Div("3", className="big-num"), html.H3("Linking decomposition to policy"),
                         html.P("The annual LMDI activity and intensity effects are regressed on changes in P and M, testing directly "
                                "whether expansion works through scale and mitigation through intensity.")),
                ]),
                callout("caution", "Scope",
                        "The analysis is Ireland-only. Quota abolition and CAP reform applied to every EU member state, so no untreated "
                        "foreign comparator exists; within-Ireland variation in exposure provides the comparison instead.")),
        section("The study at a glance",
                kpi_row(kpi("35", "years of CRF3 emissions", "1990–2024"), kpi("19", "policy instruments coded", "11 mitigation · 5 pressure · 3 strategies"),
                        kpi("3", "triangulated designs", "breaks & LMDI · ARDL · regional DiD"), kpi("30 / 30", "automated verification checks pass")),
                html.Div(className="roadmap", children=[
                    dcc.Link(className="road-step", href=h, children=[html.Span(n, className="road-num"), html.Span(t)])
                    for h, n, t in [("/questions", "2", "Research questions & framework"), ("/data", "3", "Explore the dataset"),
                                    ("/methods", "4", "Implementation step by step"), ("/results", "5", "Results"),
                                    ("/conclusions", "6", "Conclusions & policy")]])),
    ])


def register_callbacks(app):
    @app.callback(Output("ov-fig", "figure"), Input("ov-mode", "value"))
    def _upd(mode):
        return emissions_fig(mode)
