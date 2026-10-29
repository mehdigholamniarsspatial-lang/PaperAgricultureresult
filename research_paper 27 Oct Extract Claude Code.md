# Expansion versus Mitigation: Production-Oriented Policy and Agricultural Greenhouse-Gas Emissions in Ireland, 1990–2024

**Authors:** [Author names and affiliations]
**Corresponding author:** [Name, e-mail]
**Manuscript status:** Working paper, prepared from the study's interactive results platform (analysis run of 21 October 2026, random seed 20261019)
**Target journal:** *Climate Policy*

---

## Abstract

Irish agriculture produced 37.9% of national greenhouse-gas (GHG) emissions in 2024. Agricultural (IPCC/CRF sector 3) emissions that year, 19.63 Mt CO₂e, were within 0.7% of their 1990 level (19.76 Mt CO₂e), despite three decades of agri-environment schemes, nitrates regulation and, since 2021, legally binding carbon budgets. This paper asks whether the flat emission path reflects *failed mitigation* or *mitigation offset by policies that expanded output*. We build a new annual production-pressure index (P) and score it on the same implementation × coverage × bindingness scale used for a mitigation index (M), which puts the two policy sets on one comparable scale for the first time. We then combine three designs whose identifying assumptions fail in different ways: (i) trend, structural-break and exact Logarithmic Mean Divisia Index (LMDI) decomposition analysis; (ii) an autoregressive distributed-lag (ARDL) policy-mix model with restricted moving-block bootstrap inference, dynamic counterfactuals and explicit power analysis; and (iii) a within-Ireland regional difference-in-differences (DiD) design using pre-2015 dairy exposure. Emissions follow four regimes (breaks in 2000, 2012 and 2020; bootstrap UDmax p = 0.013), but no break lies within a year of Food Harvest 2020 (2010) or milk-quota abolition (2015). After quota abolition (2014–2021), scale and yield growth added 2,988 kt CO₂e while falling emission intensity removed only 963 kt, an intensity offset of 0.32 (0.21–0.33 across emission-factor assumptions). In the ARDL model a sustained 0.1-unit rise in production pressure raises long-run emissions by 7.2% (θ_P = 0.69, bootstrap p = 0.032). Production pressure above its 2000 level raised 2024 emissions by 11.2% (90% CI 6.7–15.7%) and added 12.5 Mt CO₂e over 2000–2024. The mitigation index shows no emission-reducing effect (θ_M = +0.47, p = 0.985). This positive coefficient is best read as reverse timing, since schemes expanded in the same years as output, and not as a causal effect. The positive pressure effect holds in all 14 estimable robustness variants and in all eight leave-one-policy-out runs. The regional design does not support a quota-abolition effect, because regions were already diverging before 2015. Interrupted time-series estimates locate the turn in 2010, not 2015. Meeting the 2030 sectoral ceiling (15.5 Mt CO₂e, −25% against 2018) would need roughly 23% fewer livestock units than in 2024 if the recent intensity trend continues, and 5–16% fewer even if intensity fell 1–3% a year. Expansion left a measurable footprint. The mostly voluntary, intensity-oriented mitigation portfolio left too small a footprint for anything to be offset.

**Keywords:** agricultural emissions; policy coherence; policy mix; production pressure; milk quota abolition; LMDI decomposition; ARDL; block bootstrap; difference-in-differences; Ireland

**JEL codes:** Q15, Q18, Q54, Q58, C22

---

## Highlights

- A new production-pressure index (P) is scored on the same implementation × coverage × bindingness scale as a mitigation index (M), so expansion and mitigation policy become commensurable.
- Irish CRF3 emissions were flat over 1990–2024 (−0.65%), but they moved through four regimes, with a sustained upturn from 2012.
- After milk-quota abolition, falling emission intensity cancelled only about one third of the emission growth caused by scale and yield (intensity offset = 0.32).
- Production pressure raised 2024 emissions by 11.2% (6.7–15.7%) and added 12.5 Mt CO₂e over 2000–2024. No emission-reducing effect of the mitigation portfolio can be detected.
- On recent intensity trends, the 2030 sectoral ceiling implies about 23% fewer livestock units than in 2024.

---

## 1. Introduction

Agriculture is the largest source of greenhouse-gas emissions in Ireland, responsible for 37.9% of the national total in 2024 (EPA, 2026). That share is exceptionally high among developed economies. It reflects a grass-based ruminant production system oriented towards export dairy and beef. Since the early 1990s the sector has been subject to a growing set of policies described, wholly or partly, as environmental or climate mitigation. These include the Rural Environment Protection Scheme (REPS, from 1994), the Nitrates Action Programme (from 2006), successive agri-environment schemes (AEOS, GLAS, ACRES), breeding and efficiency programmes (BDGP, BEEP-S, SCEP), advisory tools such as the Carbon Navigator, and, from 2022, direct limits on chemical nitrogen. The Climate Action and Low Carbon Development (Amendment) Act 2021 and the 2022 sectoral emissions ceiling then committed agriculture to a 25% reduction against 2018 by 2030.

Yet sector-3 emissions under the Common Reporting Format (CRF3) were 19.63 Mt CO₂e in 2024, against 19.76 Mt CO₂e in 1990, a change of −0.65%. The 2024 level was only 5.3% below the 2018 baseline, so most of the required 25% cut remains to be achieved within six years. Beneath the flat endpoints the path was far from flat: emissions fell through the 2000s to a low of 17.78 Mt in 2011, then rose sharply to 21.27 Mt in 2021. Something pushed them back up.

Two explanations compete. **Explanation A** holds that *mitigation was weak*. On this view instruments were voluntary, under-resourced or slow to deliver. This fits stakeholder accounts of capacity and coordination constraints (Augustenborg et al., 2026) and Ireland's record as a climate-policy laggard (Torney & O'Gorman, 2019). **Explanation B** holds that *mitigation was offset by expansion*. From 2007 the nitrates derogation allowed higher stocking rates. Milk quotas were raised from 2008 and abolished in 2015. National strategies (Food Harvest 2020, Food Wise 2025) set quantified growth targets. Under B, mitigation instruments may have worked but been cancelled by policies that increased output.

The distinction matters for policy. If mitigation instruments simply do not work, the remedy is better instruments. If they work but are cancelled by expansion policy, adding more instruments will not close the gap while the expansion incentives remain.

The central research question is therefore:

> **Is the flat emission path failed mitigation, or mitigation offset by policies that expanded output?**

Existing work establishes the *direction* of each mechanism. Productivity growth lowered emission intensity, but per-farm emissions rose with expansion after quota abolition (Läpple et al., 2022). Ex ante, Food Harvest 2020 was expected to raise emissions, and its growth targets were incoherent with reduction targets (Donnellan et al., 2013). Ireland's efficiency-based strategy failed to offset intensification pressure (Balaine et al., 2022). Herd-composition shifts move implied emission factors, so aggregate claims about intensity need care (Henn et al., 2023). What is not known is the *size of the offset*. Cross-country evaluations of climate policy measure instruments labelled as climate policy and treat other sectoral policy as background (Eskander & Fankhauser, 2020; Stechemesser et al., 2024). The policy-mix and policy-coherence literature stresses interactions between instruments, but mostly qualitatively (Nilsson et al., 2012; Rogge & Reichardt, 2016). To our knowledge, no study has placed expansion and mitigation policy on one scale and measured how much one offsets the other.

This paper makes three contributions.

1. **Measurement.** We construct an annual production-pressure index P, scored on the same implementation × coverage × bindingness scale that the INPACT approach applies to mitigation (M). The two policy sets become commensurable, and policy incoherence becomes a measurable quantity, the net signal $S = M - P$.
2. **Attribution with a short series.** We combine three designs whose assumptions fail in different ways: breaks and exact decomposition, an ARDL policy-mix model with block-bootstrap inference, and a within-Ireland regional DiD. We add explicit power analysis so that null results can be interpreted.
3. **Linking decomposition to policy.** We regress the annual LMDI activity and intensity effects on changes in P and M. This tests directly whether expansion works through scale and mitigation through intensity.

The analysis covers Ireland only. Quota abolition and CAP reform applied to every EU member state, so no untreated foreign comparator exists. Within-Ireland variation in exposure provides the comparison instead.

The remainder of the paper is organised as follows. Section 2 reviews the policy context and literature. Section 3 sets out the conceptual framework, research questions and pre-specified hypotheses. Section 4 describes the data and harmonisation. Section 5 presents the methods. Section 6 reports results. Section 7 discusses them, Section 8 sets out limitations, and Section 9 concludes.

---

## 2. Background and Literature

### 2.1 Irish agricultural policy, 1990–2024: two policy sets pulled in opposite directions

Table 1 summarises the policy context by period. Expansion instruments acted on *how much* was produced, and several of them relaxed binding legal limits. Mitigation instruments acted mainly on *how* it was produced, and most were voluntary contractual schemes. The main binding mitigation instrument, the Nitrates Action Programme, was designed for water quality rather than climate.

**Table 1. Policy context by period**

| Period | Production pressure (expansion) | Mitigation |
|---|---|---|
| 1990–2004 | Coupled suckler-cow, special-beef and ewe premia | REPS agri-environment scheme (from 1994) |
| 2005–2009 | CAP decoupling (2005) ends coupled premia; nitrates derogation from 2007; quota increments from 2006 and +2% in 2008 | Nitrates Action Programme (S.I. 378/2006); Farm Waste Management Scheme |
| 2010–2014 | Food Harvest 2020 (+50% milk volume target); +1% a year quota increases | REPS run-off; AEOS; Carbon Navigator; Sustainable Dairy Assurance Scheme (2014) |
| 2015–2021 | EU milk-quota abolition (31 March 2015); Food Wise 2025; TAMS II dairy equipment grants | GLAS; Beef Data and Genomics Programme; BEEP-S |
| 2021–2024 | Food Vision 2030 (mixed goals); derogation renewed and tightened from 2024 | 5th NAP chemical-N limits and protected urea (S.I. 113/2022); ACRES; SCEP. Climate Act 2021 and the 2022 ceiling are event markers |

Five dates are treated as policy events throughout: decoupling (2005), the first nitrates derogation (2007), Food Harvest 2020 (2010), quota abolition (2015) and the sectoral emissions ceiling (2022).

### 2.2 Evaluating climate policy in agriculture

Cross-country ex-post evaluations have estimated the emission effect of climate legislation (Eskander & Fankhauser, 2020) and identified the policy combinations that achieved large reductions (Stechemesser et al., 2024). These studies define the treatment as instruments labelled as climate policy. Sectoral policies that raise output enter only as background variation. For agriculture this matters a great deal. The main drivers of herd size and nitrogen use in the EU (milk quotas, coupled payments, derogations and national growth strategies) are not climate instruments at all.

### 2.3 Policy coherence, policy mixes and layering

The policy-coherence literature distinguishes sector–environment interactions that reinforce, are neutral to, or counteract each other (Nilsson et al., 2012). The policy-mix framework stresses that instruments operate jointly and that the mix, not the instrument, determines outcomes (Rogge & Reichardt, 2016). Policy-design scholarship describes "layering", in which new goals are added on top of existing instruments without removing contradictory ones (Howlett & Rayner, 2013). These frameworks predict that Irish mitigation effort could be neutralised by concurrent expansion policy. They have mostly been applied qualitatively, however, and do not yield an estimate of how large the offset was.

### 2.4 Decomposition and the rebound analogy

Index-decomposition analysis, and the LMDI family in particular, splits emission changes exactly into activity, structure and intensity effects (Ang & Liu, 2001; Ang, 2015). In energy economics, the share of an efficiency gain that is cancelled by induced demand is the *rebound effect* (Greening et al., 2000). The agricultural analogue is the extent to which lower emissions per litre or per head are cancelled by more litres and more heads. We formalise this as the *intensity offset* (Section 3.2).

### 2.5 Evidence for Ireland

Läpple et al. (2022) find that EU milk-quota abolition raised dairy expansion and per-farm emissions despite lower emission intensity. Donnellan et al. (2013) show that the Food Harvest 2020 targets were incompatible with emission-reduction commitments. Balaine et al. (2022) conclude that the efficiency-based strategy did not offset intensification. Henn et al. (2023) caution that herd-composition shifts change implied emission factors. Augustenborg et al. (2026) identify five stakeholder-perceived barriers to environmental policy implementation in Ireland: policy incoherence, competing political priorities, capacity, financial constraints and planning constraints.

