"""Final consistency check: every headline number quoted in the manuscript text must match results.json, and every
figure and table referenced in the text must exist (and vice versa).

Usage:  python tools/check_paper_numbers.py
Exit code 1 if any check fails.
"""
import json
import math
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = (ROOT / "paper" / "paper_src.md").read_text(encoding="utf-8")
D = json.loads((ROOT / "dashboard" / "data" / "results.json").read_text(encoding="utf-8"))
K = D["key"]
TXT = SRC.replace("−", "-")   # minus sign -> hyphen for matching

fails = []


def expect(label, value, fmt, pattern=None, count_min=1):
    """The formatted value must appear in the text (inside `pattern` with {v} placeholder, if given)."""
    v = fmt.format(value).replace("-", "-")
    pat = re.escape(v) if pattern is None else pattern.replace("{v}", re.escape(v))
    n = len(re.findall(pat, TXT))
    if n < count_min:
        fails.append(f"{label}: expected '{v}' ({n} found, pattern {pat!r})")
    return n


lr = {r["index"]: r for r in D["long_run"]}
o = K["offset"]; a = K["ardl"]; b = K["breaks"]; l = K["lmdi"]; rb = K["robustness"]; pw = K["power"]; c = K["ceiling_2030"]
mech = K["mechanism"]; sub = K["subindex"]; its = K["its"]; pol = K["policy"]

# ARDL long-run multipliers
expect("theta_P", lr["P"]["theta"], "{:.2f}", r"θ~P~ = \+?{v}")
expect("theta_M", lr["M"]["theta"], "{:.2f}", r"θ~M~ = \+?{v}")
expect("p_boot_P", a["p_boot_P"], "{:.3f}", r"θ~P~ = \+?0\.46, bootstrap \*p\* = {v}")
expect("p_boot_M", a["p_boot_M"], "{:.2f}", r"θ~M~ = \+0\.22, \*p\* = {v}")
expect("pct_per_0p1_P", a["pct_per_0p1_P"], "{:.1f}", r"{v}% higher long-run emissions")
expect("ARDL lags", f"({a['model']['p']},{a['model']['qM']},{a['model']['qP']})", "ARDL{}", count_min=3)
expect("bounds F", a["bounds_F"], "{:.2f}", r"\*F\* = {v}")
expect("p_equal_opposite", K["ardl"]["p_equal_opposite"], "{:.3f}", r"\*p\* = {v}")
expect("theta_S", a["theta_S"], "{:.2f}", r"θ~S~ = {v}")

# counterfactuals
expect("pressure effect 2024", o["pressure_effect_pct"], "{:.1f}", r"\+{v}%")
expect("pressure lo/hi", f"{o['pressure_lo']:.1f}–{o['pressure_hi']:.1f}", "{}")
expect("mitigation effect 2024", o["mitigation_effect_pct"], "{:.1f}", r"{v}% \*higher\*")
expect("cum P Mt", o["cum_P_kt"] / 1e3, "{:.1f}", r"{v} Mt CO₂e")
negdraws = sum(1 for d in D["boot_draws"] if d["dM"] < 0)
expect("negative mitigation draws", negdraws, "{} of 999")

# breaks and trend
expect("break years", ", ".join(map(str, b["break_years"])), "{}")
expect("UDmax and p", f"{b['UDmax']:.1f}, bootstrap *p* = {b['p_UDmax']:.3f}", "{}", r"UDmax = {v}")
expect("1990-2024 change", K["trend"]["change_pct_1990_2024"], "{:.2f}", r"{v}%")

# LMDI
expect("IO", l["P4_intensity_offset"], "{:.2f}", r"IO = {v}")
expect("P4 scale growth", l["P4_activity_plus_productivity"], "{:,.0f}", r"{v} kt")
expect("P4 intensity", -l["P4_intensity"], "{:,.0f}", r"{v} kt")
expect("dairy herd P4 Mt", l["P4_dairy_herd"] / 1e3, "{:.2f}", r"{v} Mt CO₂e")

