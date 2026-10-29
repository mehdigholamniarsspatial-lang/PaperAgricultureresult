"""Export analysis outputs (from the re-run notebook) into JSON files read by the dashboard."""
import pickle, json, math
import numpy as np, pandas as pd
from pathlib import Path
S = pickle.load(open("outputs/state.pkl", "rb"))
OUT = Path(__file__).resolve().parent.parent / "dashboard" / "data"   # run from the notebook project folder (needs outputs/state.pkl)

def clean(o):
    if isinstance(o, dict): return {str(k): clean(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)): return [clean(v) for v in o]
    if isinstance(o, np.ndarray): return [clean(v) for v in o.tolist()]
    if isinstance(o, (np.bool_,)): return bool(o)
    if isinstance(o, (np.integer,)): return int(o)
    if isinstance(o, (np.floating, float)):
        return None if (math.isnan(o) or math.isinf(o)) else round(float(o), 6)
    if isinstance(o, pd.Timestamp): return str(o)
    return o

def recs(df, index=False):
    d = df.reset_index() if index else df
    return clean(d.to_dict("records"))

R = S["RESULTS"]; panel = S["panel"]
keep = ['agri_total_kt','enteric_kt','manure_kt','soils_kt','liming_kt','urea_kt','fuel_agri_kt','fuel_fishing_kt','crf3_kt',
        'crf3_ch4_kt','crf3_n2o_kt','crf3_co2_kt','ch4_enteric_cattle_kt','ch4_enteric_sheep_kt','ch4_manure_cattle_kt',
        'ch4_enteric_dairy_kt','ch4_enteric_other_cattle_kt','ch4_manure_dairy_kt','ch4_manure_other_cattle_kt',
        'dairy_cows','other_cows','cattle_total','sheep_total','pigs_total','other_cattle','other_cattle_lsu','lsu_coef_other_cattle',
        'livestock_units','milk_mlitres','milk_fat_pct','milk_protein_pct','milk_per_cow_l','milk_price_real','milk_price_nominal',
        'fertiliser_price_real','fertiliser_price_nominal','feed_price_real','output_all_price_real','input_all_price_real',
        'milk_feed_ratio','cpi','gni_star_meur','fertiliser_n_use_t','n_fert_kt','n_manure_kt','nex_dairy_kg','nex_other_cattle_kg',
        'nex_sheep_kg','dairy_kt','other_cattle_kt','sheep_kt','M','P','S','G','M_mandatory','M_incentive','M_voluntary']
pan = panel[keep].copy(); pan.index.name = "Year"
data = {}
data["panel"] = {"years": [int(y) for y in pan.index], "cols": {c: clean(pan[c].values) for c in keep}}
data["regional"] = recs(S["R"][["unit","Year","dairy_cows","other_cows","cattle_total","sheep_total","other_cattle","livestock_units","emis_imputed_kt","exposure_pp"]])
data["key"] = clean(S["KEY"])
data["scoreM"] = {"years": [int(y) for y in S["scoreM"].index], "cols": {c: clean(S["scoreM"][c].values) for c in S["scoreM"]}}
data["scoreP"] = {"years": [int(y) for y in S["scoreP"].index], "cols": {c: clean(S["scoreP"][c].values) for c in S["scoreP"]}}
data["scoreG"] = {"years": [int(y) for y in S["scoreG"].index], "cols": {c: clean(S["scoreG"][c].values) for c in S["scoreG"]}}
data["codebook"] = recs(R["02_codebooks_with_coverage"].fillna(""))
data["kappa"] = recs(S["kap"])
data["trend"] = recs(S["trend_tab"])
data["bp"] = recs(R["11_breaks_bai_perron"].assign(break_years=lambda x: x["break_years"].astype(str)))
data["chow"] = recs(R["12_known_date_chow"])
data["fit_m"] = clean(np.exp(S["fit_m"]))
data["ud_boot"] = clean(S["ud_boot"])
data["lmdi_phase"] = recs(S["lmdi_phase"])
data["lmdi_annual"] = recs(S["ch"])
data["lmdi_comp"] = recs(R["21_lmdi_by_component"].astype({"phase": str}))
data["lmdi_sens"] = recs(S["sens"])
data["unit_roots"] = recs(R["30_unit_roots"])
data["lag_grid"] = recs(S["grid"])
coef = R["32_ardl_coefficients"]; data["ardl_coef"] = recs(coef, index=True)
X = S["X"]; fitted = X.values @ coef["coef"].reindex(X.columns).values
data["ardl_fit"] = {"years": [int(y) for y in X.index], "fitted": clean(np.exp(fitted)), "observed": clean(panel.loc[X.index, "crf3_kt"].values)}
data["diag"] = recs(S["diag"]); data["bounds"] = recs(S["bt"]); data["long_run"] = recs(S["lr_tab"])
data["net_signal"] = recs(R["41_net_signal_model"])
data["boot_draws"] = recs(S["bd"][["theta_M","theta_P","dM","dP"]])
data["nullM"] = clean(S["nullM"]); data["nullP"] = clean(S["nullP"])
data["offset"] = recs(S["off"]); data["paths"] = recs(S["paths"], index=True)
data["power"] = recs(S["pw"]); data["robust"] = recs(S["rob"].drop(columns=["note"], errors="ignore"))
data["subindex"] = recs(S["sub"]); data["its"] = recs(S["its_tab"])
data["did"] = recs(S["did"]); data["event"] = recs(S["ev"]); data["exposure"] = recs(R["64_regional_exposure"])
data["mech"] = recs(S["mech_tab"]); data["validation"] = recs(R["06_P_validation_dairy"], index=True)
data["ceiling"] = recs(S["sc"]); data["gwpstar"] = recs(S["gs"], index=True)
man = S["manifest"].drop(columns=["sha256"]); man["sha256_short"] = S["manifest"]["sha256"].str[:12]
data["manifest"] = recs(man)
for k, v in data.items():
    pass
json.dump(data, open(OUT / "results.json", "w"), separators=(",", ":"))
pan.to_csv(OUT / "ireland_agri_panel_1990_2024.csv")
print((OUT / "results.json").stat().st_size / 1e3, "kB")
