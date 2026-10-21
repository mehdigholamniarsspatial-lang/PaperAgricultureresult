"""Loads the exported analysis results and holds the variable catalogue.

All numbers come from `data/results.json`, written by `tools/export_results.py` after a
full re-run of `ireland_agri_ghg_analysis.ipynb` (seed 20261019). Nothing is recomputed
here except light arithmetic for the interactive calculators.
"""
import json
import math
from pathlib import Path

HERE = Path(__file__).parent
DATA = json.loads((HERE / "data" / "results.json").read_text())
PANEL_CSV = HERE / "data" / "ireland_agri_panel_1990_2024.csv"

YEARS = DATA["panel"]["years"]
COLS = DATA["panel"]["cols"]
KEY = DATA["key"]


def series(col):
    """Return (years, values) for a panel column, dropping missing years."""
    vals = COLS[col]
    pairs = [(y, v) for y, v in zip(YEARS, vals) if v is not None]
    return [p[0] for p in pairs], [p[1] for p in pairs]


def value(col, year):
    return COLS[col][YEARS.index(year)]


def fmt(x, nd=1, pct=False, sign=False):
    if x is None or (isinstance(x, float) and math.isnan(x)):
        return "–"
    s = f"{x:+,.{nd}f}" if sign else f"{x:,.{nd}f}"
    s = s.replace("-", "−")
    return s + ("%" if pct else "")


def pfmt(p):
    if p is None:
        return "–"
    if p < 0.001:
        return "< 0.001"
    return f"{p:.3f}"