### 2.6 The gap

The direction of each mechanism is known, but the *size* of the offset between expansion and mitigation policy has not been measured. Measuring it needs (i) a common scale for both policy sets, (ii) an attribution strategy that works with a single national series of about 30 annual observations, and (iii) a link between the accounting decomposition and the policy variables. This paper provides all three.

---

## 3. Conceptual Framework and Hypotheses

### 3.1 Emissions = scale × intensity

The framework rests on an accounting identity: emissions equal activity times intensity. Production-pressure policy (the derogation, quota increases and abolition, growth strategies, TAMS capital grants) is expected to *raise* activity: herd size, nitrogen use and milk volume. Mitigation policy (nitrates rules, agri-environment schemes, genetics programmes, advisory tools) is expected to *lower* intensity: emissions per litre, per head and per kg N.

```
Production pressure P ──raises (+)──► Activity (herd size, N use, milk volume) ─┐
                                                                                ├─×──► CRF3 emissions  E = Activity × Intensity
Mitigation M ─────────lowers (−)──► Intensity (per litre, per head, per kg N) ──┘
```

Total emissions fall only if intensity falls faster than activity grows. Expansion policies act on *how much* is produced, while Irish mitigation policy has mostly acted on *how* it is produced.

### 3.2 Intensity offset

We define the intensity offset over any period with positive scale growth as

$$
IO=\frac{-\Delta E^{\text{intensity}}}{\Delta E^{\text{activity}}+\Delta E^{\text{productivity}}}
$$

IO is the share of scale-driven emission growth cancelled by lower emissions per unit. $IO = 1$ means efficiency exactly cancelled growth. $IO < 1$ means efficiency gains did not keep pace with expansion, the agricultural analogue of a rebound effect above 100% in energy economics (Greening et al., 2000). IO is defined only when $\Delta E^{\text{activity}} + \Delta E^{\text{productivity}} > 0$.

### 3.3 Policy incoherence as a measurable quantity

With M and P on one scale, the net policy signal is

$$
S_t = M_t - P_t .
$$

If P and M rise in the same period, S understates mitigation effort. This makes the sector–environment incoherence of Nilsson et al. (2012) and the layering of Howlett & Rayner (2013) measurable.

### 3.4 Research questions and pre-specified hypotheses

Hypotheses and decision rules were fixed in the analysis code before estimation. With about 28 usable annual observations, every test uses α = 0.10. Rules are applied mechanically: a hypothesis is "supported" only if its pre-registered condition holds.

**Table 2. Research questions, hypotheses, tests and decision rules**

| RQ | Question | Hypothesis | Primary test | Supported if |
|---|---|---|---|---|
| RQ1 | Do breaks in the emission path coincide with policy changes? | H1: an endogenous break lies within ±1 year of 2010 (Food Harvest 2020) or 2015 (quota abolition) | Bai–Perron structural breaks with bootstrap UDmax | UDmax p < 0.10 and a break date within ±1 year |
| RQ2 | Did intensity gains keep pace with scale growth? | H2: intensity offset IO < 1 after 2015 (efficiency did not keep pace) | Exact LMDI decomposition; decomposition–regression link | IO < 1 across the dairy emission-factor range |
| RQ3 | Did production pressure offset mitigation? | H3a: θ_M < 0 (mitigation lowers emissions); H3b: θ_P > 0 (pressure raises them); H3c: offset ratio ≥ 0.5 | ARDL long-run multipliers, restricted block bootstrap, dynamic counterfactuals | One-sided bootstrap p < 0.10; for H3c the pressure effect's 90% interval excludes zero |
| RQ4 | Do effects differ by instrument type and by regional exposure? | H4a: mandatory instruments have the largest negative effect; H4b: more dairy-exposed regions expanded more after 2015 | Sub-index ARDL; within-Ireland regional DiD | p < 0.10 with the predicted sign; placebo not significant |

### 3.5 Dimensions of policy success

Following Marsh & McConnell (2010), we distinguish three dimensions of policy success. *Programme* success asks whether instruments changed outcomes, and is tested by RQ1–RQ4. *Process* success asks whether instruments were implemented as designed, and is captured by the implementation score I. *Political* success asks whether instruments survived competing priorities, and is discussed against the five stakeholder-identified barriers of Augustenborg et al. (2026).

---

## 4. Data

### 4.1 Sources

The analysis draws on 58 raw files from four agencies plus the authors' policy codebooks (Table 3). Every series is annual and read unchanged from the publishing agency, and every loaded file is fingerprinted with SHA-256. A source catalogue of 50 datasets and parameters, with download and documentation links, accompanies the study's online platform.

**Table 3. Data sources**

| Agency | Product | Form | Content used | Years |
|---|---|---|---|---|
| EPA | Provisional GHG inventory workbook 1990–2025 | Excel workbook | CRF3 total, 5 categories, 3 gases | 1990–2024 |
| UNFCCC | Ireland CRT 2025 submission | 34 workbooks, one per inventory year | Dairy / non-dairy CH₄ split, N excretion, mineral N 1990–99 | 1990–2023 |
| Eurostat | `env_air_gge`, `aei_fm_usefert`, LSU coefficients | CSV extracts | Species CH₄ detail, mineral N 2000–24, livestock-unit coefficients | 1990–2024 |
| CSO | AAA01/07/09, AKA01, AHA01–05, CPA01, NA002 | PxStat CSV | Livestock (national and regional), milk, prices, CPI, GNI* | 1991–2024 |
| Authors | Policy codebooks (`pressure_codebook.csv`, `mitigation_codebook_PROVISIONAL.csv`) | CSV | 20 instruments scored I × C × B | 1990–2024 |

### 4.2 Outcome: CRF sector 3 emissions

The outcome is IPCC/CRF sector 3 (agriculture), in kt CO₂-equivalent, using AR5 100-year global warming potentials (CH₄ = 28, N₂O = 265; Myhre et al., 2013), the metric of Ireland's inventory:

$$
E_t^{\text{CRF3}} = E_t^{\text{Agriculture}} - E_t^{1.A.4.c.ii} - E_t^{1.A.4.c.iii}
\;=\;\sum_{c\in\{3A,3B,3D,3G,3H\}} E_{c,t}
\;=\;E^{CO_2}_t+28\,E^{CH_4}_t+265\,E^{N_2O}_t .
$$

The EPA "Agriculture" row follows the Climate Action Plan definition, which also includes agricultural and forestry fuel (1.A.4.c.ii) and fishing (1.A.4.c.iii). These are subtracted. The result is checked every run against both the sum of the five reported categories (enteric fermentation 3.A, manure management 3.B, agricultural soils 3.D, liming 3.G, urea 3.H) and the sum of the three gases, with a gap below 0.0001%. Other sector-3 categories are not occurring or not applicable for Ireland.

Three inventory vintages are combined: the EPA provisional inventory (2026) for CRF3, which is the only source with 2024; Eurostat `env_air_gge` for species detail; and CRT 2025 for the dairy/non-dairy split and 1990s fertiliser. They agree to within 0.01% for 1990–2020 and 0.21% for 2021–2023. The LMDI "other" term absorbs any difference between vintages, so the decomposition stays exact.

### 4.3 Activity variables

**Livestock.** CSO June livestock tables AAA01 (1991–2004), AAA07 (2005–2014) and AAA09 (2015–) cover disjoint years and are stacked without back-filling, so 1990 stays missing. Dairy cows fall 8.7% at the AAA01→AAA07 switch while total cattle fall only 0.3%. The CRT shows the same step, which identifies it as a classification change. Every model in which the herd enters therefore includes a 2005 indicator. Livestock units are

$$
\text{LU}_t = 1.0\cdot D_t + \sum_{k} \lambda_k N_{k,t} + 0.1\cdot Sh_t,\qquad \lambda_k\in\{0.4,0.7,0.8,1.0\},
$$

where $D$ = dairy cows, $N_k$ = CSO non-dairy cattle categories weighted by Eurostat LSU coefficients $\lambda_k$, and $Sh$ = sheep. The implied LU per non-dairy animal falls from 0.673 to 0.638 as the herd becomes younger.

**Milk.** Domestic milk intake by processors (CSO AKA01) starts in 1992. Yield is $\text{yield}_t = \text{milk}_t (10^6\,\text{L}) \times 10^3 / D_t (10^3\ \text{head})$.

**Nitrogen.** Mineral N fertiliser comes from CRT 2025 Table 3.D for 1990–1999 and Eurostat `aei_fm_usefert` for 2000–2024. CRT Table 3.D is headed "t N/year" but the values are in kg N. Dividing by 1,000 reproduces the Eurostat figures for 2000–2005 exactly. Manure N excreted is

$$
N^{\text{manure}}_t=\frac{\text{nex}^{D}_t D_t+\text{nex}^{O}_t O_t+\text{nex}^{Sh}_t Sh_t}{10^3},
$$

with N-excretion rates (kg N/head/yr) from CRT Table 3.B(b). The dairy rate rises from 97.9 (1991) to 108.4 (2023), the non-dairy cattle rate falls from 54.8 to 48.1, and the sheep rate is about 7.5.

### 4.4 Prices and macro controls

Five CSO agricultural price-index vintages (bases 2000, 2005, 2010, 2015, 2020) are chain-linked by the overlap method:

$$
\tilde I^{\,old}_{t}=I^{old}_t\cdot\exp\!\Big(\frac{1}{|\mathcal O|}\sum_{s\in\mathcal O}\ln\frac{I^{new}_s}{I^{old}_s}\Big),
\qquad p^{real}_t=\frac{\tilde I_t}{CPI_t}\times 100\quad(2020=100),
$$

where $\mathcal O$ is the set of overlapping years. The newest vintage is kept in overlaps, and the geometric mean treats ratios symmetrically (Eurostat, 2016). The largest overlap deviation across 20 links is 2.88%. Prices start in 1995. Modified GNI (GNI*, CSO NA002) enters one robustness variant. No weather variable is used.

### 4.5 Regional panel

Quota abolition should bind hardest where dairy was already dominant. The 2014/2016 NUTS3 revision moved Louth from the Border to the Mid-East and unified Tipperary. We therefore build five constant-boundary units: West, Midland and South-West, which are unchanged; **Border + Dublin/Mid-East**, which absorbs Louth's move; and **Mid-West + South-East**, which absorbs the Tipperary unification. These units sum to the State within 0.014% (dairy), 0.004% (cattle) and 0.003% (sheep). The panel covers 1991–2024. Regional imputed livestock emissions (head counts × national implied emission factors per head) are available to 2023.

**Table 4. Exposure to quota abolition: dairy share of all cows, 2010–2014**

| Region | Dairy share of cows (%) |
|---|---|
| West | 16.3 |
| Midland | 35.3 |
| Border + Dublin/Mid-East | 38.3 |
| Mid-West + South-East | 58.4 |
| South-West | 73.7 |

Exposure ranges from 16% to 74%, a wide contrast for a continuous-intensity design (Card, 1992).

### 4.6 Harmonisation and missing-data rules

Missing years are **never** interpolated, back-cast or set to zero. Inventory notation keys (NO/NE/NA) become missing. Each estimator uses the largest common sample and reports it. The CRT-based dairy split and N excretion end in 2023, because the 2024 CRT had not been published, and they are not imputed. As a result the LMDI decomposition and the regional emission series end in 2023, while CRF3 runs to 2024.

### 4.7 Descriptive statistics

**Table 5. Selected series, 1990–2024**

