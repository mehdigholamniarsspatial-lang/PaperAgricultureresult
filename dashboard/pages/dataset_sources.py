"""Step 3 – 'Data sources & resources' tab: the full source catalogue (from data/data_sources.json), interactively."""
import csv
import io
import json
from pathlib import Path

import plotly.graph_objects as go
from dash import html, dcc, Input, Output, State, ALL, ctx, no_update

from ..components import section, card, kpi, kpi_row, callout, table, badge
from ..theme import base_layout, empty_fig, BLUE, ORANGE, AQUA, YELLOW, MAGENTA, GREEN, VIOLET, INK, INK2, MUTED, GRID, GRAPH_CONFIG

HERE = Path(__file__).resolve().parents[1] / "data"
CATALOGUE = json.loads((HERE / "data_sources.json").read_text(encoding="utf-8"))
ITEMS = CATALOGUE["items"]
BY_ID = {d["id"]: d for d in ITEMS}
SOURCES_XLSX = HERE / "data_sources.xlsx"

GROUPS = list(dict.fromkeys(d["group"] for d in ITEMS))
GROUP_COL = dict(zip(GROUPS, [BLUE, VIOLET, YELLOW, AQUA, ORANGE, MAGENTA, GREEN]))
GROUP_SHORT = {"EPA GHG inventory": "EPA", "Ireland CRT 2025 (UNFCCC)": "UNFCCC CRT", "Eurostat": "Eurostat", "CSO": "CSO",
               "Policy codebooks": "Codebooks", "Reference parameters": "Reference", "Derived in notebook": "Derived"}
TAGS = ["Outcome", "Decomposition (LMDI)", "ARDL controls & prices", "Regional DiD", "Policy indices",
        "Checks & harmonisation", "Robustness & supplements", "Not used"]
KINDS = ["Raw dataset", "Codebook", "Reference parameter", "Derived variable"]
VIEWS = [("cards", "Resource cards"), ("timeline", "Coverage timeline"), ("lineage", "Source → analysis"), ("table", "Full table")]


def group_years(g):
    ys = [(d["y0"], d["y1"]) for d in ITEMS if d["group"] == g and d["y0"]]
    return f"{min(a for a, _ in ys)}–{max(b for _, b in ys)}" if ys else "–"


def filtered(groups, query, tags, kinds, opts):
    q = (query or "").lower().strip()
    out = []
    for d in ITEMS:
        if groups and d["group"] not in groups:
            continue
        if tags and not set(tags) & set(d["tags"]):
            continue
        if kinds and d["kind"] not in kinds:
            continue
        if "link" in (opts or []) and not d["download"]:
            continue
        if "hide" in (opts or []) and not d["used"]:
            continue
        if q and q not in " ".join(str(d[k]) for k in ("id", "group", "parameter", "description", "unit", "years", "dataset",
                                                       "provider", "role")).lower():
            continue
        out.append(d)
    return out


# ------------------------------------------------------------------ pieces
def gbadge(g):
    return html.Span(GROUP_SHORT[g], className="gbadge", style={"--g": GROUP_COL[g]})


def link_buttons(d, small=True):
    cls = "btn-sm" if small else "btn"
    kids = []
    if d["download"]:
        kids.append(html.A("⬇ Download", href=d["download"], target="_blank", rel="noopener", className=f"btn {cls} src-link"))
    if d["docs"]:
        kids.append(html.A("📄 Documentation", href=d["docs"], target="_blank", rel="noopener", className=f"btn {cls} src-link"))
    if not kids:
        kids.append(html.Span(d.get("download_note") or "Produced in this study — no external download", className="src-nolink"))
    return html.Div(kids, className="btn-row")


def resource_card(d, selected=None):
    return html.Div(className="res-card" + (" is-unused" if not d["used"] else "") + (" is-sel" if d["id"] == selected else ""),
                    style={"--g": GROUP_COL[d["group"]]}, children=[
        html.Div(className="res-top", children=[html.Span(f"#{d['id']}", className="res-id"), gbadge(d["group"]),
                                                html.Span(d["years"] or "–", className="res-years")]),
        html.Div(d["parameter"], className="res-param"),
        html.Div(d["description"], className="res-desc"),
        html.Div(className="res-meta", children=[html.Span([html.B("Unit "), d["unit"] or "–"]),
                                                 html.Span([html.B("Table "), d["dataset"] or "–"])]),
        html.Div([html.Span(t, className="tag" + (" tag-off" if t == "Not used" else "")) for t in d["tags"]], className="tag-row"),
        html.Div(className="res-foot", children=[link_buttons(d),
                                                 html.Button("Details →", id={"type": "src-pick", "index": d["id"]}, className="btn btn-sm")]),
    ])


