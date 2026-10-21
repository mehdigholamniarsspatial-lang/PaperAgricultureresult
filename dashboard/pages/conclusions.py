"""Step 6 – discussion, policy implications, limitations and next steps."""
from dash import html

from ..components import page_header, section, card, callout, kpi, kpi_row, details
from ..data_store import KEY

REFS = [
    "Ang, B. W. (2015). LMDI decomposition approach: A guide for implementation. Energy Policy, 86, 233–238.",
    "Augustenborg, C. A., Lentz, P., & Pender, A. (2026). Barriers to environmental policy implementation: Stakeholder perceptions in the context of Ireland. Journal of Environmental Policy & Planning, 28(3), 531–553.",
    "Bai, J., & Perron, P. (2003). Computation and analysis of multiple structural change models. Journal of Applied Econometrics, 18(1), 1–22.",
    "Balaine, L., Läpple, D., Buckley, C., & Dillon, E. (2022). Reconciling socio-economic and environmental sustainability in agri-food development. EuroChoices, 21(2), 52–57.",
    "Cameron, A. C., Gelbach, J. B., & Miller, D. L. (2008). Bootstrap-based improvements for inference with clustered errors. Review of Economics and Statistics, 90(3), 414–427.",
    "Donnellan, T., Hanrahan, K., Breen, J. P., & Gillespie, P. (2013). Climate change and agricultural policy coherence: Agricultural growth and GHG emissions in Ireland. AES Conference, Warwick.",
    "Greening, L. A., Greene, D. L., & Difiglio, C. (2000). Energy efficiency and consumption — the rebound effect — a survey. Energy Policy, 28(6–7), 389–401.",
    "Hamed, K. H., & Rao, A. R. (1998). A modified Mann–Kendall trend test for autocorrelated data. Journal of Hydrology, 204(1–4), 182–196.",
    "Läpple, D., Carter, C. A., & Buckley, C. (2022). EU milk quota abolition, dairy expansion, and greenhouse gas emissions. Agricultural Economics, 53(1), 125–142.",
    "Lawlor, D. A., Tilling, K., & Davey Smith, G. (2016). Triangulation in aetiological epidemiology. International Journal of Epidemiology, 45(6), 1866–1886.",
    "Marsh, D., & McConnell, A. (2010). Towards a framework for establishing policy success. Public Administration, 88(2), 564–583.",
    "Nilsson, M., et al. (2012). Understanding policy coherence: Analytical framework and examples of sector–environment policy interactions in the EU. Environmental Policy and Governance, 22(6), 395–423.",
    "Pesaran, M. H., Shin, Y., & Smith, R. J. (2001). Bounds testing approaches to the analysis of level relationships. Journal of Applied Econometrics, 16(3), 289–326.",
    "Smith, M. A., Cain, M., & Allen, M. R. (2021). Further improvement of warming-equivalent emissions calculation. npj Climate and Atmospheric Science, 4, 19.",
    "Stechemesser, A., Koch, N., Mark, E., et al. (2024). Climate policies that achieved major emission reductions: Global evidence from two decades. Science, 385(6711), 884–892.",
    "Webb, M. D. (2023). Reworking wild bootstrap-based inference for clustered errors. Canadian Journal of Economics, 56(3), 839–858.",
    "Young, A. (2019). Channeling Fisher: Randomization tests and the statistical insignificance of seemingly significant experimental results. Quarterly Journal of Economics, 134(2), 557–598.",
]


