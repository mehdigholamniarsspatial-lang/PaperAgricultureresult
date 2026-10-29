# Verification report: first draft and literature review against the program outputs

Prepared 29 October 2026, before the manuscript was rewritten.

**Authoritative source.** `dashboard/data/results.json`, exported from a full re-run of
`project_policy_rev/ireland_agri_ghg_analysis.ipynb` (seed 20261019) with the revised policy codebook
(`policy_export/01_policy_codebook.csv`, revised 29 October 2026). The independent verification script
(`tools/verify_workflow.py`) passes all 30 checks on this run.

**Inputs checked.**

1. First draft: `Expansion_vs_Mitigation_Irish_Agri_GHG_paper 28 OCT 2028.docx` (states that its results come from the run of 21 October 2026, i.e. the *pre-revision* codebook).
2. Literature review: `Section 1.3 Related literature — Combine.docx` (29 October 2026).
3. Dashboard source code (`dashboard/`), `tools/export_results.py`, `paper/make_figures.py`, `paper/build_paper.py`.

## 1. Policy parameters: draft versus revised codebook

| Item | First draft (21 Oct run) | Program (29 Oct run, revised codebook) | Consequence |
|---|---|---|---|
| Instruments | 20 (P01–P08, M01–M12) | 19 (P01–P05, G01–G03, M01–M11) | Every codebook table, figure and instrument count in the draft is outdated |
| Scoring rule | x = I × C × B | x = I × s × e × B × w (coverage *s*, eligibility *e*, content weight *w*) | Equations 6–7, Section 3.4 and Table A1 rewritten |
| Growth strategies | Inside P (P04 Food Harvest 2020, P06 Food Wise 2025, P07 Food Vision 2030) | Separate strategy signal G (G01–G03), not part of P or S; a robustness variant adds G to P | P is lower and flatter after 2010; conceptual framing of P changed |
| Suckler programmes | M08 BDGP, M09 BEEP-S, M12 SCEP coded separately | One lineage M08 with time-varying eligibility | – |
| SBLAS | Absent | M11 Sustainable Beef and Lamb Assurance Scheme (2017–2024) | – |
| Eligibility | Fixed per instrument (e.g. derogation 0.30, TAMS 0.15) | Time-varying for P03, M05, M08; ranges and confidence grades recorded | – |
| Index values 2024 | P = 0.336; M = 0.638; S = 0.302 | P = 0.281; M = 0.693; S = 0.412 | All descriptive statistics of the indices changed |
| Second coder kappa | κ~w~ = 0.60 (75 policy-years) | κ~w~ = 0.46 (82 policy-years), linear weights | Still a placeholder; see §4 |

## 2. Numerical results: draft versus program

All of the following numbers in the first draft are superseded. None was reused.

| Quantity | First draft | Program (29 Oct) |
|---|---|---|
| Selected ARDL lags (AICc) | ARDL(1,0,2), AICc −135.5 | **ARDL(1,0,0)**, AICc −131.8 |
| θ~P~ (bootstrap *p*) | 0.69 (0.032); +7.2% per 0.1 | **0.46 (0.043); +4.7% per 0.1** |
| θ~M~ (bootstrap *p*) | +0.47 (0.985) | **+0.22 (0.880)** |
| Bounds test | *F* = 5.23, level relationship at 10% and 5% | ***F* = 1.17, no level relationship** (below the I(0) bound) |
| Effect of post-2000 change in P on 2024 emissions | +11.2% (6.7–15.7%) | **+2.2% (1.1–3.2%)** |
| Cumulative pressure effect 2000–2024 | +12.5 Mt CO₂e | **−7.2 Mt CO₂e** (P fell below its 2000 level after decoupling and rebuilt only from 2017) |
| Effect of post-2000 change in M on 2024 emissions | +29.1% (9.6–51.2%); 1 negative draw of 999 | **+14.4% (−3.8–39.1%); 109 negative draws of 999** |
| Robustness variants (estimable / θ~P~ > 0 / significant) | 14 / 14 / 13 | **17 / 17 / 14** |
| Leave-one-policy-out runs | 8, all significant; θ~P~ 0.49–1.12 | **5, four significant; θ~P~ 0.35–1.23** |
| θ~M~ significantly negative in any variant | Never | **Yes, in two** (drop NAP; score E01–E02 in M) |
| Empirical size of nominal 10% HAC test (M / P) | 0.15 / 0.32 | **0.23 / 0.26** |
| MDE at 80% power (M / P) | 0.40 / 0.40 | **0.43 / 0.35** |
| Sub-index θ (mandatory / incentive / voluntary) | +0.20 / +0.59 / +0.95 | **+0.25 / +0.58 / −0.59 (*p* = 0.03)** |
| Mechanism: ΔP → activity effect | −218 kt per 0.1 (*p* = 0.15) | **+748 kt per 0.1 (*p* = 0.008)** |
| Mechanism: ΔP → dairy-herd activity | −22 kt (*p* = 0.61) | **+259 kt (*p* = 0.048)** |
| Mechanism: ΔM → intensity | +62 kt (*p* = 0.18) | **+29 kt (*p* = 0.73)** |
| Equal-and-opposite test (Σβ + Σγ = 0) | not reported | *F* = 8.57, *p* = 0.008 |
| Net-signal model θ~S~ | not reported | −0.20 (*p* = 0.21) |
| Construct validation of P (ΔP → dairy-herd growth) | not reported | Σ coefficients 0.49, *p* = 0.035 |

