"""Appendix – acronyms and abbreviations used in the research, as an interactive table."""
import csv
import io
import re
from pathlib import Path

from dash import html, dcc, Input, Output, State, no_update

from ..components import page_header, section, card, kpi, kpi_row, table, badge
from ..data_store import DATA

HERE = Path(__file__).parent

# acronym, full form, category, what it means in this study
ACRONYMS = [
    # Methods & statistics
    ("ARDL", "AutoRegressive Distributed Lag", "Methods & statistics",
     "Time-series model of emissions on their own lags and on current and lagged policy indices and controls. Its long-run coefficients θ_M and θ_P answer RQ3."),
    ("LMDI", "Logarithmic Mean Divisia Index", "Methods & statistics",
     "Exact index decomposition (LMDI-I) that splits the change in emissions into activity, productivity and intensity effects with no residual."),
    ("DiD", "Difference-in-Differences", "Methods & statistics",
     "Regional design comparing regions with high and low dairy exposure before and after quota abolition in 2015 (RQ4)."),
    ("TWFE", "Two-Way Fixed Effects", "Methods & statistics",
     "Regression with region and year fixed effects, used to estimate the continuous-exposure difference-in-differences."),
    ("ITS", "Interrupted Time Series", "Methods & statistics",
     "Segmented regression testing for a change in level and trend of emissions at a policy date."),
    ("HAC", "Heteroskedasticity and Autocorrelation Consistent", "Methods & statistics",
     "Newey–West standard errors that stay valid when residuals are autocorrelated or have changing variance."),
    ("OLS", "Ordinary Least Squares", "Methods & statistics", "Standard linear regression estimator."),
    ("AIC", "Akaike Information Criterion", "Methods & statistics", "Model-selection criterion trading fit against the number of parameters."),
    ("AICc", "Corrected Akaike Information Criterion", "Methods & statistics",
     "AIC with a small-sample correction; selects the ARDL lag order with n = 28 observations."),
    ("BIC", "Bayesian Information Criterion", "Methods & statistics",
     "Model-selection criterion with a stronger penalty than AIC; selects the number of structural breaks."),
    ("SSR", "Sum of Squared Residuals", "Methods & statistics", "Total squared prediction error of a fitted model; minimised in the break search."),
    ("UDmax", "Unweighted Double maximum", "Methods & statistics",
     "Bai–Perron test statistic for at least one structural break when the number of breaks is unknown; its p-value is bootstrapped."),
    ("ADF", "Augmented Dickey–Fuller", "Methods & statistics", "Unit-root test (null: the series is non-stationary)."),
    ("KPSS", "Kwiatkowski–Phillips–Schmidt–Shin", "Methods & statistics", "Stationarity test (null: the series is stationary); used alongside ADF."),
    ("RESET", "Regression Equation Specification Error Test", "Methods & statistics", "Ramsey test for functional-form misspecification of the ARDL."),
    ("CUSUM", "Cumulative Sum (of recursive residuals)", "Methods & statistics", "Test for parameter stability of the ARDL over time."),
    ("RI", "Randomisation Inference", "Methods & statistics",
     "Permutation p-value: the DiD estimate is compared with the 120 estimates obtained by reassigning exposure across the five regions."),
    ("WCB", "Wild Cluster Bootstrap", "Methods & statistics", "Bootstrap p-value for regressions with few clusters (here five regions)."),
    ("MDE", "Minimum Detectable Effect", "Methods & statistics", "Smallest effect the design can detect with 80% power; effects below it cannot be ruled out."),
    ("AR(1)", "First-order AutoRegressive process", "Methods & statistics", "Error structure in which each residual depends on the previous one."),
    ("CI", "Confidence Interval", "Methods & statistics", "Range that contains the true value with a stated probability (90% or 95%)."),
    ("SE", "Standard Error", "Methods & statistics", "Estimated standard deviation of a coefficient estimate."),
    ("SD", "Standard Deviation", "Methods & statistics", "Spread of a variable; effects are also reported per 1 SD change in an index."),
    # Study symbols
    ("M", "Mitigation index", "Study indices & symbols", "Sum of the scores of the 11 mitigation instruments in each year (implementation × coverage × eligibility × bindingness)."),
    ("P", "Production-pressure index", "Study indices & symbols", "Sum of the scores of the 5 expansion (production-pressure) instruments in each year."),
    ("G", "Strategy signal", "Study indices & symbols", "Sum of the scores of the 3 national growth strategies (G01–G03); reported separately from P."),
    ("S", "Net policy signal", "Study indices & symbols", "S = M − P: positive when mitigation effort outweighs production pressure."),
    ("I × s × e × B × w", "Implementation × coverage × eligibility × bindingness × content weight", "Study indices & symbols", "The components multiplied to score one policy in one year (w = 1 except Food Vision 2030, w = 0.5)."),
    ("IO", "Intensity Offset", "Study indices & symbols", "Share of the activity-driven emission increase cancelled by falling emission intensity."),
    ("RQ", "Research Question", "Study indices & symbols", "The four research questions RQ1–RQ4 that structure the study."),
    ("LU", "Livestock Unit", "Study indices & symbols", "Common unit that weights animals by feed requirement (one dairy cow ≈ 1 LU)."),
    ("LSU", "Livestock Unit (Eurostat coefficients)", "Study indices & symbols", "Eurostat's livestock-unit coefficients used to build LU."),
    ("EF", "Emission Factor", "Study indices & symbols", "Emissions per head or per unit of input, e.g. kg CH₄ per dairy cow per year."),
    # Emissions & inventory
    ("GHG", "Greenhouse Gas", "Emissions & inventory", "Gases that trap heat in the atmosphere; here CH₄ and N₂O from agriculture."),
    ("CH₄", "Methane", "Emissions & inventory", "Greenhouse gas from enteric fermentation and manure; the largest part of agricultural emissions."),
    ("N₂O", "Nitrous oxide", "Emissions & inventory", "Greenhouse gas from fertiliser, manure and urine nitrogen applied to soils."),
    ("CO₂e", "Carbon dioxide equivalent", "Emissions & inventory", "Common unit that converts each gas to CO₂ using its global warming potential."),
    ("GWP", "Global Warming Potential", "Emissions & inventory", "Warming of a gas relative to CO₂ over a time horizon."),
    ("GWP100", "Global Warming Potential over 100 years", "Emissions & inventory", "Metric used in the inventory (AR5: CH₄ = 28, N₂O = 265)."),
    ("GWP*", "GWP-star", "Emissions & inventory", "Alternative metric that reflects the warming from changes in short-lived methane emissions; used as a supplement."),
    ("CRF", "Common Reporting Format", "Emissions & inventory", "UNFCCC sector classification of GHG inventories."),
    ("CRF3", "Common Reporting Format sector 3 (Agriculture)", "Emissions & inventory",
     "The study's outcome: IPCC sector 3 agricultural emissions, excluding agricultural fuel combustion and fishing."),
    ("CRT", "Common Reporting Tables", "Emissions & inventory",
     "UNFCCC reporting tables (successor to CRF) in Ireland's 2025 submission; source of the dairy split and nitrogen detail."),
    ("NO / NE / NA", "Not Occurring / Not Estimated / Not Applicable", "Emissions & inventory", "Inventory notation keys; treated as missing values."),
    ("AR5", "IPCC Fifth Assessment Report", "Emissions & inventory", "Source of the GWP100 values used in the inventory."),
    # Institutions & data
    ("EPA", "Environmental Protection Agency (Ireland)", "Institutions & data", "Publishes Ireland's greenhouse-gas inventory; source of CRF3 emissions 1990–2024."),
    ("CSO", "Central Statistics Office (Ireland)", "Institutions & data", "Source of livestock numbers (national and regional), milk intake, prices, CPI and GNI*."),
    ("UNFCCC", "United Nations Framework Convention on Climate Change", "Institutions & data", "Treaty body to which Ireland submits its annual inventory (CRT)."),
    ("IPCC", "Intergovernmental Panel on Climate Change", "Institutions & data", "Sets inventory guidelines and the sector classification."),
    ("DAFM", "Department of Agriculture, Food and the Marine", "Institutions & data", "Irish ministry running farm schemes; future source of eligibility shares."),
    ("OECD", "Organisation for Economic Co-operation and Development", "Institutions & data", "Its composite-indicator handbook guides the index construction."),
    ("EU", "European Union", "Institutions & data", "Sets the milk quota, the CAP and nitrates rules."),
    ("CAP", "Common Agricultural Policy", "Institutions & data", "EU farm policy; the 2005 decoupling ended coupled livestock premia."),
    ("NUTS", "Nomenclature of Territorial Units for Statistics", "Institutions & data", "EU regional classification; CSO regional data use NUTS 2 and NUTS 3."),
    ("GISCO", "Geographic Information System of the Commission", "Institutions & data", "Eurostat service providing the NUTS boundaries for the regional map."),
    ("CPI", "Consumer Price Index", "Institutions & data", "Deflator that converts nominal prices to real prices."),
    ("GNI*", "Modified Gross National Income", "Institutions & data", "Ireland's measure of domestic economic activity; an ARDL control."),
    ("SHA-256", "Secure Hash Algorithm, 256-bit", "Institutions & data", "Fingerprint recorded for every raw file to prove provenance."),
    ("CSV", "Comma-Separated Values", "Institutions & data", "Plain-text table format used for downloads."),
    ("S.I.", "Statutory Instrument", "Institutions & data", "Irish secondary legislation, e.g. S.I. 113/2022 (nitrates regulations)."),
    # Policies & schemes
    ("REPS", "Rural Environment Protection Scheme", "Policies & schemes", "Agri-environment scheme 1994–2014 (M01)."),
    ("NAP", "Nitrates Action Programme", "Policies & schemes", "Good Agricultural Practice regulations limiting nitrogen use (M02, M09)."),
    ("AEOS", "Agri-Environment Options Scheme", "Policies & schemes", "Agri-environment scheme 2010–2018 (M04)."),
    ("SDAS", "Sustainable Dairy Assurance Scheme", "Policies & schemes", "Origin Green dairy sustainability certification from 2014 (M06)."),
    ("GLAS", "Green Low-Carbon Agri-Environment Scheme", "Policies & schemes", "Agri-environment scheme 2015–2022 (M07)."),
    ("BDGP", "Beef Data and Genomics Programme", "Policies & schemes", "Payments for genotyping and breeding more efficient suckler herds (part of M08)."),
    ("BEEP-S", "Beef Environmental Efficiency Programme – Sucklers", "Policies & schemes", "Payments for weighing calves and cows to improve suckler efficiency (part of M08)."),
    ("LESS", "Low Emission Slurry Spreading", "Policies & schemes", "Trailing-shoe and similar spreading methods that cut ammonia and N losses (excluded from the M09 baseline)."),
    ("ACRES", "Agri-Climate Rural Environment Scheme", "Policies & schemes", "Agri-environment scheme from 2023 (M10)."),
    ("SCEP", "Suckler Carbon Efficiency Programme", "Policies & schemes", "Successor to BEEP-S from 2023 (part of M08)."),
    ("TAMS II", "Targeted Agricultural Modernisation Scheme II", "Policies & schemes", "Capital grants, including the Dairy Equipment Scheme that supported expansion (P05)."),
]