def cards_view(rows, selected):
    if not rows:
        return html.P("No resource matches these filters.", className="fig-note")
    out = []
    for g in GROUPS:
        sub = [d for d in rows if d["group"] == g]
        if sub:
            out.append(html.H3([html.Span(className="dot", style={"background": GROUP_COL[g]}), g,
                                html.Span(f"{len(sub)}", className="count")], className="res-group-h"))
            out.append(html.Div([resource_card(d, selected) for d in sub], className="res-grid"))
    return html.Div(out)


def timeline_fig(rows, selected):
    rows = [d for d in rows if d["y0"]]
    if not rows:
        return empty_fig("No dated resource matches these filters")
    rows = sorted(rows, key=lambda d: d["id"])
    lab = [f"#{d['id']} · {d['parameter'][:46] + ('…' if len(d['parameter']) > 46 else '')}" for d in rows]
    fig = go.Figure()
    for g in GROUPS:
        idx = [i for i, d in enumerate(rows) if d["group"] == g]
        if not idx:
            continue
        fig.add_trace(go.Bar(
            y=[lab[i] for i in idx], x=[rows[i]["y1"] - rows[i]["y0"] + 1 for i in idx], base=[rows[i]["y0"] - 0.5 for i in idx],
            orientation="h", name=g, marker=dict(color=GROUP_COL[g], cornerradius=3,
                                                 opacity=[1 if selected in (None, rows[i]["id"]) else 0.35 for i in idx],
                                                 line=dict(color=[INK if rows[i]["id"] == selected else "rgba(0,0,0,0)" for i in idx], width=1.5)),
            customdata=[[rows[i]["id"], rows[i]["years"], rows[i]["dataset"][:70]] for i in idx],
            hovertemplate="<b>%{y}</b><br>%{customdata[1]} · %{customdata[2]}<extra>" + GROUP_SHORT[g] + "</extra>"))
    base_layout(fig, height=24 * len(rows) + 150, hover="closest")
    fig.update_layout(barmode="overlay", margin=dict(l=330, r=20, t=30, b=110), bargap=0.25,
                      legend=dict(orientation="h", yref="container", y=0, yanchor="bottom", x=0, xanchor="left"))
    fig.update_yaxes(autorange="reversed", categoryorder="array", categoryarray=lab, showgrid=False, tickfont=dict(size=11.5))
    fig.update_xaxes(range=[1989.3, 2024.7], dtick=5, showgrid=True, gridcolor=GRID, title="Years used in the analysis")
    for y, t in ((2004.5, "CSO table switch"), (2023.5, "CRT ends")):
        fig.add_vline(x=y, line=dict(color=MUTED, width=1, dash="dot"))
        fig.add_annotation(x=y, y=1, yref="paper", yanchor="bottom", text=t, showarrow=False, font=dict(size=10.5, color=INK2))
    return fig


def sankey_fig(rows):
    if not rows:
        return empty_fig("No resource matches these filters")
    gs = [g for g in GROUPS if any(d["group"] == g for d in rows)]
    ts = [t for t in TAGS if any(t in d["tags"] for d in rows)]
    nodes = gs + ts
    link = {}
    for d in rows:
        for t in d["tags"]:
            link[(d["group"], t)] = link.get((d["group"], t), 0) + 1
    hexa = lambda c, a: f"rgba({int(c[1:3], 16)},{int(c[3:5], 16)},{int(c[5:7], 16)},{a})"
    fig = go.Figure(go.Sankey(
        arrangement="snap",
        node=dict(label=[f"{n}" for n in nodes], pad=14, thickness=16, line=dict(width=0),
                  color=[GROUP_COL[g] for g in gs] + ["#7d7c76" if t == "Not used" else INK2 for t in ts],
                  hovertemplate="%{label}: %{value} entries<extra></extra>"),
        link=dict(source=[nodes.index(a) for a, _ in link], target=[nodes.index(b) for _, b in link], value=list(link.values()),
                  color=[hexa(GROUP_COL[a], 0.35) for a, _ in link],
                  hovertemplate="%{source.label} → %{target.label}: %{value} entries<extra></extra>")))
    base_layout(fig, height=max(380, 26 * len(nodes) + 80), legend=False, hover="closest")
    fig.update_layout(margin=dict(l=10, r=10, t=10, b=10), font=dict(size=12.5, color=INK))
    return fig


