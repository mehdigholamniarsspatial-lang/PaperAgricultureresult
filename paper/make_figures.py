"""Regenerate the dashboard figures as static, print-quality PNGs from results.json."""
import json, sys, math
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

SRC = Path(sys.argv[1])
OUT = Path(sys.argv[2]); OUT.mkdir(parents=True, exist_ok=True)
D = json.loads(SRC.read_text(encoding="utf-8"))
K = D["key"]; Y = D["panel"]["years"]; C = D["panel"]["cols"]

# Okabe–Ito colour-blind-safe palette (Okabe & Ito, 2008). YELLOW is mapped to sky blue because pure yellow is
# illegible for thin lines on white; RED (vermilion) is reserved for targets and data breaks.
BLUE, ORANGE, AQUA, YELLOW, MAGENTA, GREEN, VIOLET, RED = (
    "#0072B2", "#E69F00", "#009E73", "#56B4E9", "#CC79A7", "#009E73", "#CC79A7", "#D55E00")
INK, INK2, MUTED, GRID = "#0b0b0b", "#52514e", "#898781", "#e1e0d9"
EVENTS = {2005: "Decoupling", 2007: "Derogation", 2010: "Food Harvest 2020", 2015: "Quota abolition", 2022: "Sectoral ceiling"}

plt.rcParams.update({
    "font.family": "Arial", "font.size": 9, "axes.edgecolor": "#c3c2b7", "axes.labelcolor": INK2,
    "xtick.color": INK2, "ytick.color": INK2, "axes.spines.top": False, "axes.spines.right": False,
    "axes.grid": True, "grid.color": GRID, "grid.linewidth": 0.6, "axes.axisbelow": True,
    "legend.frameon": False, "legend.fontsize": 8, "savefig.dpi": 300, "savefig.bbox": "tight",
})
W = 6.3


def ser(col):
    p = [(y, v) for y, v in zip(Y, C[col]) if v is not None]
    return [a for a, _ in p], [b for _, b in p]


def events(ax, label=True, at=None, color=MUTED, which=EVENTS):
    for yr, lab in which.items():
        ax.axvline(yr, color=MUTED, ls=":", lw=0.9, zorder=0)
        if label:
            y0 = ax.get_ylim()[0] if at is None else at
            ax.text(yr + 0.25, y0, lab, rotation=90, va="bottom", ha="left", fontsize=6.5, color=color)


def save(fig, name):
    # Every bottom-row axis whose x-axis is calendar time gets an explicit "Year" label.
    for ax in fig.axes:
        if not ax.axison or ax.get_xlabel():
            continue
        lo, hi = ax.get_xlim()
        ss = ax.get_subplotspec()
        if 1985 < lo < hi < 2040 and (ss is None or ss.is_last_row()):
            ax.set_xlabel("Year")
    fig.savefig(OUT / f"{name}.png", facecolor="white")
    plt.close(fig)


# ---------------------------------------------------------------- dataset figures
def fig_emissions():
    fig, ax = plt.subplots(figsize=(W, 3.3))
    cats = [("enteric_kt", "Enteric fermentation (3.A)", BLUE), ("soils_kt", "Agricultural soils (3.D)", ORANGE),
            ("manure_kt", "Manure management (3.B)", AQUA), ("liming_kt", "Liming (3.G)", YELLOW), ("urea_kt", "Urea (3.H)", VIOLET)]
    ys = Y
    stack = [[(v or 0) / 1e3 for v in C[c]] for c, _, _ in cats]
    ax.stackplot(ys, *stack, labels=[l for _, l, _ in cats], colors=[c for _, _, c in cats], alpha=0.85, lw=0)
    y, e = ser("crf3_kt")
    ax.plot(y, [v / 1e3 for v in e], color=INK, lw=1.6, marker="o", ms=2.5, label="CRF3 total")
    e24, tgt = K["ceiling_2030"]["crf3_2024"] / 1e3, K["ceiling_2030"]["target_2030"] / 1e3
    ax.plot([2024, 2030], [e24, tgt], color=RED, ls="--", lw=1.4, marker="o", ms=3.5, label="Path to 2030 ceiling (15.5 Mt)")
    ax.set_ylim(0, 23.5); ax.set_xlim(1989.5, 2031)
    ax.set_ylabel("Mt CO$_2$e (AR5 GWP100)")
    events(ax, at=0.4, color="white")
    ax.legend(ncol=3, loc="upper center", bbox_to_anchor=(0.5, -0.22))
    save(fig, "fig_emissions")