| Variable | Unit | 1990/first | 2000 | 2010 | 2015 | 2018 | 2024/last | Peak (year) | Trough (year) |
|---|---|---|---|---|---|---|---|---|---|
| CRF3 emissions | kt CO₂e | 19,760 | 20,321 | 18,166 | 19,346 | 20,728 | 19,631 | 21,657 (1998) | 17,780 (2011) |
| Enteric fermentation | kt CO₂e | 12,480 | 12,685 | 11,205 | 12,226 | 12,917 | 12,696 | – | – |
| Agricultural soils | kt CO₂e | 4,393 | 4,715 | 4,154 | 4,155 | 4,693 | 3,903 | – | – |
| Manure management | kt CO₂e | 2,435 | 2,463 | 2,281 | 2,500 | 2,567 | 2,406 | – | – |
| Dairy cows | thousand head | 1,331 (1991) | 1,178 | 1,071 | 1,296 | 1,481 | 1,624 | 1,647 (2023) | 1,055 (2005) |
| Non-dairy cattle | thousand head | 5,581 (1991) | 5,860 | 5,536 | 5,668 | 5,868 | 5,559 | 6,406 (1998) | 5,376 (2011) |
| Sheep | thousand head | 8,888 (1991) | 7,555 | 4,745 | 5,139 | 5,109 | 5,176 | 8,898 (1992) | 4,745 (2010) |
| Livestock units | thousand LU | 5,975 (1991) | 5,924 | 5,221 | 5,452 | 5,757 | 5,686 | 6,378 (1998) | 5,106 (2011) |
| Milk intake | million L | 5,106 (1992) | 5,012 | 5,173 | 6,395 | 7,585 | 8,428 | 8,825 (2022) | 4,785 (2009) |
| Milk yield | L per cow | 3,996 (1992) | 4,256 | 4,831 | 4,935 | 5,122 | 5,190 | 5,459 (2021) | 3,996 (1992) |
| Mineral N fertiliser | kt N | 379 | 408 | 338 | 331 | 408 | 310 | 443 (1999) | 281 (2023) |
| Mitigation index M | index | 0.000 | 0.068 | 0.405 | 0.586 | 0.617 | 0.638 | 0.683 (2020) | 0.000 (1990) |
| Pressure index P | index | 0.241 | 0.241 | 0.358 | 0.450 | 0.450 | 0.336 | 0.450 (2015–20) | 0.000 (2005) |
| Net signal S | index | −0.241 | −0.172 | 0.047 | 0.136 | 0.167 | 0.302 | 0.369 (2007) | −0.241 (1990) |

*Note:* CRF3 and categories in AR5 GWP100. "First" values are given where a series starts after 1990.

**Composition.** In 2024 enteric fermentation accounted for 64.7% of CRF3 (63.2% in 1990), agricultural soils 19.9% (22.2%), manure management 12.3% (12.3%), liming 2.3% and urea 0.9%. By gas, methane was 74.1% (72.3% in 1990), nitrous oxide 22.7% (25.4%) and CO₂ 3.2%. Dairy-cattle methane rose from 19.6% of CRF3 in 1995 to 23.3% in 2015 and 29.2% in 2023. Soils N₂O follows fertiliser use, which peaked in 1999.

### 4.8 Policy codebooks

Twenty instruments are coded: 8 production-pressure instruments (P01–P08) and 12 mitigation instruments (M01–M12). Two framework laws (E01, E02) are recorded as event markers but not entered in either index, to avoid double counting.

**Table 6. Production-pressure codebook (P)**

| ID | Instrument | Type | Years | Coverage key (share s) | Eligible e | Bindingness B | Implementation I |
|---|---|---|---|---|---|---|---|
| P01 | Coupled livestock premia (suckler cow, special beef, ewe premia) | incentive | 1990–2004 | beef_sheep (0.482) | 1.00 | 0.50 | 1 |
| P02 | Milk quota increases (Agenda 2000 increments; Health Check soft landing) | conditional | 2006–2014 | dairy (0.185) | 1.00 | 0.75 | 0.25 (2006–07), 0.75 (2008), 1 (2009–14) |
| P03 | Nitrates derogation (stocking above 170 kg organic N/ha) | conditional | 2007–2024 | dairy (0.194) | 0.30* | 0.75 | 1 (2007–23), 0.75 (2024) |
| P04 | Food Harvest 2020 (+50% milk volume target) | strategy | 2010–2014 | cattle_sheep (0.701) | 1.00 | 0.25 | 1 |
| P05 | EU milk quota abolition | mandatory removal | 2015–2024 | dairy (0.216) | 1.00 | 1.00 | 1 |
| P06 | Food Wise 2025 (+65% primary output value) | strategy | 2015–2020 | cattle_sheep (0.698) | 1.00 | 0.25 | 1 |
| P07 | Food Vision 2030 | strategy | 2021–2024 | cattle_sheep (0.702) | 1.00 | 0.25 | 0.5 (mixed goals) |
| P08 | TAMS II Dairy Equipment Scheme | incentive | 2015–2022 | dairy (0.216) | 0.15* | 0.50 | 1 |

*Provisional eligibility shares, to be replaced with DAFM statistics.

**Table 7. Mitigation codebook (M, provisional)**

| ID | Instrument | Type | Years | Coverage key (share s) | Eligible e | B | Implementation I |
|---|---|---|---|---|---|---|---|
| M01 | Rural Environment Protection Scheme (REPS 1–4) | incentive | 1994–2014 | n_soils_manure (0.342) | 0.40 | 0.50 | 0.25 (1994), 0.5 (1995), 1 (1996–2009), 0.5 (2010–13), 0.25 (2014) |
| M02 | Nitrates Action Programme (GAP Regulations) | mandatory | 2006–2024 | n_soils_manure (0.354) | 1.00 | 1.00 | 0.5 (2006), 1 (2007–24) |
| M03 | Farm Waste Management Scheme | incentive | 2006–2009 | manure (0.125) | 0.40 | 0.50 | 1 |
| M04 | Agri-Environment Options Scheme (AEOS) | incentive | 2010–2014 | n_soils_manure (0.343) | 0.10 | 0.50 | 1 |
| M05 | Carbon Navigator and advisory programmes | voluntary | 2013–2024 | cattle_sheep (0.706) | 0.20 | 0.25 | 1 |
| M06 | Sustainable Dairy Assurance Scheme (Origin Green) | voluntary | 2014–2024 | dairy (0.207) | 0.90 | 0.25 | 1 |
| M07 | Green Low-Carbon Agri-Environment Scheme (GLAS) | incentive | 2015–2023 | n_soils_manure (0.348) | 0.35 | 0.50 | 0.5 (2015), 1 (2016–22), 0.5 (2023) |
| M08 | Beef Data and Genomics Programme (BDGP) | incentive | 2015–2020 | beef_sheep (0.482) | 0.50 | 0.50 | 1 |
| M09 | Beef Environmental Efficiency Programme – Sucklers (BEEP-S) | incentive | 2020–2022 | beef_sheep (0.439) | 0.30 | 0.50 | 1 |
| M10 | Chemical N reduction measures (5th NAP limits; protected urea; LESS) | mandatory | 2022–2024 | fertiliser (0.083) | 1.00 | 1.00 | 0.5 (2022), 1 (2023–24) |
| M11 | Agri-Climate Rural Environment Scheme (ACRES) | incentive | 2023–2024 | n_soils_manure (0.323) | 0.35 | 0.50 | 1 |
| M12 | Suckler Carbon Efficiency Programme (SCEP) | incentive | 2023–2024 | beef_sheep (0.420) | 0.30 | 0.50 | 1 |

*Event markers (not in the indices):* E01, the Climate Action and Low Carbon Development (Amendment) Act 2021 (Act No. 32 of 2021); E02, the agriculture sectoral emissions ceiling of July 2022 (−25% by 2030 against 2018).

Coverage keys denote the share of CRF3 in the targeted activity: *dairy* = dairy CH₄; *beef_sheep* = non-dairy cattle + sheep CH₄; *cattle_sheep* = all cattle + sheep CH₄; *n_soils_manure* = soils + manure management; *manure* = manure management; *fertiliser* = direct N₂O from mineral N + urea CO₂; *all* = all of CRF3.

---

## 5. Methods

No single method can identify a causal policy effect from one national series of about 28 usable observations. The study therefore combines three designs whose identifying assumptions fail in different ways, so that their agreement, rather than any single estimate, carries the inference (Lawlor et al., 2016; Munafò & Davey Smith, 2018).

- **Design A, descriptive:** trends, breaks and decomposition (Mann–Kendall, Theil–Sen, Bai–Perron with bootstrap UDmax, exact LMDI-I). Answers RQ1 and RQ2.
- **Design B, policy-mix time series:** ARDL(1,0,2), 1997–2024, n = 28, with restricted bootstrap p-values, counterfactuals and power/MDE. Answers RQ3 and RQ4a.
- **Design C, within-Ireland comparison:** regional DiD across five constant-boundary regions, with exposure = pre-2015 dairy share and randomisation inference. Answers RQ4b.

The pipeline runs in six stages: (1) load and hash; (2) harmonise (CRF3 boundary, livestock stacking, regions, price chain-linking); (3) build the annual panel (1990–2024) and the regional panel (5 × 1991–2024); (4) build the policy indices M, P and S; (5) estimate the models (breaks, LMDI, ARDL + bootstrap, counterfactuals, power, DiD, 2030 scenarios); (6) export and verify (34 result sheets, 7 figures, 30 independent checks).

### 5.1 Policy indices

Each policy *p* receives an annual score

$$
x_{pt}=I_{pt}\;C_p\;B_p,\qquad C_p=s_{a(p),\,t^0_p-1}\;e_p , \tag{1}
$$

where:

- **I** = implementation, on a five-point grid {0, 0.25, 0.5, 0.75, 1};
- **C** = coverage = $s$ × $e$, where $s$ is the share of CRF3 in the targeted activity $a(p)$ in the year *before* the policy starts ($t^0_p - 1$) and $e$ is the eligible fraction;
- **B** = bindingness: 0.25 = information, voluntary scheme or strategy target; 0.5 = incentive payment; 0.75 = conditional relaxation of a legal limit; 1.0 = mandatory rule or removal of a legal cap.

The product is non-compensatory: a policy counts only if it is in force, covers emissions and carries a signal (OECD et al., 2008). The indices are

$$
M_t=\sum_{p\in\mathcal M}x_{pt},\qquad P_t=\sum_{q\in\mathcal P}x_{qt},\qquad S_t=M_t-P_t . \tag{2}
$$

*Why coverage is fixed before adoption.* If coverage were measured each year, a policy that expanded dairy would raise the dairy share and therefore its own weight. Fixing exposure weights before treatment is standard in shift-share designs (Goldsmith-Pinkham, Sorkin & Swift, 2020).

*Inter-coder reliability.* A linearly weighted Cohen's kappa is computed on the five-point grid (Cohen, 1968):

$$
\kappa_w=1-\frac{\sum_{ij}w_{ij}O_{ij}}{\sum_{ij}w_{ij}E_{ij}},\qquad w_{ij}=\frac{|i-j|}{k-1},
$$

where $O_{ij}$ is the observed share of policy-years that coder 1 placed in category *i* and coder 2 in category *j*, and $E_{ij}$ is the share expected under independent scoring. Kappa is computed separately for implementation and bindingness. **The second coding is currently a provisional placeholder pending independent blind coding.** The reported values (implementation κ_w = 0.60 over 75 policy-years; bindingness κ_w = 1.00 over 8 policies) are therefore illustrative only.

### 5.2 Trends and structural breaks (RQ1)

*Monotonic trend.* With $y_t = \ln E_t$, we compute the Mann–Kendall statistic with the Hamed–Rao variance correction for autocorrelation, together with the Theil–Sen slope:

$$
S=\sum_{i<j}\operatorname{sgn}(y_j-y_i),\qquad Z=\frac{S-\operatorname{sgn}(S)}{\sqrt{\operatorname{Var}^*(S)}},\qquad \operatorname{Var}^*(S)=\operatorname{Var}(S)\cdot\frac{n}{n^*_s},
$$

$$
\hat\beta_{\text{Sen}}=\operatorname{median}_{i<j}\frac{y_j-y_i}{j-i}\quad\Rightarrow\quad \%\,\text{per year}=100\,(e^{\hat\beta}-1).
$$

The factor $n/n^*_s$ inflates the variance under positive autocorrelation, which would otherwise overstate significance (Hamed & Rao, 1998; Yue et al., 2002).

*Structural breaks.* A Bai–Perron segmented-trend model

$$
\ln E_t=\alpha_j+\delta_j t+u_t,\qquad T_{j-1}<t\le T_j,\; j=1,\dots,m+1 \tag{3}
$$

is estimated by global SSR minimisation. Closed-form segment SSRs are combined by dynamic programming for m = 1…4 breaks with a minimum segment length h = 5 years (trimming ε ≈ 0.15 of n = 35; Bai & Perron, 2003). The number of breaks is chosen by

$$
\text{BIC}(m)=n\ln\frac{SSR_m}{n}+\big[2(m+1)+m\big]\ln n .
$$

Whether there is any break is tested with

$$
\text{UDmax}=\max_{1\le m\le 4}F(m),\qquad F(m)=\frac{(SSR_0-SSR_m)/2m}{SSR_m/\big(n-2(m+1)\big)} . \tag{4}
$$