def sunburst_fig(rows):
    if not rows:
        return empty_fig("No resource matches these filters")
    ids, labels, parents, colors, hover = [], [], [], [], []
    for g in GROUPS:
        sub = [d for d in rows if d["group"] == g]
        if not sub:
            continue
        ids.append(g); labels.append(GROUP_SHORT[g]); parents.append(""); colors.append(GROUP_COL[g]); hover.append(g)
        for t in dict.fromkeys(d["dataset"] or "–" for d in sub):
            tid = f"{g}/{t}"
            ids.append(tid); labels.append(t.split(" - ")[0][:28]); parents.append(g); colors.append(GROUP_COL[g]); hover.append(t)
            for d in sub:
                if (d["dataset"] or "–") == t:
                    ids.append(f"{tid}/{d['id']}"); labels.append(f"#{d['id']}"); parents.append(tid); colors.append(GROUP_COL[g])
                    hover.append(f"#{d['id']} {d['parameter']}<br>{d['description'][:90]}")
    fig = go.Figure(go.Sunburst(ids=ids, labels=labels, parents=parents, marker=dict(colors=colors, line=dict(color="#fff", width=1)),
                                hovertext=hover, hoverinfo="text", insidetextorientation="radial", maxdepth=2))
    base_layout(fig, height=520, legend=False, hover="closest")
    fig.update_layout(margin=dict(l=10, r=10, t=10, b=10))
    return fig


def table_rows(rows):
    mdlink = lambda u, t: f"[{t}]({u})" if u else ""
    return [{"id": d["id"], "group": d["group"], "parameter": d["parameter"], "description": d["description"], "unit": d["unit"],
             "years": d["years"], "dataset": d["dataset"], "provider": d["provider"], "download": mdlink(d["download"], "⬇ download") or d.get("download_note", ""),
             "docs": mdlink(d["docs"], "documentation"), "role": d["role"], "tags": ", ".join(d["tags"])} for d in rows]


def table_view(rows):
    return table(table_rows(rows), [("id", "#"), ("group", "Source group"), ("parameter", "Parameter (panel column)"), ("description", "Description"),
                                    ("unit", "Unit"), ("years", "Years used"), ("dataset", "Dataset / table"), ("provider", "Provider"),
                                    ("download", "Direct download", {"presentation": "markdown"}), ("docs", "Documentation", {"presentation": "markdown"}),
                                    ("role", "Role in the analysis"), ("tags", "Used in")],
                 id="src-table", page_size=15, filter=True)


def detail_panel(sel):
    d = BY_ID.get(sel)
    if not d:
        return html.Div(className="res-hint", children="Select any resource — click a card's “Details”, a bar on the timeline or a row "
                                                        "in the table — to see its full record, links and related resources here.")
    related = [r for r in ITEMS if r["id"] != d["id"] and ((r["dataset"] and r["dataset"] == d["dataset"]) or
                                                          (r["group"] == d["group"] and set(r["tags"]) & set(d["tags"])))][:10]
    strip = html.Div(className="cov-strip", children=[
        html.Span(className="cov-y" + (" on" if d["y0"] and d["y0"] <= y <= d["y1"] else ""), title=str(y),
                  style={"--g": GROUP_COL[d["group"]]}) for y in range(1990, 2025)])
    field = lambda k, v: html.Div([html.Div(k, className="dl-k"), html.Div(v or "–", className="dl-v")])
    return html.Div(className="res-detail", style={"--g": GROUP_COL[d["group"]]}, children=[
        html.Div(className="res-top", children=[html.Span(f"#{d['id']}", className="res-id"), gbadge(d["group"]), badge(d["kind"], "neutral"),
                                                html.Span(className="grow"),
                                                html.Button("✕", id="src-clear", className="btn btn-sm", title="Close")]),
        html.H3(d["parameter"], className="res-param big"),
        html.P(d["description"]),
        html.Div(className="dl-grid", children=[field("Unit", d["unit"]), field("Years used", d["years"]), field("Dataset / table", d["dataset"]),
                                                field("Provider", d["provider"]), field("Role in the analysis", d["role"]),
                                                field("Used in", ", ".join(d["tags"]))]),
        html.Div([html.Div("Coverage 1990–2024", className="dl-k"), strip,
                  html.Div([html.Span("1990"), html.Span("2024")], className="cov-ends")]),
        link_buttons(d, small=False),
        html.Div([html.Div("Related resources", className="dl-k"),
                  html.Div([html.Button(f"#{r['id']} {r['parameter'][:38]}", id={"type": "src-pick", "index": r["id"]}, className="chip-btn",
                                        style={"--g": GROUP_COL[r["group"]]}) for r in related] or [html.Span("–")], className="btn-row")],
                 className="related") if related else None,
    ])