def fig_drivers():
    fig, axs = plt.subplots(2, 3, figsize=(W, 3.9), sharex=True)
    spec = [("crf3_kt", "CRF3 emissions", "kt CO$_2$e", INK), ("dairy_cows", "Dairy cows", "thousand head", BLUE),
            ("other_cattle", "Non-dairy cattle", "thousand head", ORANGE), ("sheep_total", "Sheep", "thousand head", AQUA),
            ("milk_per_cow_l", "Milk yield", "litres per cow", VIOLET), ("n_fert_kt", "Mineral N fertiliser", "kt N", YELLOW)]
    for ax, (col, t, u, c) in zip(axs.flat, spec):
        y, v = ser(col)
        ax.plot(y, v, color=c, lw=1.5)
        ax.set_title(t, fontsize=8.5, color=INK, loc="left")
        ax.set_ylabel(u, fontsize=7.5)
        ax.tick_params(labelsize=7)
        if col == "dairy_cows":
            ax.axvline(2004.5, color=RED, ls="--", lw=0.8)
            ax.text(2005.5, 1560, "2005 classification\nbreak", fontsize=6, color=RED)
        for yr in (2010, 2015):
            ax.axvline(yr, color=MUTED, ls=":", lw=0.8, zorder=0)
    fig.tight_layout(h_pad=1.0, w_pad=0.8)
    save(fig, "fig_drivers")


REGIONS = ["West", "Midland", "Border + Dublin/Mid-East", "Mid-West + South-East", "South-West"]
REGION_COL = {"West": BLUE, "Midland": ORANGE, "South-West": AQUA, "Border + Dublin/Mid-East": YELLOW, "Mid-West + South-East": VIOLET}


def fig_regional():
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(W, 2.8), gridspec_kw={"width_ratios": [1, 1.5]})
    ex = K["regional_exposure_pct"]
    regs = sorted(REGIONS, key=lambda r: ex[r])
    a1.barh(regs, [ex[r] for r in regs], color=[REGION_COL[r] for r in regs])
    for i, r in enumerate(regs):
        a1.text(ex[r] + 1, i, f"{ex[r]:.1f}", va="center", fontsize=7.5)
    a1.set_xlim(0, 85); a1.set_xlabel("dairy share of all cows, 2010–2014 (%)")
    a1.grid(axis="y", visible=False); a1.tick_params(axis="y", labelsize=7.5)
    a1.set_title("(a) Exposure to quota abolition", loc="left", fontsize=8.5, color=INK)
    for r in REGIONS:
        rows = sorted([x for x in D["regional"] if x["unit"] == r], key=lambda x: x["Year"])
        base = next(x["dairy_cows"] for x in rows if x["Year"] == 2014)
        a2.plot([x["Year"] for x in rows], [100 * x["dairy_cows"] / base for x in rows], color=REGION_COL[r], lw=1.4, label=r)
    a2.axhline(100, color=MUTED, lw=0.6)
    a2.axvline(2015, color=MUTED, ls=":", lw=0.9); a2.axvline(2004.5, color=RED, ls="--", lw=0.7)
    a2.set_ylabel("dairy cows, 2014 = 100")
    a2.set_title("(b) Regional dairy herd", loc="left", fontsize=8.5, color=INK)
    a2.legend(fontsize=6.5, loc="upper left")
    fig.tight_layout(w_pad=1.5)
    save(fig, "fig_regional")


