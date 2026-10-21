"""Chart colours and a shared Plotly layout so every figure reads as one system."""
import plotly.graph_objects as go

# Validated categorical order (light surface). Colour follows the entity, never its rank.
BLUE, ORANGE, AQUA, YELLOW, MAGENTA, GREEN, VIOLET, RED = (
    "#2a78d6", "#eb6834", "#1baf7a", "#eda100", "#e87ba4", "#008300", "#6250d6", "#e34948")
PAL = [BLUE, ORANGE, AQUA, YELLOW, MAGENTA, GREEN, VIOLET, RED]

INK, INK2, MUTED = "#0b0b0b", "#52514e", "#898781"
GRID, AXIS, SURFACE = "#e1e0d9", "#c3c2b7", "#fcfcfb"

# Fixed entity colours used across every page
C_M, C_P, C_S = BLUE, ORANGE, AQUA            # mitigation, pressure, net signal
C_OBS = INK
FACTOR_COL = {"activity": BLUE, "productivity": ORANGE, "intensity": AQUA, "other": YELLOW}
FACTOR_LAB = {"activity": "Activity (herd, N use)", "productivity": "Productivity (milk yield)",
              "intensity": "Intensity (emissions per unit)", "other": "Other categories"}
COMP_LAB = {"dairy": "Dairy cattle CH₄", "other_cattle": "Other cattle CH₄", "sheep": "Sheep CH₄",
            "soils_fert": "Soils N₂O: mineral N", "soils_manureN": "Soils N₂O: manure N", "other": "Other categories"}
REGION_COL = {"West": BLUE, "Midland": ORANGE, "South-West": AQUA, "Border + Dublin/Mid-East": YELLOW,
              "Mid-West + South-East": VIOLET}

FONT = 'system-ui, -apple-system, "Segoe UI", Roboto, sans-serif'


def base_layout(fig, height=420, title=None, ytitle=None, xtitle=None, legend=True, hover="x unified"):
    fig.update_layout(
        height=height, margin=dict(l=60, r=24, t=56 if title else 24, b=48),
        paper_bgcolor=SURFACE, plot_bgcolor=SURFACE,
        font=dict(family=FONT, size=13, color=INK2),
        title=dict(text=title, x=0, xanchor="left", font=dict(size=15, color=INK)) if title else None,
        hovermode=hover, hoverlabel=dict(bgcolor="white", bordercolor=AXIS, font=dict(family=FONT, color=INK, size=12)),
        legend=dict(orientation="h", yanchor="bottom", y=1.0, x=0, xanchor="left", font=dict(size=12),
                    bgcolor="rgba(0,0,0,0)") if legend else None,
        showlegend=legend,
    )
    fig.update_xaxes(showgrid=False, linecolor=AXIS, ticks="outside", tickcolor=AXIS, title=xtitle, zeroline=False)
    fig.update_yaxes(gridcolor=GRID, linecolor=AXIS, zeroline=False, title=ytitle)
    return fig


def add_events(fig, events, y_text=1.0, show_labels=True, row=None, col=None):
    for y, lab in events.items():
        fig.add_vline(x=y, line=dict(color=MUTED, width=1, dash="dot"))
        if show_labels:
            fig.add_annotation(x=y, y=y_text, yref="paper", text=lab, showarrow=False, textangle=-90,
                               xanchor="left", yanchor="top", xshift=3, font=dict(size=10, color=INK2))
    return fig


def empty_fig(msg="Select at least one item", height=360):
    fig = go.Figure()
    fig.add_annotation(text=msg, x=0.5, y=0.5, xref="paper", yref="paper", showarrow=False, font=dict(size=14, color=MUTED))
    base_layout(fig, height=height, legend=False)
    fig.update_xaxes(visible=False); fig.update_yaxes(visible=False)
    return fig


GRAPH_CONFIG = {"displaylogo": False, "responsive": True,
                "modeBarButtonsToRemove": ["lasso2d", "select2d", "autoScale2d"],
                "toImageButtonOptions": {"format": "png", "scale": 3}}