# ------------------------------------------------------------------ layout
def tab_sources():
    urls = {d["download"] for d in ITEMS if d["download"]}
    tables = {d["dataset"] for d in ITEMS if d["kind"] == "Raw dataset"}
    return html.Div([
        callout("plain", "The full source catalogue", CATALOGUE["note"]),
        kpi_row(kpi(str(len(ITEMS)), "parameters & datasets catalogued"), kpi(str(len(GROUPS)), "source groups"),
                kpi(str(len(tables)), "distinct published tables"), kpi(str(len(urls)), "direct download links", "open data, no login"),
                kpi(str(sum(not d["used"] for d in ITEMS)), "screened but not used", "kept for transparency")),
        section("Source groups",
                html.Div(className="grp-grid", children=[
                    html.Button(id={"type": "src-grp", "index": g}, className="grp-tile", style={"--g": GROUP_COL[g]}, children=[
                        html.Div(GROUP_SHORT[g], className="grp-name"), html.Div(g, className="grp-full"),
                        html.Div([html.B(str(sum(d["group"] == g for d in ITEMS))), " entries · ", group_years(g)], className="grp-meta")])
                    for g in GROUPS]),
                sub="Click a group to show only its resources; click it again (or “All groups”) to reset."),
        card(
            html.Div(className="control-grid", children=[
                html.Div([html.Label("Search", className="ctl-label"),
                          dcc.Input(id="src-q", type="search", debounce=0.3, placeholder="e.g. methane, AAA07, Eurostat, LMDI, kt N…",
                                    className="src-search")], className="span-2"),
                html.Div([html.Label("Used in", className="ctl-label"),
                          dcc.Dropdown(id="src-tags", options=TAGS, value=[], multi=True, placeholder="Any analysis stage")], className="span-2"),
                html.Div([html.Label("Source groups", className="ctl-label"),
                          dcc.Checklist(id="src-groups", value=GROUPS, className="chk chips", inline=True,
                                        options=[{"label": html.Span([html.Span(className="dot", style={"background": GROUP_COL[g]}), GROUP_SHORT[g]]),
                                                  "value": g} for g in GROUPS])], className="span-3"),
                html.Div([html.Label("Groups", className="ctl-label"), html.Button("All groups", id="src-all", className="btn btn-sm")]),
                html.Div([html.Label("Type", className="ctl-label"),
                          dcc.Checklist(id="src-kinds", value=KINDS, className="chk", inline=True,
                                        options=[{"label": f" {k}", "value": k} for k in KINDS])], className="span-2"),
                html.Div([html.Label("Options", className="ctl-label"),
                          dcc.Checklist(id="src-opts", value=[], className="chk", inline=True,
                                        options=[{"label": " Only with a direct download", "value": "link"},
                                                 {"label": " Hide not-used tables", "value": "hide"}])], className="span-2"),
            ]),
            html.Div(className="control-row src-bar", children=[
                html.Span(id="src-count", className="src-count"),
                html.Span(className="grow"),
                html.Button("⬇ Catalogue (CSV, current filter)", id="src-dl-csv", className="btn btn-sm"),
                html.Button("⬇ Original workbook (XLSX)", id="src-dl-xlsx", className="btn btn-sm"),
            ]),
            dcc.Download(id="src-dl"),
        ),
        dcc.Store(id="src-sel"),
        html.Div(id="src-detail"),
        html.Div(className="control-row", children=[
            html.Span("View", className="ctl-label"),
            dcc.RadioItems(id="src-view", value="cards", className="seg", inline=True, options=[{"label": b, "value": a} for a, b in VIEWS])]),
        html.Div(id="src-body"),
    ])


