Revised policy score tables — aligned with Appendix B (final revision, 29 October 2026)
=====================================================================================

All seven tables were regenerated from the component values in the final appendix
(Tables B.13–B.18) and reproduce its Table B.9 to three decimals.

Changes relative to the previous version of these files
-------------------------------------------------------
1. Instrument identifiers follow the appendix: P01–P05 (production pressure), G01–G03
   (strategy signal, formerly P04/P06/P07), M01–M11 (mitigation), E01–E02 (event markers).
   Old P05 -> P04 (quota abolition); old P08 -> P05 (TAMS II); old M08 + M09 + M12
   (BDGP, BEEP-S, SCEP) are merged into M08 "suckler genetics and data programmes";
   old M10 -> M09 (chemical N maxima); old M11 -> M10 (ACRES); new M11 = Sustainable Beef
   and Lamb Assurance Scheme (2017–2024).
2. Strategies form a separate index G (Equation B.3) and are no longer summed into P.
   G03 carries content weight w = 0.50 (new column content_weight).
3. Eligibility is time-varying for P03, M05 and M08 and is encoded with the same
   "year-range:value" syntax as implementation; the annual values are also written out in
   02_policy_implementation_I_by_year.csv (columns P03_e, M05_e, M08_e).
4. Component values updated to the appendix (e.g. P03 e 0.35–0.60 instead of 0.30; P05 e 0.45
   instead of 0.15; M01 e 0.35; M03 e 0.47; M04 e 0.07; M05 e 0.05–0.10; M06 e 0.95; M07 e 0.28;
   M10 e 0.23; P02 period 2000–2014 with the continuous z path incl. the corrected 2001–2005
   value 0.278; M02 I = 0.75 in 2007–2008; M03, M06, M11 ramps; P04 I = 0.75 in 2015).
5. New columns in 01_policy_codebook.csv: eligibility_range, bindingness_range,
   content_weight, confidence_s_e_B_I, appendix_refs (reference numbers of Appendix B.12).
   climate_relevance is no longer a column: the 0.50 weight on M02 is a robustness variant only.
6. 03_policy_scores_by_year.csv gives the annual contribution x = I × s × e × B (× w for G).
   04_policy_indices_M_P_S_by_year.csv adds the G column; M_mandatory = M02 + M09,
   M_incentive = M01, M03, M04, M07, M08, M10; M_voluntary = M05, M06, M11.
7. 05_policy_coder2_codebook.csv: coder-2 values are unchanged and only remapped to the new
   IDs (they remain simulated/PROVISIONAL). 06_policy_kappa.csv is recomputed (quadratic-weighted
   kappa on the 0/0.25/0.5/0.75/1 grid over coder-1 policy-years, n = 82; continuous P02 values
   snapped to the grid).
8. 07_policy_key_values.csv recomputed; adds G_2000, G_2024, first_year_S_positive and
   M_mandatory_2024. Note that largest_P_step is now 2016 (quota abolition + TAMS at full scale)
   because strategies no longer enter P.

Coverage shares retain the six-decimal inventory values from the previous file where the
reference year is unchanged. M11 uses the appendix value 0.460 (Low confidence); linear
interpolation between the 2014 (0.481786) and 2019 (0.438777) beef_sheep shares in the previous
file would give 0.4646.