CATEGORIES = list(dict.fromkeys(a[2] for a in ACRONYMS))
CAT_TONE = dict(zip(CATEGORIES, ["blue", "green", "orange", "violet", "aqua"]))

# Where each acronym appears: scan the page sources once at start-up
PAGE_FILES = [("/", "The problem", ["overview.py"]), ("/questions", "Research questions", ["questions.py"]),
              ("/data", "Dataset", ["dataset.py", "dataset_sources.py", "dataset_map.py", "../data_store.py"]),
              ("/methods", "Implementation & methods", ["methods.py"]), ("/results", "Results", ["results.py"]),
              ("/conclusions", "Conclusions", ["conclusions.py"])]
_SRC = {path: "\n".join((HERE / f).read_text(encoding="utf-8") for f in files) for path, _, files in PAGE_FILES}
_SRC["/data"] += "\n".join(r["name"] for r in DATA["codebook"])   # policy names shown in the codebook table


def _pattern(acr):
    parts = [p.strip() for p in acr.split("/")] if " / " in acr else [acr.split(" (")[0]]
    alts = []
    for p in parts:
        p = p.replace("₂", "(?:₂|2)").replace("₄", "(?:₄|4)") if any(c in p for c in "₂₄") else re.escape(p)
        alts.append(p.replace(r"\ ", r"\s"))
    tail = r"(?![A-Za-z])" if acr == "RQ" else r"(?![A-Za-z0-9])"   # RQ appears as RQ1…RQ4
    return re.compile(r"(?<![A-Za-z0-9])(?:" + "|".join(alts) + r")" + tail)