# robustness
expect("variants estimable", rb["m_estimable"], "all {}")
expect("variants significant", rb["sig_P"], "{}", r"significant at the 10% level in \*\*{v}\*\*")
expect("LOO significant", rb["loo_sig_P"], "{}", r"Four of the five leave-one-policy-out runs" if rb["loo_sig_P"] == 4 else "{v} of the five")
expect("LOO range", f"{rb['loo_theta_P_range'][0]:.2f}", "{}", r"ranging from {v}")
expect("LOO range hi", f"{rb['loo_theta_P_range'][1]:.2f}", "{}", r"to {v}")
expect("sig M negative", rb["sig_M_negative"], "{}", r"significantly negative in \*\*two\*\*" if rb["sig_M_negative"] == 2 else "{v}")

# power
expect("MDE_M", pw["MDE_M"], "{:.2f}", r"\|θ\| ≈ {v} for M")
expect("MDE_P", pw["MDE_P"], "{:.2f}", r"{v} for P")
expect("size M", pw["size_nominal_M"], "{:.2f}", r"true size of {v} for M")
expect("size P", pw["size_nominal_P"], "{:.2f}", r"{v} for P")

# sub-indices, mechanism, ITS
expect("voluntary theta", sub["voluntary"]["theta"], "{:.2f}", r"θ = {v}, \*p\* = 0\.03")
expect("mandatory theta", sub["mandatory"]["theta"], "{:+.2f}", r"θ = {v}")
expect("mech activity", mech["activity effect (kt)|P"]["kt_per_0p1"], "{:+.0f}", r"\({v} kt per 0\.1")
expect("mech dairy", mech["dairy-herd activity effect (kt)|P"]["kt_per_0p1"], "{:+.0f}", r"\({v} kt per 0\.1")
expect("mech activity p", mech["activity effect (kt)|P"]["p"], "{:.3f}", r"\*p\* = {v}")
expect("ITS 2010 slope", its["CRF3 emissions|2010"]["slope_change_pct_per_yr"], "{:.1f}", r"steepened by {v} percentage points")
expect("validation P", K["validation_P_dairy"]["sum_coef"], "{:.2f}", r"coefficients {v}")
expect("validation p", K["validation_P_dairy"]["p_two_sided"], "{:.3f}", r"\*p\* = {v}")

# indices
expect("M_2024", pol["M_2024"], "{:.2f}", r"to {v} in 2024")
expect("P_2024", pol["P_2024"], "{:.2f}", r"to {v}")
expect("S_2024", pol["S_2024"], "{:.2f}", r"\+{v}")
expect("largest P step", pol["largest_P_step"], "{:+.3f}", r"\({v}\) occurred in " + str(pol["largest_P_step_year"]))
expect("both rose share", round(100 * pol["share_years_both_rose"]), "{}%", r"in {v} of the years")
expect("kappa impl", K["kappa"]["implementation"], "{:.2f}", r"κ~w~ = {v}")

# ceiling
expect("target 2030", c["target_2030"], "{:,.0f} kt CO₂e")
expect("LU trend", c["LU_change_needed_trend"], "{:.1f}%", r"\*\*-{v}\*\*".replace("-{v}", "{v}") if False else r"{v}")
expect("LU -1", -c["LU_change_needed_minus1"], "{:.1f}%")
expect("LU -3", -c["LU_change_needed_minus3"], "{:.1f}%")
expect("intensity trend", c["intensity_trend_pct"], "{:.2f}% a year")
expect("CRF3 2024", c["crf3_2024"], "{:,.0f} kt")
expect("gap 2024", -c["gap_pct_2024"], "{:.1f}% below")

# GWP*
expect("GWP* 2024", K["gwp_star"]["ch4_gwpstar_2024"] / 1e3, "{:.1f} Mt CO₂-we")

# DiD main spec
did = K["regional_did"]["log imputed livestock emissions|two-way FE"]
expect("DiD emissions", did["pct_per_10pp"], "{:.1f}% more per 10 pp")
expect("DiD placebo", did["placebo_pct"], "{:+.1f}%")