SHORT = {"P01": "Coupled livestock premia", "P02": "Milk quota increases", "P03": "Nitrates derogation", "P04": "Milk quota abolition",
         "P05": "TAMS II Dairy Equipment", "G01": "Food Harvest 2020", "G02": "Food Wise 2025", "G03": "Food Vision 2030 (w = 0.5)",
         "M01": "REPS", "M02": "Nitrates Action Programme", "M03": "Farm Waste Management Scheme", "M04": "AEOS",
         "M05": "Carbon Navigator / advisory", "M06": "Sustainable Dairy Assurance", "M07": "GLAS", "M08": "Suckler programmes (BDGP/BEEP-S/SCEP)",
         "M09": "Chemical N maxima (5th NAP)", "M10": "ACRES", "M11": "Sustainable Beef & Lamb Assurance"}


def fig_scores():
    fig, axs = plt.subplots(3, 1, figsize=(W, 5.4), gridspec_kw={"height_ratios": [5, 3, 11]})
    names = {r["policy_id"]: r["name"] for r in D["codebook"]}
    for ax, key, title, cmap in [(axs[0], "scoreP", "(a) Production-pressure instruments (P)", "Oranges"),
                                 (axs[1], "scoreG", "(b) Strategy signal (G; not part of P)", "Greens"),
                                 (axs[2], "scoreM", "(c) Mitigation instruments (M)", "Blues")]:
        sc = D[key]; ids = list(sc["cols"].keys()); yrs = sc["years"]
        mat = np.array([[v or 0 for v in sc["cols"][i]] for i in ids])
        im = ax.imshow(mat, aspect="auto", cmap=cmap,
                       extent=[yrs[0] - 0.5, yrs[-1] + 0.5, len(ids) - 0.5, -0.5], vmin=0)
        short = [f"{i} {SHORT.get(i, names[i].split('(')[0].strip())}" for i in ids]
        ax.set_yticks(range(len(ids))); ax.set_yticklabels(short, fontsize=6.5)
        ax.grid(False); ax.set_title(title, loc="left", fontsize=8.5, color=INK)
        ax.tick_params(axis="x", labelsize=7)
        cb = fig.colorbar(im, ax=ax, pad=0.01, fraction=0.03); cb.ax.tick_params(labelsize=6.5); cb.set_label("score x", fontsize=7)
    fig.tight_layout(h_pad=1.2)
    save(fig, "fig_scores")


# ---------------------------------------------------------------- methods figure
def fig_framework():
    fig, ax = plt.subplots(figsize=(W, 2.2)); ax.axis("off"); ax.set_xlim(0, 10); ax.set_ylim(0, 3.2)

    def box(x, y, w, h, txt, fc, ec):
        ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.04,rounding_size=0.12", fc=fc, ec=ec, lw=1.2))
        ax.text(x + w / 2, y + h / 2, txt, ha="center", va="center", fontsize=7.5, color=INK)
    box(0.1, 2.0, 2.6, 0.95, "Production pressure P\n(derogation, quota increases\nand abolition, TAMS II)", "#fde3d8", ORANGE)
    box(0.1, 0.2, 2.6, 0.95, "Mitigation M\n(nitrates rules, agri-env.\nschemes, genetics, advice)", "#dbe8f8", BLUE)
    box(4.2, 2.0, 2.4, 0.95, "Activity\n(herd size, N use,\nmilk volume)", "#f4f3ef", INK2)
    box(4.2, 0.2, 2.4, 0.95, "Intensity\n(emissions per litre,\nper head, per kg N)", "#f4f3ef", INK2)
    box(7.5, 1.1, 2.5, 0.95, "CRF3 emissions\nE = Activity × Intensity", "#d6f1e6", AQUA)
    kw = dict(arrowstyle="-|>", lw=1.3, mutation_scale=12)
    ax.annotate("", (4.2, 2.47), (3.08, 2.47), arrowprops=dict(color=ORANGE, **kw)); ax.text(3.64, 2.58, "raises (+)", ha="center", fontsize=7.5, color=ORANGE)
    ax.annotate("", (4.2, 0.67), (3.08, 0.67), arrowprops=dict(color=BLUE, **kw)); ax.text(3.64, 0.78, "lowers (−)", ha="center", fontsize=7.5, color=BLUE)
    ax.annotate("", (7.5, 1.75), (6.6, 2.47), arrowprops=dict(color=INK2, **kw))
    ax.annotate("", (7.5, 1.4), (6.6, 0.67), arrowprops=dict(color=INK2, **kw))
    ax.text(7.1, 1.57, "×", fontsize=12, ha="center", va="center", color=INK)
    save(fig, "fig_framework")