def register_callbacks(app):
    @app.callback(Output("src-groups", "value"),
                  Input({"type": "src-grp", "index": ALL}, "n_clicks"), Input("src-all", "n_clicks"), State("src-groups", "value"),
                  prevent_initial_call=True)
    def _grp(_, __, cur):
        t = ctx.triggered_id
        if t == "src-all":
            return GROUPS
        if not t or not ctx.triggered[0]["value"]:
            return no_update
        return GROUPS if cur == [t["index"]] else [t["index"]]

    @app.callback(Output("src-body", "children"), Output("src-count", "children"),
                  Input("src-groups", "value"), Input("src-q", "value"), Input("src-tags", "value"), Input("src-kinds", "value"),
                  Input("src-opts", "value"), Input("src-view", "value"), Input("src-sel", "data"))
    def _body(groups, q, tags, kinds, opts, view, sel):
        if ctx.triggered_id == "src-sel" and view in ("table", "lineage"):
            return no_update, no_update  # selection only highlights cards / timeline bars; keep the table's page and sort
        rows = filtered(groups, q, tags, kinds, opts)
        n_links = len({d["download"] for d in rows if d["download"]})
        count = [html.B(f"{len(rows)} of {len(ITEMS)}"), f" resources · {n_links} download links · "
                 f"{len({d['dataset'] for d in rows})} tables / files"]
        if view == "timeline":
            undated = sum(1 for d in rows if not d["y0"])
            body = card(dcc.Graph(id="src-tl", figure=timeline_fig(rows, sel), config=GRAPH_CONFIG, className="graph"),
                        html.P("Each bar is the span of years a parameter enters the analysis. Click a bar to open its record. "
                               + (f"{undated} entries without a year span (e.g. reference constants) are not drawn."
                                  if undated else ""), className="fig-note"))
        elif view == "lineage":
            body = html.Div([
                card(html.H3("Which sources feed which part of the analysis"),
                     dcc.Graph(figure=sankey_fig(rows), config=GRAPH_CONFIG, className="graph"),
                     html.P("Link width = number of catalogue entries. An entry that feeds several stages (e.g. the CRT dairy split → LMDI, "
                            "policy coverage and regional imputation) is counted once per stage.", className="fig-note")),
                card(html.H3("Source group → published table → parameter"),
                     dcc.Graph(figure=sunburst_fig(rows), config=GRAPH_CONFIG, className="graph"),
                     html.P("Click a segment to zoom into it; click the centre to zoom back out.", className="fig-note")),
            ])
        elif view == "table":
            body = card(html.P("Filter each column with the row under the header; click a row to open its record.", className="fig-note"),
                        table_view(rows))
        else:
            body = cards_view(rows, sel)
        return body, count

    @app.callback(Output("src-detail", "children"), Input("src-sel", "data"))
    def _detail(sel):
        return detail_panel(sel)

    app.clientside_callback(
        """function(sel) {
            if (sel) { setTimeout(() => { const el = document.getElementById("src-detail");
                if (el) { el.scrollIntoView({behavior: "smooth", block: "start"}); } }, 80); }
            return window.dash_clientside.no_update;
        }""",
        Output("src-detail", "title"), Input("src-sel", "data"), prevent_initial_call=True)

    @app.callback(Output("src-sel", "data", allow_duplicate=True), Input({"type": "src-pick", "index": ALL}, "n_clicks"),
                  prevent_initial_call=True)
    def _pick(_):
        if not ctx.triggered_id or not ctx.triggered[0]["value"]:
            return no_update
        return ctx.triggered_id["index"]

    @app.callback(Output("src-sel", "data", allow_duplicate=True), Input("src-tl", "clickData"), prevent_initial_call=True)
    def _tl(cd):
        return cd["points"][0]["customdata"][0] if cd else no_update

    @app.callback(Output("src-sel", "data", allow_duplicate=True), Input("src-table", "active_cell"),
                  State("src-table", "derived_viewport_data"), prevent_initial_call=True)
    def _tb(cell, view):
        if not cell or not view or cell["row"] >= len(view) or cell["column_id"] in ("download", "docs"):
            return no_update
        return view[cell["row"]]["id"]

    @app.callback(Output("src-sel", "data", allow_duplicate=True), Input("src-clear", "n_clicks"), prevent_initial_call=True)
    def _clear(n):
        return None if n else no_update

    @app.callback(Output("src-dl", "data"), Input("src-dl-csv", "n_clicks"), Input("src-dl-xlsx", "n_clicks"),
                  State("src-groups", "value"), State("src-q", "value"), State("src-tags", "value"), State("src-kinds", "value"),
                  State("src-opts", "value"), prevent_initial_call=True)
    def _dl(_, __, groups, q, tags, kinds, opts):
        if ctx.triggered_id == "src-dl-xlsx":
            return dcc.send_file(str(SOURCES_XLSX), filename="Ireland_agri_GHG_data_sources.xlsx")
        buf = io.StringIO()
        cols = ["id", "group", "parameter", "description", "unit", "years", "dataset", "provider", "download", "docs", "role", "tags"]
        w = csv.DictWriter(buf, fieldnames=cols, extrasaction="ignore")
        w.writeheader()
        for d in filtered(groups, q, tags, kinds, opts):
            w.writerow({**d, "download": d["download"] or d.get("download_note", ""), "tags": "; ".join(d["tags"])})
        return dcc.send_string(buf.getvalue(), "Ireland_agri_GHG_data_sources.csv")