Unchanged between runs (they do not depend on the policy coding): CRF3 levels; trend tests; Bai–Perron breaks (2000, 2012, 2020; UDmax *p* = 0.013); the LMDI decomposition (IO = 0.32; 0.21–0.33); the interrupted time-series estimates; the regional DiD; the 2030 ceiling arithmetic; GWP\*.

## 3. Claims in the first draft that the program no longer supports

1. "Production pressure *raised* 2024 emissions by 11.2% and added 12.5 Mt CO₂e" (abstract, highlights, §4.1, §4.6, §5.1, §6). The revised counterfactual gives +2.2% and a *negative* cumulative total, because P in 2024 is barely above its 2000 level. The headline must be restated in terms of the long-run multiplier (+4.7% per 0.1) and the mechanism result (ΔP tracks the activity effect), not the 2000-based counterfactual.
2. "Expansion left a measurable emissions footprint" is causal language; the bounds test now fails and the estimates are conditional associations. The manuscript uses "is associated with" throughout and reports the bounds test result explicitly.
3. "The positive pressure effect holds in all 14 variants and all eight leave-one-out runs" and "θ~M~ is never significantly negative" are obsolete (see §2).
4. "The bounds test indicates a level relationship" is reversed.
5. "The mechanism link does not confirm either half of the division of labour" is reversed for the pressure half: ΔP is now significantly associated with the activity and dairy-herd effects.
6. "MDE ≈ 0.40 for both indices" → 0.43 (M) and 0.35 (P).
7. Henn et al. (2023) is cited in §1.3.4 for herd-composition effects on implied emission factors, but no verifiable reference exists (the draft itself flags it). The citation has been removed; the point is made without attribution.
8. The draft's Section 1.3 cites 12 sources; the new literature review supplies 53 verified additions. Sources the review marks as unconfirmed in detail are listed in §5.

## 4. Discrepancies between the user's policy_export files and the program

| Quantity | `policy_export/06–07` (user) | Program | Status |
|---|---|---|---|
| Implementation κ~w~ | 0.784 | 0.459 (linear weights, continuous P02 codes snapped to the grid); 0.705 with quadratic weights | Unresolved. The program's value is reported; the kappa is a placeholder in any case |
| `share_years_both_rose` | 0.294 | 0.455 (10 of 22 years in which either index rose) | Unresolved; program value used (45%) |

All other index values in `07_policy_key_values.csv` (M, P, S, G in 2000 and 2024; largest P step; first positive S year; mandatory sub-index) agree with the program to 1 × 10⁻⁶.

## 5. Literature review: conflicts with the program and items the author must confirm

Conflicts resolved in favour of the program:

- The review labels Food Harvest 2020, Food Wise 2025 and Food Vision 2030 as P04, P06 and P07 ("production-pressure instruments"). In the revised codebook they are G01–G03, a separate strategy signal that is *not* part of P. The manuscript text and the evidence table use the new identifiers and wording.
- The review cites "EPA (2026)" for the *final* 1990–2024 inventory, while the program reads the *provisional* 1990–2025 workbook (the only source containing 2024). Both are now cited as EPA (2026a, provisional workbook, data source) and EPA (2026b, final report, 37.9% share).
- "Bernal et al. (2017)" is corrected to Lopez Bernal et al. (2017) throughout.
- The review's figure "Ireland's dairy herd grew by about 38% between 2010 and 2018" is consistent with the panel (1,071 → 1,481 thousand head, +38.3%).

Reference details the review flags as unconfirmed (carried into the manuscript as [AUTHOR INPUT REQUIRED] notes where they matter; no citation was invented):

- DOIs missing: Abadie et al. (2010); Gerber et al. (2011); Sorrell (2009).
- Volume/issue/pages missing: Candel & Biesbroek (2016); Dai et al. (2021); Daugbjerg & Swinbank (2016); Hertel et al. (2014); Nabuurs et al. (2022).
- Pages not independently retrievable by the reviewer: EEA (2026, Report 09/2026); Department of the Taoiseach (2022) press release.
- Figures quoted from the user's file and not visible in accessible abstracts: Läpple et al. (2022) (86% rise in farm emissions; 13% fall in intensity); Augustenborg et al. (2026) (34 interviews; five barriers).
- Callaway et al. (2024) is a working paper; Munafò & Davey Smith (2018) and Sorrell (2009) entries have no DOI.

## 6. Code-level checks

- `dashboard/data_store.py`, `pages/*.py` read every number from `results.json`; no hard-coded result values remain from the earlier run (checked by searching for the superseded values 0.69, 0.47, 11.2, 12.5, 5.23).
- `paper/make_figures.py` draws every figure from `results.json`; its spot checks (θ~P~ and θ~M~ 90% intervals; the 2024 pressure effect) agree with `key.offset` and `long_run`.
- `tools/export_results.py` exports G and `scoreG`; `key.meta.run_utc` and `seed` identify the run.
- The paper build (`paper/build_paper.py`) numbers figures and tables from the source order, so no manual numbering can drift.