def appears_on(acr):
    if len(acr) == 1:   # single-letter symbols match everywhere; point to where they are defined
        return [("/methods", "Implementation & methods"), ("/results", "Results")]
    rx = _pattern(acr)
    return [(path, label) for path, label, _ in PAGE_FILES if rx.search(_SRC[path])]


ROWS = [{"acronym": a, "full": f, "category": c, "meaning": m,
         "pages": ", ".join(l for _, l in appears_on(a)) or "Analysis notebook only"}
        for a, f, c, m in ACRONYMS]
LETTERS = sorted({r["acronym"][0].upper() for r in ROWS if r["acronym"][0].isalpha()})


def filtered(query, cats, letter):
    q = (query or "").lower().strip()
    out = []
    for r in ROWS:
        if cats and r["category"] not in cats:
            continue
        if letter and not r["acronym"].upper().startswith(letter):
            continue
        if q and q not in " ".join((r["acronym"], r["full"], r["meaning"])).lower():
            continue
        out.append(r)
    return sorted(out, key=lambda r: r["acronym"].lower())


def detail(r):
    if not r:
        return html.P("Click a row in the table to see what the acronym means and where it is used.", className="fig-note")
    links = appears_on(r["acronym"])
    return html.Div([
        html.Div([html.Span(r["acronym"], className="acr-big"), badge(r["category"], CAT_TONE[r["category"]])], className="acr-head"),
        html.H3(r["full"]),
        html.P(r["meaning"]),
        html.Div([html.Span("Appears on: ", className="ctl-label")] +
                 ([dcc.Link(l, href=p, className="btn btn-sm") for p, l in links] or
                  [html.Span("Used in the analysis notebook; not shown on these pages.", className="small")]), className="btn-row"),
    ])