Asymptotic critical values are unreliable at n = 35 (Diebold & Chen, 1996). The p-value therefore comes from a parametric bootstrap: H₀ (one trend with AR(1) errors) is fitted, 999 series are simulated under H₀, UDmax is recomputed for each, and $p = (1 + \#\{\text{UDmax}^* \ge \text{UDmax}\})/(B+1)$. Ninety-percent intervals for the break dates come from a residual bootstrap of the selected model (499 draws). Known-date Chow tests at 2010 and 2015 complement the search.

### 5.3 Exact LMDI decomposition (RQ2)

Emission components are written as exact products of factors:

$$
\begin{aligned}
E^{dairy}&=\underbrace{D}_{\text{herd}}\times\underbrace{\tfrac{\text{milk}}{D}}_{\text{yield}}\times\underbrace{\tfrac{E^{dairy}}{\text{milk}}}_{\text{per litre}},
\qquad E^{other}=O\times\tfrac{E^{other}}{O},\qquad E^{sheep}=Sh\times\tfrac{E^{sheep}}{Sh},\\
E^{soils}&=N^{fert}\cdot\tfrac{E^{soils}}{N^{fert}+N^{man}}+N^{man}\cdot\tfrac{E^{soils}}{N^{fert}+N^{man}},\qquad
E^{other\ cat.}=E^{CRF3}-\textstyle\sum_i E_i .
\end{aligned}
$$

The additive LMDI-I form gives

$$
\Delta E^{k}=\sum_i L\big(E_i^T,E_i^0\big)\,\ln\frac{x_{ik}^T}{x_{ik}^0},\qquad L(a,b)=\frac{a-b}{\ln a-\ln b},\;L(a,a)=a , \tag{5}
$$

and because $\ln\prod_k x_k=\sum_k\ln x_k$,

$$
\sum_k\Delta E^k=\sum_i L(E_i^T,E_i^0)\ln\frac{E_i^T}{E_i^0}=\sum_i\big(E_i^T-E_i^0\big)=E^T-E^0 ,
$$

so there is no residual (Ang & Liu, 2001; Ang, 2015). The verified residual is 1.9 × 10⁻¹¹ kt. Factors are grouped as *activity* (herd sizes, N inputs), *productivity* (milk per cow), *intensity* (emissions per litre, per head, per kg N) and *other* (other categories and differences between vintages). Effects are chained year by year from 1992, the first year with milk data, to 2023, the last year of the CRT dairy split, and summed within five policy phases: P1 coupled support (1992–2004), P2 decoupling and derogation (2004–09), P3 Food Harvest and quota increases (2009–14), P4 post-quota expansion (2014–21) and P5 sectoral ceiling (2021–23). Soils N₂O is allocated to mineral and manure N in proportion to inputs, using one implied N₂O intensity per kt N. Sensitivity to the dairy/non-dairy emission-factor ratio is checked at 1.8, 2.2 and 2.6, which brackets the CRT ratio of 2.2–2.85.

The decomposition is an accounting identity. It shows *what* moved emissions, not *which policy* caused the movement. Changes in inventory methodology also appear as intensity change even when farm practice is unchanged.

### 5.4 ARDL policy-mix model (RQ3)

The model is

$$
\ln E_t=\alpha+\tau t+\sum_{i=1}^{p}\phi_i\ln E_{t-i}+\sum_{j=0}^{q_M}\beta_jM_{t-j}+\sum_{j=0}^{q_P}\gamma_jP_{t-j}+\lambda'X_t+\varepsilon_t , \tag{6}
$$

where $X_t$ contains the log real milk price and log real fertiliser price, the main output- and input-market drivers. The linear trend prevents the two rising indices from absorbing smooth drift. The lagged dependent variable captures slow adjustment of herds and soil-N pools. The ARDL is valid whether regressors are I(0), I(1) or cointegrated (Pesaran et al., 2001).

*Lag selection.* All 18 candidates, $p\in\{0,1\}$ and $q_M,q_P\in\{0,1,2\}$, are estimated on the *same* sample (1997–2024, n = 28), because prices start in 1995 and up to two lags are allowed. The small-sample criterion $\text{AICc}=\text{AIC}+2k(k+1)/(n-k-1)$ selects **ARDL(1, 0, 2)**:

$$
\ln E_t=\alpha+\tau t+\phi\ln E_{t-1}+\beta_0M_t+\gamma_0P_t+\gamma_1P_{t-1}+\gamma_2P_{t-2}+\lambda'X_t+\varepsilon_t .
$$

*Long-run multipliers.*

$$
\theta_M=\frac{\sum_j\beta_j}{1-\sum_i\phi_i},\qquad \theta_P=\frac{\sum_j\gamma_j}{1-\sum_i\phi_i} , \tag{7}
$$

with delta-method variances $\operatorname{Var}(\hat\theta)\approx\nabla\theta'\,\hat V_{HAC}\,\nabla\theta$, where $\partial\theta_P/\partial\gamma_j = 1/(1-\phi)$ and $\partial\theta_P/\partial\phi = \sum_j\gamma_j/(1-\phi)^2$. $\hat V_{HAC}$ is the Newey–West covariance with 2 lags and a small-sample correction (rule of thumb $0.75\,T^{1/3}\approx2.3$; Newey & West, 1987; Stock & Watson, 2020). A sustained change of 0.1 in an index changes long-run emissions by $100(e^{0.1\theta}-1)$ percent.

*Bounds test and diagnostics.* The Pesaran–Shin–Smith bounds test (case V, unrestricted intercept and trend, k = 4) is applied to

$$
\Delta y_t=c+\tau t+\pi_y y_{t-1}+\pi_M M_{t-1}+\pi_P P_{t-1}+\pi_X'X_{t-1}+\textstyle\sum\psi\,\Delta(\cdot)+u_t,\qquad H_0:\pi_y=\pi_M=\pi_P=\pi_X=0 .
$$

An F statistic above the I(1) bound indicates a level relationship. Residual diagnostics are the Breusch–Godfrey test (2 lags), Jarque–Bera, Breusch–Pagan, RESET and CUSUM. ADF and KPSS unit-root tests characterise the integration order of each variable.

### 5.5 Restricted recursive moving-block bootstrap

With 28 observations, textbook HAC t-tests reject too often. In Monte Carlo simulation, a nominal 10% HAC test rejects 15% of the time for θ_M and 32% for θ_P when the true effect is zero (cf. Kiefer & Vogelsang, 2005). The decisive p-values therefore come from a bootstrap that imposes the null (Davidson & MacKinnon, 2000; Li & Maddala, 1996):

1. Re-estimate the model without the tested index *v* (null model, H₀: θ_v = 0).
2. Centre its residuals and cut them into overlapping blocks of length 3, which preserves serial dependence (≈ T^{1/3}; Hall, Horowitz & Jing, 1995).
3. Draw blocks with replacement to form a new residual series ε*.
4. Generate pseudo-emissions recursively from the null model:
   $$
   y^*_t=\hat\alpha+\hat\tau t+\hat\phi\,y^*_{t-1}+\sum_{w\neq v}\hat b_w'w_t+\hat\lambda'X_t+\varepsilon^*_t .
   $$
5. Re-estimate the full ARDL (including *v*) on y* and record θ*_v.
6. Repeat B = 999 times and compute the one-sided p-value
   $$
   p^{*}_v=\frac{1+\#\{\theta_v^{*(b)}\ \text{beyond}\ \hat\theta_v\}}{B+1},
   $$
   testing θ_M < 0 for H3a and θ_P > 0 for H3b.

B = 999 makes α(B + 1) an integer. Robustness variants use B = 299 and sub-indices B = 499. A single generator seeded at 20261019 makes every draw reproducible.

### 5.6 Dynamic counterfactuals and the offset ratio (RQ3)

To express coefficients in tonnes, each index is frozen at its level in year $t_0 = 2000$ and the fitted dynamics are propagated:

$$
\Delta_{v,t}=\sum_i\phi_i\Delta_{v,t-i}+\sum_j b_{v,j}\,\big(v_{t-j}-v_{t_0}\big),\qquad
E^{cf}_t=E_t\,e^{-\Delta_{v,t}},\qquad OR_T=\frac{\Delta_{P,T}}{-\Delta_{M,T}} , \tag{8}
$$

where $\Delta_{v,t}$ is the log-point effect of index *v* in year *t* and $b_{v,j}$ are its lag coefficients. The **offset ratio** OR is defined only when the mitigation effect is negative, by analogy with the rebound effect. Ninety-percent intervals come from an *unrestricted* block bootstrap (999 draws).

### 5.7 Power and minimum detectable effect

To interpret null results, we (i) set a true long-run effect |θ| on the grid {0, 0.1, 0.2, 0.3, 0.5, 0.75, 1, 1.5}; (ii) simulate 500 emission series from the fitted model with that θ, using the observed paths of M, P and X and block-resampled residuals; (iii) re-estimate the full model on each series and record the t-statistic; (iv) take the 90th percentile at θ = 0 as the size-adjusted critical value; and (v) compute power(θ) as the share of t-statistics above it. The MDE is the smallest |θ| with 80% power, found by linear interpolation (Bloom, 1995; Gelman & Carlin, 2014).

### 5.8 Robustness, instrument sub-indices and interrupted time series

*Robustness grid.* Fourteen pre-specified variants plus eight leave-one-policy-out runs (Appendix B). The rule, fixed in advance, is that a sign is **robust** if it holds in at least 80% of estimable variants.

*Sub-indices by instrument type (RQ4a).*

$$
\ln E_t=\dots+\beta^{s}M^{s}_t+\beta^{rest}\big(M_t-M^{s}_t\big)+\sum_j\gamma_jP_{t-j}+\dots,\quad s\in\{\text{mandatory, incentive, voluntary}\},
$$

where each sub-index is estimated in turn with the rest of M and P held as controls (bootstrap B = 499).

*Interrupted time series at pre-specified dates.*

$$
y_t=\beta_0+\beta_1t+\sum_{e\in\{2010,2015,2022\}}\Big[\lambda_e\mathbb 1(t\ge e)+\delta_e\,(t-e+1)\,\mathbb 1(t\ge e)\Big]+\lambda'X_t+u_t ,
$$

where $\lambda_e$ is the level change and $\delta_e$ the slope change at event *e* (segmented regression; Bernal et al., 2017). Outcomes are ln CRF3 and ln dairy cows, the latter with a post-2005 dummy. The sample is 1995–2024 with HAC errors. The 2022 event has only three post-event years and is treated as descriptive.

### 5.9 Regional difference-in-differences (RQ4b)

If quota abolition drove expansion, regions where dairy was already dominant should have expanded more after 2015. We estimate a continuous-exposure DiD:

$$
y_{rt}=\alpha_r+\gamma_t+\beta\,\big(\text{Exp}_r-\overline{\text{Exp}}\big)\,\mathbb 1[t\ge2015]+\mu_r\,\mathbb 1[t\ge2005]+\kappa_r t+u_{rt} , \tag{9}
$$

where $\alpha_r$ are region effects; $\gamma_t$ are year effects that absorb everything national (policy, prices, weather); $\mu_r$ absorb the CSO classification break; and $\kappa_r t$ are region-specific trends, included in a second specification. Exposure is the region's dairy share of all cows in 2010–2014, and β is scaled per 10 percentage points. Outcomes are log dairy cows, log livestock units and log imputed livestock emissions.

*Inference with five clusters.* Conventional cluster-robust errors are unreliable with five clusters (Cameron et al., 2008). **Randomisation inference** reassigns the five exposure values over regions in all 5! = 120 permutations (Fisher, 1935; Young, 2019):

$$
p_{RI}=\frac{1}{120}\sum_{\pi\in S_5}\mathbb 1\big(|\hat\beta_\pi|\ge|\hat\beta|\big).
$$

The **wild cluster bootstrap** imposes β = 0 and flips residuals by region with Webb's six-point weights, $y^*_{rt}=\hat y^{(0)}_{rt}+\hat u^{(0)}_{rt}\,w_r$ with $w_r\in\{\pm\sqrt{1.5},\pm1,\pm\sqrt{0.5}\}$ (Webb, 2023; B = 999).

*Placebo and event study.* A placebo dates "abolition" to 2010 using pre-2015 data only. A significant placebo signals differential pre-trends (Rambachan & Roth, 2023). The event study is

$$
y_{rt}=\alpha_r+\gamma_t+\sum_{k\neq2014}\beta_k\,\frac{\text{Exp}_r-\overline{\text{Exp}}}{0.10}\,\mathbb 1[t=k]+u_{rt},\qquad 2005\le t\le2024 .
$$

### 5.10 Decomposition–regression link

To connect the accounting to the policy, the annual LMDI effects are regressed on changes in the indices:

$$
\Delta E^{k}_t=c+\sum_{j=0}^{1}\pi^{k}_{j}\Delta P_{t-j}+\sum_{j=0}^{1}\rho^{k}_{j}\Delta M_{t-j}+\psi'\Delta X_t+\omega\,d_{2005}+\nu_t , \tag{10}
$$

for $k$ ∈ {activity, dairy-herd activity, intensity}. The framework predicts $\sum\pi>0$ for activity and $\sum\rho<0$ for intensity. Estimation uses Newey–West errors over 1997–2023 (n = 27), and results are reported per 0.1 index units.

### 5.11 What the 2030 ceiling implies

$$
E^{*}_{2030}=0.75\,E_{2018},\qquad I_{2030}=\frac{E_{2024}}{LU_{2024}}\,e^{6g},\qquad LU^{*}_{2030}=\frac{E^{*}_{2030}}{I_{2030}} ,
$$

where *g* is the annual log change in emissions per livestock unit. Scenarios use the 2012–2024 Theil–Sen trend, or annual falls of 1%, 2% and 3%. The statutory ceiling also covers agricultural fuel, so applying it to CRF3 is an approximation.

### 5.12 Supplement: warming-equivalent methane (GWP*)

$$
E^{*}_t=4.53\,E^{CH_4}_t-4.25\,E^{CH_4}_{t-20}
$$

(Smith, Cain & Allen, 2021). GWP* is reported only as a supplementary perspective. The outcome throughout is GWP100.

### 5.13 Reproducibility and verification

A single notebook (`ireland_agri_ghg_analysis.ipynb`) runs everything, from raw files to every table and figure, with a fixed seed (20261019). A full run takes about five minutes. An independent script re-derives every stage. All 30 verification checks pass (Appendix D), including re-hashing 53 loaded files, exact CRF3 identities, chain-link fit, an exact LMDI residual, an independent OLS reproduction of θ_M and θ_P, and the 2030 target arithmetic.

---

## 6. Results

### 6.1 Hypothesis scorecard

**Table 8. Verdicts on the pre-specified hypotheses**

| Hypothesis | Statement | Verdict | Evidence |
|---|---|---|---|
| H1 | Breaks at 2010 or 2015 | ✕ Not supported | 3 breaks (2000, 2012, 2020); none within ±1 yr of a policy date |
| H2 | Intensity offset < 1 after 2015 | ✓ Supported | IO = 0.32 (0.21–0.33 across EF ratios) |
| H3a | Mitigation lowers emissions (θ_M < 0) | ✕ Not supported | θ_M = +0.47, bootstrap p = 0.985 |
| H3b | Pressure raises emissions (θ_P > 0) | ✓ Supported | θ_P = +0.69, bootstrap p = 0.032 |
| H3c | Offset ratio ≥ 0.5 | ○ Undefined | Mitigation effect is not negative, so OR cannot be computed |
| H4a | Mandatory instruments strongest | ✕ Not supported | All M sub-indices positive, p > 0.8 |
| H4b | Exposed regions expanded more after 2015 | ✕ Not supported | Significant placebo: divergence began before 2015 |

**Headline.** Expansion left a footprint, and mitigation left too little to offset it. A sustained 0.1-unit rise in production pressure raised long-run emissions by about 7%, adding 12.5 Mt CO₂e over 2000–2024. The mostly voluntary, intensity-oriented mitigation portfolio shows no detectable effect on total emissions.

### 6.2 The policy indices

The mitigation index rose from 0.07 in 2000 to 0.64 in 2024. The pressure index rose from 0.24 to 0.34, and the net signal moved from −0.17 to +0.30. P was high until 2004, when coupled headage premia were in force, collapsed to zero with decoupling in 2005, and was then rebuilt through the derogation, the quota increases and Food Harvest 2020. The largest one-year rise in P (+0.175) occurred in 2010, when Food Harvest 2020 was added to the quota increments. P peaked at 0.45 in 2015–2020. M rose in two steps: with the Nitrates Action Programme in 2006–07 (0.07 → 0.45), and with GLAS and the beef schemes in 2015–16 (0.47 → 0.62). M reached its maximum of 0.68 in 2020.

Because both indices rose between 2005 and 2020, the net signal grew far less than mitigation effort. S was 0.05 in 2010 and only 0.17 in 2016, even though M had risen to 0.62 by then. This is policy incoherence made measurable. By instrument type, the mandatory sub-index dominates M by 2024 (0.44 of 0.64), followed by incentive (0.12, down from a 2020 peak of 0.25) and voluntary (0.08).

### 6.3 RQ1: Trends and structural breaks

Over the full period there is no monotonic trend. The Theil–Sen slope is −0.06% per year (Mann–Kendall z = −0.60, p = 0.55; Hamed–Rao-corrected z = −0.34, p = 0.73). Sub-period trends are strongly significant and opposite in sign (Table 9).

**Table 9. Mann–Kendall trend tests**

| Test | S | z | p | Sen slope (%/yr) |
|---|---|---|---|---|
| Mann–Kendall (original), 1990–2024 | −43 | −0.60 | 0.551 | −0.06 |
| Mann–Kendall (Hamed–Rao), 1990–2024 | −43 | −0.34 | 0.731 | −0.06 |
| Hamed–Rao, 1990–1998 | 36 | 3.65 | < 0.001 | +1.22 |
| Hamed–Rao, 1998–2011 | −87 | −4.71 | < 0.001 | −1.43 |
| Hamed–Rao, 2011–2018 | 28 | 3.34 | < 0.001 | +2.25 |
| Hamed–Rao, 2018–2024 | −7 | −0.90 | 0.368 | −0.82 |

A single trend is firmly rejected (UDmax = 112.4, bootstrap p = 0.013). BIC selects three breaks (Table 10).

**Table 10. Bai–Perron break selection**

| m | SSR | BIC | F(m vs 0) | Break years |
|---|---|---|---|---|
| 0 | 0.0970 | −199.0 | – | none |
| 1 | 0.0393 | −220.0 | 22.8 | 2006 |
| 2 | 0.0149 | −243.2 | 39.9 | 2000, 2013 |
| **3** | **0.0037** | **−281.0** | **112.4** | **2000, 2012, 2020** |
| 4 | 0.0033 | −274.2 | 87.6 | 2000, 2005, 2012, 2020 |

**Table 11. Emission regimes**

| Regime | Trend (% per year) | Break-date 90% interval |
|---|---|---|
| 1990–1999 | +1.06 | – |
| 2000–2011 | −1.25 | 2000–2000 |
| 2012–2019 | +2.00 | 2010–2012 |
| 2020–2024 | −1.86 | 2019–2020 |

Emissions rose 1.1% a year to 1999, fell 1.25% a year in 2000–2011, rose 2.0% a year in 2012–2019 and fell 1.9% a year from 2020. **None of the break dates lies within a year of 2010 or 2015, so H1 is not supported.** The 2012 upturn starts two years after Food Harvest 2020 and three years before quota abolition. This timing is consistent with expansion that anticipated abolition during the 2009–2014 quota increases. Known-date Chow tests reject stability at both 2010 (F = 16.8, p < 0.001) and 2015 (F = 20.0, p < 0.001). With three breaks in the series, however, they cannot attribute the change to either date.

### 6.4 RQ2: What moved emissions? LMDI decomposition

**Table 12. LMDI factor effects by policy phase (kt CO₂e, cumulative within phase)**

| Phase | Years | Activity | Productivity | Intensity | Other | Net change | Intensity offset |
|---|---|---|---|---|---|---|---|
| P1 Coupled support | 1992–2004 | −633 | +406 | −105 | −34 | −367 | – |
| P2 Decoupling and derogation | 2004–2009 | −1,204 | −45 | −380 | −22 | −1,651 | – |
| P3 Food Harvest and quota increases | 2009–2014 | +511 | +184 | +175 | +93 | +964 | −0.25 |
| P4 Post-quota expansion | 2014–2021 | +2,147 | +840 | −963 | +319 | +2,344 | **0.32** |
| P5 Sectoral ceiling | 2021–2023 | −549 | −357 | −297 | −132 | −1,334 | – |

*Notes:* IO is defined only when activity + productivity > 0. P2 includes the 2004–05 classification break (dairy activity −340 kt, partly offset by +191 kt productivity). P5 ends in 2023.

After quota abolition, scale and yield growth (+2,988 kt) outran intensity gains (−963 kt), giving **IO = 0.32**. Only about a third of the growth was cancelled. Dairy-herd growth alone added 1.32 Mt CO₂e in 2014–2021. The result is robust to the dairy/non-dairy emission-factor ratio (Table 13): IO stays between 0.21 and 0.33, and the dairy-herd effect between 1.06 and 1.35 Mt. **H2 is supported.**

**Table 13. Sensitivity of P4 to the dairy/non-dairy emission-factor ratio**

| EF ratio | P4 dairy-herd effect (kt) | P4 intensity offset |
|---|---|---|
| 1.8 | 1,064 | 0.21 |
| 2.2 | 1,216 | 0.28 |
| 2.6 | 1,350 | 0.33 |

Two further patterns stand out. First, in 2009–2014 (P3) intensity *rose* (+175 kt) rather than fell, so the intensity offset was negative. Second, in the phases where emissions fell (1992–2009 and 2021–2023), they fell mainly because herds and fertiliser use shrank (activity effects of −633, −1,204 and −549 kt), not because intensity improved.

### 6.5 RQ3: The policy-mix model

**Model selection and fit.** AICc selects ARDL(1, 0, 2) (AICc = −135.5). The next-best candidate is ARDL(1, 0, 0) with AICc = −134.8 (Appendix C). The model is estimated on 1997–2024 (n = 28).

**Table 14. ARDL(1,0,2) short-run coefficients (dependent variable ln CRF3)**

| Term | Coefficient | HAC s.e. | HAC p |
|---|---|---|---|
| Constant α | 2.4898 | 0.5037 | < 0.001 |
| Trend τ | −0.0036 | 0.0014 | 0.008 |
| ln E(t−1), φ | 0.7441 | 0.0544 | < 0.001 |
| M(t), β₀ | 0.1190 | 0.0431 | 0.006 |
| P(t), γ₀ | 0.0178 | 0.0426 | 0.676 |
| P(t−1), γ₁ | 0.0211 | 0.0737 | 0.775 |
| P(t−2), γ₂ | 0.1389 | 0.0583 | 0.017 |
| ln real milk price | 0.0394 | 0.0217 | 0.070 |
| ln real fertiliser price | −0.0364 | 0.0086 | < 0.001 |

With $\hat\phi$ = 0.744 and $\sum\hat\gamma_j$ = 0.178, the long-run pressure multiplier is $\hat\theta_P$ = 0.178 / (1 − 0.744) = **0.695**, and the mitigation multiplier is $\hat\theta_M$ = 0.119 / (1 − 0.744) = **0.465**.

**Table 15. Long-run multipliers**

| Index | θ | SE (delta, HAC) | HAC p (one-sided) | Bootstrap p (one-sided) | % per +0.1 | SD of index | % per 1 SD |
|---|---|---|---|---|---|---|---|
| P | 0.695 | 0.153 | < 0.001 | **0.032** | +7.2 | 0.127 | +9.2 |
| M | 0.465 | 0.175 | 0.996 | **0.985** | +4.8 | 0.236 | +11.6 |

*Notes:* One-sided tests are θ_P > 0 and θ_M < 0. Ninety-percent unrestricted-bootstrap intervals exclude zero for θ_P. For θ_M they lie entirely above zero.

**Diagnostics.** Every diagnostic passes at the 10% level (Table 16). The bounds statistic F = 5.23 exceeds the I(1) bound at 10% (4.06) and 5% (4.57), indicating a level relationship. At 1% the result is inconclusive (I(0) 4.40, I(1) 5.72). Unit-root tests show mixed integration orders: P is stationary in levels (ADF p = 0.001), M appears I(1) (ADF p = 0.26 in levels, < 0.001 in differences), and ln CRF3 is borderline in levels (ADF p = 0.10, KPSS p = 0.02). This mix justifies the ARDL bounds framework (Appendix E). The hypothesis that the two indices have equal and opposite per-unit effects, $\sum\beta+\sum\gamma=0$, is rejected (F = 28.1, p < 0.001). In a model with the net signal S alone, θ_S = −0.37 (p = 0.11).

**Table 16. Residual diagnostics**

| Diagnostic | Statistic | p-value | At 10% |
|---|---|---|---|
| Breusch–Godfrey (2 lags) | 2.40 | 0.121 | pass |
| Jarque–Bera normality | 0.16 | 0.922 | pass |
| Breusch–Pagan heteroskedasticity | 0.47 | 0.863 | pass |
| RESET (squares) | – | 0.915 | pass |
| CUSUM (OLS residuals) | 0.33 | 1.000 | pass |

**Interpretation.** Production pressure raised long-run emissions by 7.2% per sustained 0.1-unit rise (bootstrap p = 0.032), so **H3b is supported**. The mitigation coefficient has the wrong sign (+0.47) and is never negative in the bootstrap, so **H3a is not supported**. A positive association this large is not plausible as a causal effect of mitigation policy. It reflects schemes expanding in the same years as output, in other words reverse timing. All of these are conditional associations, not causal estimates.

### 6.6 RQ3: Counterfactuals and the offset ratio

Holding P at its 2000 level and simulating the fitted ARDL forward, **production pressure raised 2024 emissions by 11.2% (90% CI 6.7–15.7%) and added 12.5 Mt CO₂e cumulatively over 2000–2024.** This dynamic effect is larger than the static long-run value implied by the 2000–2024 change in P (+0.095 → +6.8%). The difference arises because P stood well above its 2024 level during 2010–2020, and the lagged adjustment still carries part of that higher pressure into 2024.

Freezing M at its 2000 level gives a counterfactual *below* observed emissions: the rise in M is associated with 29.1% *higher* 2024 emissions (90% CI 9.6–51.2%). Only 1 of 999 bootstrap draws gives a negative mitigation effect. With no negative mitigation effect, there is nothing for pressure to offset. The offset ratio is undefined and **H3c is not supported**. In short, expansion left a measurable footprint, while the mitigation portfolio left too small a footprint to be offset.

### 6.7 Robustness and statistical power

**Robustness.** θ_P is positive in **all 14** estimable core specifications and significant at 10% in **13** (Appendix B). The single exception adds GNI* and shock-year dummies (θ_P = 0.49, p = 0.13), because GNI* is collinear with quota abolition. All **8 of 8** leave-one-policy-out runs remain significant, with θ_P ranging from 0.49 (omitting Food Harvest 2020) to 1.12 (omitting quota abolition, the most influential single instrument). θ_M is positive in 13 of 14 specifications and is **never** significantly negative. The only negative estimate, from the static first-difference model (θ_M = −0.03), is far from significant (p = 0.30).

**Power.** Nominal 10% HAC tests have true size 0.15 for M and 0.32 for P, which confirms the need for bootstrap inference. With size-adjusted critical values, the minimum detectable effect at 80% power is |θ| ≈ 0.40 for both indices, about 4% per 0.1 index units (Table 17). Mitigation effects larger than |θ| ≈ 0.40 would very likely have been detected. Smaller ones cannot be ruled out.

**Table 17. Size-adjusted power by true effect size**

| True \|θ\| | 0 | 0.1 | 0.2 | 0.3 | 0.5 | 0.75 | 1.0 | 1.5 |
|---|---|---|---|---|---|---|---|---|
| Power, θ_M | 0.10 | 0.23 | 0.44 | 0.66 | 0.94 | 1.00 | 1.00 | 1.00 |
| Power, θ_P | 0.10 | 0.26 | 0.49 | 0.70 | 0.91 | 0.98 | 0.99 | 1.00 |

### 6.8 RQ4a: Mitigation by instrument type

**Table 18. Mitigation sub-index estimates**

| Instrument type | Active years | θ | Bootstrap p (θ < 0) | θ at 3-year lag |
|---|---|---|---|---|
| Mandatory | 19 | +0.20 | 0.966 | +0.09 |
| Incentive | 28 | +0.59 | 0.904 | −1.13 |
| Voluntary | 12 | +0.95 | 0.826 | +0.09 |

No sub-index shows a detectable emission-reducing effect, so **H4a is not supported**. Only the incentive sub-index turns negative at a three-year lag (θ = −1.13). This is an isolated estimate that was not tested formally.

### 6.9 Timing: interrupted time series

**Table 19. Segmented regression at pre-specified dates (controls for prices)**

| Outcome | Event | Level change (%) | p (level) | Slope change (pp/yr) | p (slope) |
|---|---|---|---|---|---|
| CRF3 emissions | 2010 | −2.92 | < 0.001 | **+2.25** | < 0.001 |
| CRF3 emissions | 2015 | +3.24 | < 0.001 | −0.20 | 0.384 |
| CRF3 emissions | 2022† | +8.45 | 0.003 | −6.40 | < 0.001 |
| Dairy cows | 2010 | −2.53 | 0.002 | **+4.17** | < 0.001 |
| Dairy cows | 2015 | +5.96 | 0.018 | +0.32 | 0.297 |
| Dairy cows | 2022† | −4.69 | 0.195 | −1.60 | 0.224 |

†Descriptive only (three post-event years).

**The turn came in 2010, not 2015.** Controlling for prices, the emission trend steepened by 2.2 percentage points a year after 2010 (p < 0.001), and the dairy-herd trend by 4.2 points. Neither trend changed significantly at 2015 (emissions −0.2, p = 0.38), although both show a level shift in that year. Expansion began under the quota increases and Food Harvest 2020 and continued at the same pace after abolition.

### 6.10 RQ4b: Regional difference-in-differences

**Table 20. Continuous-exposure DiD, post-2015 effect per +10 pp pre-2015 dairy exposure**

| Outcome | Specification | % per +10 pp | p (RI) | p (WCB) | Placebo 2010 (%) | Placebo p (RI) | n |
|---|---|---|---|---|---|---|---|
| log dairy cows | two-way FE | −0.50 | 0.842 | 0.866 | +2.91 | 0.067 | 170 |
| log dairy cows | TWFE + region trends | −0.69 | 0.567 | 0.663 | +2.77 | 0.042 | 170 |
| log livestock units | two-way FE | +1.17 | 0.142 | 0.215 | +1.32 | 0.008 | 170 |
| log livestock units | TWFE + region trends | +0.72 | 0.133 | 0.039 | +1.24 | 0.050 | 170 |
| log imputed livestock emissions | two-way FE | +2.11 | 0.108 | 0.171 | +1.63 | 0.017 | 165 |
| log imputed livestock emissions | TWFE + region trends | +1.28 | 0.075 | 0.058 | +1.51 | 0.008 | 165 |

In the main specification, imputed livestock emissions rose 2.1% more per 10 pp of exposure after 2015 (p_RI = 0.11, p_WCB = 0.17). But the event-study gap opens steadily from 2005. The placebo dated to 2010 (+1.6%, p_RI = 0.017) is almost as large as the main estimate and is significant. More exposed regions were already diverging before abolition, so parallel trends fail and **H4b is not supported**. The region-trend specification for emissions is nominally significant (+1.3%, p_RI = 0.075, p_WCB = 0.058). Its placebo is significant too (p_RI = 0.008), however, so it cannot be read as an abolition effect either. The dairy herd itself grew no faster in percentage terms in more exposed regions (−0.5% per 10 pp; p = 0.84). Post-quota growth was national and came partly from low-dairy regions.

### 6.11 Mechanism: linking the decomposition to policy

**Table 21. LMDI effects regressed on changes in P and M (sum of lag 0 and lag 1, per +0.1 index units)**

| LMDI outcome | Policy | kt per +0.1 | SE (per 0.1) | p (two-sided) |
|---|---|---|---|---|
| Activity effect | ΔP | −218.4 | 147.3 | 0.154 |
| Activity effect | ΔM | +53.8 | 191.9 | 0.782 |
| Dairy-herd activity effect | ΔP | −21.9 | 42.3 | 0.611 |
| Dairy-herd activity effect | ΔM | +84.9 | 64.9 | 0.206 |
| Intensity effect | ΔP | **+111.2** | 47.5 | **0.030** |
| Intensity effect | ΔM | +61.6 | 43.9 | 0.176 |

*Notes:* Newey–West errors, 1997–2023, n = 27.

The hypothesised division of labour is **not confirmed**. ΔP is not associated with the activity effect (−218 kt per 0.1; p = 0.15). It is, however, associated with the intensity effect (+111 kt per 0.1; p = 0.03): years of rising pressure were years in which emissions per head and per litre rose, which is consistent with intensification. ΔM is associated with neither.

### 6.12 The 2030 sectoral ceiling

The 2030 target is 0.75 × 20,728 kt (2018) = **15,546 kt CO₂e** (15.5 Mt). CRF3 was 19,631 kt in 2024, 5.3% below 2018. Emissions per livestock unit rose by 0.37% a year over 2012–2024.

**Table 22. Livestock units compatible with the 2030 ceiling**

| Scenario for emissions per LU, 2024–2030 | Required LU in 2030 (thousand) | Change vs 2024 |
|---|---|---|
| 2012–2024 trend continues (+0.37%/yr) | 4,403 | **−22.6%** |
| Intensity falls 1% a year | 4,782 | −15.9% |
| Intensity falls 2% a year | 5,083 | −10.6% |
| Intensity falls 3% a year | 5,405 | −4.9% |

*Note:* Livestock units in 2024 = 5,686 thousand.

If the recent intensity trend continues, livestock units must fall by about 23% by 2030. Even with intensity falling 1, 2 or 3% a year, they must still fall by 16%, 11% or 5%. A 3% annual fall would be almost three times the fastest five-year rate of intensity decline since 1992 (about 1.1% a year).

### 6.13 Supplement: GWP*

In 2024 CRF3 methane was 14.6 Mt CO₂e under GWP100 but +5.5 Mt CO₂-we under GWP*, up from +1.7 Mt CO₂-we in 2015. GWP* reflects the change in methane's warming contribution rather than its level; negative values mean methane was lower than 20 years earlier. The metric changes the level of the methane series, but not the conclusions about which policies moved emissions.

---

## 7. Discussion

### 7.1 Expansion with little to offset

Three independent pieces of evidence point the same way. First, scale and yield growth after 2014 outran intensity gains by more than three to one (IO = 0.32). Second, the policy-mix model attributes an 11.2% rise in 2024 emissions to production pressure, a result that survives every pre-specified robustness variant in sign and nearly all in significance. Third, the same model finds no emission-reducing effect of mitigation. A rival account would need to explain all three. The evidence therefore favours a refined version of Explanation B. Production-oriented policy measurably raised emissions. But the mitigation portfolio did not produce a detectable reduction that expansion then cancelled. Expansion had little mitigation to offset. Read this way, Explanation A, that mitigation was weak, also holds, as a statement about the *portfolio's* effect on totals.

### 7.2 Timing: 2010, not 2015

Three results agree that the trend changed in 2010–2012: the Bai–Perron break in 2012 (90% interval 2010–2012), the interrupted time-series slope change in 2010 and not 2015, and the regional pre-trends from 2005 onward. Expansion began under the quota increases and Food Harvest 2020, and abolition continued it rather than starting it. Analyses that treat 2015 as the single turning point understate the "soft-landing" years in which the sector positioned itself for a quota-free regime. This qualification complements the farm-level evidence of Läpple et al. (2022) without contradicting it.

### 7.3 Why mitigation did not register

Most mitigation instruments were voluntary or incentive-based schemes that acted on intensity. The main binding instrument, the Nitrates Action Programme, was designed for water quality. An intensity-only portfolio can lower emissions per litre while totals rise, and this is exactly what the decomposition shows for 2014–2021. The positive association between M and emissions is best read as reverse timing: schemes such as GLAS grew in the same years as the herd. The power analysis bounds what the data can say. Long-run mitigation effects with |θ| above about 0.40 (roughly 4% per 0.1 index units) would very likely have been detected. Smaller beneficial effects cannot be excluded. The mechanism regression adds a further caution: rising pressure coincided with rising *intensity*, consistent with intensification at the margin (higher stocking rates and more nitrogen per hectare), which would work directly against an intensity-based mitigation strategy.

### 7.4 Relation to stakeholder-identified barriers

Of the five barriers identified by Augustenborg et al. (2026), **policy incoherence** is supported quantitatively. P and M rose together over 2005–2020, the net signal grew far more slowly than mitigation effort, and P has a detectable effect on emissions. **Competing political priorities** are consistent with the regime change near Food Harvest 2020, a growth strategy adopted alongside mitigation commitments. **Capacity, financial and planning constraints** cannot be separated with these data. In the terms of Marsh & McConnell (2010), the mitigation portfolio shows some *process* success, in that instruments were implemented and coverage grew, but no detectable *programme* success on total emissions. Its *political* success was limited by the parallel growth agenda.

### 7.5 Policy implications

The findings carry four implications. They are offered as interpretations of the evidence, not as estimated policy effects.

1. **Coherence before additionality.** Because pressure has a detectable effect and the mitigation portfolio does not, adding further intensity-oriented instruments is unlikely, on its own, to close the gap while expansion incentives remain. Assessing growth instruments (derogations, capital grants for capacity, volume targets) for their emission consequences would address the measured source of the problem.
2. **Targets on totals, not only intensity.** An intensity offset of 0.32 means efficiency gains cancelled about a third of scale growth. Policy framed around emissions per litre can succeed on its own terms while total emissions rise.
3. **The arithmetic of the 2030 ceiling.** On recent trends, compliance implies roughly 16–23% fewer livestock units by 2030 unless intensity falls far faster than ever observed. That implication should be stated explicitly in sectoral planning.
4. **Measuring the net signal.** The common I × C × B scale lets governments track whether new instruments raise mitigation intensity faster than concurrent sectoral policy raises pressure. The index is transferable to other land-based sectors that face growth and decarbonisation mandates at once.

---

## 8. Limitations

- **Provisional policy coding.** The mitigation index M uses the authors' provisional coding under the INPACT scoring rule and is to be replaced by the INPACT export. Eligibility shares for the nitrates derogation (0.30) and TAMS II (0.15) are provisional pending DAFM statistics. The second coder for P is a placeholder, so the reported kappa values do not yet measure reliability.
- **Short national series.** With n = 28 in the ARDL, inference rests on the bootstrap, and power is limited (MDE ≈ 0.40). Results are conditional associations, not causal estimates. The positive M coefficient shows the limits of a time-series design when instruments are adopted alongside output growth.
- **No untreated comparator.** Quota abolition and CAP reform applied EU-wide. The regional design relies on within-Ireland exposure, and its parallel-trends assumption fails.
- **Five clusters.** Regional inference uses randomisation inference and the wild cluster bootstrap, which are appropriate but cannot create information that five units do not contain. Event-study bands are indicative only.
- **Inventory data.** LMDI and regional emissions end in 2023, because the 2024 CRT split is not yet available. Changes in inventory methodology appear as intensity change, and regional emissions are imputed from national implied emission factors.
- **Omitted drivers.** The model has no weather control, and macro shocks enter only in one robustness variant (where GNI* is collinear with quota abolition).
- **Ceiling approximation.** The statutory ceiling includes agricultural fuel, so applying it to CRF3 approximates the true constraint.

---

## 9. Conclusions and Future Research

Three decades of farm climate policy left Irish agricultural emissions almost exactly where they started. This paper puts expansion and mitigation policy on one scale and attributes the flat path with three designs that fail in different ways. Production-oriented policy measurably raised emissions. A sustained 0.1-unit rise in pressure raised long-run emissions by about 7%, and pressure added 11.2% to 2024 emissions and 12.5 Mt CO₂e over 2000–2024. The mostly voluntary, intensity-oriented mitigation portfolio shows no detectable effect on totals, so expansion had little mitigation to offset. The turn came in 2010–2012, under the quota increases and Food Harvest 2020, not at abolition in 2015. After abolition, efficiency gains cancelled only a third of scale growth. On current trends, the 2030 ceiling implies 16–23% fewer livestock units unless intensity falls far faster than it ever has.

**Next steps: data.**
- Replace the provisional mitigation coding with the INPACT export for M.
- Obtain independent, blind second coding for P.
- Use DAFM statistics for derogation and TAMS II eligibility shares.
- Use the CRT 2026 submission to extend the LMDI and regional emissions to 2024.

**Next steps: design.**
- Build a county-level panel from the Census of Agriculture and DAFM derogation statistics for a continuous-treatment design (Callaway et al., 2024).
- Transfer the common-scale approach to other jurisdictions where land-based sectors face growth and decarbonisation mandates at the same time.

---

## Data and Code Availability

All numbers in this paper come from a full re-run of `ireland_agri_ghg_analysis.ipynb` (seed 20261019, run 2026-10-21) and reproduce the manuscript (Revision 4). Data come from the EPA, Ireland's CRT 2025 submission to the UNFCCC, the CSO and Eurostat. The annual panel (1990–2024), the result tables and an interactive results platform (problem, questions, dataset explorer, methods with live calculators, results and conclusions) are available from the authors. The platform reads every number from the exported `results.json` and recomputes nothing except light arithmetic for its interactive calculators.

---

## References

Ang, B. W. (2015). LMDI decomposition approach: A guide for implementation. *Energy Policy*, 86, 233–238.

Ang, B. W., & Liu, F. L. (2001). A new energy decomposition method: Perfect in decomposition and consistent in aggregation. *Energy*, 26(6), 537–548.

Augustenborg, C. A., Lentz, P., & Pender, A. (2026). Barriers to environmental policy implementation: Stakeholder perceptions in the context of Ireland. *Journal of Environmental Policy & Planning*, 28(3), 531–553.

Bai, J., & Perron, P. (2003). Computation and analysis of multiple structural change models. *Journal of Applied Econometrics*, 18(1), 1–22.

Balaine, L., Läpple, D., Buckley, C., & Dillon, E. (2022). Reconciling socio-economic and environmental sustainability in agri-food development. *EuroChoices*, 21(2), 52–57.

Bernal, J. L., Cummins, S., & Gasparrini, A. (2017). Interrupted time series regression for the evaluation of public health interventions: A tutorial. *International Journal of Epidemiology*, 46(1), 348–355.

Bloom, H. S. (1995). Minimum detectable effects: A simple way to report the statistical power of experimental designs. *Evaluation Review*, 19(5), 547–556.

Callaway, B., Goodman-Bacon, A., & Sant'Anna, P. H. C. (2024). Difference-in-differences with a continuous treatment. NBER Working Paper 32117.

Cameron, A. C., Gelbach, J. B., & Miller, D. L. (2008). Bootstrap-based improvements for inference with clustered errors. *Review of Economics and Statistics*, 90(3), 414–427.

Card, D. (1992). Using regional variation in wages to measure the effects of the federal minimum wage. *ILR Review*, 46(1), 22–37.

Cohen, J. (1968). Weighted kappa: Nominal scale agreement with provision for scaled disagreement or partial credit. *Psychological Bulletin*, 70(4), 213–220.

Davidson, R., & MacKinnon, J. G. (2000). Bootstrap tests: How many bootstraps? *Econometric Reviews*, 19(1), 55–68.

Diebold, F. X., & Chen, C. (1996). Testing structural stability with endogenous breakpoint: A size comparison of analytic and bootstrap procedures. *Journal of Econometrics*, 70(1), 221–241.

Donnellan, T., Hanrahan, K., Breen, J. P., & Gillespie, P. (2013). Climate change and agricultural policy coherence: Agricultural growth and GHG emissions in Ireland. Agricultural Economics Society Conference, Warwick.

EPA (2026). *Ireland's Provisional Greenhouse Gas Emissions 1990–2025*. Environmental Protection Agency, Wexford.

Eskander, S. M. S. U., & Fankhauser, S. (2020). Reduction in greenhouse gas emissions from national climate legislation. *Nature Climate Change*, 10, 750–756.

Eurostat (2016). *Handbook on Prices and Volume Measures in National Accounts*. Publications Office of the European Union, Luxembourg.

Fisher, R. A. (1935). *The Design of Experiments*. Oliver & Boyd, Edinburgh.

Gelman, A., & Carlin, J. (2014). Beyond power calculations: Assessing Type S (sign) and Type M (magnitude) errors. *Perspectives on Psychological Science*, 9(6), 641–651.

Goldsmith-Pinkham, P., Sorkin, I., & Swift, H. (2020). Bartik instruments: What, when, why, and how. *American Economic Review*, 110(8), 2586–2624.

Greening, L. A., Greene, D. L., & Difiglio, C. (2000). Energy efficiency and consumption — the rebound effect — a survey. *Energy Policy*, 28(6–7), 389–401.

Hall, P., Horowitz, J. L., & Jing, B.-Y. (1995). On blocking rules for the bootstrap with dependent data. *Biometrika*, 82(3), 561–574.

Hamed, K. H., & Rao, A. R. (1998). A modified Mann–Kendall trend test for autocorrelated data. *Journal of Hydrology*, 204(1–4), 182–196.

Henn, D., et al. (2023). [Herd composition and implied emission factors — full reference to be completed by the authors.]

Howlett, M., & Rayner, J. (2013). Patching vs packaging in policy formulation: Assessing policy portfolio design. *Politics and Governance*, 1(2), 170–182.

Kiefer, N. M., & Vogelsang, T. J. (2005). A new asymptotic theory for heteroskedasticity-autocorrelation robust tests. *Econometric Theory*, 21(6), 1130–1164.

Läpple, D., Carter, C. A., & Buckley, C. (2022). EU milk quota abolition, dairy expansion, and greenhouse gas emissions. *Agricultural Economics*, 53(1), 125–142.

Lawlor, D. A., Tilling, K., & Davey Smith, G. (2016). Triangulation in aetiological epidemiology. *International Journal of Epidemiology*, 45(6), 1866–1886.

Li, H., & Maddala, G. S. (1996). Bootstrapping time series models. *Econometric Reviews*, 15(2), 115–158.

Marsh, D., & McConnell, A. (2010). Towards a framework for establishing policy success. *Public Administration*, 88(2), 564–583.

Munafò, M. R., & Davey Smith, G. (2018). Robust research needs many lines of evidence. *Nature*, 553, 399–401.

Myhre, G., Shindell, D., Bréon, F.-M., et al. (2013). Anthropogenic and natural radiative forcing. In *Climate Change 2013: The Physical Science Basis. Contribution of Working Group I to the Fifth Assessment Report of the IPCC* (pp. 659–740). Cambridge University Press.

Newey, W. K., & West, K. D. (1987). A simple, positive semi-definite, heteroskedasticity and autocorrelation consistent covariance matrix. *Econometrica*, 55(3), 703–708.

Nilsson, M., Zamparutti, T., Petersen, J. E., Nykvist, B., Rudberg, P., & McGuinn, J. (2012). Understanding policy coherence: Analytical framework and examples of sector–environment policy interactions in the EU. *Environmental Policy and Governance*, 22(6), 395–423.

OECD, European Commission & Joint Research Centre (2008). *Handbook on Constructing Composite Indicators: Methodology and User Guide*. OECD Publishing, Paris.

Pesaran, M. H., Shin, Y., & Smith, R. J. (2001). Bounds testing approaches to the analysis of level relationships. *Journal of Applied Econometrics*, 16(3), 289–326.

Rambachan, A., & Roth, J. (2023). A more credible approach to parallel trends. *Review of Economic Studies*, 90(5), 2555–2591.

Rogge, K. S., & Reichardt, K. (2016). Policy mixes for sustainability transitions: An extended concept and framework for analysis. *Research Policy*, 45(8), 1620–1635.

Smith, M. A., Cain, M., & Allen, M. R. (2021). Further improvement of warming-equivalent emissions calculation. *npj Climate and Atmospheric Science*, 4, 19.

Stechemesser, A., Koch, N., Mark, E., et al. (2024). Climate policies that achieved major emission reductions: Global evidence from two decades. *Science*, 385(6711), 884–892.

Stock, J. H., & Watson, M. W. (2020). *Introduction to Econometrics* (4th ed.). Pearson.

Torney, D., & O'Gorman, R. (2019). A laggard in good times and bad? The limited impact of EU membership on Ireland's climate change and environmental policy. *Irish Political Studies*, 34(4), 575–594.

Webb, M. D. (2023). Reworking wild bootstrap-based inference for clustered errors. *Canadian Journal of Economics*, 56(3), 839–858.

Young, A. (2019). Channeling Fisher: Randomization tests and the statistical insignificance of seemingly significant experimental results. *Quarterly Journal of Economics*, 134(2), 557–598.

Yue, S., Pilon, P., Phinney, B., & Cavadias, G. (2002). The influence of autocorrelation on the ability to detect trend in hydrological series. *Hydrological Processes*, 16(9), 1807–1829.

---

## Appendix A. Acronyms and symbols

| Acronym | Meaning | Note |
|---|---|---|
| ACRES | Agri-Climate Rural Environment Scheme | Agri-environment scheme from 2023 (M11) |
| ADF | Augmented Dickey–Fuller | Unit-root test (null: non-stationary) |
| AEOS | Agri-Environment Options Scheme | Agri-environment scheme 2010–2014 (M04) |
| AIC / AICc | (Corrected) Akaike Information Criterion | Lag selection; AICc corrects for small samples |
| AR(1) | First-order autoregressive process | Error structure under the UDmax null |
| AR5 | IPCC Fifth Assessment Report | Source of GWP100 values |
| ARDL | Autoregressive distributed lag | Policy-mix time-series model |
| BDGP | Beef Data and Genomics Programme | M08 |
| BEEP-S | Beef Environmental Efficiency Programme – Sucklers | M09 |
| BIC | Bayesian Information Criterion | Selects the number of breaks |
| CAP | Common Agricultural Policy | EU farm policy; 2005 decoupling |
| CH₄ / N₂O / CO₂e | Methane / nitrous oxide / CO₂ equivalent | – |
| CI | Confidence interval | 90% unless stated |
| CPI | Consumer price index | Deflator |
| CRF / CRF3 | Common Reporting Format / sector 3 (agriculture) | Outcome boundary |
| CRT | Common Reporting Tables | UNFCCC inventory submission format |
| CSO | Central Statistics Office (Ireland) | Livestock, milk, prices, CPI, GNI* |
| CUSUM | Cumulative sum of recursive residuals | Parameter stability test |
| DAFM | Department of Agriculture, Food and the Marine | Future source of eligibility shares |
| DiD | Difference-in-differences | Regional design |
| EF | Emission factor | e.g. kg CH₄ per dairy cow per year |
| EPA | Environmental Protection Agency (Ireland) | Inventory compiler |
| GHG | Greenhouse gas | – |
| GISCO | Geographic Information System of the Commission | Regional boundaries |
| GLAS | Green Low-Carbon Agri-Environment Scheme | M07 |
| GNI* | Modified gross national income | Robustness control |
| GWP / GWP100 / GWP* | Global warming potential (100-yr) / warming-equivalent metric | – |
| HAC | Heteroskedasticity and autocorrelation consistent | Newey–West covariance |
| I × C × B | Implementation × coverage × bindingness | Policy score |
| IO | Intensity offset | Share of scale growth cancelled by intensity |
| IPCC | Intergovernmental Panel on Climate Change | – |
| ITS | Interrupted time series | Segmented regression |
| KPSS | Kwiatkowski–Phillips–Schmidt–Shin | Stationarity test |
| LESS | Low Emission Slurry Spreading | Part of M10 |
| LMDI | Logarithmic Mean Divisia Index | Exact decomposition |
| LU / LSU | Livestock unit / Eurostat LSU coefficients | – |
| M / P / S | Mitigation index / production-pressure index / net signal | – |
| MDE | Minimum detectable effect | 80% power |
| NAP | Nitrates Action Programme | M02, M10 |
| NO / NE / NA | Not occurring / not estimated / not applicable | Treated as missing |
| NUTS | Nomenclature of Territorial Units for Statistics | – |
| OLS | Ordinary least squares | – |
| OR | Offset ratio | Defined only if mitigation effect < 0 |
| REPS | Rural Environment Protection Scheme | M01 |
| RESET | Regression Equation Specification Error Test | Functional form |
| RI | Randomisation inference | Five-region DiD |
| SCEP | Suckler Carbon Efficiency Programme | M12 |
| SDAS | Sustainable Dairy Assurance Scheme | M06 |
| SE / SD | Standard error / standard deviation | – |
| SHA-256 | Secure Hash Algorithm, 256-bit | File provenance |
| S.I. | Statutory Instrument | Irish secondary legislation |
| SSR | Sum of squared residuals | – |
| TAMS II | Targeted Agricultural Modernisation Scheme II | P08 |
| TWFE | Two-way fixed effects | – |
| UDmax | Unweighted double maximum | Test for any break |
| UNFCCC | UN Framework Convention on Climate Change | – |
| WCB | Wild cluster bootstrap | Webb weights |

## Appendix B. Full robustness grid

Bootstrap p-values in this table use B = 299, so the baseline p differs slightly from the B = 999 value in the main text.

| Variant | n | θ_M | p (θ_M < 0) | θ_P | p (θ_P > 0) |
|---|---|---|---|---|---|
| Baseline | 28 | 0.465 | 0.987 | 0.695 | 0.040 |
| No deterministic trend | 28 | 0.096 | 0.850 | 0.546 | 0.037 |
| Fixed lags ARDL(1,1,1) | 28 | 0.409 | 0.927 | 0.643 | 0.043 |
| Equal bindingness (B = 1) | 28 | 0.228 | 0.963 | 0.181 | 0.023 |
| Drop Nitrates Action Programme from M | 28 | 0.411 | 0.897 | 0.430 | 0.007 |
| NAP weighted by climate relevance 0.5 | 28 | 0.536 | 0.973 | 0.524 | 0.023 |
| Food Vision 2030 coded as zero pressure | 28 | 0.474 | 0.997 | 0.641 | 0.037 |
| Extended controls (GNI*, 2018, 2022 dummies) | 28 | 0.424 | 0.947 | 0.487 | 0.133 |
| Milk-to-feed price ratio as control | 28 | 0.561 | 0.973 | 0.861 | 0.043 |
| Static model (p = 0) | 28 | 0.175 | 0.933 | 0.305 | 0.003 |
| Pre-ceiling sample (to 2021) | 25 | 0.435 | 0.970 | 0.657 | 0.070 |
| CH₄-only outcome | 28 | 0.708 | 0.970 | 0.962 | 0.073 |
| N₂O-only outcome | 28 | 0.205 | 0.870 | 0.484 | 0.017 |
| First differences (static) | 28 | −0.027 | 0.298 | 0.058 | 0.080 |
| Leave out P01 Coupled livestock premia | 28 | 0.289 | – | 0.882 | 0.033 |
| Leave out P02 Milk quota increases | 28 | 0.265 | – | 0.521 | 0.057 |
| Leave out P03 Nitrates derogation | 28 | 0.461 | – | 0.701 | 0.040 |
| Leave out P04 Food Harvest 2020 | 28 | 0.175 | – | 0.494 | 0.067 |
| Leave out P05 EU milk quota abolition | 28 | 0.943 | – | 1.123 | 0.027 |
| Leave out P06 Food Wise 2025 | 28 | 0.824 | – | 0.982 | 0.050 |
| Leave out P07 Food Vision 2030 | 28 | 0.474 | – | 0.641 | 0.047 |
| Leave out P08 TAMS II | 28 | 0.498 | – | 0.716 | 0.050 |

## Appendix C. ARDL lag-selection grid (common sample 1997–2024, n = 28)

| p | q_M | q_P | Parameters k | AICc |
|---|---|---|---|---|
| **1** | **0** | **2** | **9** | **−135.53** (selected) |
| 1 | 0 | 0 | 7 | −134.80 |
| 1 | 1 | 2 | 10 | −133.19 |
| 1 | 0 | 1 | 8 | −132.91 |
| 1 | 1 | 0 | 8 | −130.85 |
| 1 | 2 | 2 | 11 | −129.26 |
| 1 | 1 | 1 | 9 | −128.50 |
| 1 | 2 | 0 | 9 | −126.45 |
| 1 | 2 | 1 | 10 | −123.59 |
| 0 | 0 | 2 | 8 | −88.46 |
| 0 | 1 | 2 | 9 | −85.66 |
| 0 | 0 | 0 | 6 | −85.38 |
| 0 | 0 | 1 | 7 | −84.98 |
| 0 | 1 | 0 | 7 | −81.78 |
| 0 | 1 | 1 | 8 | −81.14 |
| 0 | 2 | 2 | 10 | −80.94 |
| 0 | 2 | 0 | 8 | −78.09 |
| 0 | 2 | 1 | 9 | −76.97 |

## Appendix D. Independent workflow verification (30 / 30 checks pass)

| Stage | Check | Result |
|---|---|---|
| 1 Load | SHA-256 of every loaded file matches the provenance sheet | 53 files re-hashed; no mismatch |
| 1 Load | Only documented provisional inputs are loaded | only `pressure_codebook_coder2_PROVISIONAL` |
| 2 Livestock | CSO tables cover disjoint years | 1991–2004 / 2005–2014 / 2015–2026 |
| 2 Livestock | Panel dairy cows equal CSO State totals | max difference 0 |
| 2 Livestock | Five constant-boundary units sum to the State | dairy 0.014%, cattle 0.004%, sheep 0.003% |
| 2 Livestock | 1990 livestock left missing | NaN (never imputed) |
| 2 Livestock | LU = 1.0·dairy + Eurostat LSU + 0.1·sheep | LSU per non-dairy head 0.632–0.682 |
| 3 Prices | Chain-link overlaps fit | max deviation 2.88% across 20 links |
| 3 Prices | Linked indices and CPI equal 100 in 2020 | exact |
| 3 Prices | Real price = nominal / CPI × 100 | exact |
| 4 Emissions | CRF3 = Agriculture − 1.A.4.c.ii − 1.A.4.c.iii | 19,760.0 (1990); 19,631.2 (2024) kt CO₂e |
| 4 Emissions | CRF3 = sum of 5 categories (≤ 0.0001%) | gap 0 |
| 4 Emissions | CRF3 = CO₂ + CH₄ + N₂O (≤ 0.0001%) | gap 2 × 10⁻¹⁴ % |
| 5 CRT | 34 workbooks, 1990–2023, no gaps | complete |
| 5 CRT | Panel split equals CRT Table 3 rows | 1990–2023 |
| 5 CRT | 2024 split left missing | NaN (never imputed) |
| 5 CRT | CRT cattle CH₄ vs Eurostat | 1990–2020 ≤ 0.004%; 2021–23 ≤ 0.21% |
| 5 CRT | Table 3.D unit is kg N | kg / 1,000 = Eurostat t N exactly, 2000–05 |
| 5 CRT | Panel mineral N 1990–1999 = CRT | 379,311 t (1990); 442,916 t (1999) |
| 5 CRT | Manure N = CRT rates × CSO head counts; 2024 missing | 2023: 108.4 / 48.1 / 7.52 kg N/head |
| 6 Panel | 35 unique years, 1990–2024 | pass |
| 6 Panel | No weather variable | pass |
| 7 Indices | M and P recomputed independently (I × C × B) | P₂₀₂₄ 0.3362; M₂₀₂₄ 0.6383 |
| 8 LMDI | Annual effects sum exactly to ΔCRF3 | residual 1.9 × 10⁻¹¹ kt |
| 9 ARDL | θ_M, θ_P reproduced by an independent OLS | θ_M 0.4651, θ_P 0.6946, n = 28 |
| 9 ARDL | `key_results.json` = `results.xlsx` | pass |
| 10 Ceiling | 2030 target = 0.75 × CRF3₂₀₁₈ | 15,546.2 kt CO₂e |
| 11 Outputs | 34 sheets; 7 figures in PNG and PDF | pass |
| 11 Outputs | Provisional inputs listed in the JSON | coder-2 placeholder scores (kappa only) |

## Appendix E. Unit-root tests

| Variable | Form | ADF statistic | ADF p | KPSS statistic | KPSS p |
|---|---|---|---|---|---|
| ln CRF3 | level | −3.13 | 0.100 | 0.185 | 0.022 |
| ln CRF3 | first difference | −3.22 | 0.019 | 0.168 | > 0.10 |
| M | level | −2.64 | 0.262 | 0.087 | > 0.10 |
| M | first difference | −4.19 | 0.001 | 0.086 | > 0.10 |
| P | level | −4.61 | 0.001 | 0.106 | > 0.10 |
| P | first difference | −4.90 | < 0.001 | 0.098 | > 0.10 |
| ln real milk price | level | −3.12 | 0.101 | 0.218 | 0.010 |
| ln real milk price | first difference | −6.62 | < 0.001 | 0.346 | > 0.10 |
| ln real fertiliser price | level | −2.96 | 0.143 | 0.064 | > 0.10 |
| ln real fertiliser price | first difference | −5.89 | < 0.001 | 0.500 | 0.042 |