# ---------------------------------------------------------------- results figures
def fig_indices():
    fig, ax = plt.subplots(figsize=(W, 2.9))
    for col, lab, c, ls in [("M", "Mitigation index M", BLUE, "-"), ("P", "Production-pressure index P", ORANGE, "-"), ("S", "Net signal S = M − P", AQUA, "--"),
                            ("G", "Strategy signal G", INK2, ":")]:
        y, v = ser(col); ax.plot(y, v, color=c, lw=1.8, ls=ls, label=lab)
    ax.axhline(0, color=MUTED, lw=0.7)
    ax.set_ylabel("index value"); ax.set_ylim(-0.48, 0.8)
    events(ax, at=-0.46)
    ax.legend(ncol=4, loc="upper center", bbox_to_anchor=(0.5, -0.22))
    save(fig, "fig_indices")


def fig_breaks():
    fig, ax = plt.subplots(figsize=(W, 2.9))
    y, e = ser("crf3_kt")
    ax.plot(y, [v / 1e3 for v in e], color=INK, lw=1.2, marker="o", ms=3, label="CRF3 emissions (observed)")
    b = K["breaks"]; edges = [1990] + b["break_years"] + [2025]; fit = D["fit_m"]
    for j in range(len(edges) - 1):
        idx = [i for i, yy in enumerate(Y) if edges[j] <= yy < edges[j + 1]]
        ax.plot([Y[i] for i in idx], [fit[i] / 1e3 for i in idx], color=ORANGE, lw=2.4, label="Bai–Perron segmented trend" if j == 0 else None)
        mid = Y[idx[len(idx) // 2]]
        ax.text(mid, max(fit[i] for i in idx) / 1e3 + 0.35, f"{b['segment_slopes_pct'][j]:+.2f}%/yr".replace("-", "−"), ha="center", fontsize=7.5, color=ORANGE)
    for (lo, hi), by in zip(b["ci90"], b["break_years"]):
        ax.axvspan(lo - 0.5, hi + 0.5, color=ORANGE, alpha=0.12, lw=0)
        ax.axvline(by, color=ORANGE, ls="--", lw=0.9)
    for yr in (2010, 2015):
        ax.axvline(yr, color=MUTED, ls=":", lw=0.9)
        ax.text(yr + 0.25, 22.3, EVENTS[yr], rotation=90, fontsize=6.5, color=MUTED, va="top")
    ax.set_ylim(17.2, 22.4); ax.set_ylabel("Mt CO$_2$e")
    ax.legend(loc="lower left", fontsize=7.5)
    save(fig, "fig_breaks")


FCOL = {"activity": BLUE, "productivity": ORANGE, "intensity": AQUA, "other": YELLOW}
FLAB = {"activity": "Activity (herd, N use)", "productivity": "Productivity (milk yield)",
        "intensity": "Intensity (emissions per unit)", "other": "Other categories"}


def fig_lmdi_phase():
    rows = D["lmdi_phase"]
    fig, ax = plt.subplots(figsize=(W, 3.0))
    labs = [f"{r['phase'].split(' ', 1)[0]}\n{r['years'].replace('-', '–')}" for r in rows]
    x = np.arange(len(rows)); w = 0.19
    for k, f in enumerate(FCOL):
        ax.bar(x + (k - 1.5) * w, [r[f] for r in rows], w, color=FCOL[f], label=FLAB[f])
    ax.scatter(x, [r["net_change"] for r in rows], marker="D", s=26, color=INK, zorder=3, label="Net change")
    for xi, r in zip(x, rows):
        ax.text(xi + 0.07, r["net_change"], f"{r['net_change']:+,.0f}".replace("-", "−"), ha="left", va="center", fontsize=7, fontweight="bold")
    ax.axhline(0, color=INK2, lw=0.7)
    ax.set_xticks(x); ax.set_xticklabels(labs, fontsize=7.5)
    ax.set_ylabel("kt CO$_2$e, cumulative within phase"); ax.set_xlabel("Policy phase")
    ax.legend(ncol=3, loc="upper center", bbox_to_anchor=(0.5, -0.22), fontsize=7.5)
    save(fig, "fig_lmdi_phase")


def fig_lmdi_annual():
    by = {}
    for r in D["lmdi_annual"]:
        by.setdefault(r["year"], {}).setdefault(r["factor"], 0)
        by[r["year"]][r["factor"]] += r["effect"]
    yrs = sorted(by)
    fig, ax = plt.subplots(figsize=(W, 2.9))
    pos = np.zeros(len(yrs)); neg = np.zeros(len(yrs))
    for f in FCOL:
        v = np.array([by[y].get(f, 0) for y in yrs])
        ax.bar(yrs, np.where(v > 0, v, 0), 0.75, bottom=pos, color=FCOL[f], label=FLAB[f])
        ax.bar(yrs, np.where(v < 0, v, 0), 0.75, bottom=neg, color=FCOL[f])
        pos += np.where(v > 0, v, 0); neg += np.where(v < 0, v, 0)
    ax.scatter(yrs, [sum(by[y].values()) for y in yrs], color=INK, s=10, zorder=3, label="Annual change in CRF3")
    for b in (2004.5, 2009.5, 2014.5, 2021.5):
        ax.axvline(b, color=MUTED, ls=":", lw=0.9)
    for xm, lab in [(1998, "P1"), (2007, "P2"), (2012, "P3"), (2018, "P4"), (2022.5, "P5")]:
        ax.text(xm, ax.get_ylim()[1] * 0.95, lab, ha="center", fontsize=7.5, color=MUTED)
    ax.axhline(0, color=INK2, lw=0.7)
    ax.set_ylabel("kt CO$_2$e, year on year")
    ax.legend(ncol=3, loc="upper center", bbox_to_anchor=(0.5, -0.22), fontsize=7.5)
    save(fig, "fig_lmdi_annual")


def q(xs, p):
    return float(np.quantile([x for x in xs if x is not None], p))


def fig_ardl():
    bd = D["boot_draws"]; lr = {r["index"]: r for r in D["long_run"]}
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(W, 2.7), gridspec_kw={"width_ratios": [1.1, 1]})
    for i, (ix, lab, c) in enumerate([("P", "θ$_P$ (pressure)", ORANGE), ("M", "θ$_M$ (mitigation)", BLUE)]):
        th = [d[f"theta_{ix}"] for d in bd]
        lo, hi = q(th, 0.05), q(th, 0.95)
        a1.plot([lo, hi], [i, i], color=c, lw=3, alpha=0.5)
        a1.plot(lr[ix]["theta"], i, "o", color=c, ms=7)
        a1.text(lr[ix]["theta"], i + 0.22, f"{lr[ix]['theta']:.2f} [{lo:.2f}, {hi:.2f}]", ha="center", fontsize=7.5)
    a1.axvline(0, color=INK2, lw=0.8)
    a1.set_yticks([0, 1]); a1.set_yticklabels(["θ$_P$ (pressure)", "θ$_M$ (mitigation)"])
    a1.set_ylim(-0.6, 1.6); a1.set_xlabel("long-run effect θ (log points per index unit)")
    a1.set_title("(a) Estimates with 90% bootstrap intervals", loc="left", fontsize=8.5, color=INK)
    a2.scatter([d["theta_M"] for d in bd], [d["theta_P"] for d in bd], s=4, color=VIOLET, alpha=0.3, lw=0)
    a2.scatter([K["ardl"]["theta_M"]], [K["ardl"]["theta_P"]], s=40, color=INK, marker="D", zorder=3, label="estimate")
    a2.axhline(0, color=INK2, lw=0.7); a2.axvline(0, color=INK2, lw=0.7)
    a2.set_xlabel("θ$_M$ (mitigation)"); a2.set_ylabel("θ$_P$ (pressure)")
    a2.set_title("(b) 999 unrestricted bootstrap draws", loc="left", fontsize=8.5, color=INK)
    a2.legend(loc="lower right")
    fig.tight_layout(w_pad=1.5)
    save(fig, "fig_ardl")


def fig_cf():
    rows = D["paths"]; yrs = [r["Year"] for r in rows]
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(W, 2.8), gridspec_kw={"width_ratios": [1.5, 1]})
    a1.plot(yrs, [r["observed_kt"] / 1e3 for r in rows], color=INK, lw=2, label="Observed")
    a1.plot(yrs, [r["no_pressure_change_kt"] / 1e3 for r in rows], color=ORANGE, lw=1.8, ls="--", label="P frozen at 2000 level")
    a1.plot(yrs, [r["no_mitigation_change_kt"] / 1e3 for r in rows], color=BLUE, lw=1.8, ls="--", label="M frozen at 2000 level")
    a1.fill_between(yrs, [r["no_pressure_change_kt"] / 1e3 for r in rows], [r["observed_kt"] / 1e3 for r in rows], color=ORANGE, alpha=0.12, lw=0)
    a1.set_ylabel("Mt CO$_2$e"); a1.legend(fontsize=6.5, ncol=3, loc="upper center", bbox_to_anchor=(0.5, -0.25))
    a1.set_title("(a) Observed and counterfactual paths", loc="left", fontsize=8.5, color=INK)
    eff = [100 * (math.exp(d["dP"]) - 1) for d in D["boot_draws"]]
    a2.hist(eff, bins=35, color=ORANGE, alpha=0.8)
    o = K["offset"]
    for v, ls in [(o["pressure_effect_pct"], "-"), (o["pressure_lo"], ":"), (o["pressure_hi"], ":")]:
        a2.axvline(v, color=INK, ls=ls, lw=1)
    a2.set_xlabel("effect of P change since 2000\non 2024 emissions (%)"); a2.set_ylabel("bootstrap draws")
    a2.set_title("(b) Bootstrap distribution", loc="left", fontsize=8.5, color=INK)
    fig.tight_layout(w_pad=1.5)
    save(fig, "fig_cf")


