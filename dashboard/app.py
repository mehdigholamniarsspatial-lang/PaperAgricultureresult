"""Expansion versus mitigation: research dashboard (Plotly Dash).

Run locally:   python run_local.py          (http://127.0.0.1:8050)
On Vercel:     api/index.py exposes the Flask server as `app`.
"""
from pathlib import Path
import dash
from dash import Dash, html, dcc, Input, Output, State

from .pages import overview, questions, dataset, methods, results, conclusions, appendix

HERE = Path(__file__).parent

PAGES = [
    ("/", "1", "The problem", overview),
    ("/questions", "2", "Research questions", questions),
    ("/data", "3", "Dataset", dataset),
    ("/methods", "4", "Implementation & methods", methods),
    ("/results", "5", "Results", results),
    ("/conclusions", "6", "Conclusions", conclusions),
    ("/appendix", "A", "Appendix", appendix),
]

app = Dash(
    __name__,
    title="Expansion vs mitigation · Irish agricultural emissions",
    assets_folder=str(HERE / "assets"),
    suppress_callback_exceptions=True,
    update_title=None,
    meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"},
               {"name": "description", "content": "Interactive presentation of a policy evaluation of Irish agricultural greenhouse-gas emissions, 1990–2024."}],
    external_stylesheets=["https://fonts.googleapis.com/css2?family=Source+Serif+4:opsz,wght@8..60,500;8..60,600;8..60,700&display=swap"],
)
server = app.server


def nav():
    return html.Nav(className="sidebar", children=[
        html.Div(className="brand", children=[
            html.Div("☘", className="brand-mark"),
            html.Div([html.Div("Expansion vs mitigation", className="brand-title"),
                      html.Div("Irish agricultural GHG, 1990–2024", className="brand-sub")]),
        ]),
        html.Div("Research steps", className="nav-label"),
        html.Div(id="nav-links", className="nav-links"),
        html.Div(className="sidebar-foot", children=[
            html.Div("Mehdi Gholamnia"),
            html.Div("INPACT project · University of Galway"),
            html.Div("October 2026", className="muted"),
        ]),
    ])


app.layout = html.Div(className="shell", children=[
    dcc.Location(id="url"),
    html.Button("☰ Menu", id="nav-burger", className="nav-burger", n_clicks=0),
    html.Div(nav(), id="nav-wrap", className="nav-wrap"),
    html.Main(id="page", className="main"),
])


@app.callback(Output("page", "children"), Output("nav-links", "children"), Input("url", "pathname"))
def route(path):
    path = (path or "/").rstrip("/") or "/"
    current = next((p for p in PAGES if p[0] == path), PAGES[0])
    links = [dcc.Link(href=p[0], className="nav-link" + (" active" if p is current else ""), children=[
        html.Span(p[1], className="nav-num"), html.Span(p[2])]) for p in PAGES]
    idx = PAGES.index(current)
    pager = html.Div(className="pager", children=[
        dcc.Link(["← ", PAGES[idx - 1][2]], href=PAGES[idx - 1][0], className="pager-link") if idx > 0 else html.Span(),
        dcc.Link([PAGES[idx + 1][2], " →"], href=PAGES[idx + 1][0], className="pager-link next") if idx < len(PAGES) - 1 else html.Span(),
    ])
    return [current[3].layout(), pager], links


app.clientside_callback(
    """function(n, path, cls) {
        const trig = (window.dash_clientside.callback_context.triggered[0] || {}).prop_id || "";
        if (trig.startsWith("nav-burger")) { return (cls || "").includes("open") ? "nav-wrap" : "nav-wrap open"; }
        return "nav-wrap";
    }""",
    Output("nav-wrap", "className"), Input("nav-burger", "n_clicks"), Input("url", "pathname"), State("nav-wrap", "className"),
)

for _, _, _, mod in PAGES:
    if hasattr(mod, "register_callbacks"):
        mod.register_callbacks(app)