# --------------------------------------------------------------------------------------
# Variable catalogue (data dictionary shown on the Dataset page)
# group, label, unit, source, role, status, description
# --------------------------------------------------------------------------------------
VARIABLES = {
    "crf3_kt": ("Emissions", "CRF3 agricultural emissions (outcome)", "kt CO₂e",
                "EPA provisional GHG inventory 1990–2025", "Outcome", "Real",
                "IPCC sector 3 total = EPA 'Agriculture' − agricultural fuel (1.A.4.c.ii) − fishing (1.A.4.c.iii). AR5 GWP100."),
    "enteric_kt": ("Emissions", "Enteric fermentation (3.A)", "kt CO₂e", "EPA inventory", "Category", "Real",
                   "Methane from digestion in ruminants (cattle, sheep)."),
    "manure_kt": ("Emissions", "Manure management (3.B)", "kt CO₂e", "EPA inventory", "Category", "Real",
                  "CH₄ and N₂O from stored slurry and manure."),
    "soils_kt": ("Emissions", "Agricultural soils (3.D)", "kt CO₂e", "EPA inventory", "Category", "Real",
                 "N₂O from fertiliser, manure and urine deposited on soils."),
    "liming_kt": ("Emissions", "Liming (3.G)", "kt CO₂e", "EPA inventory", "Category", "Real", "CO₂ from lime applied to soils."),
    "urea_kt": ("Emissions", "Urea application (3.H)", "kt CO₂e", "EPA inventory", "Category", "Real", "CO₂ from urea fertiliser."),
    "crf3_ch4_kt": ("Emissions", "CRF3 methane (CH₄)", "kt CO₂e", "EPA inventory (gas sheet)", "Gas", "Real", "CH₄ × 28."),
    "crf3_n2o_kt": ("Emissions", "CRF3 nitrous oxide (N₂O)", "kt CO₂e", "EPA inventory (gas sheet)", "Gas", "Real", "N₂O × 265."),
    "crf3_co2_kt": ("Emissions", "CRF3 carbon dioxide (CO₂)", "kt CO₂e", "EPA inventory (gas sheet)", "Gas", "Real", "Liming and urea CO₂."),
    "dairy_kt": ("Emissions", "Dairy cattle CH₄ (enteric + manure)", "kt CO₂e", "Ireland CRT 2025, Table 3 (3.A.1.a, 3.B.1.a)", "LMDI component", "Real (to 2023)",
                 "Dairy split from the inventory's own tables; 2024 not yet published, so not imputed."),
    "other_cattle_kt": ("Emissions", "Non-dairy cattle CH₄ (enteric + manure)", "kt CO₂e", "Ireland CRT 2025, Table 3 (3.A.1.b, 3.B.1.b)", "LMDI component", "Real (to 2023)",
                        "Beef and suckler herd methane."),
    "sheep_kt": ("Emissions", "Sheep enteric CH₄", "kt CO₂e", "Eurostat env_air_gge (CRF 3.A.2)", "LMDI component", "Real", "Sheep methane × 28."),
    "dairy_cows": ("Livestock", "Dairy cows (June)", "thousand head", "CSO AAA01 / AAA07 / AAA09", "Activity", "Real",
                   "June livestock survey. Classification break at 2004→05 (−8.7%) handled by a dummy."),
    "other_cattle": ("Livestock", "Non-dairy cattle (June)", "thousand head", "CSO AAA01 / AAA07 / AAA09", "Activity", "Real", "Total cattle − dairy cows."),
    "cattle_total": ("Livestock", "Total cattle (June)", "thousand head", "CSO", "Activity", "Real", "All bovine animals."),
    "sheep_total": ("Livestock", "Total sheep (June)", "thousand head", "CSO", "Activity", "Real", "All sheep."),
    "livestock_units": ("Livestock", "Livestock units (LU)", "thousand LU", "CSO + Eurostat LSU coefficients", "Activity; 2030 scenario", "Real",
                        "1.0 × dairy cows + Eurostat LSU on non-dairy cattle categories (0.4–1.0) + 0.1 × sheep."),
    "lsu_coef_other_cattle": ("Livestock", "LU per non-dairy animal", "LU per head", "Derived", "Diagnostic", "Real",
                              "Falls from 0.673 to 0.638 as the herd gets younger."),
    "milk_mlitres": ("Milk", "Milk intake by processors", "million litres", "CSO AKA01", "Productivity", "Real", "Domestic intake; starts 1992."),
    "milk_per_cow_l": ("Milk", "Milk yield per cow", "litres per cow", "Derived (AKA01 ÷ dairy cows)", "LMDI productivity factor", "Real",
                       "Milk intake × 1,000 ÷ dairy cows (thousand)."),
    "milk_fat_pct": ("Milk", "Milk fat content", "%", "CSO AKA01", "Context", "Real", "Average fat content."),
    "milk_protein_pct": ("Milk", "Milk protein content", "%", "CSO AKA01", "Context", "Real", "Average protein content."),
    "n_fert_kt": ("Nitrogen", "Mineral N fertiliser use", "kt N", "CRT 2025 Table 3.D (1990–99); Eurostat aei_fm_usefert (2000–24)", "LMDI soils activity", "Real",
                  "CRT values are in kg N (despite the header) and divided by 1,000."),
    "n_manure_kt": ("Nitrogen", "Manure N excreted", "kt N", "CRT 2025 Table 3.B(b) rates × CSO head counts", "LMDI soils activity", "Real (to 2023)",
                    "Σ N-excretion rate × head count for dairy, non-dairy cattle and sheep."),
    "nex_dairy_kg": ("Nitrogen", "N excretion per dairy cow", "kg N/head/yr", "CRT 2025 Table 3.B(b)", "Input to manure N", "Real (to 2023)", "97.9 (1991) → 108.4 (2023)."),
    "nex_other_cattle_kg": ("Nitrogen", "N excretion per non-dairy animal", "kg N/head/yr", "CRT 2025 Table 3.B(b)", "Input to manure N", "Real (to 2023)", "54.8 → 48.1."),
    "nex_sheep_kg": ("Nitrogen", "N excretion per sheep", "kg N/head/yr", "CRT 2025 Table 3.B(b)", "Input to manure N", "Real (to 2023)", "About 7.5."),
    "milk_price_real": ("Prices & economy", "Real milk price index", "index, 2020 = 100", "CSO AHA01–05 (chain-linked) ÷ CPI", "ARDL control", "Real",
                        "Five base-year vintages linked by geometric-mean overlap, deflated by CPI."),
    "fertiliser_price_real": ("Prices & economy", "Real fertiliser price index", "index, 2020 = 100", "CSO AHA01–05 ÷ CPI", "ARDL control", "Real", "Input price control."),
    "feed_price_real": ("Prices & economy", "Real feed price index", "index, 2020 = 100", "CSO AHA01–05 ÷ CPI", "Robustness", "Real", "Used in the milk-to-feed ratio."),
    "milk_feed_ratio": ("Prices & economy", "Milk-to-feed price ratio", "ratio", "Derived", "Robustness control", "Real", "Alternative profitability control."),
    "cpi": ("Prices & economy", "Consumer price index", "index, 2020 = 100", "CSO CPA01", "Deflator", "Real", "All items, rebased to 2020."),
    "gni_star_meur": ("Prices & economy", "Modified GNI (GNI*)", "€ million, constant prices", "CSO NA002", "Robustness control", "Real", "Macro-economic control in one variant."),
    "M": ("Policy indices", "Mitigation index M", "index", "Author coding (INPACT scoring rule)", "Policy", "Provisional",
          "Σ over 12 mitigation instruments of I × C × B. Replace with INPACT export."),
    "P": ("Policy indices", "Production-pressure index P", "index", "Authors' codebook", "Policy", "Real coding (coder 1)",
          "Σ over 8 expansion instruments of I × C × B."),
    "S": ("Policy indices", "Net policy signal S = M − P", "index", "Derived", "Policy", "Derived", "Positive when mitigation outweighs pressure."),
    "M_mandatory": ("Policy indices", "M sub-index: mandatory", "index", "Derived", "Sub-index", "Provisional", "Nitrates Action Programme, chemical-N limits."),
    "M_incentive": ("Policy indices", "M sub-index: incentive", "index", "Derived", "Sub-index", "Provisional", "REPS, GLAS, BDGP, BEEP-S, ACRES, SCEP…"),
    "M_voluntary": ("Policy indices", "M sub-index: voluntary", "index", "Derived", "Sub-index", "Provisional", "Carbon Navigator, SDAS."),
}