# ---- figure / table cross-references
figs = re.findall(r"^FIG (\w+) \|", SRC, re.M)
tabs = re.findall(r"^TAB (\w+)(?:=\w+)? \|", SRC, re.M)
refs_f = set(re.findall(r"\{\{fig:(\w+)\}\}", SRC)); refs_t = set(re.findall(r"\{\{tab:(\w+)\}\}", SRC))
for f in figs:
    if f not in refs_f:
        fails.append(f"figure '{f}' is never cited in the text")
for t in tabs + ["dictionary"]:
    if t not in refs_t:
        fails.append(f"table '{t}' is never cited in the text")
for r in refs_f - set(figs):
    fails.append(f"undefined figure reference {r}")
for r in refs_t - set(tabs) - {"dictionary"}:
    fails.append(f"undefined table reference {r}")
for f in figs:
    fn = re.search(rf"^FIG {f} \| .+? \| (\S+) \|", SRC, re.M).group(1)
    if not (ROOT / "paper" / "figures" / fn).exists():
        fails.append(f"figure file missing: {fn}")

# ---- superseded first-draft values must not appear
for bad in ["0.69, bootstrap", "11.2%", "12.5 Mt", "θ~M~ = +0.47", "ARDL(1,0,2)", "ARDL(1, 0, 2)", "F* = 5.23", "Henn et al."]:
    if bad in SRC:
        fails.append(f"superseded value present: {bad!r}")

# ---- every in-text citation has a reference entry
bib = SRC.split('::: {custom-style="Bibliography"}', 1)[1].split("\n:::", 1)[0]
entries = [e for e in bib.split("\n\n") if e.strip()]
body = SRC.split('::: {custom-style="Bibliography"}', 1)[0]
cites = set()
for m in re.finditer(r"\(([^()]*?\d{4}[a-z]?[^()]*?)\)", body):
    for part in m.group(1).split(";"):
        mm = re.search(r"([A-Z][^,]*?)(?:,| et al\.,?| &)?\s*(\d{4}[a-z]?)$", part.strip())
        if mm:
            cites.add((mm.group(1).split(" et al")[0].split(" &")[0].strip(), mm.group(2)))
for m in re.finditer(r"([A-Z][A-Za-zÁ-ÿ'’-]+(?: et al\.| and [A-Z][A-Za-zÁ-ÿ'’-]+)?) \((\d{4}[a-z]?)\)", body):
    cites.add((m.group(1).split(" et al")[0].split(" and ")[0], m.group(2)))
SKIP = {"Act", "Table", "Figure", "Section", "Equation", "Equations", "AR5", "GWP100", "IPCC", "CSO", "UNFCCC", "RQ3", "P",
        "BDGP", "BEEP-S", "SCEP", "Food", "March", "October", "S.I.", "Scheme", "Programme", "REPS", "GLAS", "AEOS", "ACRES",
        "BDGP 2015–2022", "BEEP-S 2019–2022", "Food Harvest", "Food Harvest 2020 and Food Wise", "S.I. 113/", "S.I. 378/", "SCEP from"}
ALIAS = {"CCAC": "Climate Change Advisory Council", "DAFF": "Department of Agriculture, Fisheries and Food",
         "DAFM": "Department of Agriculture, Food and the Marine", "EEA": "European Environment Agency",
         "EPA": "Environmental Protection Agency", "OECD": "Organisation for Economic Co-operation and Development",
         "Eurostat": "Eurostat"}
for name, year in sorted(cites):
    surname = name.split(",")[0].strip()
    if surname in SKIP or len(surname) < 3 or re.search(r"\d", surname):
        continue
    key = ALIAS.get(surname, surname)
    yr = re.compile(r"\(" + re.escape(year) + r"[,)]")
    if not any((e.startswith(key) or e.startswith(surname)) and yr.search(e[:len(key) + 60]) for e in entries):
        if not any(key.split()[-1] in e[:120] and yr.search(e) for e in entries):
            fails.append(f"citation without reference entry: {name} ({year})")

print(f"{len(entries)} reference entries, {len(figs)} figures, {len(tabs)} tables checked")
if fails:
    print("FAILED checks:")
    for f in fails:
        print(" -", f)
    sys.exit(1)
print("all number, cross-reference and citation checks pass")
