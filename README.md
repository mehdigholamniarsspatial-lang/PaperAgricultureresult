# Expansion versus mitigation — research dashboard

An interactive Python (Plotly Dash) platform presenting the study
*Expansion versus mitigation: production-oriented policy and agricultural emissions in Ireland, 1990–2024*.

| Step | Page | What it contains |
|---|---|---|
| 1 | The problem | The puzzle, competing explanations, literature gap, contribution |
| 2 | Research questions | RQ1–RQ4 with hypotheses and decision rules, conceptual framework, interactive policy timeline |
| 3 | Dataset | Sources, coverage map, searchable data dictionary, series explorer, emissions composition, regional panel, policy-codebook calculator, data table + CSV download, verification and provenance |
| 4 | Implementation & methods | Pipeline, then 10 steps with plain-language purpose, LaTeX maths, algorithms and settings; live LMDI waterfall, index builder, bootstrap null distributions and counterfactual calculator |
| 5 | Results | Hypothesis scorecard and 10 result tabs, each with "what this shows / how to read it / finding"; 2030 ceiling calculator |
| 6 | Conclusions | Discussion, policy implications, limitations, next steps, references |

Every number comes from a full re-run of `ireland_agri_ghg_analysis.ipynb` (seed 20261019) and matches the manuscript.

## Project layout

```
app.py                       Vercel entry point (zero-config Flask: exposes the Dash server as `app`)
dashboard/app.py             Dash app, navigation and routing
dashboard/pages/*.py         One module per research step
dashboard/data/results.json  All analysis outputs used by the site (exported from the notebook)
dashboard/data/*.csv         Annual panel offered for download
dashboard/assets/style.css   Styling
tools/export_results.py      Re-creates results.json from a notebook run
requirements.txt             dash + plotly only (no pandas needed at runtime)
```

## Run locally

```bash
pip install -r requirements.txt
python run_local.py           # http://127.0.0.1:8050
```

## Deploy on Vercel

**Option A — GitHub (recommended)**
1. Create a new GitHub repository and push this folder to it.
2. In Vercel: *Add New → Project → Import* the repository.
3. Framework preset: **Other**. Leave build and output settings empty. Click **Deploy**.

**Option B — Vercel CLI**
```bash
npm i -g vercel
cd ireland-agri-dashboard
vercel            # first deploy (preview)
vercel --prod     # production URL
```

No `vercel.json` is needed. Vercel detects `app.py` at the project root, installs `requirements.txt`,
and serves every URL (pages, Dash assets and callbacks) through the Flask instance named `app`.
`app.py`, `requirements.txt` and the `dashboard/` folder must sit at the **root** of the repository. The first request after a period of inactivity takes a few seconds (cold start).

## Updating the numbers after a new analysis run

1. Run the notebook as a script so its objects are saved (see `tools/export_results.py`: it reads
   `outputs/state.pkl`, a pickle of the notebook's DataFrames and `KEY` dictionary).
2. `python tools/export_results.py` writes `dashboard/data/results.json` and the panel CSV.
3. Redeploy.
