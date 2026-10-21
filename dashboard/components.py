"""Small layout helpers shared by all pages."""
from dash import html, dcc, dash_table
from .theme import GRAPH_CONFIG


def page_header(step, title, lead):
    return html.Header(className="page-header", children=[
        html.Div(step, className="eyebrow"),
        html.H1(title),
        html.P(lead, className="lead"),
    ])


def section(title, *children, sub=None, id=None):
    kids = [html.H2(title)]
    if sub:
        kids.append(html.P(sub, className="section-sub"))
    kids.extend(children)
    return html.Section(className="section", children=kids, **({"id": id} if id else {}))


def card(*children, cls=""):
    return html.Div(className=f"card {cls}".strip(), children=list(children))


def kpi(value, label, note=None, tone=""):
    kids = [html.Div(value, className="kpi-value"), html.Div(label, className="kpi-label")]
    if note:
        kids.append(html.Div(note, className="kpi-note"))
    return html.Div(className=f"kpi {tone}".strip(), children=kids)


def kpi_row(*kpis):
    return html.Div(className="kpi-row", children=list(kpis))


def callout(kind, title, body):
    """kind: finding | plain | read | caution | maths"""
    icons = {"finding": "◆", "plain": "💬", "read": "👁", "caution": "!", "maths": "∑"}
    return html.Div(className=f"callout callout-{kind}", children=[
        html.Div(className="callout-title", children=[html.Span(icons.get(kind, "•"), className="callout-icon"), title]),
        html.Div(body if isinstance(body, list) else [body], className="callout-body"),
    ])


def md(text, math=False, cls="md"):
    return dcc.Markdown(text, mathjax=math, className=cls, dangerously_allow_html=False)


def maths(tex_block, caption=None):
    """Display-math block. tex_block is LaTeX without $$."""
    kids = [dcc.Markdown(f"$$\n{tex_block}\n$$", mathjax=True, className="math-block")]
    if caption:
        kids.append(html.Div(caption, className="math-caption"))
    return html.Div(className="math-wrap", children=kids)


def graph(fig, id=None, height=None):
    kw = dict(figure=fig, config=GRAPH_CONFIG, className="graph")
    if id:
        kw["id"] = id
    return dcc.Graph(**kw)


def table(rows, columns, id=None, page_size=12, filter=False, sort=True, height=None, style_cond=None):
    """rows: list of dicts; columns: list of (id, name[, type/format])"""
    cols = []
    for c in columns:
        d = {"id": c[0], "name": c[1]}
        if len(c) > 2 and c[2]:
            d.update(c[2])
        cols.append(d)
    kw = dict(
        data=rows, columns=cols, page_size=page_size, sort_action="native" if sort else "none",
        filter_action="native" if filter else "none",
        style_table={"overflowX": "auto"},
        style_cell={"fontFamily": 'system-ui, -apple-system, "Segoe UI", sans-serif', "fontSize": "13px", "padding": "8px 10px",
                    "textAlign": "left", "whiteSpace": "normal", "height": "auto", "border": "none",
                    "borderBottom": "1px solid #ecebe6", "color": "#1f1f1d", "maxWidth": "420px"},
        style_header={"backgroundColor": "#f3f2ee", "fontWeight": "600", "color": "#34332f", "borderBottom": "1px solid #d6d5ce"},
        style_cell_conditional=[{"if": {"column_id": c}, "minWidth": "200px"} for c in
                                ("name", "variable", "check", "variant", "description", "input", "note", "role", "o", "test", "w", "term")],
        style_data_conditional=(style_cond or []) + [{"if": {"row_index": "odd"}, "backgroundColor": "#fbfbf9"}],
        style_filter={"backgroundColor": "#fff"},
        css=[{"selector": ".dash-spreadsheet td div", "rule": "line-height: 1.35;"}],
    )
    if id:
        kw["id"] = id
    return dash_table.DataTable(**kw)


def num(nd):
    return {"type": "numeric", "format": {"specifier": f",.{nd}f"}}


def badge(text, tone="neutral"):
    return html.Span(text, className=f"badge badge-{tone}")


def steps_list(items):
    return html.Ol(className="steps", children=[html.Li(i) for i in items])


def two_col(left, right, ratio="1-1"):
    return html.Div(className=f"grid-2 r{ratio}", children=[html.Div(left), html.Div(right)])


def details(summary, *children, open=False):
    return html.Details(open=open, className="details", children=[html.Summary(summary), *children])