ROB_LAB = {
    "baseline": "Baseline", "no deterministic trend": "No deterministic trend", "fixed lags ARDL(1,1,1)": "Fixed lags ARDL(1,1,1)",
}


def fig_robust():
    rows = [r for r in D["robust"] if r["estimable"]]
    labs = []
    for r in rows:
        v = r["variant"]
        if v.startswith("leave out"):
            v = "Leave out " + v.split(":")[0].replace("leave out ", "")
        labs.append(v[:1].upper() + v[1:])
    fig, axs = plt.subplots(1, 2, figsize=(W, 4.8), sharey=True)
    yy = np.arange(len(rows))[::-1]
    for ax, par, c in [(axs[0], "P", ORANGE), (axs[1], "M", BLUE)]:
        for yv, r in zip(yy, rows):
            p = r[f"p_boot_{par}"]
            filled = p is not None and p < 0.10
            ax.plot(r[f"theta_{par}"], yv, "o", ms=5, mec=c, mfc=c if filled else "white", mew=1.2)
        ax.axvline(rows[0][f"theta_{par}"], color=c, ls=":", lw=0.9)
        ax.axvline(0, color=INK2, lw=0.8)
        ax.set_xlabel(f"θ$_{par}$"); ax.grid(axis="y", visible=False)
        ax.set_title(f"({'a' if par == 'P' else 'b'}) θ$_{par}$ ({'pressure' if par == 'P' else 'mitigation'})", loc="left", fontsize=8.5, color=INK)
    axs[0].set_yticks(yy); axs[0].set_yticklabels(labs, fontsize=6.5)
    fig.tight_layout(w_pad=1.0)
    save(fig, "fig_robust")


