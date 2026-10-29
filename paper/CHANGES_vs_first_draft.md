# What changed relative to the first draft (28 October 2026 file)

The first draft reported the analysis run of 21 October 2026 with the earlier policy codebook. The submission manuscript
reports a full re-run of 29 October 2026 (13:01 UTC, seed 20261019) with the revised codebook. The re-run reproduces
`dashboard/data/results.json` bit-for-bit and passes all 30 independent verification checks. No figure, table or number
from the first draft was reused; the discrepancies are itemised in `verification_report.md`.

## Results that changed (revised policy parameters)

| | First draft | Manuscript |
|---|---|---|
| Codebook | 20 instruments, I × C × B | 19 instruments (5 P, 3 G, 11 M), I × *s* × *e* × B × *w*; strategies as a separate signal G |
| ARDL model | (1,0,2) | (1,0,0) |
| θ~P~ | 0.69, *p* = 0.032, +7.2% per 0.1 | 0.46, *p* = 0.043, +4.7% per 0.1 |
| θ~M~ | +0.47, *p* = 0.985 | +0.22, *p* = 0.88 |
| Bounds test | level relationship (*F* = 5.23) | no level relationship (*F* = 1.17); multipliers reported as indicative |
| Pressure effect on 2024 emissions | +11.2% (6.7–15.7%); +12.5 Mt cumulative | +2.2% (1.1–3.2%); −7.2 Mt cumulative (P fell after decoupling and only rebuilt above its 2000 level from 2017) |
| Robustness | 14 variants, 8 leave-one-out, θ~M~ never significantly negative | 17 variants (14 significant), 5 leave-one-out (4 significant), θ~M~ significantly negative in 2 |
| Mechanism link | ΔP not associated with the activity effect | ΔP → activity +748 kt per 0.1 (*p* = 0.008); dairy-herd +259 kt (*p* = 0.048) |
| Sub-indices | all positive | voluntary sub-index −0.59 (*p* = 0.03) |
| Power / MDE | size 0.15 / 0.32; MDE 0.40 | size 0.23 / 0.26; MDE 0.43 (M), 0.35 (P) |
| New results | – | equal-and-opposite test (*p* = 0.008); net-signal model θ~S~ = −0.20; construct validation of P (ΔP predicts dairy-herd growth, *p* = 0.035) |

Unchanged: CRF3 levels and composition, trend tests, structural breaks, LMDI decomposition (IO = 0.32), interrupted
time series, regional DiD, 2030 ceiling arithmetic, GWP\*.

## Framing

- The headline is no longer "pressure *raised* 2024 emissions by 11.2% and added 12.5 Mt". It is now that production pressure is *associated* with higher long-run emissions (+4.7% per 0.1) and acts through the activity (scale) channel, while the net effect of the small post-2000 change in P on 2024 emissions is +2.2%. Causal language has been replaced by associational language throughout, and the failed bounds test is stated.
- The abstract was cut to about 250 words and the Highlights were replaced by a *Key policy insights* box (Climate Policy format). The table of contents was removed.
- Section 1.3 (Related literature) was replaced by the five-part review supplied on 29 October (ex post evaluation and attribution; mechanisms and dynamics; agriculture as a distinct evaluation problem; expansion, intensity and coherence; Ireland), adapted to the revised instrument identifiers (growth strategies are G01–G03, not P04/P06/P07). The evidence table is Appendix F (73 sources).
- Section 1.1 and the research gap (1.4) now cite the hard-to-abate literature (Herrero et al., 2016; Leahy et al., 2020; EEA, 2025) and the limits of cross-country, sector-model and coherence studies.
- Section 2.8 states that the parameter values are the revised codebook of 29 October 2026 and names the alternative codings re-estimated in the robustness grid.
- The discussion links the findings to Läpple et al. (2022), Jongeneel and Gonzalez-Martinez (2022), the European Court of Auditors (2021), Pe'er et al. (2020), DeBoe et al. (2020), Henderson and Lankoski (2021), Hasler et al. (2022), Cullen et al. (2021), Finn and Ó hUallacháin (2012), Velthof et al. (2014), Ellerman and Wing (2003), Daugbjerg and Swinbank (2016), Abadie (2021) and OECD (2022).
- Henn et al. (2023), which could not be verified, was removed. "Bernal et al. (2017)" became Lopez Bernal et al. (2017). EPA (2026) was split into 2026a (provisional workbook, the data source) and 2026b (final report, the 37.9% share).
- The limitations no longer quote the superseded θ~P~ = 0.69; sensitivity to coding is now shown from the robustness grid (equal bindingness θ~P~ = 0.20; dropping the NAP turns θ~M~ significantly negative).

## Figures and tables

- All 18 figures regenerated from `results.json` at 300 dpi with the Okabe–Ito colour-blind-safe palette, Arial throughout, a "Year" label on every time axis, and legends moved clear of the axis labels. Figure 4 has three panels (P, G, M).
- Tables are regenerated from `results.json`; 31 tables (including six appendix tables) are numbered automatically by the build script.
- `tools/check_paper_numbers.py` confirms that 50 headline numbers in the text equal the values in `results.json`, that every figure and table is cited and exists, that no superseded first-draft value remains, and that every in-text citation has a reference entry (96 entries).

## References

- 53 references added from the literature review; 96 entries in total, APA 7th, alphabetical.
- Fields the review could not confirm are marked [AUTHOR INPUT REQUIRED] in the list: DOIs for Abadie et al. (2010), Gerber et al. (2011) and Sorrell (2009); volume/issue/pages for Candel & Biesbroek (2016), Dai et al. (2021), Daugbjerg & Swinbank (2016), Hertel et al. (2014) and Nabuurs et al. (2022).

## Supplementary material

- `supplementary_figures/Fig01…Fig18_*.png` (300 dpi) with a README.
- `supplementary_data/Fig01…_*.csv` (22 files: the data behind every figure) and `Tab01…Tab31/A1–F1_*.csv` (every manuscript table), with a README. Generated by `tools/export_supplementary.py`.

## Still open for the authors

21 highlighted [AUTHOR INPUT REQUIRED] items: co-authors and affiliations, corresponding e-mail and ORCID, funding,
conflicts, CRediT roles, acknowledgements, repository DOI, the word count, the unconfirmed reference fields above, and the
substantive data items: the INPACT export for M and an independent blind second coding of the revised P and G codebook
(the reported kappa is a placeholder). The user-supplied `policy_export/06–07` values for kappa (0.784) and
`share_years_both_rose` (0.294) differ from the program (0.459; 0.455); the program values are used.