GROUPS = ["Emissions", "Livestock", "Milk", "Nitrogen", "Prices & economy", "Policy indices"]


def coverage(col):
    ys, _ = series(col)
    return (ys[0], ys[-1], len(ys)) if ys else (None, None, 0)


EVENTS = {2005: "Decoupling", 2007: "Derogation", 2010: "Food Harvest 2020", 2015: "Quota abolition", 2022: "Sectoral ceiling"}

PHASES = [("P1", "Coupled support", 1992, 2004), ("P2", "Decoupling & derogation", 2004, 2009),
          ("P3", "Food Harvest & quota increases", 2009, 2014), ("P4", "Post-quota expansion", 2014, 2021),
          ("P5", "Sectoral ceiling", 2021, 2023)]

POLICY_NAMES = {r["policy_id"]: r["name"] for r in DATA["codebook"]}
CODEBOOK = {r["policy_id"]: r for r in DATA["codebook"]}

COVERAGE_LABEL = {"dairy": "dairy CH₄", "beef_sheep": "non-dairy cattle + sheep CH₄", "cattle_sheep": "all cattle + sheep CH₄",
                  "n_soils_manure": "soils + manure management", "manure": "manure management",
                  "fertiliser": "direct N₂O from mineral N + urea CO₂", "all": "all of CRF3"}

# Verification checks documented in DATA_DOCUMENTATION.md, section 3
VERIFICATION = [
    ("1 Load", "SHA-256 of every loaded file matches the provenance sheet", "53 files re-hashed; no mismatch"),
    ("1 Load", "Only documented simulated inputs are loaded", "only pressure_codebook_coder2_SIMULATED"),
    ("1 Load", "Duplicate monthly downloads are byte-identical", "AHM05, AJM01, AJM08, AJM09, AJM10"),
    ("2 Livestock", "CSO tables cover disjoint years", "1991–2004 / 2005–2014 / 2015–2026"),
    ("2 Livestock", "Panel dairy cows equal CSO State totals", "max difference 0"),
    ("2 Livestock", "Five constant-boundary units sum to the State", "dairy 0.014%, cattle 0.004%, sheep 0.003%"),
    ("2 Livestock", "1990 livestock left missing", "NaN (never imputed)"),
    ("2 Livestock", "Livestock units = 1.0·dairy + Eurostat LSU + 0.1·sheep", "LSU per non-dairy head 0.632–0.682"),
    ("3 Prices", "Chain-link overlaps fit", "max deviation 2.88% across 20 links"),
    ("3 Prices", "Linked indices and CPI equal 100 in 2020", "exact"),
    ("3 Prices", "Real price = nominal / CPI × 100", "exact"),
    ("4 Emissions", "CRF3 = Agriculture − 1.A.4.c.ii − 1.A.4.c.iii", "19,760.0 (1990); 19,631.2 (2024) kt CO₂e"),
    ("4 Emissions", "CRF3 = sum of 5 categories (≤ 0.0001%)", "gap 0"),
    ("4 Emissions", "CRF3 = CO₂ + CH₄ + N₂O (≤ 0.0001%)", "gap 2 × 10⁻¹⁴ %"),
    ("5 CRT", "34 workbooks, 1990–2023, no gaps", "complete"),
    ("5 CRT", "Panel split equals CRT Table3 rows", "1990–2023"),
    ("5 CRT", "2024 split left missing", "NaN (never imputed)"),
    ("5 CRT", "CRT cattle CH₄ vs Eurostat", "1990–2020 ≤ 0.004%; 2021–23 ≤ 0.21%"),
    ("5 CRT", "Table3.D unit is kg N", "kg / 1,000 = Eurostat t N exactly, 2000–05"),
    ("5 CRT", "Panel mineral N 1990–1999 = CRT", "379,311 t (1990); 442,916 t (1999)"),
    ("5 CRT", "Manure N = CRT rates × CSO head counts; 2024 missing", "2023: 108.4 / 48.1 / 7.52 kg N/head"),
    ("6 Panel", "35 unique years, 1990–2024", "pass"),
    ("6 Panel", "No weather variable", "pass"),
    ("7 Indices", "M and P recomputed independently (I × C × B)", "P₂₀₂₄ 0.3362; M₂₀₂₄ 0.6383"),
    ("8 LMDI", "Annual effects sum exactly to ΔCRF3", "residual 1.9 × 10⁻¹¹ kt"),
    ("9 ARDL", "θ_M, θ_P reproduced by an independent OLS", "θ_M 0.4651, θ_P 0.6946, n = 28"),
    ("9 ARDL", "key_results.json = results.xlsx", "pass"),
    ("10 Ceiling", "2030 target = 0.75 × CRF3₂₀₁₈", "15,546.2 kt CO₂e"),
    ("11 Outputs", "34 sheets; 7 figures in PNG and PDF", "pass"),
    ("11 Outputs", "Simulated inputs listed honestly in the JSON", "coder-2 scores (kappa only)"),
]