def fig_power():
    fig, ax = plt.subplots(figsize=(W * 0.62, 2.6))
    for ix, c in [("M", BLUE), ("P", ORANGE)]:
        rr = sorted([r for r in D["power"] if r["index"] == ix], key=lambda r: r["theta_abs"])
        ax.plot([r["theta_abs"] for r in rr], [r["power_size_adjusted"] for r in rr], color=c, lw=1.8, marker="o", ms=3.5, label=f"θ$_{ix}$")
    ax.axhline(0.8, color=MUTED, ls="--", lw=0.8); ax.text(1.5, 0.82, "80% power", fontsize=7, ha="right", color=MUTED)
    ax.axvline(K["power"]["MDE_P"], color=ORANGE, ls=":", lw=0.8)
    ax.axvline(K["power"]["MDE_M"], color=BLUE, ls=":", lw=0.8)
    ax.set_xlabel("true |θ| (log points per index unit)"); ax.set_ylabel("size-adjusted power"); ax.set_ylim(0, 1.05)
    ax.legend(loc="lower right")
    save(fig, "fig_power")


def fig_its():
    fig, ax = plt.subplots(figsize=(W * 0.75, 2.6))
    outs = [("CRF3 emissions", BLUE), ("Dairy cows", ORANGE)]
    evs = [2010, 2015, 2022]; x = np.arange(3); w = 0.36
    for k, (o, c) in enumerate(outs):
        rr = {r["event"]: r for r in D["its"] if r["outcome"] == o}
        vals = [rr[e]["slope_change_pct_per_yr"] for e in evs]
        bars = ax.bar(x + (k - 0.5) * w, vals, w, color=c, label=o)
        for xi, e, v in zip(x, evs, vals):
            p = rr[e]["p_slope"]
            ax.text(xi + (k - 0.5) * w, v + (0.25 if v >= 0 else -0.6), "p<0.001" if p < 0.001 else f"p={p:.2f}", ha="center", fontsize=6.5)
    ax.axhline(0, color=INK2, lw=0.7)
    ax.set_xticks(x); ax.set_xticklabels(["2010\nFood Harvest 2020", "2015\nQuota abolition", "2022†\nSectoral ceiling"], fontsize=7.5)
    ax.set_ylabel("change in trend (pp per year)"); ax.legend(loc="lower left")
    save(fig, "fig_its")