def layout():
    k = KEY
    return html.Div([
        page_header("Step 6 · Conclusions", "Expansion left a footprint; mitigation too little to offset",
                    "Production-oriented policy measurably raised Irish agricultural emissions. The mitigation portfolio, mostly voluntary and "
                    "intensity-oriented, shows no detectable effect on total emissions — so expansion had little mitigation to offset."),
        kpi_row(kpi(f"+{k['offset']['pressure_effect_pct']:.1f}%", "2024 emissions due to production pressure since 2000", "90% CI 6.7–15.7%", tone="tone-orange"),
                kpi(f"{k['offset']['cum_P_kt'] / 1e3:.1f} Mt", "CO₂e added by pressure, 2000–2024"),
                kpi(f"{k['lmdi']['P4_intensity_offset']:.2f}", "share of post-quota growth cancelled by intensity gains"),
                kpi("16–23%", "fewer livestock units needed by 2030", "unless intensity falls far faster", tone="tone-red")),
        section("Discussion",
                html.Div(className="grid-3", children=[
                    card(html.H3("Expansion with little to offset"),
                         html.P("Three pieces of evidence point the same way: scale and yield growth after 2014 outran intensity gains more than three to "
                                "one; the policy-mix model attributes an 11.2% rise in 2024 emissions to production pressure; and the same model finds no "
                                "emission-reducing effect of mitigation. A rival account would need to explain all three.")),
                    card(html.H3("Timing: 2010, not 2015"),
                         html.P("The trend changed in 2010–2012. Expansion began under the quota increases and Food Harvest 2020; abolition continued it "
                                "rather than starting it. Analyses that treat 2015 as the single turning point understate the soft-landing years.")),
                    card(html.H3("Why mitigation did not register"),
                         html.P("Most instruments were voluntary or incentive-based schemes acting on intensity, and the main binding one was designed for "
                                "water quality. An intensity-only portfolio can lower emissions per litre while totals rise. The positive M association is "
                                "best read as reverse timing: schemes such as GLAS grew in the same years as the herd.")),
                ]),
                callout("read", "Relation to stakeholder-identified barriers",
                        "Of the five barriers in Augustenborg et al. (2026), policy incoherence is supported (P and M rose together 2005–2020 and P has a "
                        "detectable effect) and competing political priorities are consistent with the break near Food Harvest 2020. Capacity, financial "
                        "and planning constraints cannot be separated with these data.")),
        section("Implications for policy",
                html.Div(className="impl-grid", children=[
                    html.Div(className="impl", children=[html.Div("1", className="impl-n"), html.H3("Screen expansion instruments"),
                                                         html.P("Assess derogations, growth strategies and capital grants for their emission effect at design and "
                                                                "renewal. The next derogation renewal is an immediate opportunity.")]),
                    html.Div(className="impl", children=[html.Div("2", className="impl-n"), html.H3("Add activity-level instruments"),
                                                         html.P("At recent intensity trends the 2030 ceiling requires about a fifth fewer livestock units. Voluntary "
                                                                "reduction or diversification schemes, and conditions on expansion supports, belong in the mix.")]),
                    html.Div(className="impl", children=[html.Div("3", className="impl-n"), html.H3("Track the net policy signal"),
                                                         html.P("Update the production-pressure index annually alongside INPACT and report it with Climate Action "
                                                                "Plan progress, to show whether the policy mix pulls in one direction.")]),
                    html.Div(className="impl", children=[html.Div("4", className="impl-n"), html.H3("Build in evaluability"),
                                                         html.P("With 28 annual observations only effects of about 4% per 0.1 index units are reliably detectable. "
                                                                "Farm-level administrative data and staggered roll-outs would allow far more precise evaluation.")]),
                ])),
        section("Limitations",
                html.Div(className="grid-2", children=[
                    card(html.Ul([
                        html.Li([html.B("Short series. "), "Twenty-eight observations limit precision; effects below the MDE cannot be ruled out."]),
                        html.Li([html.B("Observational identification. "), "ARDL estimates are conditional associations. Adding GNI* leaves θ_P positive (0.49) "
                                 "but not significant (p = 0.13) because GNI* grows fastest after quota abolition."]),
                        html.Li([html.B("Regional design. "), "Five regions give little power and pre-trends rule out a causal reading."]),
                    ])),
                    card(html.Ul([
                        html.Li([html.B("Policy measurement. "), "Index scores rest on coding judgements; M is provisional and coder 2 is simulated."]),
                        html.Li([html.B("Inventory detail. "), "One implied N₂O intensity for mineral and manure N; the dairy split ends in 2023; "
                                 "inventory method changes appear as intensity change."]),
                    ])),
                ])),
        section("Next steps",
                html.Div(className="grid-2", children=[
                    card(html.H3("Data"), html.Ul([html.Li("INPACT export for the mitigation index M"), html.Li("A real, blind second coder for P"),
                                                   html.Li("DAFM statistics for derogation and TAMS II eligibility shares"),
                                                   html.Li("CRT 2026 submission to extend the LMDI and regional emissions to 2024")])),
                    card(html.H3("Design"), html.Ul([html.Li("County-level panel from the Census of Agriculture and DAFM derogation statistics for a "
                                                             "continuous-treatment design (Callaway et al., 2024)"),
                                                     html.Li("Transfer the common-scale approach to other jurisdictions where land-based sectors face "
                                                             "growth and decarbonisation mandates at once"), html.Li("Submit to Climate Policy")])),
                ])),
        section("Key references", details("Show references", html.Ol([html.Li(r) for r in REFS], className="refs"))),
        html.Div(className="footer-note", children=[
            html.P("All numbers on this site come from a full re-run of ireland_agri_ghg_analysis.ipynb (seed 20261019) and reproduce the manuscript "
                   "(Revision 4) exactly. Data: EPA, Ireland's CRT 2025 submission to the UNFCCC, CSO and Eurostat."),
        ]),
    ])