def layout():
    return html.Div([
        page_header("Appendix", "Acronyms and abbreviations",
                    "Every acronym used in the study and on this site, with its full form and what it means here. "
                    "Search, filter by category or initial letter, and click a row for details."),
        kpi_row(kpi(str(len(ROWS)), "acronyms and symbols"),
                *[kpi(str(sum(r["category"] == c for r in ROWS)), c) for c in CATEGORIES[:3]]),
        section("Table A1 · Acronyms",
                card(
                    html.Div(className="control-grid", children=[
                        html.Div([html.Label("Search", className="ctl-label"),
                                  dcc.Input(id="ac-q", type="search", debounce=False, placeholder="e.g. ARDL, methane, scheme…",
                                            className="text-input")], className="span-2"),
                        html.Div([html.Label("Category", className="ctl-label"),
                                  dcc.Checklist(id="ac-cat", value=[], className="chk", inline=True,
                                                options=[{"label": f" {c}", "value": c} for c in CATEGORIES])], className="span-2"),
                        html.Div([html.Label("Initial letter", className="ctl-label"),
                                  dcc.RadioItems(id="ac-letter", value="", className="seg", inline=True,
                                                 options=[{"label": "All", "value": ""}] + [{"label": l, "value": l} for l in LETTERS])],
                                 className="span-3"),
                        html.Div([html.Label("Download", className="ctl-label"),
                                  html.Button("⬇ Table A1 (CSV)", id="ac-dl-btn", className="btn")]),
                    ]),
                    html.P(id="ac-count", className="fig-note"),
                    dcc.Download(id="ac-dl"),
                    table(filtered("", [], ""), [("acronym", "Acronym"), ("full", "Full form"), ("category", "Category"),
                                                 ("pages", "Appears on")], id="ac-table", page_size=15,
                          style_cond=[{"if": {"column_id": "acronym"}, "fontWeight": 700, "color": "#0b0b0b"}]),
                ),
                card(html.Div(id="ac-detail", children=detail(None)))),
    ])


def register_callbacks(app):
    @app.callback(Output("ac-table", "data"), Output("ac-count", "children"), Output("ac-table", "active_cell"),
                  Output("ac-table", "page_current"),
                  Input("ac-q", "value"), Input("ac-cat", "value"), Input("ac-letter", "value"))
    def _filter(q, cats, letter):
        rows = filtered(q, cats, letter)
        return rows, f"Showing {len(rows)} of {len(ROWS)} acronyms.", None, 0

    @app.callback(Output("ac-detail", "children"), Input("ac-table", "active_cell"), State("ac-table", "derived_viewport_data"))
    def _detail(cell, view):
        if not cell or not view or cell["row"] >= len(view):
            return detail(None)
        return detail(view[cell["row"]])

    @app.callback(Output("ac-dl", "data"), Input("ac-dl-btn", "n_clicks"), State("ac-table", "data"), prevent_initial_call=True)
    def _dl(n, rows):
        if not rows:
            return no_update
        buf = io.StringIO()
        w = csv.DictWriter(buf, fieldnames=["acronym", "full", "category", "meaning", "pages"])
        w.writeheader()
        w.writerows(rows)
        return dict(content=buf.getvalue(), filename="table_A1_acronyms.csv")