def fig_event():
    fig, ax = plt.subplots(figsize=(W, 2.8))
    for o, c, lab in [("log imputed livestock emissions", BLUE, "Imputed livestock emissions"), ("log livestock units", AQUA, "Livestock units"), ("log dairy cows", ORANGE, "Dairy cows")]:
        rr = sorted([r for r in D["event"] if r["outcome"] == o], key=lambda r: r["year"])
        yrs = [r["year"] for r in rr]; b = [100 * r["beta"] for r in rr]; se = [100 * r["se"] for r in rr]
        if o.startswith("log imputed"):
            ax.fill_between(yrs, [x - 1.645 * s for x, s in zip(b, se)], [x + 1.645 * s for x, s in zip(b, se)], color=c, alpha=0.15, lw=0, label="90% band (emissions; indicative)")
        ax.plot(yrs, b, color=c, lw=1.6, marker="o", ms=3, label=lab)
    ax.axhline(0, color=INK2, lw=0.7); ax.axvline(2014.5, color=MUTED, ls=":", lw=0.9)
    ax.text(2014.7, ax.get_ylim()[1] * 0.9, "quota abolition", fontsize=7, color=MUTED)
    ax.set_ylabel("% per +10 pp exposure (2014 = 0)")
    ax.set_xticks(range(2005, 2025, 2))
    ax.legend(fontsize=7, loc="upper left")
    save(fig, "fig_event")


def fig_mech():
    rows = D["mech"]
    outs = ["activity effect (kt)", "dairy-herd activity effect (kt)", "intensity effect (kt)"]
    fig, ax = plt.subplots(figsize=(W * 0.8, 2.7))
    x = np.arange(3); w = 0.36
    for k, (pol, c) in enumerate([("P", ORANGE), ("M", BLUE)]):
        rr = {r["outcome"]: r for r in rows if r["policy"] == pol}
        vals = [rr[o]["kt_per_0p1"] for o in outs]; err = [1.645 * 0.1 * rr[o]["se"] for o in outs]
        ax.bar(x + (k - 0.5) * w, vals, w, yerr=err, color=c, capsize=3, error_kw=dict(lw=0.8, ecolor=INK2), label=f"Δ{pol} (per +0.1)")
    ax.axhline(0, color=INK2, lw=0.7)
    ax.set_xticks(x); ax.set_xticklabels(["Activity", "Dairy-herd activity", "Intensity"])
    ax.set_ylabel("kt CO$_2$e per +0.1 (±90% CI)"); ax.legend(loc="lower right")
    save(fig, "fig_mech")


def fig_ceiling():
    rows = D["ceiling"]
    fig, ax = plt.subplots(figsize=(W * 0.75, 2.6))
    labs = ["Trend continues\n(+0.37%/yr)", "−1%/yr", "−2%/yr", "−3%/yr"]
    vals = [r["required_LU_change_vs_2024_pct"] for r in rows]
    ax.bar(labs, vals, color=[RED, ORANGE, YELLOW, AQUA], width=0.6)
    for i, v in enumerate(vals):
        ax.text(i, v - 1.2, f"{v:.1f}%".replace("-", "−"), ha="center", fontsize=8)
    ax.axhline(0, color=INK2, lw=0.7); ax.set_ylim(-26, 1)
    ax.set_ylabel("required change in LU, 2024–2030 (%)")
    ax.set_xlabel("assumed annual change in emissions per livestock unit")
    ax.tick_params(axis="x", labelsize=7.5); ax.grid(axis="x", visible=False)
    save(fig, "fig_ceiling")


def fig_gwp():
    rows = D["gwpstar"]; yrs = [r["Year"] for r in rows]
    fig, ax = plt.subplots(figsize=(W, 2.6))
    ax.plot(yrs, [r["ch4_gwp100_kt"] / 1e3 for r in rows], color=BLUE, lw=1.8, label="CH$_4$ in GWP100 (Mt CO$_2$e)")
    ax.plot(yrs, [r["ch4_gwpstar_kt"] / 1e3 for r in rows], color=ORANGE, lw=1.8, label="CH$_4$ in GWP* (Mt CO$_2$-we)")
    ax.axhline(0, color=INK2, lw=0.7)
    ax.set_ylabel("Mt CO$_2$e / CO$_2$-we"); ax.legend(loc="center left", fontsize=7.5)
    save(fig, "fig_gwp")


for f in [fig_emissions, fig_drivers, fig_regional, fig_scores, fig_framework, fig_indices, fig_breaks, fig_lmdi_phase,
          fig_lmdi_annual, fig_ardl, fig_cf, fig_robust, fig_power, fig_its, fig_event, fig_mech, fig_ceiling, fig_gwp]:
    f(); print("ok", f.__name__)

# Spot checks against values quoted in the manuscript
bd = D["boot_draws"]
print("theta_P 90%:", q([d['theta_P'] for d in bd], .05), q([d['theta_P'] for d in bd], .95))
print("theta_M 90%:", q([d['theta_M'] for d in bd], .05), q([d['theta_M'] for d in bd], .95))
print("pressure effect check:", K["offset"]["pressure_effect_pct"], np.median([100*(math.exp(d['dP'])-1) for d in bd]))
