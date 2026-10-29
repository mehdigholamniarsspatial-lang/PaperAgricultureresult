::: {custom-style="Running Label"}
Working paper · October 2026
:::

::: {custom-style="Paper Title"}
Expansion versus Mitigation: Production-Oriented Policy and Agricultural Greenhouse-Gas Emissions in Ireland, 1990–2024
:::

::: {custom-style="Paper Author"}
Mehdi Gholamnia^1^ [AUTHOR INPUT REQUIRED: names and affiliations of any co-authors]
:::

::: {custom-style="Paper Affiliation"}
^1^ INPACT Project, University of Galway, Ireland
:::

::: {custom-style="Paper Meta"}
**Corresponding author:** Mehdi Gholamnia, [AUTHOR INPUT REQUIRED: institutional e-mail address and ORCID iD]
:::

::: {custom-style="Paper Meta"}
**Manuscript status:** Working paper prepared from the study's interactive results platform. All results come from the analysis run of 29 October 2026 (random seed 20261019), which uses the revised policy codebook of 29 October 2026.
:::

::: {custom-style="Paper Meta"}
**Intended submission:** *Climate Policy*
:::

::: {custom-style="Paper Meta"}
**Word count:** [AUTHOR INPUT REQUIRED: confirm against the target journal's limit after final editing]
:::

PAGEBREAK

# Abstract {.unnumbered}

::: {custom-style="Abstract Text"}
Agriculture produced 37.9% of Ireland's greenhouse-gas (GHG) emissions in 2024. Emissions from IPCC/CRF sector 3 that year (19.63 Mt CO₂e) were within 0.7% of their 1990 level (19.76 Mt CO₂e), after three decades of agri-environment schemes and nitrates regulation and, since 2021, legally binding carbon budgets. This paper asks whether the flat emission path reflects *failed mitigation* or *mitigation offset by policies that expanded output*. We construct a new annual production-pressure index (P) and score it on the same implementation × coverage × eligibility × bindingness scale used for a mitigation index (M); non-binding national growth strategies are tracked separately as a strategy signal (G). This places the two policy sets on one scale for the first time. We then combine three designs whose identifying assumptions fail in different ways: (i) trend, structural-break and exact Logarithmic Mean Divisia Index (LMDI) decomposition analysis; (ii) an autoregressive distributed-lag (ARDL) policy-mix model with restricted moving-block bootstrap inference, dynamic counterfactuals and explicit power analysis; and (iii) a within-Ireland regional difference-in-differences (DiD) design based on pre-2015 dairy exposure. Emissions follow four regimes, with breaks in 2000, 2012 and 2020 (bootstrap UDmax *p* = 0.013), but no break falls within a year of Food Harvest 2020 (2010) or milk-quota abolition (2015). After quota abolition (2014–2021), growth in scale and yield added 2,988 kt CO₂e, whereas declining emission intensity removed only 963 kt. This gives an intensity offset of 0.32 (0.21–0.33 across emission-factor assumptions). In the ARDL model, a sustained 0.1-unit rise in production pressure is associated with 4.7% higher long-run emissions (θ~P~ = 0.46, bootstrap *p* = 0.043), and year-to-year changes in P line up with the activity (scale) component of the decomposition (+748 kt CO₂e per 0.1, *p* = 0.008). Because P in 2024 was close to its 2000 level, its net effect on 2024 emissions is small (+2.2%, 90% CI 1.1–3.2%). The mitigation index shows no emission-reducing effect (θ~M~ = +0.22, *p* = 0.88). The positive pressure coefficient holds in all 17 estimable robustness variants (significant in 14) and in all five leave-one-policy-out runs (significant in four), but the bounds test does not confirm a level relationship, so the long-run multipliers are indicative. The regional design does not support a quota-abolition effect, because regions were already diverging before 2015, and interrupted time-series estimates place the turning point in 2010 rather than 2015. Meeting the 2030 sectoral ceiling (15.5 Mt CO₂e, 25% below 2018) would require roughly 23% fewer livestock units than in 2024 if the recent intensity trend continues, and 5–16% fewer even if intensity fell by 1–3% a year. Production pressure acts on emissions through scale, as hypothesised. The largely voluntary, intensity-oriented mitigation portfolio shows no detectable reduction in total emissions, so there was little mitigation for expansion to offset.

**Keywords:** agricultural emissions; policy coherence; policy mix; production pressure; milk quota abolition; LMDI decomposition; ARDL; block bootstrap; difference-in-differences; Ireland

**JEL classification:** Q15, Q18, Q54, Q58, C22
:::

## Highlights {.unnumbered}

- A new production-pressure index (P) is scored on the same implementation × coverage × eligibility × bindingness scale as a mitigation index (M), so expansion and mitigation policy can be compared directly.
- Irish CRF3 emissions were flat over 1990–2024 (−0.65%) but passed through four distinct regimes, with a sustained upturn from 2012.
- After milk-quota abolition, falling emission intensity cancelled only about one third of the emission growth caused by scale and yield (intensity offset = 0.32).
- A sustained 0.1-unit rise in production pressure is associated with 4.7% higher long-run emissions, acting through herd and nitrogen growth. No emission-reducing effect of the mitigation portfolio can be detected.
- On recent intensity trends, the 2030 sectoral ceiling implies about 23% fewer livestock units than in 2024.

PAGEBREAK

::: {custom-style="TOC Heading"}
Contents
:::

TOCFIELD

PAGEBREAK

# 1. Introduction

## 1.1 Background and motivation

Agriculture is the largest source of greenhouse-gas emissions in Ireland, accounting for 37.9% of the national total in 2024 (Environmental Protection Agency [EPA], 2026). This share is exceptionally high among developed economies. It reflects a grass-based ruminant production system oriented towards export markets for dairy and beef. Since the early 1990s the sector has been subject to a growing body of policy described, wholly or partly, as environmental or climate mitigation. This includes the Rural Environment Protection Scheme (REPS, from 1994), the Nitrates Action Programme (from 2006), successive agri-environment schemes (AEOS, GLAS and ACRES), breeding and efficiency programmes (BDGP, BEEP-S and SCEP), advisory tools such as the Carbon Navigator and, from 2022, direct limits on chemical nitrogen. The Climate Action and Low Carbon Development (Amendment) Act 2021 and the 2022 sectoral emissions ceiling subsequently committed agriculture to a 25% reduction in emissions, relative to 2018, by 2030.

Despite this policy activity, emissions reported under sector 3 of the Common Reporting Format (CRF3) were 19.63 Mt CO₂e in 2024, against 19.76 Mt CO₂e in 1990, a change of −0.65% ({{fig:emissions}}). The 2024 level was only 5.3% below the 2018 baseline, so most of the required 25% reduction must still be achieved within six years. The flat endpoints conceal a path that was far from flat. Emissions fell through the 2000s to a low of 17.78 Mt CO₂e in 2011 and then rose sharply to 21.27 Mt CO₂e in 2021. Some force pushed them back up.

Two explanations compete. **Explanation A** holds that *mitigation was weak*: instruments were voluntary, under-resourced or slow to take effect. This account is consistent with stakeholder reports of capacity and coordination constraints (Augustenborg et al., 2026) and with Ireland's record as a climate-policy laggard (Torney & O'Gorman, 2019). **Explanation B** holds that *mitigation was offset by expansion*. From 2007 the nitrates derogation permitted higher stocking rates. Milk quotas were raised from 2008 and abolished in 2015. National strategies (Food Harvest 2020 and Food Wise 2025) set quantified growth targets. Under Explanation B, mitigation instruments may have worked yet been cancelled by policies that increased output.

The distinction matters for policy design. If mitigation instruments are ineffective, the remedy is better instruments. If they are effective but cancelled by expansion policy, additional instruments will not close the emissions gap while expansion incentives remain in place. The central research question of this paper is therefore:

> **Does the flat emission path reflect failed mitigation, or mitigation offset by policies that expanded output?**

## 1.2 Policy context: two policy sets pulling in opposite directions

{{tab:context}} summarises Irish agricultural policy by period from 1990 to 2024. Expansion instruments acted on *how much* was produced, and several of them relaxed binding legal limits. Mitigation instruments acted mainly on *how* it was produced, and most took the form of voluntary contractual schemes. The principal binding mitigation instrument, the Nitrates Action Programme, was designed to protect water quality rather than to reduce greenhouse-gas emissions.

TAB context | Policy context by period, 1990–2024

| Period | Production pressure (expansion) | Mitigation |
|:---|:---|:---|
| 1990–2004 | Coupled suckler-cow, special-beef and ewe premia; Agenda 2000 quota increases (2000–2001) | REPS agri-environment scheme (from 1994) |
| 2005–2009 | CAP decoupling (2005) ends coupled premia; nitrates derogation from 2007; +2% quota increase in 2008 | Nitrates Action Programme (S.I. 378/2006); Farm Waste Management Scheme |
| 2010–2014 | Quota increases of 1% a year; Food Harvest 2020 (+50% milk volume target; strategy signal G) | REPS run-off; AEOS; Carbon Navigator; Sustainable Dairy Assurance Scheme (2014) |
| 2015–2021 | EU milk-quota abolition (31 March 2015); TAMS II dairy equipment grants; Food Wise 2025 (G) | GLAS; suckler genetics and data programmes (BDGP, BEEP-S); Sustainable Beef and Lamb Assurance Scheme (2017) |
| 2021–2024 | Derogation renewed and tightened from 2024; Food Vision 2030 (mixed goals; G) | Fifth NAP chemical-N maxima (S.I. 113/2022); ACRES; SCEP. Climate Act 2021 and the 2022 ceiling are event markers |

NOTE: CAP = Common Agricultural Policy; NAP = Nitrates Action Programme; S.I. = Statutory Instrument. Non-binding national growth strategies form the separate strategy signal G and are not part of P. Acronyms are defined in full in {{tab:acronyms}}.

Five dates are treated as policy events throughout the analysis: decoupling (2005), the first nitrates derogation (2007), Food Harvest 2020 (2010), quota abolition (2015) and the sectoral emissions ceiling (2022).

## 1.3 Related literature

### 1.3.1 Evaluating climate policy in agriculture

Cross-country ex post evaluations have estimated the emission effects of climate legislation (Eskander & Fankhauser, 2020) and identified the policy combinations associated with large reductions (Stechemesser et al., 2024). These studies define the treatment as instruments labelled as climate policy, so sectoral policies that raise output enter only as background variation. This matters considerably for agriculture. The main drivers of herd size and nitrogen use in the European Union (milk quotas, coupled payments, derogations and national growth strategies) are not climate instruments at all.

### 1.3.2 Policy coherence, policy mixes and layering

The policy-coherence literature distinguishes sector–environment interactions that reinforce each other, are neutral or counteract each other (Nilsson et al., 2012). The policy-mix framework stresses that instruments operate jointly and that outcomes are determined by the mix rather than by individual instruments (Rogge & Reichardt, 2016). Scholarship on policy design describes *layering*, in which new goals are added on top of existing instruments without removing contradictory ones (Howlett & Rayner, 2013). Together these frameworks predict that Irish mitigation effort could be neutralised by concurrent expansion policy. They have mostly been applied qualitatively, however, and do not yield an estimate of how large such an offset might be.

### 1.3.3 Decomposition and the rebound analogy

Index-decomposition analysis, and the LMDI family in particular, splits changes in emissions exactly into activity, structure and intensity effects (Ang, 2015; Ang & Liu, 2001). In energy economics, the share of an efficiency gain that is cancelled by induced demand is known as the *rebound effect* (Greening et al., 2000). The agricultural analogue is the extent to which lower emissions per litre of milk or per animal are cancelled by more litres and more animals. We formalise this concept as the *intensity offset* (Section 3.1).

### 1.3.4 Evidence for Ireland

Läpple et al. (2022) find that EU milk-quota abolition increased dairy expansion and per-farm emissions despite lower emission intensity. Donnellan et al. (2013) show that the Food Harvest 2020 targets were incompatible with emission-reduction commitments. Balaine et al. (2022) conclude that Ireland's efficiency-based strategy did not offset intensification pressure. Henn et al. (2023) caution that shifts in herd composition alter implied emission factors, so aggregate claims about intensity require care. Augustenborg et al. (2026) identify five stakeholder-perceived barriers to environmental policy implementation in Ireland: policy incoherence, competing political priorities, capacity, financial constraints and planning constraints.

## 1.4 Research gap, research questions and contributions

The *direction* of each mechanism is therefore established, but the *size* of the offset between expansion and mitigation policy has not been measured. Cross-country evaluations treat non-climate sectoral policy as background, and the policy-coherence literature remains largely qualitative. To our knowledge, no study has placed expansion and mitigation policy on a common scale and quantified how much one offsets the other. Doing so requires (i) a common scale for both policy sets, (ii) an attribution strategy that works with a single national series of about 30 annual observations, and (iii) a link between the accounting decomposition and the policy variables.

The study addresses four research questions, formalised as pre-specified hypotheses in Section 3.2:

- **RQ1.** Do breaks in the emission path coincide with policy changes?
- **RQ2.** Did gains in emission intensity keep pace with growth in scale?
- **RQ3.** Did production pressure offset mitigation?
- **RQ4.** Do effects differ by instrument type and by regional exposure to quota abolition?

The paper makes three contributions:

1. **Measurement.** We construct an annual production-pressure index P, scored on the same implementation × coverage × eligibility × bindingness (I × *s* × *e* × B) scale that the INPACT approach applies to mitigation (M). The two policy sets become commensurable, and policy incoherence becomes a measurable quantity, the net signal *S* = *M* − *P*. Non-binding growth strategies are kept apart as a strategy signal G.
2. **Attribution with a short series.** We combine three designs whose assumptions fail in different ways: structural breaks with exact decomposition, an ARDL policy-mix model with block-bootstrap inference, and a within-Ireland regional DiD. Explicit power analysis allows null results to be interpreted.
3. **Linking decomposition to policy.** We regress the annual LMDI activity and intensity effects on changes in P and M. This tests directly whether expansion operates through scale and mitigation through intensity.

The analysis is confined to Ireland. Quota abolition and CAP reform applied to every EU member state, so no untreated foreign comparator exists. Within-Ireland variation in exposure provides the comparison instead.

## 1.5 Structure of the paper

The remainder of the paper is organised as follows. Section 2 describes the dataset, including its sources, variables, time coverage, sample sizes and pre-processing. Section 3 sets out the conceptual framework, the pre-specified hypotheses and the estimation methods. Section 4 reports the results in the same order as the sections of the study's interactive results platform. Section 5 discusses the findings, their policy implications and the study's limitations, and Section 6 concludes.

# 2. Dataset

## 2.1 Data sources

The analysis draws on 58 raw files from four public agencies, together with the authors' policy codebooks ({{tab:sources}}). Of these files, 53 are loaded into the analysis; the remaining five duplicate information already loaded and are retained only for provenance. Every series is annual and is read unchanged from the publishing agency. Every loaded file is fingerprinted with the SHA-256 hash algorithm so that the inputs can be verified on each run. A catalogue of 50 source datasets and parameters, with download and documentation links, accompanies the study's online platform.

TAB sources | Data sources

| Agency | Product | Form | Content used | Years |
|:---|:---|:---|:---|:---|
| Environmental Protection Agency (EPA) | Provisional GHG inventory workbook, 1990–2025 | Excel workbook | CRF3 total, five emission categories, three gases | 1990–2024 |
| UNFCCC | Ireland Common Reporting Tables (CRT), 2025 submission | 34 workbooks, one per inventory year | Dairy/non-dairy CH₄ split, N excretion rates, mineral N 1990–1999 | 1990–2023 |
| Eurostat | `env_air_gge`, `aei_fm_usefert`, livestock-unit (LSU) coefficients | CSV extracts | Species-level CH₄ detail, mineral N 2000–2024, LSU coefficients | 1990–2024 |
| Central Statistics Office (CSO) | AAA01/07/09, AKA01, AHA01–05, CPA01, NA002 | PxStat CSV | Livestock (national and regional), milk, agricultural prices, CPI, GNI* | 1991–2024 |
| Authors | Policy codebooks (`pressure_codebook.csv`, `mitigation_codebook_PROVISIONAL.csv`) | CSV | 19 instruments (5 P, 3 G, 11 M) scored I × *s* × *e* × B (× *w*) | 1990–2024 |

NOTE: UNFCCC = United Nations Framework Convention on Climate Change. The mitigation codebook is provisional (see Section 5.6).

## 2.2 Variables

{{tab:dictionary}} summarises every variable in the annual panel, including its unit, data type, source and coverage. The variables fall into six groups: emissions (the outcome, its categories and gases, and the livestock components used in the decomposition), livestock, milk, nitrogen, prices and macroeconomic controls, and policy indices. Emission variables are continuous annual flows in kilotonnes of CO₂-equivalent (kt CO₂e). Livestock variables are June head counts. Price variables are chain-linked index numbers, and the policy variables are composite indices constructed by the authors (Section 3.4).

TABLEINCLUDE dictionary

## 2.3 Time period and sample sizes

The annual national panel covers 35 years, 1990–2024. Not every variable is available for every year, and every estimator uses the largest common sample for its variables (Section 2.9). Livestock series begin in 1991, milk series in 1992 and agricultural price indices in 1995. The CRT-based dairy split and N-excretion rates end in 2023, because the 2024 CRT submission had not been published at the time of analysis. {{tab:samples}} reports the resulting sample for each analysis.

TAB samples | Analysis samples by method

| Analysis | Unit of observation | Period | Observations | Binding constraint |
|:---|:---|:---|:---|:---|
| Trend tests and structural breaks | Nation-year | 1990–2024 | 35 | Full CRF3 series |
| Exact LMDI decomposition | Annual change | 1992–2023 | 31 annual changes | Milk intake (from 1992); CRT dairy split (to 2023) |
| ARDL policy-mix model | Nation-year | 1997–2024 | 28 | Prices from 1995 plus up to two lags |
| Interrupted time series | Nation-year | 1995–2024 | 30 | Price controls |
| Decomposition–regression link | Annual change | 1997–2023 | 27 | LMDI end year and price lags |
| Regional DiD (livestock outcomes) | Region-year | 1991–2024 | 170 (5 × 34) | CSO regional livestock series |
| Regional DiD (imputed emissions) | Region-year | 1991–2023 | 165 (5 × 33) | National implied emission factors (to 2023) |
| Regional event study | Region-year | 2005–2024 | 5 × 20 | Post-classification-break years |

## 2.4 Outcome: CRF sector 3 emissions

The outcome is IPCC/CRF sector 3 (agriculture), measured in kt CO₂e using the 100-year global warming potentials of the IPCC Fifth Assessment Report (AR5; CH₄ = 28, N₂O = 265; Myhre et al., 2013), which is the metric used in Ireland's national inventory:

$$
E_t^{\text{CRF3}} = E_t^{\text{Agriculture}} - E_t^{1.A.4.c.ii} - E_t^{1.A.4.c.iii}
=\sum_{c\in\{3A,3B,3D,3G,3H\}} E_{c,t}
=E^{CO_2}_t+28\,E^{CH_4}_t+265\,E^{N_2O}_t \qquad (1)
$$

The EPA "Agriculture" row follows the Climate Action Plan definition, which also includes agricultural and forestry fuel combustion (1.A.4.c.ii) and fishing (1.A.4.c.iii); these are subtracted. On every run the result is checked against both the sum of the five reported categories (enteric fermentation 3.A, manure management 3.B, agricultural soils 3.D, liming 3.G and urea application 3.H) and the sum of the three gases, with a discrepancy below 0.0001%. The remaining sector-3 categories are not occurring or not applicable in Ireland. {{fig:emissions}} shows the outcome and its composition by category.

FIG emissions | Irish agricultural (CRF sector 3) greenhouse-gas emissions by category, 1990–2024, and the linear path to the 2030 sectoral ceiling | fig_emissions.png | 6.3
FIGNOTE: Stacked areas show the five inventory categories in Mt CO₂e (AR5 GWP100); the black line is the CRF3 total. The dashed red line joins 2024 emissions to the 2030 target of 15.5 Mt CO₂e (75% of the 2018 level). Dotted vertical lines mark the five policy events. Data: EPA (2026).

Three inventory vintages are combined. The EPA provisional inventory (2026) provides CRF3, as it is the only source that includes 2024; Eurostat `env_air_gge` provides species-level detail; and the CRT 2025 submission provides the dairy/non-dairy split and fertiliser data for the 1990s. The vintages agree to within 0.01% for 1990–2020 and 0.21% for 2021–2023. The LMDI "other" term absorbs any difference between vintages, so the decomposition remains exact.

## 2.5 Activity variables

**Livestock.** The CSO June livestock tables AAA01 (1991–2004), AAA07 (2005–2014) and AAA09 (2015 onwards) cover disjoint years and are stacked without back-filling, so 1990 remains missing. Dairy cows fall by 8.7% at the AAA01→AAA07 switch, whereas total cattle fall by only 0.3%. The CRT shows the same step, which identifies it as a classification change rather than a real fall in the herd. Every model in which the herd enters therefore includes an indicator for 2005. Livestock units (LU) are computed as

$$
\text{LU}_t = 1.0\cdot D_t + \sum_{k} \lambda_k N_{k,t} + 0.1\cdot Sh_t,\qquad \lambda_k\in\{0.4,0.7,0.8,1.0\} \qquad (2)
$$

where *D* denotes dairy cows, *N*~k~ the CSO non-dairy cattle categories weighted by the Eurostat LSU coefficients λ~k~, and *Sh* sheep. The implied LU per non-dairy animal falls from 0.673 to 0.638 as the herd becomes younger.

**Milk.** Domestic milk intake by processors (CSO AKA01) begins in 1992. Yield per cow is computed as yield~t~ = milk~t~ (million litres) × 10³ / *D*~t~ (thousand head).

**Nitrogen.** Mineral N fertiliser use is taken from CRT 2025 Table 3.D for 1990–1999 and from Eurostat `aei_fm_usefert` for 2000–2024. Although CRT Table 3.D is headed "t N/year", its values are in kg N: dividing by 1,000 reproduces the Eurostat figures for 2000–2005 exactly. Manure N excreted is

$$
N^{\text{manure}}_t=\frac{\text{nex}^{D}_t D_t+\text{nex}^{O}_t O_t+\text{nex}^{Sh}_t Sh_t}{10^3} \qquad (3)
$$

where *O* denotes non-dairy cattle and the N-excretion rates (kg N per head per year) are taken from CRT Table 3.B(b). The dairy rate rises from 97.9 (1991) to 108.4 (2023), the non-dairy cattle rate falls from 54.8 to 48.1, and the sheep rate is approximately 7.5. {{fig:drivers}} plots the outcome alongside its main activity drivers.

FIG drivers | CRF3 emissions and their main activity drivers, 1990–2024 | fig_drivers.png | 6.3
FIGNOTE: Each panel has its own vertical scale. The dashed red line in the dairy-cow panel marks the 2004–2005 CSO classification break. Dotted vertical lines mark Food Harvest 2020 (2010) and quota abolition (2015). Data: EPA (2026), CSO, CRT 2025 and Eurostat.

## 2.6 Prices and macroeconomic controls

Five CSO agricultural price-index vintages (with bases 2000, 2005, 2010, 2015 and 2020) are chain-linked by the overlap method:

$$
\tilde I^{\,old}_{t}=I^{old}_t\cdot\exp\Big(\frac{1}{|\mathcal O|}\sum_{s\in\mathcal O}\ln\frac{I^{new}_s}{I^{old}_s}\Big),
\qquad p^{real}_t=\frac{\tilde I_t}{CPI_t}\times 100 \qquad (4)
$$

where 𝒪 is the set of overlapping years and real prices are expressed with 2020 = 100. The newest vintage is retained in overlapping years, and the geometric mean treats ratios symmetrically (Eurostat, 2016). The largest overlap deviation across the 20 links is 2.88%. Price series begin in 1995. Modified gross national income (GNI*, CSO NA002) enters one robustness variant. No weather variable is used.

## 2.7 Regional panel

If quota abolition drove expansion, its effect should be strongest where dairying was already dominant. The 2014/2016 revision of the NUTS3 regions moved County Louth from the Border region to the Mid-East and unified County Tipperary. We therefore construct five constant-boundary units: the West, the Midland and the South-West, whose boundaries are unchanged; **Border + Dublin/Mid-East**, which absorbs Louth's move; and **Mid-West + South-East**, which absorbs the unification of Tipperary. These units sum to the State totals within 0.014% (dairy cows), 0.004% (cattle) and 0.003% (sheep). The regional panel covers 1991–2024. Imputed regional livestock emissions, calculated as head counts multiplied by national implied emission factors per head, are available to 2023.

Exposure to quota abolition is measured as each region's dairy share of all cows in 2010–2014 ({{tab:exposure}}; {{fig:regional}}a). Exposure ranges from 16% to 74%, which provides a wide contrast for a continuous-intensity design (Card, 1992).

TAB exposure | Exposure to quota abolition: dairy share of all cows, 2010–2014

| Region | Dairy share of cows (%) |
|:---|---:|
| West | 16.3 |
| Midland | 35.3 |
| Border + Dublin/Mid-East | 38.3 |
| Mid-West + South-East | 58.4 |
| South-West | 73.7 |

FIG regional | Regional exposure to quota abolition and the regional dairy herd, 1991–2024 | fig_regional.png | 6.3
FIGNOTE: (a) Dairy share of all cows in 2010–2014 for the five constant-boundary units. (b) Dairy-cow numbers indexed to 2014 = 100. The dashed red line marks the 2004–2005 classification break; the dotted line marks quota abolition. Data: CSO AAA01/07/09.

## 2.8 Policy codebooks

Nineteen instruments are coded: five production-pressure instruments (P01–P05) and three national growth strategies (G01–G03; {{tab:codebookP}}), and eleven mitigation instruments (M01–M11; {{tab:codebookM}}). The strategies set non-binding sectoral targets and are reported as a separate strategy signal G rather than summed into P; a robustness variant adds them to P. Three overlapping suckler programmes (BDGP, BEEP-S and SCEP) are coded as one lineage (M08). Eligibility *e* may vary over time (P03, M05 and M08) and is coded with the same year-range syntax as implementation. Plausible ranges for *e* and *B* and a confidence grade for each component are recorded with the codebook. Two framework laws (E01 and E02) are recorded as event markers but are not entered in any index, to avoid double counting. {{fig:scores}} shows the resulting annual score of each instrument.

TAB codebookP | Production-pressure (P) and strategy-signal (G) codebook

| ID | Instrument | Type | Years | Coverage key (share *s*) | Eligible *e* | Bindingness *B* | Implementation *I* |
|:---|:---|:---|:---|:---|:---|:---|:---|
| P01 | Coupled livestock premia (special beef, suckler cow, slaughter and ewe premia) | Incentive | 1990–2004 | beef_sheep (0.482) | 1 [0.85–1.00] | 0.50 | 1 |
| P02 | Milk quota increases (Agenda 2000 allocation; 2% in 2008; 1% p.a. 2009–2013) | Conditional | 2000–2014 | dairy (0.185) | 1 | 0.75 | 0.18 (2000); 0.28 (2001–07); 0.48, 0.58, 0.68, 0.79, 0.89 (2008–12); 1 (2013–14) |
| P03 | Nitrates derogation (stocking above 170 kg organic N/ha) | Conditional | 2007–2024 | dairy (0.194) | 0.35 (2007–13); 0.45 (2014–17); 0.55 (2018–21); 0.6 (2022–24) | 0.75 | 0.25 (2007); 1 (2008–23); 0.75 (2024) |
| P04 | EU milk quota abolition | Mandatory removal | 2015–2024 | dairy (0.216) | 1 | 1.00 [0.75–1.00] | 0.75 (2015); 1 (2016–24) |
| P05 | TAMS II Dairy Equipment Scheme (capital grants) | Incentive | 2015–2023 | dairy (0.216) | 0.45 [0.35–0.60] | 0.50 | 0.5 (2015); 1 (2016–22); 0.25 (2023) |
| G01 | Food Harvest 2020 (+50% milk volume target) | Strategy | 2010–2014 | cattle_sheep (0.701) | 1 | 0.25 | 0.5 (2010); 1 (2011–14) |
| G02 | Food Wise 2025 (+65% primary production value) | Strategy | 2015–2020 | cattle_sheep (0.698) | 1 | 0.25 | 0.5 (2015); 1 (2016–20) |
| G03 | Food Vision 2030 | Strategy | 2021–2024 | cattle_sheep (0.702) | 1 | 0.25 | 1 |

NOTE: Values in square brackets are the plausible ranges for *e* and *B*; a confidence grade for each component is recorded in the codebook file. All instruments have content weight *w* = 1 except G03, which carries a content weight *w* = 0.50, the expansionary share of a strategy that pairs an export-value target with a methane-reduction target. P02 implementation is the normalised cumulative quota increase. Coverage keys are defined below {{tab:codebookM}}.

TAB codebookM | Mitigation codebook (M; provisional coding)

| ID | Instrument | Type | Years | Coverage key (share *s*) | Eligible *e* | *B* | Implementation *I* |
|:---|:---|:---|:---|:---|:---|:---|:---|
| M01 | Rural Environment Protection Scheme (REPS 1–4) | Incentive | 1994–2014 | n_soils_manure (0.342) | 0.35 [0.25–0.45] | 0.50 | 0.25 (1994); 0.5 (1995); 1 (1996–2009); 0.5 (2010–13); 0.25 (2014) |
| M02 | Nitrates Action Programme (Good Agricultural Practice Regulations) | Mandatory | 2006–2024 | n_soils_manure (0.354) | 1 | 1.00 | 0.5 (2006); 0.75 (2007–08); 1 (2009–24) |
| M03 | Farm Waste Management Scheme (revised, nitrates-driven) | Incentive | 2006–2009 | manure (0.125) | 0.47 [0.40–0.55] | 0.50 | 0.25 (2006); 0.5 (2007); 0.75 (2008); 1 (2009) |
| M04 | Agri-Environment Options Scheme (AEOS) | Incentive | 2010–2018 | n_soils_manure (0.343) | 0.07 [0.05–0.10] | 0.50 | 0.5 (2010); 1 (2011–14); 0.5 (2015–16); 0.15 (2017–18) |
| M05 | Carbon Navigator and advisory programmes | Voluntary | 2013–2024 | cattle_sheep (0.706) | 0.1 (2013–14); 0.05 (2015–22); 0.1 (2023–24) | 0.25 | 0.25 (2013); 0.5 (2014); 1 (2015–22); 0.5 (2023–24) |
| M06 | Sustainable Dairy Assurance Scheme (Origin Green) | Voluntary | 2014–2024 | dairy (0.207) | 0.95 [0.90–0.99] | 0.25 [0.25–0.50] | 0.25 (2014); 0.5 (2015); 0.75 (2016); 1 (2017–24) |
| M07 | Green Low-Carbon Agri-Environment Scheme (GLAS) | Incentive | 2015–2022 | n_soils_manure (0.348) | 0.28 [0.20–0.36] | 0.50 | 0.5 (2015); 0.75 (2016); 1 (2017–22) |
| M08 | Suckler genetics and data programmes (BDGP 2015–2022; BEEP-S 2019–2022; SCEP from 2023) | Incentive | 2015–2024 | beef_sheep (0.482) | 0.24 (2015–18); 0.33 (2019–22); 0.24 (2023–24) | 0.50 | 0.75 (2015); 1 (2016–20); 0.75 (2021–22); 1 (2023–24) |
| M09 | Chemical nitrogen maxima (5th Nitrates Action Programme increment) | Mandatory | 2022–2024 | fertiliser (0.083) | 1 [0.70–1.00] | 1.00 [0.75–1.00] | 0.5 (2022); 1 (2023–24) |
| M10 | Agri-Climate Rural Environment Scheme (ACRES) | Incentive | 2023–2024 | n_soils_manure (0.323) | 0.23 [0.18–0.32] | 0.50 | 0.75 (2023); 1 (2024) |
| M11 | Sustainable Beef and Lamb Assurance Scheme (Origin Green) | Voluntary | 2017–2024 | beef_sheep (0.460) | 0.9 [0.85–0.95] | 0.25 | 0.5 (2017); 1 (2018–24) |

NOTE: Ranges as in {{tab:codebookP}}. Event markers not entered in the indices: E01, the Climate Action and Low Carbon Development (Amendment) Act 2021 (Act No. 32 of 2021); E02, the agriculture sectoral emissions ceiling of July 2022 (−25% by 2030 against 2018). Coverage keys denote the share of CRF3 in the targeted activity: *dairy* = dairy CH₄; *beef_sheep* = non-dairy cattle and sheep CH₄; *cattle_sheep* = all cattle and sheep CH₄; *n_soils_manure* = agricultural soils and manure management; *manure* = manure management; *fertiliser* = direct N₂O from mineral N plus urea CO₂.

FIG scores | Annual policy scores (x = I × s × e × B × w) by instrument, 1990–2024 | fig_scores.png | 6.3
FIGNOTE: (a) The five production-pressure instruments, whose sum is the index P. (b) The three growth strategies, whose sum is the strategy signal G. (c) The eleven mitigation instruments, whose sum is the index M. Darker cells indicate higher scores; each panel has its own colour scale. Mitigation scores are based on provisional coding. Instrument names are abbreviated; see {{tab:codebookP}}, {{tab:codebookM}} and {{tab:acronyms}}.

## 2.9 Pre-processing and harmonisation

The raw files were processed into the analysis panels in the following steps. Each step is re-checked by an independent verification script (Section 3.16; {{tab:verification}}).

1. **Loading and provenance.** Each raw file is read unchanged and its SHA-256 hash is recorded. The only provisional input loaded is the placeholder second-coder file used for the inter-coder reliability statistic.
2. **Emissions boundary.** CRF3 is derived from the EPA "Agriculture" row by subtracting agricultural fuel and fishing (Equation 1) and reconciled with the category and gas totals.
3. **Inventory vintages.** EPA, Eurostat and CRT series are combined as described in Section 2.4. Differences between vintages are left in the LMDI "other" term rather than adjusted.
4. **Livestock stacking.** The three CSO livestock tables are stacked on their disjoint years. The 2004–2005 classification break is retained in the data and modelled with an indicator, not smoothed.
5. **Constant-boundary regions.** NUTS3 regions are aggregated to the five constant-boundary units described in Section 2.7.
6. **Unit corrections.** CRT Table 3.D fertiliser values are converted from kg N to tonnes N (division by 1,000).
7. **Price chain-linking and deflation.** The five CSO price vintages are linked by the overlap method and deflated by the CPI (Equation 4).
8. **Derived variables.** Livestock units, milk yield, manure N and the policy indices M, P, S and G are computed from the harmonised series (Equations 2, 3, 5 and 6).
9. **Missing data.** Missing years are **never** interpolated, back-cast or set to zero. Inventory notation keys (NO, NE and NA) are converted to missing values. Each estimator uses the largest common sample and reports it. Because the 2024 CRT had not been published, the CRT-based dairy split and N-excretion rates end in 2023 and are not imputed. The LMDI decomposition and the regional emission series therefore end in 2023, whereas CRF3 runs to 2024.

## 2.10 Descriptive statistics

{{tab:descriptives}} reports selected series at key years together with their peaks and troughs.

TAB descriptives | Selected series, 1990–2024

| Variable | Unit | 1990 / first | 2000 | 2010 | 2015 | 2018 | 2024 / last | Peak (year) | Trough (year) |
|:---|:---|---:|---:|---:|---:|---:|---:|:---|:---|
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
| Mitigation index M | index | 0.000 | 0.060 | 0.390 | 0.461 | 0.623 | 0.693 | 0.693 (2024) | 0.000 (1990) |
| Pressure index P | index | 0.241 | 0.266 | 0.146 | 0.252 | 0.344 | 0.281 | 0.352 (2022) | 0.039 (2005–06) |
| Net signal S | index | −0.241 | −0.206 | 0.244 | 0.209 | 0.279 | 0.412 | 0.412 (2024) | −0.241 (1990) |
| Strategy signal G | index | 0.000 | 0.000 | 0.088 | 0.087 | 0.174 | 0.088 | 0.175 (2011–14) | 0.000 (1990) |

NOTE: CRF3 and its categories are expressed in AR5 GWP100. "First" values are reported where a series starts after 1990 (year in parentheses).

**Composition.** In 2024 enteric fermentation accounted for 64.7% of CRF3 (63.2% in 1990), agricultural soils for 19.9% (22.2%), manure management for 12.3% (12.3%), liming for 2.3% and urea for 0.9% ({{fig:emissions}}). By gas, methane accounted for 74.1% (72.3% in 1990), nitrous oxide for 22.7% (25.4%) and CO₂ for 3.2%. Dairy-cattle methane rose from 19.6% of CRF3 in 1995 to 23.3% in 2015 and 29.2% in 2023. Nitrous oxide from soils tracks fertiliser use, which peaked in 1999 ({{fig:drivers}}).

# 3. Methodology

## 3.1 Conceptual framework

The framework rests on an accounting identity: emissions equal activity multiplied by intensity ({{fig:framework}}). Production-pressure policy (the derogation, quota increases and abolition, and TAMS capital grants; growth strategies are tracked separately) is expected to *raise* activity, that is, herd size, nitrogen use and milk volume. Mitigation policy (nitrates rules, agri-environment schemes, genetics programmes and advisory tools) is expected to *lower* intensity, that is, emissions per litre, per head and per kg N. Total emissions fall only if intensity falls faster than activity grows. Expansion policies act on *how much* is produced, whereas Irish mitigation policy has mostly acted on *how* it is produced.

FIG framework | Conceptual framework: production pressure acts on activity, mitigation acts on intensity | fig_framework.png | 6.0
FIGNOTE: CRF3 emissions are the product of activity and emission intensity. The framework predicts that P raises activity and M lowers intensity; the decomposition–regression link (Section 3.13) tests both predictions.

**Intensity offset.** Over any period with positive scale growth, we define the intensity offset (IO) as

$$
IO=\frac{-\Delta E^{\text{intensity}}}{\Delta E^{\text{activity}}+\Delta E^{\text{productivity}}} \qquad (5)
$$

IO is the share of scale-driven emission growth that is cancelled by lower emissions per unit. A value of IO = 1 means that efficiency gains exactly cancelled growth, and IO < 1 means that efficiency gains did not keep pace with expansion. The latter is the agricultural analogue of a rebound effect above 100% in energy economics (Greening et al., 2000). IO is defined only when Δ*E*^activity^ + Δ*E*^productivity^ > 0.

**Policy incoherence as a measurable quantity.** With M and P on one scale, the net policy signal is *S*~t~ = *M*~t~ − *P*~t~. If P and M rise in the same period, S understates mitigation effort. This makes the sector–environment incoherence described by Nilsson et al. (2012) and the layering described by Howlett and Rayner (2013) measurable.

## 3.2 Research questions and pre-specified hypotheses

The hypotheses and decision rules were fixed in the analysis code before estimation ({{tab:hypotheses}}). With about 28 usable annual observations, every test uses a significance level of α = 0.10. The rules are applied mechanically: a hypothesis is "supported" only if its pre-registered condition holds.

TAB hypotheses | Research questions, hypotheses, tests and decision rules

| RQ | Question | Hypothesis | Primary test | Supported if |
|:---|:---|:---|:---|:---|
| RQ1 | Do breaks in the emission path coincide with policy changes? | H1: an endogenous break lies within ±1 year of 2010 (Food Harvest 2020) or 2015 (quota abolition) | Bai–Perron structural breaks with bootstrap UDmax | UDmax *p* < 0.10 and a break date within ±1 year |
| RQ2 | Did intensity gains keep pace with scale growth? | H2: intensity offset IO < 1 after 2015 (efficiency did not keep pace) | Exact LMDI decomposition; decomposition–regression link | IO < 1 across the range of dairy emission factors |
| RQ3 | Did production pressure offset mitigation? | H3a: θ~M~ < 0 (mitigation lowers emissions); H3b: θ~P~ > 0 (pressure raises emissions); H3c: offset ratio ≥ 0.5 | ARDL long-run multipliers, restricted block bootstrap, dynamic counterfactuals | One-sided bootstrap *p* < 0.10; for H3c, the 90% interval of the pressure effect excludes zero |
| RQ4 | Do effects differ by instrument type and by regional exposure? | H4a: mandatory instruments have the largest negative effect; H4b: more dairy-exposed regions expanded more after 2015 | Sub-index ARDL; within-Ireland regional DiD | *p* < 0.10 with the predicted sign; placebo not significant |

**Dimensions of policy success.** Following Marsh and McConnell (2010), we distinguish three dimensions of policy success. *Programme* success asks whether instruments changed outcomes and is tested by RQ1–RQ4. *Process* success asks whether instruments were implemented as designed and is captured by the implementation score I. *Political* success asks whether instruments survived competing priorities and is discussed in relation to the five stakeholder-identified barriers of Augustenborg et al. (2026).

## 3.3 Research design and analytical pipeline

No single method can identify a causal policy effect from one national series of about 28 usable observations. The study therefore combines three designs whose identifying assumptions fail in different ways, so that inference rests on their agreement rather than on any single estimate (Lawlor et al., 2016; Munafò & Davey Smith, 2018):

- **Design A (descriptive):** trends, structural breaks and decomposition, using Mann–Kendall and Theil–Sen trend tests, Bai–Perron breaks with a bootstrap UDmax test, and exact LMDI-I decomposition. This design answers RQ1 and RQ2.
- **Design B (policy-mix time series):** an ARDL(1,0,0) model estimated over 1997–2024 (*n* = 28), with restricted bootstrap *p*-values, dynamic counterfactuals and power and minimum-detectable-effect (MDE) analysis. This design answers RQ3 and RQ4a.
- **Design C (within-Ireland comparison):** a regional DiD across five constant-boundary regions, with exposure defined as the pre-2015 dairy share and inference by randomisation. This design answers RQ4b.

The pipeline runs in six stages: (1) loading and hashing the raw files; (2) harmonisation (CRF3 boundary, livestock stacking, regions and price chain-linking); (3) construction of the annual panel (1990–2024) and the regional panel (5 regions × 1991–2024); (4) construction of the policy indices M, P, S and G; (5) estimation (structural breaks, LMDI, ARDL with bootstrap, counterfactuals, power analysis, DiD and 2030 scenarios); and (6) export and verification (34 result sheets, 7 figures and 30 independent checks).

## 3.4 Policy indices

Each policy *p* receives an annual score

$$
x_{pt}=I_{pt}\,s_p\,e_{pt}\,B_p\,w_p \qquad (6)
$$

where:

- **I** is implementation, scored on a five-point grid {0, 0.25, 0.5, 0.75, 1} (see below for P02);
- **s** is coverage, the share of CRF3 in the targeted activity *a*(*p*), fixed in the year *before* the policy starts (*t*^0^~p~ − 1); where that year precedes the inventory split, the nearest available year is used and the value is graded low-confidence (P01, P02 and M11);
- **e** is the eligible fraction of the targeted activity reached by the instrument, which may change over time (for example, as successive derogation decisions widened eligibility);
- **B** is bindingness: 0.25 for information, voluntary schemes or strategy targets; 0.5 for incentive payments; 0.75 for the conditional relaxation of a legal limit; and 1.0 for a mandatory rule or the removal of a legal cap;
- **w** is a content weight, equal to 1 except for Food Vision 2030 (*w* = 0.5), whose growth target is paired with a methane-reduction target.

Implementation is scored on the five-point grid except where a continuous measure is available: for the quota increases (P02), I is the cumulative quota increase normalised to its 2013 end point.

The product is non-compensatory: a policy counts only if it is in force, covers emissions and carries a signal (OECD et al., 2008). The indices are

$$
M_t=\sum_{p\in\mathcal M}x_{pt},\qquad P_t=\sum_{q\in\mathcal P}x_{qt},\qquad S_t=M_t-P_t,\qquad G_t=\sum_{g\in\mathcal G}x_{gt} \qquad (7)
$$

The strategy signal G is reported alongside P but is not part of it: strategies set targets without changing the legal or financial conditions of production, so summing them with binding instruments would mix announcements with constraints.

*Why coverage is fixed before adoption.* If coverage were measured in each year, a policy that expanded dairying would raise the dairy share and thereby its own weight. Fixing exposure weights before treatment is standard practice in shift-share designs (Goldsmith-Pinkham et al., 2020).

*Inter-coder reliability.* A linearly weighted Cohen's kappa is computed on the five-point grid (Cohen, 1968):

$$
\kappa_w=1-\frac{\sum_{ij}w_{ij}O_{ij}}{\sum_{ij}w_{ij}E_{ij}},\qquad w_{ij}=\frac{|i-j|}{k-1} \qquad (8)
$$

where *O*~ij~ is the observed share of policy-years that coder 1 placed in category *i* and coder 2 in category *j*, and *E*~ij~ is the share expected under independent scoring. Continuous codes (P02) are assigned to the nearest grid point. Kappa is computed separately for implementation and bindingness over the P and G instruments. **The second coding is currently a provisional placeholder pending independent blind coding**; it predates the revised codebook and was only remapped to the new identifiers. The reported values (implementation κ~w~ = 0.46 over 82 policy-years; bindingness κ~w~ = 1.00 over 8 policies) are therefore illustrative only. [AUTHOR INPUT REQUIRED: independent blind second coding of the P codebook, to replace the placeholder kappa values.]

## 3.5 Trends and structural breaks (RQ1)

*Monotonic trend.* With *y*~t~ = ln *E*~t~, we compute the Mann–Kendall statistic with the Hamed–Rao variance correction for autocorrelation, together with the Theil–Sen slope:

$$
S=\sum_{i<j}\operatorname{sgn}(y_j-y_i),\qquad Z=\frac{S-\operatorname{sgn}(S)}{\sqrt{\operatorname{Var}^*(S)}},\qquad \operatorname{Var}^*(S)=\operatorname{Var}(S)\cdot\frac{n}{n^*_s} \qquad (9)
$$

$$
\hat\beta_{\text{Sen}}=\operatorname{median}_{i<j}\frac{y_j-y_i}{j-i},\qquad \%\text{ per year}=100\,(e^{\hat\beta}-1) \qquad (10)
$$

The factor *n*/*n*\*~s~ inflates the variance under positive autocorrelation, which would otherwise overstate significance (Hamed & Rao, 1998; Yue et al., 2002).

*Structural breaks.* A Bai–Perron segmented-trend model,

$$
\ln E_t=\alpha_j+\delta_j t+u_t,\qquad T_{j-1}<t\le T_j,\quad j=1,\dots,m+1 \qquad (11)
$$

is estimated by global minimisation of the sum of squared residuals (SSR). Closed-form segment SSRs are combined by dynamic programming for *m* = 1, …, 4 breaks with a minimum segment length of *h* = 5 years (trimming ε ≈ 0.15 of *n* = 35; Bai & Perron, 2003). The number of breaks is selected by

$$
\text{BIC}(m)=n\ln\frac{SSR_m}{n}+\big[2(m+1)+m\big]\ln n \qquad (12)
$$

The presence of any break is tested with

$$
\text{UDmax}=\max_{1\le m\le 4}F(m),\qquad F(m)=\frac{(SSR_0-SSR_m)/2m}{SSR_m/\big(n-2(m+1)\big)} \qquad (13)
$$

Asymptotic critical values are unreliable at *n* = 35 (Diebold & Chen, 1996). The *p*-value is therefore obtained from a parametric bootstrap. The null model (a single trend with AR(1) errors) is fitted, 999 series are simulated under the null, UDmax is recomputed for each, and *p* = (1 + #{UDmax\* ≥ UDmax})/(*B* + 1). Ninety-percent intervals for the break dates are obtained from a residual bootstrap of the selected model (499 draws). Known-date Chow tests at 2010 and 2015 complement the search.

## 3.6 Exact LMDI decomposition (RQ2)

Emission components are written as exact products of factors:

$$
\begin{aligned}
E^{dairy}&=D\times\frac{\text{milk}}{D}\times\frac{E^{dairy}}{\text{milk}},\qquad E^{other}=O\times\frac{E^{other}}{O},\qquad E^{sheep}=Sh\times\frac{E^{sheep}}{Sh},\\
E^{soils}&=N^{fert}\cdot\frac{E^{soils}}{N^{fert}+N^{man}}+N^{man}\cdot\frac{E^{soils}}{N^{fert}+N^{man}},\qquad
E^{other\ cat.}=E^{CRF3}-\sum_i E_i
\end{aligned} \qquad (14)
$$

where, for dairy, the three factors are herd size, yield and emissions per litre. The additive LMDI-I form gives

$$
\Delta E^{k}=\sum_i L\big(E_i^T,E_i^0\big)\,\ln\frac{x_{ik}^T}{x_{ik}^0},\qquad L(a,b)=\frac{a-b}{\ln a-\ln b},\quad L(a,a)=a \qquad (15)
$$

and because ln ∏~k~ *x*~k~ = Σ~k~ ln *x*~k~,

$$
\sum_k\Delta E^k=\sum_i L(E_i^T,E_i^0)\ln\frac{E_i^T}{E_i^0}=\sum_i\big(E_i^T-E_i^0\big)=E^T-E^0 \qquad (16)
$$

so the decomposition has no residual (Ang, 2015; Ang & Liu, 2001). The verified residual is 1.9 × 10⁻¹¹ kt. Factors are grouped into *activity* (herd sizes and N inputs), *productivity* (milk per cow), *intensity* (emissions per litre, per head and per kg N) and *other* (other categories and differences between inventory vintages). Effects are chained year by year from 1992, the first year with milk data, to 2023, the last year of the CRT dairy split. They are summed within five policy phases: P1, coupled support (1992–2004); P2, decoupling and derogation (2004–2009); P3, Food Harvest and quota increases (2009–2014); P4, post-quota expansion (2014–2021); and P5, sectoral ceiling (2021–2023). Soil N₂O is allocated to mineral and manure N in proportion to inputs, using a single implied N₂O intensity per kt N. Sensitivity to the dairy/non-dairy emission-factor ratio is checked at 1.8, 2.2 and 2.6, a range that brackets the CRT ratio of 2.2–2.85.

The decomposition is an accounting identity. It shows *what* moved emissions, not *which policy* caused the movement. Changes in inventory methodology also appear as changes in intensity even when farm practice is unchanged.

## 3.7 ARDL policy-mix model (RQ3)

The policy-mix model is

$$
\ln E_t=\alpha+\tau t+\sum_{i=1}^{p}\phi_i\ln E_{t-i}+\sum_{j=0}^{q_M}\beta_jM_{t-j}+\sum_{j=0}^{q_P}\gamma_jP_{t-j}+\lambda'X_t+\varepsilon_t \qquad (17)
$$

where *X*~t~ contains the log real milk price and the log real fertiliser price, the main output- and input-market drivers. The linear trend prevents the two rising indices from absorbing smooth drift, and the lagged dependent variable captures the slow adjustment of herds and soil-N pools. The ARDL framework is valid whether the regressors are I(0), I(1) or cointegrated (Pesaran et al., 2001).

*Lag selection.* All 18 candidate specifications, with *p* ∈ {0, 1} and *q*~M~, *q*~P~ ∈ {0, 1, 2}, are estimated on the *same* sample (1997–2024, *n* = 28), because prices start in 1995 and up to two lags are allowed. The small-sample criterion AICc = AIC + 2*k*(*k* + 1)/(*n* − *k* − 1) selects **ARDL(1, 0, 0)**:

$$
\ln E_t=\alpha+\tau t+\phi\ln E_{t-1}+\beta_0M_t+\gamma_0P_t+\lambda'X_t+\varepsilon_t \qquad (18)
$$

*Long-run multipliers.* The long-run effects of the two indices are

$$
\theta_M=\frac{\sum_j\beta_j}{1-\sum_i\phi_i},\qquad \theta_P=\frac{\sum_j\gamma_j}{1-\sum_i\phi_i} \qquad (19)
$$

with delta-method variances Var(θ̂) ≈ ∇θ′ *V̂*~HAC~ ∇θ, where ∂θ~P~/∂γ~j~ = 1/(1 − φ) and ∂θ~P~/∂φ = Σ~j~γ~j~/(1 − φ)². *V̂*~HAC~ is the Newey–West covariance matrix with two lags and a small-sample correction (rule of thumb 0.75*T*^1/3^ ≈ 2.3; Newey & West, 1987; Stock & Watson, 2020). A sustained change of 0.1 in an index changes long-run emissions by 100(*e*^0.1θ^ − 1) percent.

*Bounds test and diagnostics.* The Pesaran–Shin–Smith bounds test (case V, unrestricted intercept and trend, *k* = 4) is applied to

$$
\Delta y_t=c+\tau t+\pi_y y_{t-1}+\pi_M M_{t-1}+\pi_P P_{t-1}+\pi_X'X_{t-1}+\sum\psi\,\Delta(\cdot)+u_t,\qquad H_0:\pi_y=\pi_M=\pi_P=\pi_X=0 \qquad (20)
$$

An *F* statistic above the I(1) bound indicates a level relationship. Residual diagnostics comprise the Breusch–Godfrey test (two lags), the Jarque–Bera test, the Breusch–Pagan test, the RESET test and the CUSUM test. Augmented Dickey–Fuller (ADF) and KPSS unit-root tests characterise the order of integration of each variable.

## 3.8 Restricted recursive moving-block bootstrap

With 28 observations, textbook HAC *t*-tests reject too often. In Monte Carlo simulation, a nominal 10% HAC test rejects 23% of the time for θ~M~ and 26% of the time for θ~P~ when the true effect is zero (cf. Kiefer & Vogelsang, 2005). The decisive *p*-values are therefore obtained from a bootstrap that imposes the null hypothesis (Davidson & MacKinnon, 2000; Li & Maddala, 1996):

1. Re-estimate the model without the tested index *v* (the null model, H~0~: θ~v~ = 0).
2. Centre the residuals of the null model and cut them into overlapping blocks of length 3, which preserves serial dependence (≈ *T*^1/3^; Hall et al., 1995).
3. Draw blocks with replacement to form a new residual series ε\*.
4. Generate pseudo-emissions recursively from the null model: *y*\*~t~ = α̂ + τ̂*t* + φ̂*y*\*~t−1~ + Σ~w≠v~ *b̂*′~w~*w*~t~ + λ̂′*X*~t~ + ε\*~t~.
5. Re-estimate the full ARDL (including *v*) on *y*\* and record θ\*~v~.
6. Repeat *B* = 999 times and compute the one-sided *p*-value *p*\*~v~ = (1 + #{θ\*~v~ beyond θ̂~v~})/(*B* + 1), testing θ~M~ < 0 for H3a and θ~P~ > 0 for H3b.

The choice *B* = 999 makes α(*B* + 1) an integer. Robustness variants use *B* = 299 and the sub-indices *B* = 499. A single random-number generator seeded at 20261019 makes every draw reproducible.

## 3.9 Dynamic counterfactuals and the offset ratio (RQ3)

To express the coefficients in tonnes, each index is frozen at its level in the year *t*~0~ = 2000 and the fitted dynamics are propagated forward:

$$
\Delta_{v,t}=\sum_i\phi_i\Delta_{v,t-i}+\sum_j b_{v,j}\,\big(v_{t-j}-v_{t_0}\big),\qquad
E^{cf}_t=E_t\,e^{-\Delta_{v,t}},\qquad OR_T=\frac{\Delta_{P,T}}{-\Delta_{M,T}} \qquad (21)
$$

where Δ~v,t~ is the log-point effect of index *v* in year *t* and *b*~v,j~ are its lag coefficients. The **offset ratio** (OR) is defined only when the mitigation effect is negative, by analogy with the rebound effect. Ninety-percent intervals are obtained from an *unrestricted* block bootstrap (999 draws).

## 3.10 Power and minimum detectable effect

To interpret null results, we (i) set a true long-run effect |θ| on the grid {0, 0.1, 0.2, 0.3, 0.5, 0.75, 1, 1.5}; (ii) simulate 500 emission series from the fitted model with that θ, using the observed paths of M, P and X and block-resampled residuals; (iii) re-estimate the full model on each series and record the *t*-statistic; (iv) take the 90th percentile at θ = 0 as the size-adjusted critical value; and (v) compute power(θ) as the share of *t*-statistics above that value. The MDE is the smallest |θ| with 80% power, found by linear interpolation (Bloom, 1995; Gelman & Carlin, 2014).

## 3.11 Robustness, instrument sub-indices and interrupted time series

*Robustness grid.* We estimate seventeen pre-specified variants and five leave-one-policy-out runs ({{tab:robustgrid}}). Besides alternative lags, trends, controls, samples and outcomes, the variants change the policy coding: equal bindingness, dropping the Nitrates Action Programme or down-weighting it for climate relevance, adding the strategy signal G to P, the alternative bindingness values recorded in the codebook (quota abolition *B* = 0.75; SDAS *B* = 0.50), and scoring the two framework laws in M at *B* = 0.25. The rule, fixed in advance, is that a sign is **robust** if it holds in at least 80% of the estimable variants.

*Sub-indices by instrument type (RQ4a).* Each mitigation sub-index *s* ∈ {mandatory, incentive, voluntary} is estimated in turn, with the remainder of M and the pressure index held as controls (bootstrap *B* = 499):

$$
\ln E_t=\dots+\beta^{s}M^{s}_t+\beta^{rest}\big(M_t-M^{s}_t\big)+\sum_j\gamma_jP_{t-j}+\dots \qquad (22)
$$

*Interrupted time series at pre-specified dates.* The segmented regression

$$
y_t=\beta_0+\beta_1t+\sum_{e\in\{2010,2015,2022\}}\Big[\lambda_e\mathbf{1}(t\ge e)+\delta_e\,(t-e+1)\,\mathbf{1}(t\ge e)\Big]+\lambda'X_t+u_t \qquad (23)
$$

estimates a level change λ~e~ and a slope change δ~e~ at each event *e* (Bernal et al., 2017). The outcomes are ln CRF3 and ln dairy cows, the latter with a post-2005 indicator. The sample is 1995–2024 with HAC standard errors. The 2022 event has only three post-event years and is treated as descriptive.

## 3.12 Regional difference-in-differences (RQ4b)

If quota abolition drove expansion, regions in which dairying was already dominant should have expanded more after 2015. We estimate a continuous-exposure DiD model:

$$
y_{rt}=\alpha_r+\gamma_t+\beta\,\big(\text{Exp}_r-\overline{\text{Exp}}\big)\,\mathbf{1}[t\ge2015]+\mu_r\,\mathbf{1}[t\ge2005]+\kappa_r t+u_{rt} \qquad (24)
$$

where α~r~ are region effects; γ~t~ are year effects that absorb all national influences (policy, prices and weather); μ~r~ absorb the CSO classification break; and κ~r~*t* are region-specific trends, which are included in a second specification. Exposure is the region's dairy share of all cows in 2010–2014, and β is scaled per 10 percentage points. The outcomes are log dairy cows, log livestock units and log imputed livestock emissions.

*Inference with five clusters.* Conventional cluster-robust standard errors are unreliable with five clusters (Cameron et al., 2008). **Randomisation inference** therefore reassigns the five exposure values across regions in all 5! = 120 permutations (Fisher, 1935; Young, 2019):

$$
p_{RI}=\frac{1}{120}\sum_{\pi\in S_5}\mathbf{1}\big(|\hat\beta_\pi|\ge|\hat\beta|\big) \qquad (25)
$$

The **wild cluster bootstrap** imposes β = 0 and flips residuals by region using Webb's six-point weights, *y*\*~rt~ = *ŷ*^(0)^~rt~ + *û*^(0)^~rt~ *w*~r~ with *w*~r~ ∈ {±√1.5, ±1, ±√0.5} (Webb, 2023; *B* = 999).

*Placebo test and event study.* A placebo test dates "abolition" to 2010 using pre-2015 data only; a significant placebo signals differential pre-trends (Rambachan & Roth, 2023). The event-study specification is

$$
y_{rt}=\alpha_r+\gamma_t+\sum_{k\neq2014}\beta_k\,\frac{\text{Exp}_r-\overline{\text{Exp}}}{0.10}\,\mathbf{1}[t=k]+u_{rt},\qquad 2005\le t\le2024 \qquad (26)
$$

## 3.13 Decomposition–regression link

To connect the accounting decomposition with policy, the annual LMDI effects are regressed on changes in the indices:

$$
\Delta E^{k}_t=c+\sum_{j=0}^{1}\pi^{k}_{j}\Delta P_{t-j}+\sum_{j=0}^{1}\rho^{k}_{j}\Delta M_{t-j}+\psi'\Delta X_t+\omega\,d_{2005}+\nu_t \qquad (27)
$$

for *k* ∈ {activity, dairy-herd activity, intensity}. The framework predicts Σπ > 0 for activity and Σρ < 0 for intensity. Estimation uses Newey–West standard errors over 1997–2023 (*n* = 27), and results are reported per 0.1 index units.

## 3.14 Implications of the 2030 ceiling

The livestock numbers compatible with the 2030 sectoral ceiling are computed as

$$
E^{*}_{2030}=0.75\,E_{2018},\qquad I_{2030}=\frac{E_{2024}}{LU_{2024}}\,e^{6g},\qquad LU^{*}_{2030}=\frac{E^{*}_{2030}}{I_{2030}} \qquad (28)
$$

where *g* is the annual log change in emissions per livestock unit. Scenarios use the 2012–2024 Theil–Sen trend or annual reductions of 1%, 2% and 3%. Because the statutory ceiling also covers agricultural fuel, applying it to CRF3 is an approximation.

## 3.15 Supplementary metric: warming-equivalent methane (GWP\*)

As a supplementary perspective, methane is also expressed in CO₂-warming-equivalents using GWP\* (Smith et al., 2021):

$$
E^{*}_t=4.53\,E^{CH_4}_t-4.25\,E^{CH_4}_{t-20} \qquad (29)
$$

The outcome throughout the main analysis remains GWP100.

## 3.16 Reproducibility and verification

A single notebook (`ireland_agri_ghg_analysis.ipynb`) runs the complete analysis, from the raw files to every table and figure, with a fixed random seed (20261019); a full run takes about five minutes. An independent script re-derives every stage. All 30 verification checks pass ({{tab:verification}}). They include re-hashing the 53 loaded files, exact CRF3 identities, the chain-link fit, an exact LMDI residual, an independent ordinary least squares (OLS) reproduction of θ~M~ and θ~P~, and the 2030 target arithmetic.

# 4. Results

The results are presented in the same order as the sections of the study's interactive results platform. Section 4.1 summarises the verdicts on the pre-specified hypotheses. Sections 4.2–4.11 then report, in turn, the policy indices, the trend and break analysis (RQ1), the decomposition (RQ2), the policy-mix model and its counterfactuals (RQ3), robustness, power and timing (including RQ4a), the regional design (RQ4b), the mechanism link, the 2030 ceiling and the GWP\* supplement.

## 4.1 Hypothesis scorecard

{{tab:scorecard}} reports the verdict on each pre-specified hypothesis under the decision rules of {{tab:hypotheses}}.

TAB scorecard | Verdicts on the pre-specified hypotheses

| Hypothesis | Statement | Verdict | Evidence |
|:---|:---|:---|:---|
| H1 | Breaks at 2010 or 2015 | Not supported | Three breaks (2000, 2012, 2020); none within ±1 year of a policy date |
| H2 | Intensity offset < 1 after 2015 | Supported | IO = 0.32 (0.21–0.33 across emission-factor ratios) |
| H3a | Mitigation lowers emissions (θ~M~ < 0) | Not supported | θ~M~ = +0.22, bootstrap *p* = 0.880 |
| H3b | Pressure raises emissions (θ~P~ > 0) | Supported | θ~P~ = +0.46, bootstrap *p* = 0.043 |
| H3c | Offset ratio ≥ 0.5 | Undefined | The point estimate of the mitigation effect is not negative, so the offset ratio cannot be computed |
| H4a | Mandatory instruments have the strongest effect | Not supported | Mandatory θ = +0.25 (*p* = 0.94); only the voluntary sub-index is negative (θ = −0.59, *p* = 0.03) |
| H4b | Exposed regions expanded more after 2015 | Not supported | Significant placebo: divergence began before 2015 |

The headline result is that production pressure is associated with higher emissions and acts through scale, whereas the mitigation portfolio shows no detectable effect on total emissions. A sustained 0.1-unit rise in production pressure is associated with about 5% higher long-run emissions. Because P in 2024 was close to its 2000 level, the net effect of the post-2000 change in P on 2024 emissions is small (+2.2%). The largely voluntary, intensity-oriented mitigation portfolio shows no detectable reduction in total emissions.

## 4.2 The policy indices

{{fig:indices}} plots the annual mitigation index M, the production-pressure index P, the net signal S and the strategy signal G. The mitigation index rose from 0.06 in 2000 to 0.69 in 2024. The pressure index moved only from 0.27 to 0.28, and the net signal from −0.21 to +0.41. P was high until 2004, while coupled headage premia were in force, and fell to 0.04 with decoupling in 2005, leaving only the quota increases. It was then rebuilt step by step through the derogation (from 2007), the quota increases of 2008–2014, quota abolition (2015) and TAMS II. The largest one-year rise in P (+0.078) occurred in 2016, the first full year of quota abolition and of TAMS II. P peaked at 0.35 in 2022 and eased to 0.28 in 2024 as TAMS II ended and the derogation was tightened. M rose in three steps: with the Nitrates Action Programme and the Farm Waste Management Scheme in 2006–2009 (from 0.06 to 0.44); with GLAS, the suckler programmes and the two Origin Green assurance schemes in 2015–2018 (from 0.40 to 0.62); and with the chemical-N maxima and ACRES in 2022–2024 (to 0.69). The strategy signal G was 0.18 under Food Harvest 2020 (2011–2014), 0.17 under Food Wise 2025 (2016–2020) and 0.09 under Food Vision 2030.

FIG indices | Mitigation index M, production-pressure index P, net signal S and strategy signal G, 1990–2024 | fig_indices.png | 6.3
FIGNOTE: Each index is the sum of the instrument scores x = I × s × e × B × w shown in {{fig:scores}}; G is not part of P or S. S above zero indicates that mitigation outweighs pressure on the common scale. Dotted vertical lines mark the five policy events. M is based on provisional coding.

Because both indices rose between 2005 and 2020, the net signal grew far less than mitigation effort. S *fell* from 0.31 in 2009 to 0.17 in 2016 while M rose from 0.44 to 0.50, because P rose faster over the same years; in 45% of the years in which either index rose, both rose together. This pattern is policy incoherence made measurable. By instrument type, the mandatory sub-index dominates M by 2024 (0.44 of 0.69), followed by the voluntary sub-index (0.16) and the incentive sub-index (0.10, down from a 2019 peak of 0.13). As a check on the construction of P, year-to-year changes in P predict growth of the dairy herd (sum of lag 0 and lag 1 coefficients 0.49, *p* = 0.035).

## 4.3 RQ1: Trends and structural breaks

Over the full period there is no monotonic trend. The Theil–Sen slope is −0.06% per year (Mann–Kendall *z* = −0.60, *p* = 0.55; Hamed–Rao-corrected *z* = −0.34, *p* = 0.73). Sub-period trends, by contrast, are strongly significant and opposite in sign ({{tab:mk}}).

TAB mk | Mann–Kendall trend tests on ln CRF3

| Test | *S* | *z* | *p* | Sen slope (% per year) |
|:---|---:|---:|---:|---:|
| Mann–Kendall (original), 1990–2024 | −43 | −0.60 | 0.551 | −0.06 |
| Mann–Kendall (Hamed–Rao), 1990–2024 | −43 | −0.34 | 0.731 | −0.06 |
| Hamed–Rao, 1990–1998 | 36 | 3.65 | < 0.001 | +1.22 |
| Hamed–Rao, 1998–2011 | −87 | −4.71 | < 0.001 | −1.43 |
| Hamed–Rao, 2011–2018 | 28 | 3.34 | < 0.001 | +2.25 |
| Hamed–Rao, 2018–2024 | −7 | −0.90 | 0.368 | −0.82 |

A single trend is firmly rejected (UDmax = 112.4, bootstrap *p* = 0.013), and the BIC selects three breaks ({{tab:bp}}). {{fig:breaks}} shows the fitted segmented trend, and {{tab:regimes}} reports the growth rate of each regime.

TAB bp | Bai–Perron break selection

| *m* | SSR | BIC | *F*(*m* vs 0) | Break years |
|:---|---:|---:|---:|:---|
| 0 | 0.0970 | −199.0 | – | None |
| 1 | 0.0393 | −220.0 | 22.8 | 2006 |
| 2 | 0.0149 | −243.2 | 39.9 | 2000, 2013 |
| **3** | **0.0037** | **−281.0** | **112.4** | **2000, 2012, 2020** |
| 4 | 0.0033 | −274.2 | 87.6 | 2000, 2005, 2012, 2020 |

NOTE: The selected model is shown in bold.

FIG breaks | Observed CRF3 emissions and the Bai–Perron segmented trend with three breaks, 1990–2024 | fig_breaks.png | 6.3
FIGNOTE: Orange segments show the selected model, labelled with each regime's trend growth rate. Dashed lines mark the first year of each new regime, and shaded bands show the 90% bootstrap intervals for the break dates. Dotted grey lines mark Food Harvest 2020 (2010) and quota abolition (2015).

TAB regimes | Emission regimes

| Regime | Trend (% per year) | 90% interval of the break date |
|:---|---:|:---|
| 1990–1999 | +1.06 | – |
| 2000–2011 | −1.25 | 2000–2000 |
| 2012–2019 | +2.00 | 2010–2012 |
| 2020–2024 | −1.86 | 2019–2020 |

Emissions rose by 1.1% a year to 1999, fell by 1.25% a year in 2000–2011, rose by 2.0% a year in 2012–2019 and fell by 1.9% a year from 2020. **None of the break dates lies within a year of 2010 or 2015, so H1 is not supported.** The 2012 upturn begins two years after Food Harvest 2020 and three years before quota abolition. This timing is consistent with expansion in anticipation of abolition during the quota increases of 2009–2014. Known-date Chow tests reject stability at both 2010 (*F* = 16.8, *p* < 0.001) and 2015 (*F* = 20.0, *p* < 0.001). With three breaks in the series, however, these tests cannot attribute the change to either date.

## 4.4 RQ2: What moved emissions? LMDI decomposition

{{tab:lmdi}} and {{fig:lmdiphase}} report the cumulative LMDI factor effects within each policy phase.

TAB lmdi | LMDI factor effects by policy phase (kt CO₂e, cumulative within phase)

| Phase (years) | Activity | Productivity | Intensity | Other | Net change | Intensity offset |
|:---|---:|---:|---:|---:|---:|---:|
| P1 Coupled support (1992–2004) | −633 | +406 | −105 | −34 | −367 | – |
| P2 Decoupling and derogation (2004–2009) | −1,204 | −45 | −380 | −22 | −1,651 | – |
| P3 Food Harvest and quota increases (2009–2014) | +511 | +184 | +175 | +93 | +964 | −0.25 |
| P4 Post-quota expansion (2014–2021) | +2,147 | +840 | −963 | +319 | +2,344 | **0.32** |
| P5 Sectoral ceiling (2021–2023) | −549 | −357 | −297 | −132 | −1,334 | – |

NOTE: IO is defined only when activity + productivity > 0. P2 includes the 2004–2005 classification break (dairy activity −340 kt, partly offset by +191 kt productivity). P5 ends in 2023.

FIG lmdiphase | LMDI decomposition of the change in CRF3 emissions by policy phase, 1992–2023 | fig_lmdi_phase.png | 6.3
FIGNOTE: Bars show cumulative factor effects within each phase; diamonds show the net change in CRF3 (labelled). P1 = coupled support; P2 = decoupling and derogation; P3 = Food Harvest and quota increases; P4 = post-quota expansion; P5 = sectoral ceiling.

After quota abolition, growth in scale and yield (+2,988 kt) outpaced intensity gains (−963 kt), giving **IO = 0.32**. Only about a third of the growth was cancelled. Growth of the dairy herd alone added 1.32 Mt CO₂e in 2014–2021. The result is robust to the dairy/non-dairy emission-factor ratio ({{tab:efsens}}): IO remains between 0.21 and 0.33, and the dairy-herd effect between 1.06 and 1.35 Mt CO₂e. **H2 is supported.**

TAB efsens | Sensitivity of phase P4 to the dairy/non-dairy emission-factor ratio

| EF ratio | P4 dairy-herd effect (kt CO₂e) | P4 intensity offset |
|---:|---:|---:|
| 1.8 | 1,064 | 0.21 |
| 2.2 | 1,216 | 0.28 |
| 2.6 | 1,350 | 0.33 |

Two further patterns stand out. First, in 2009–2014 (P3) intensity *rose* (+175 kt) rather than fell, so the intensity offset was negative. Second, in the phases in which emissions fell (1992–2009 and 2021–2023), they fell mainly because herds and fertiliser use contracted (activity effects of −633, −1,204 and −549 kt), not because intensity improved. The year-by-year decomposition in {{fig:lmdiannual}} confirms that activity effects dominate most annual changes.

FIG lmdiannual | Chained annual LMDI effects on CRF3 emissions, 1993–2023 | fig_lmdi_annual.png | 6.3
FIGNOTE: Stacked bars show the year-on-year contribution of each factor; dots show the annual change in CRF3. Dotted lines separate the policy phases P1–P5.

## 4.5 RQ3: The policy-mix model

**Model selection and fit.** The AICc selects ARDL(1, 0, 0) (AICc = −131.8). The next-best candidates are ARDL(1, 1, 0) and ARDL(1, 0, 1), with AICc = −128.1 and −127.9 ({{tab:laggrid}}). The model is estimated over 1997–2024 (*n* = 28), and its short-run coefficients are reported in {{tab:ardlcoef}}.

TAB ardlcoef | ARDL(1,0,0) short-run coefficients (dependent variable: ln CRF3)

| Term | Coefficient | HAC SE | HAC *p* |
|:---|---:|---:|---:|
| Constant (α) | 3.3759 | 0.8274 | < 0.001 |
| Trend (τ) | −0.0012 | 0.0019 | 0.533 |
| ln *E*(*t*−1) (φ) | 0.6563 | 0.0866 | < 0.001 |
| *M*(*t*) (β~0~) | 0.0765 | 0.0507 | 0.131 |
| *P*(*t*) (γ~0~) | 0.1580 | 0.0566 | 0.005 |
| ln real milk price | 0.0481 | 0.0301 | 0.110 |
| ln real fertiliser price | −0.0529 | 0.0139 | < 0.001 |

NOTE: *n* = 28 (1997–2024). HAC = Newey–West standard errors with two lags.

With φ̂ = 0.656 and γ̂~0~ = 0.158, the long-run pressure multiplier is θ̂~P~ = 0.158 / (1 − 0.656) = **0.460**, and the mitigation multiplier is θ̂~M~ = 0.077 / (1 − 0.656) = **0.223** ({{tab:longrun}}; {{fig:ardl}}).

TAB longrun | Long-run multipliers

| Index | θ | SE (delta, HAC) | HAC *p* (one-sided) | Bootstrap *p* (one-sided) | 90% bootstrap interval | % per +0.1 | SD of index | % per 1 SD |
|:---|---:|---:|---:|---:|:---|---:|---:|---:|
| P | 0.460 | 0.126 | < 0.001 | **0.043** | 0.25 to 0.69 | +4.7 | 0.097 | +4.5 |
| M | 0.223 | 0.153 | 0.927 | **0.880** | −0.06 to 0.56 | +2.3 | 0.237 | +5.4 |

NOTE: One-sided tests are θ~P~ > 0 and θ~M~ < 0. Bootstrap *p*-values come from the restricted bootstrap (*B* = 999); intervals come from the unrestricted bootstrap (999 draws). The interval for θ~P~ excludes zero; the interval for θ~M~ includes zero.

FIG ardl | Long-run multipliers of the ARDL(1,0,0) policy-mix model | fig_ardl.png | 6.3
FIGNOTE: (a) Point estimates with 90% unrestricted-bootstrap intervals. (b) Joint distribution of the 999 bootstrap draws of (θ~M~, θ~P~); the diamond marks the point estimate. θ~P~ is positive in every draw; θ~M~ is positive in most draws.

**Diagnostics.** Every residual diagnostic passes at the 10% level ({{tab:diag}}). The bounds statistic, *F* = 1.17, lies below the I(0) bound at every level (3.03 at 10%), so **the bounds test does not confirm a level relationship**. The unit-root tests ({{tab:unitroots}}) indicate that both indices are stationary in levels (ADF *p* = 0.010 for M and < 0.001 for P), while ln CRF3 is borderline (ADF *p* = 0.10; KPSS *p* = 0.02). The model is therefore best read as a stationary dynamic regression whose long-run multipliers summarise the cumulative response to a sustained change in an index; without a confirmed level relationship they are indicative rather than equilibrium estimates. The hypothesis that the two indices have equal and opposite per-unit effects (Σβ + Σγ = 0) is rejected (*F* = 8.57, *p* = 0.008). In a model with the net signal S alone, θ~S~ = −0.20 (*p* = 0.21).

TAB diag | Residual diagnostics for the ARDL(1,0,0) model

| Diagnostic | Statistic | *p*-value | Result at 10% |
|:---|---:|---:|:---|
| Breusch–Godfrey (2 lags) | 1.60 | 0.228 | Pass |
| Jarque–Bera normality | 1.03 | 0.597 | Pass |
| Breusch–Pagan heteroskedasticity | 0.36 | 0.894 | Pass |
| RESET (squares) | – | 0.763 | Pass |
| CUSUM (OLS residuals) | 0.58 | 0.885 | Pass |

**Interpretation.** A sustained 0.1-unit rise in production pressure is associated with 4.7% higher long-run emissions (bootstrap *p* = 0.043), so **H3b is supported**. The mitigation coefficient has the opposite sign to that hypothesised (+0.22; bootstrap *p* = 0.88), and its 90% interval includes zero, so **H3a is not supported**. A positive association is not plausible as a causal effect of mitigation policy; it reflects the expansion of schemes in the same years as output, that is, reverse timing. All of these estimates are conditional associations rather than causal effects, and the failed bounds test is a further reason to treat the long-run magnitudes as indicative.

## 4.6 RQ3: Counterfactuals and the offset ratio

Holding P at its 2000 level and simulating the fitted ARDL forward shows that **the post-2000 change in production pressure raised 2024 emissions by only 2.2% (90% CI 1.1–3.2%)** ({{fig:cf}}; {{tab:offset}}), because P in 2024 (0.28) was barely above its 2000 level (0.27). The path matters more than the end points. After decoupling, P fell far below its 2000 level, and the model attributes lower emissions to this in 2005–2016; P then rebuilt above its 2000 level, and the model attributes higher emissions to it from 2017. Summed over 2000–2024, the pressure effect is −7.2 Mt CO₂e. The comparison year is therefore decisive: relative to the post-decoupling low of 2005 (P = 0.04), the rebuilding of P to 0.28 corresponds to a long-run effect of about +12%.

FIG cf | Observed CRF3 emissions and model-based counterfactual paths, 2000–2024 | fig_cf.png | 6.3
FIGNOTE: (a) Counterfactual paths simulate the fitted ARDL with one index held at its 2000 value. The shaded gap between the observed (black) and the P-frozen (orange) paths is the model-based effect of the change in production pressure since 2000: negative while P was below its 2000 level (2005–2016) and positive afterwards. (b) Distribution of the effect of the post-2000 change in P on 2024 emissions across 999 unrestricted bootstrap draws; the solid line is the point estimate and the dotted lines bound the 90% interval.

TAB offset | Counterfactual effects of the post-2000 change in each index

| Quantity | Estimate | 90% interval |
|:---|---:|:---|
| Pressure effect on 2024 emissions (%) | +2.2 | 1.1 to 3.2 |
| Mitigation effect on 2024 emissions (%) | +14.4 | −3.8 to 39.1 |
| Cumulative pressure effect, 2000–2024 (kt CO₂e) | −7,239 | – |
| Cumulative mitigation effect, 2000–2024 (kt CO₂e) | +30,080 | – |
| Bootstrap draws with a negative mitigation effect | 109 of 999 | – |
| Offset ratio, 2024 | Undefined | 0.13 to 10.1 (in the 109 valid draws) |

NOTE: The offset ratio is defined only when the mitigation effect is negative; the interval is computed over the bootstrap draws in which it is defined.

Freezing M at its 2000 level yields a counterfactual *below* observed emissions: the rise in M is associated with 14.4% *higher* 2024 emissions, although the 90% interval (−3.8% to 39.1%) includes zero. Only 109 of 999 bootstrap draws give a negative mitigation effect, and the offset ratio in those draws ranges from 0.13 to 10.1. With no negative mitigation effect in the point estimate, the offset ratio is undefined, and **H3c is not supported**. In short, pressure moves emissions in the hypothesised direction, whereas the mitigation portfolio left no detectable reduction to be offset.

## 4.7 Robustness, statistical power and timing

### 4.7.1 Robustness

θ~P~ is positive in **all 17** estimable core specifications and significant at the 10% level in **14** ({{fig:robust}}; {{tab:robustgrid}}). The exceptions are fixed lags (θ~P~ = 0.51, *p* = 0.11), down-weighting the Nitrates Action Programme (0.42, *p* = 0.11) and adding GNI\* and shock-year indicators (0.22, *p* = 0.25), the last because GNI\* is collinear with quota abolition. Adding the strategy signal to P leaves θ~P~ unchanged (0.45, *p* = 0.02). Four of the five leave-one-policy-out runs remain significant, with θ~P~ ranging from 0.35 (omitting the quota increases) to 1.23 (omitting the coupled premia); omitting quota abolition gives θ~P~ = 0.51 (*p* = 0.12). θ~M~ is positive in 14 of 17 specifications but is significantly negative in **two**: when the Nitrates Action Programme is dropped from M (θ~M~ = −0.81, *p* = 0.03) and when the two framework laws are scored in M (θ~M~ = −0.19, *p* = 0.03). The mitigation null therefore depends on how the Nitrates Action Programme, the dominant and water-quality-oriented component of M, and the 2021–2022 climate framework are treated.

FIG robust | Robustness of the long-run multipliers across 17 specifications and 5 leave-one-policy-out runs | fig_robust.png | 6.3
FIGNOTE: Filled circles indicate a one-sided bootstrap *p* < 0.10 (*B* = 299); hollow circles are not significant. Dotted lines mark the baseline estimates. Leave-out rows drop one pressure instrument (P01–P05; see {{tab:codebookP}}) from P at a time; one-sided *p*-values for θ~M~ are not computed for these runs.

### 4.7.2 Statistical power

Nominal 10% HAC tests have a true size of 0.23 for M and 0.26 for P, which confirms the need for bootstrap inference. With size-adjusted critical values, the minimum detectable effect at 80% power is |θ| ≈ 0.43 for M and 0.35 for P, equivalent to about 4.4% and 3.5% per 0.1 index units ({{tab:power}}; {{fig:power}}). Mitigation effects larger than |θ| ≈ 0.43 would very likely have been detected; smaller effects cannot be ruled out.

TAB power | Size-adjusted power by true effect size

| True \|θ\| | 0 | 0.1 | 0.2 | 0.3 | 0.5 | 0.75 | 1.0 | 1.5 |
|:---|---:|---:|---:|---:|---:|---:|---:|---:|
| Power, θ~M~ | 0.10 | 0.20 | 0.42 | 0.60 | 0.91 | 1.00 | 1.00 | 1.00 |
| Power, θ~P~ | 0.10 | 0.29 | 0.47 | 0.75 | 0.97 | 1.00 | 1.00 | 1.00 |

NOTE: Based on 500 simulated series per effect size, with size-adjusted critical values.

FIG power | Size-adjusted power curves for the long-run multipliers | fig_power.png | 4.0
FIGNOTE: The dashed horizontal line marks 80% power; the dotted vertical lines mark the minimum detectable effects (|θ| ≈ 0.43 for M and 0.35 for P).

### 4.7.3 Mitigation by instrument type (RQ4a)

The mandatory sub-index, which the hypothesis expected to be strongest, shows no emission-reducing effect (θ = +0.25, *p* = 0.94), so **H4a is not supported** ({{tab:subindex}}). The voluntary sub-index (Carbon Navigator and the two Origin Green assurance schemes) is negative and significant (θ = −0.59, *p* = 0.03), but it is active in only 12 years, its standard error is large (1.41), and it rose in the same years as the post-quota herd, so the estimate is fragile. The incentive sub-index turns negative only at two- and three-year lags (θ = −1.87 and −2.21), estimates that were not tested formally.

TAB subindex | Mitigation sub-index estimates

| Instrument type | Active years | θ | Bootstrap *p* (θ < 0) | θ at 3-year lag |
|:---|---:|---:|---:|---:|
| Mandatory | 19 | +0.25 | 0.936 | +0.44 |
| Incentive | 28 | +0.58 | 0.784 | −2.21 |
| Voluntary | 12 | −0.59 | 0.030 | −0.67 |

NOTE: Each sub-index is estimated with the remainder of M and the pressure index as controls (*B* = 499).

### 4.7.4 Timing: interrupted time series

**The turning point came in 2010, not 2015** ({{tab:its}}; {{fig:its}}). Controlling for prices, the emission trend steepened by 2.2 percentage points a year after 2010 (*p* < 0.001), and the dairy-herd trend by 4.2 points. Neither trend changed significantly at 2015 (emissions −0.2, *p* = 0.38), although both show a level shift in that year. Expansion began under the quota increases and Food Harvest 2020 and continued at the same pace after abolition.

TAB its | Segmented regression at pre-specified dates (with price controls)

| Outcome | Event | Level change (%) | *p* (level) | Slope change (pp per year) | *p* (slope) |
|:---|:---|---:|---:|---:|---:|
| CRF3 emissions | 2010 | −2.92 | < 0.001 | **+2.25** | < 0.001 |
| CRF3 emissions | 2015 | +3.24 | < 0.001 | −0.20 | 0.384 |
| CRF3 emissions | 2022^†^ | +8.45 | 0.003 | −6.40 | < 0.001 |
| Dairy cows | 2010 | −2.53 | 0.002 | **+4.17** | < 0.001 |
| Dairy cows | 2015 | +5.96 | 0.018 | +0.32 | 0.297 |
| Dairy cows | 2022^†^ | −4.69 | 0.195 | −1.60 | 0.224 |

NOTE: ^†^ Descriptive only (three post-event years). Sample 1995–2024 with HAC standard errors.

FIG its | Change in trend at the pre-specified policy dates | fig_its.png | 4.8
FIGNOTE: Bars show the estimated slope change δ~e~ (percentage points per year) for ln CRF3 and ln dairy cows; labels give the *p*-value. ^†^ The 2022 event is descriptive only.

## 4.8 RQ4b: Regional difference-in-differences

{{tab:did}} reports the continuous-exposure DiD estimates, and {{fig:event}} shows the corresponding event-study coefficients.

TAB did | Continuous-exposure DiD: post-2015 effect per +10 pp of pre-2015 dairy exposure

| Outcome | Specification | % per +10 pp | *p* (RI) | *p* (WCB) | Placebo 2010 (%) | Placebo *p* (RI) | *n* |
|:---|:---|---:|---:|---:|---:|---:|---:|
| log dairy cows | Two-way FE | −0.50 | 0.842 | 0.888 | +2.91 | 0.067 | 170 |
| log dairy cows | TWFE + region trends | −0.69 | 0.567 | 0.638 | +2.77 | 0.042 | 170 |
| log livestock units | Two-way FE | +1.17 | 0.142 | 0.183 | +1.32 | 0.008 | 170 |
| log livestock units | TWFE + region trends | +0.72 | 0.133 | 0.045 | +1.24 | 0.050 | 170 |
| log imputed livestock emissions | Two-way FE | +2.11 | 0.108 | 0.150 | +1.63 | 0.017 | 165 |
| log imputed livestock emissions | TWFE + region trends | +1.28 | 0.075 | 0.049 | +1.51 | 0.008 | 165 |

NOTE: RI = randomisation inference over all 120 permutations; WCB = wild cluster bootstrap with Webb weights (*B* = 999); TWFE = two-way fixed effects.

FIG event | Event-study coefficients for regional dairy exposure, 2005–2024 (2014 = 0) | fig_event.png | 6.3
FIGNOTE: Coefficients are percentage differences per 10 percentage points of pre-2015 dairy exposure, relative to 2014. The shaded band is a 90% interval for imputed livestock emissions based on cluster-robust errors with five clusters and is indicative only. Imputed emissions end in 2023.

In the main specification, imputed livestock emissions rose by 2.1% more per 10 pp of exposure after 2015 (*p*~RI~ = 0.11; *p*~WCB~ = 0.15). However, the event-study gap opens steadily from 2005, and the placebo dated to 2010 (+1.6%, *p*~RI~ = 0.017) is almost as large as the main estimate and is significant. More exposed regions were already diverging before abolition, so the parallel-trends assumption fails and **H4b is not supported**. The region-trend specification for emissions is nominally significant (+1.3%, *p*~RI~ = 0.075, *p*~WCB~ = 0.049), but its placebo is also significant (*p*~RI~ = 0.008), so it cannot be interpreted as an abolition effect either. The dairy herd itself grew no faster in percentage terms in more exposed regions (−0.5% per 10 pp; *p* = 0.84). Post-quota growth was national and came partly from regions with little dairying.

## 4.9 Mechanism: linking the decomposition to policy

{{tab:mech}} and {{fig:mech}} report the regressions of the annual LMDI effects on changes in P and M.

TAB mech | LMDI effects regressed on changes in P and M (sum of lag 0 and lag 1, per +0.1 index units)

| LMDI outcome | Policy | kt CO₂e per +0.1 | SE (per 0.1) | *p* (two-sided) |
|:---|:---|---:|---:|---:|
| Activity effect | ΔP | **+748.0** | 252.3 | **0.008** |
| Activity effect | ΔM | −66.5 | 218.3 | 0.764 |
| Dairy-herd activity effect | ΔP | **+259.1** | 122.8 | **0.048** |
| Dairy-herd activity effect | ΔM | +30.0 | 59.0 | 0.617 |
| Intensity effect | ΔP | −10.2 | 77.5 | 0.897 |
| Intensity effect | ΔM | +28.9 | 84.0 | 0.735 |

NOTE: Newey–West standard errors; 1997–2023, *n* = 27.

FIG mech | Association between annual LMDI effects and changes in the policy indices | fig_mech.png | 5.0
FIGNOTE: Bars show the sum of the contemporaneous and one-year-lagged coefficients, scaled to a +0.1 change in each index, with 90% confidence intervals (Newey–West). The framework predicts positive pressure bars for activity and negative mitigation bars for intensity.

The **pressure half** of the hypothesised division of labour is confirmed. ΔP is associated with the activity effect (+748 kt per 0.1; *p* = 0.008), and in particular with the dairy-herd activity effect (+259 kt per 0.1; *p* = 0.048), but not with the intensity effect (−10 kt; *p* = 0.90). Years of rising pressure were years in which herds and nitrogen inputs grew. The **mitigation half** is not confirmed: ΔM is associated with neither effect, and in particular not with lower intensity (+29 kt; *p* = 0.73).

## 4.10 The 2030 sectoral ceiling

The 2030 target is 0.75 × 20,728 kt (2018) = **15,546 kt CO₂e** (15.5 Mt CO₂e). CRF3 emissions were 19,631 kt CO₂e in 2024, 5.3% below 2018. Emissions per livestock unit rose by 0.37% a year over 2012–2024. {{tab:ceiling}} and {{fig:ceiling}} report the livestock numbers compatible with the ceiling under alternative intensity paths.

TAB ceiling | Livestock units compatible with the 2030 ceiling

| Scenario for emissions per LU, 2024–2030 | Required LU in 2030 (thousand) | Change vs 2024 |
|:---|---:|---:|
| 2012–2024 trend continues (+0.37% per year) | 4,403 | **−22.6%** |
| Intensity falls 1% a year | 4,782 | −15.9% |
| Intensity falls 2% a year | 5,083 | −10.6% |
| Intensity falls 3% a year | 5,405 | −4.9% |

NOTE: Livestock units in 2024 = 5,686 thousand. The statutory ceiling also covers agricultural fuel, so applying it to CRF3 is an approximation.

FIG ceiling | Required change in livestock units, 2024–2030, under alternative intensity scenarios | fig_ceiling.png | 4.8
FIGNOTE: Each bar shows the change in livestock units needed for CRF3 emissions to meet the 2030 ceiling of 15.5 Mt CO₂e under the stated annual change in emissions per livestock unit.

If the recent intensity trend continues, livestock units must fall by about 23% by 2030. Even if intensity falls by 1%, 2% or 3% a year, they must still fall by 16%, 11% or 5%, respectively. An annual fall of 3% would be almost three times the fastest five-year rate of intensity decline observed since 1992 (about 1.1% a year).

## 4.11 Supplementary metric: GWP\*

In 2024, CRF3 methane amounted to 14.6 Mt CO₂e under GWP100 but +5.5 Mt CO₂-we under GWP\*, up from +1.7 Mt CO₂-we in 2015 ({{fig:gwp}}). GWP\* reflects the change in methane's warming contribution rather than its level, and negative values indicate that methane emissions were lower than 20 years earlier. The metric changes the level of the methane series but not the conclusions about which policies moved emissions.

FIG gwp | CRF3 methane under GWP100 and GWP\*, 2010–2024 | fig_gwp.png | 6.3
FIGNOTE: GWP\* converts methane into CO₂-warming-equivalents (CO₂-we) as E\* = 4.53 E(t) − 4.25 E(t − 20) (Smith et al., 2021). The main analysis uses GWP100 throughout.

# 5. Discussion

## 5.1 Expansion with little to offset

Three lines of evidence point in the same direction. First, growth in scale and yield after 2014 outpaced intensity gains by more than three to one (IO = 0.32). Second, production pressure is associated with higher long-run emissions (+4.7% per 0.1), a result that holds in sign in every pre-specified robustness variant and in significance in most of them, and changes in P line up with the activity component of the decomposition, the channel the framework predicts. Third, no emission-reducing effect of mitigation can be detected. The evidence therefore favours a refined version of Explanation B. Production-oriented policy moved emissions through scale, but the mitigation portfolio did not produce a detectable reduction that expansion then cancelled; expansion had little mitigation to offset. Read in this way, Explanation A, that mitigation was weak, also holds as a statement about the *portfolio's* effect on total emissions.

The size of the pressure footprint depends on the comparison chosen. Relative to 2000, when coupled premia were still in force, the 2024 level of pressure is almost unchanged and its net effect on 2024 emissions is small (+2.2%). Relative to the post-decoupling low of 2005, the rebuilding of pressure through the derogation, the quota increases, abolition and TAMS II corresponds to a long-run effect of about 12%. Decoupling removed one expansion instrument; the policies that followed replaced it with others that acted more directly on the dairy herd.

## 5.2 Timing: 2010, not 2015

Three results agree that the trend changed in 2010–2012: the Bai–Perron break in 2012 (90% interval 2010–2012), the interrupted time-series slope change in 2010 rather than 2015, and the regional pre-trends from 2005 onwards. Expansion began under the quota increases and Food Harvest 2020, and abolition continued it rather than starting it. Analyses that treat 2015 as the single turning point therefore understate the importance of the "soft-landing" years, in which the sector positioned itself for a quota-free regime. This qualification complements the farm-level evidence of Läpple et al. (2022) rather than contradicting it.

## 5.3 Why mitigation did not register

Most mitigation instruments were voluntary or incentive-based schemes that acted on intensity, and the main binding instrument, the Nitrates Action Programme, was designed for water quality. A portfolio that acts only on intensity can lower emissions per litre while total emissions rise, and this is precisely what the decomposition shows for 2014–2021. The positive association between M and emissions is best interpreted as reverse timing: schemes such as GLAS grew in the same years as the herd. The power analysis bounds what the data can reveal. Long-run mitigation effects with |θ| above about 0.43 (roughly 4% per 0.1 index units) would very likely have been detected, but smaller beneficial effects cannot be excluded. The mechanism regression adds a further caution: changes in M are not associated with lower intensity, which is the channel through which an intensity-oriented portfolio would have to work. Two robustness results qualify the mitigation null. When the Nitrates Action Programme, designed for water quality and the largest component of M, is removed, the remaining mitigation index is significantly associated with lower emissions; and the voluntary assurance and advisory schemes show a negative association. Both estimates are fragile, but they suggest that the portfolio average may mask instruments with modest beneficial effects.

## 5.4 Relation to stakeholder-identified barriers

Of the five barriers identified by Augustenborg et al. (2026), **policy incoherence** receives quantitative support. P and M rose together over 2005–2020, the net signal fell between 2009 and 2016 even as mitigation effort grew, and P has a detectable association with emissions. **Competing political priorities** are consistent with the regime change around Food Harvest 2020, a growth strategy adopted alongside mitigation commitments (strategy signal G). **Capacity, financial and planning constraints** cannot be separated with these data. In the terms of Marsh and McConnell (2010), the mitigation portfolio shows some *process* success, in that instruments were implemented and their coverage grew, but no detectable *programme* success on total emissions. Its *political* success was limited by the parallel growth agenda.

## 5.5 Policy implications

The findings carry four implications. They are offered as interpretations of the evidence, not as estimated policy effects.

1. **Coherence before additionality.** Because pressure has a detectable association with emissions, acting through scale, and the mitigation portfolio does not, adding further intensity-oriented instruments is unlikely, on its own, to close the gap while expansion incentives remain. Assessing growth instruments (derogations, capital grants for capacity and volume targets) for their emission consequences would address the measured source of the problem.
2. **Targets on totals, not only on intensity.** An intensity offset of 0.32 means that efficiency gains cancelled only about a third of scale growth. Policy framed around emissions per litre can succeed on its own terms while total emissions rise.
3. **The arithmetic of the 2030 ceiling.** On recent trends, compliance implies roughly 16–23% fewer livestock units by 2030 unless intensity falls far faster than has ever been observed. This implication should be stated explicitly in sectoral planning.
4. **Measuring the net signal.** The common I × *s* × *e* × B scale allows governments to track whether new instruments raise mitigation intensity faster than concurrent sectoral policy raises pressure. The index is transferable to other land-based sectors that face growth and decarbonisation mandates at the same time.

## 5.6 Limitations

- **Policy coding.** The mitigation index M uses the authors' coding under the INPACT scoring rule and is to be replaced by the INPACT export. Eligibility shares are anchored on participation statistics but several are graded low or low-to-medium confidence, and three coverage shares (P01, P02 and M11) are transferred from the nearest inventory year. The second coding of P and G is a placeholder that predates the revised codebook, so the reported kappa values do not yet measure reliability. The results are sensitive to the coding of the policy indices: moving from the earlier to the revised codebook reduced θ~P~ from 0.69 to 0.46 and changed the selected lag structure. [AUTHOR INPUT REQUIRED: INPACT export for M; independent second coding of P and G against the revised codebook.]
- **Short national series.** With *n* = 28 in the ARDL, inference rests on the bootstrap and power is limited (MDE ≈ 0.43 for M and 0.35 for P). The bounds test does not confirm a level relationship, so the long-run multipliers are indicative. The results are conditional associations, not causal estimates. The positive M coefficient illustrates the limits of a time-series design when instruments are adopted alongside output growth.
- **No untreated comparator.** Quota abolition and CAP reform applied across the EU. The regional design therefore relies on within-Ireland exposure, and its parallel-trends assumption fails.
- **Five clusters.** Regional inference uses randomisation inference and the wild cluster bootstrap. These methods are appropriate but cannot create information that five units do not contain, and the event-study bands are indicative only.
- **Inventory data.** The LMDI decomposition and the regional emissions end in 2023, because the 2024 CRT split is not yet available. Changes in inventory methodology appear as changes in intensity, and regional emissions are imputed from national implied emission factors.
- **Omitted drivers.** The model includes no weather control, and macroeconomic shocks enter only in one robustness variant, in which GNI\* is collinear with quota abolition.
- **Approximation of the ceiling.** The statutory ceiling includes agricultural fuel, so applying it to CRF3 only approximates the true constraint.

# 6. Conclusion

Three decades of farm climate policy left Irish agricultural emissions almost exactly where they began. This paper places expansion and mitigation policy on a common scale and attributes the flat emission path using three designs whose assumptions fail in different ways. Production-oriented policy is associated with higher emissions and acts through scale: a sustained 0.1-unit rise in pressure is associated with about 5% higher long-run emissions, and changes in pressure track the growth of herds and nitrogen inputs. Because decoupling removed coupled premia before later instruments rebuilt pressure, the net change in pressure between 2000 and 2024 was small, and so is its net effect on 2024 emissions. The largely voluntary, intensity-oriented mitigation portfolio shows no detectable effect on total emissions, so expansion had little mitigation to offset. The turning point came in 2010–2012, under the quota increases and Food Harvest 2020, rather than at abolition in 2015. After abolition, efficiency gains cancelled only a third of scale growth. On current trends, the 2030 ceiling implies 16–23% fewer livestock units unless emission intensity falls far faster than it ever has.

## 6.1 Future research

Several extensions would strengthen the evidence base. On the data side, the provisional mitigation coding should be replaced with the INPACT export for M; the revised P and G codebook should receive independent, blind second coding; the low-confidence eligibility and coverage shares should be refined with DAFM scheme statistics; and the CRT 2026 submission should be used to extend the LMDI decomposition and the regional emissions to 2024. On the design side, a county-level panel built from the Census of Agriculture and DAFM derogation statistics would support a continuous-treatment design (Callaway et al., 2024). The common-scale approach could also be transferred to other jurisdictions in which land-based sectors face growth and decarbonisation mandates at the same time.

# Declarations {.unnumbered}

**Funding.** [AUTHOR INPUT REQUIRED: funding source(s) and grant number(s), e.g. for the INPACT project.]

**Conflicts of interest.** [AUTHOR INPUT REQUIRED: conflict-of-interest statement.]

**Author contributions (CRediT).** [AUTHOR INPUT REQUIRED: contributor roles.]

**Acknowledgements.** [AUTHOR INPUT REQUIRED: optional acknowledgements.]

# Data and Code Availability {.unnumbered}

All numbers in this paper come from a full re-run of `ireland_agri_ghg_analysis.ipynb` (seed 20261019, run on 29 October 2026) with the revised policy codebook. Data come from the EPA, Ireland's CRT 2025 submission to the UNFCCC, the CSO and Eurostat. The annual panel (1990–2024), the result tables and an interactive results platform (covering the research problem, research questions, a dataset explorer, the methods with live calculators, the results and the conclusions) are available from the authors. The platform reads every number from the exported `results.json` file and recomputes nothing except simple arithmetic for its interactive calculators. All figures in this paper were regenerated directly from the same `results.json` file. [AUTHOR INPUT REQUIRED: public repository URL or DOI for the data, code and platform, if they are to be deposited.]

# References {.unnumbered}

::: {custom-style="Bibliography"}
Ang, B. W. (2015). LMDI decomposition approach: A guide for implementation. *Energy Policy*, *86*, 233–238.

Ang, B. W., & Liu, F. L. (2001). A new energy decomposition method: Perfect in decomposition and consistent in aggregation. *Energy*, *26*(6), 537–548.

Augustenborg, C. A., Lentz, P., & Pender, A. (2026). Barriers to environmental policy implementation: Stakeholder perceptions in the context of Ireland. *Journal of Environmental Policy & Planning*, *28*(3), 531–553.

Bai, J., & Perron, P. (2003). Computation and analysis of multiple structural change models. *Journal of Applied Econometrics*, *18*(1), 1–22.

Balaine, L., Läpple, D., Buckley, C., & Dillon, E. (2022). Reconciling socio-economic and environmental sustainability in agri-food development. *EuroChoices*, *21*(2), 52–57.

Bernal, J. L., Cummins, S., & Gasparrini, A. (2017). Interrupted time series regression for the evaluation of public health interventions: A tutorial. *International Journal of Epidemiology*, *46*(1), 348–355.

Bloom, H. S. (1995). Minimum detectable effects: A simple way to report the statistical power of experimental designs. *Evaluation Review*, *19*(5), 547–556.

Callaway, B., Goodman-Bacon, A., & Sant'Anna, P. H. C. (2024). *Difference-in-differences with a continuous treatment* (NBER Working Paper No. 32117). National Bureau of Economic Research.

Cameron, A. C., Gelbach, J. B., & Miller, D. L. (2008). Bootstrap-based improvements for inference with clustered errors. *Review of Economics and Statistics*, *90*(3), 414–427.

Card, D. (1992). Using regional variation in wages to measure the effects of the federal minimum wage. *ILR Review*, *46*(1), 22–37.

Cohen, J. (1968). Weighted kappa: Nominal scale agreement with provision for scaled disagreement or partial credit. *Psychological Bulletin*, *70*(4), 213–220.

Davidson, R., & MacKinnon, J. G. (2000). Bootstrap tests: How many bootstraps? *Econometric Reviews*, *19*(1), 55–68.

Diebold, F. X., & Chen, C. (1996). Testing structural stability with endogenous breakpoint: A size comparison of analytic and bootstrap procedures. *Journal of Econometrics*, *70*(1), 221–241.

Donnellan, T., Hanrahan, K., Breen, J. P., & Gillespie, P. (2013). *Climate change and agricultural policy coherence: Agricultural growth and GHG emissions in Ireland* [Conference paper]. Agricultural Economics Society Annual Conference, Warwick, United Kingdom.

Environmental Protection Agency. (2026). *Ireland's provisional greenhouse gas emissions 1990–2025*. Environmental Protection Agency.

Eskander, S. M. S. U., & Fankhauser, S. (2020). Reduction in greenhouse gas emissions from national climate legislation. *Nature Climate Change*, *10*, 750–756.

Eurostat. (2016). *Handbook on prices and volume measures in national accounts*. Publications Office of the European Union.

Fisher, R. A. (1935). *The design of experiments*. Oliver & Boyd.

Gelman, A., & Carlin, J. (2014). Beyond power calculations: Assessing Type S (sign) and Type M (magnitude) errors. *Perspectives on Psychological Science*, *9*(6), 641–651.

Goldsmith-Pinkham, P., Sorkin, I., & Swift, H. (2020). Bartik instruments: What, when, why, and how. *American Economic Review*, *110*(8), 2586–2624.

Greening, L. A., Greene, D. L., & Difiglio, C. (2000). Energy efficiency and consumption—The rebound effect—A survey. *Energy Policy*, *28*(6–7), 389–401.

Hall, P., Horowitz, J. L., & Jing, B.-Y. (1995). On blocking rules for the bootstrap with dependent data. *Biometrika*, *82*(3), 561–574.

Hamed, K. H., & Rao, A. R. (1998). A modified Mann–Kendall trend test for autocorrelated data. *Journal of Hydrology*, *204*(1–4), 182–196.

Henn, D., et al. (2023). [AUTHOR INPUT REQUIRED: complete reference for this study of herd composition and implied emission factors, including all authors, title, journal, volume, pages and DOI.]

Howlett, M., & Rayner, J. (2013). Patching vs packaging in policy formulation: Assessing policy portfolio design. *Politics and Governance*, *1*(2), 170–182.

Kiefer, N. M., & Vogelsang, T. J. (2005). A new asymptotic theory for heteroskedasticity-autocorrelation robust tests. *Econometric Theory*, *21*(6), 1130–1164.

Läpple, D., Carter, C. A., & Buckley, C. (2022). EU milk quota abolition, dairy expansion, and greenhouse gas emissions. *Agricultural Economics*, *53*(1), 125–142.

Lawlor, D. A., Tilling, K., & Davey Smith, G. (2016). Triangulation in aetiological epidemiology. *International Journal of Epidemiology*, *45*(6), 1866–1886.

Li, H., & Maddala, G. S. (1996). Bootstrapping time series models. *Econometric Reviews*, *15*(2), 115–158.

Marsh, D., & McConnell, A. (2010). Towards a framework for establishing policy success. *Public Administration*, *88*(2), 564–583.

Munafò, M. R., & Davey Smith, G. (2018). Robust research needs many lines of evidence. *Nature*, *553*, 399–401.

Myhre, G., Shindell, D., Bréon, F.-M., Collins, W., Fuglestvedt, J., Huang, J., Koch, D., Lamarque, J.-F., Lee, D., Mendoza, B., Nakajima, T., Robock, A., Stephens, G., Takemura, T., & Zhang, H. (2013). Anthropogenic and natural radiative forcing. In T. F. Stocker, D. Qin, G.-K. Plattner, M. Tignor, S. K. Allen, J. Boschung, A. Nauels, Y. Xia, V. Bex, & P. M. Midgley (Eds.), *Climate change 2013: The physical science basis. Contribution of Working Group I to the Fifth Assessment Report of the Intergovernmental Panel on Climate Change* (pp. 659–740). Cambridge University Press.

Newey, W. K., & West, K. D. (1987). A simple, positive semi-definite, heteroskedasticity and autocorrelation consistent covariance matrix. *Econometrica*, *55*(3), 703–708.

Nilsson, M., Zamparutti, T., Petersen, J. E., Nykvist, B., Rudberg, P., & McGuinn, J. (2012). Understanding policy coherence: Analytical framework and examples of sector–environment policy interactions in the EU. *Environmental Policy and Governance*, *22*(6), 395–423.

OECD, European Commission, & Joint Research Centre. (2008). *Handbook on constructing composite indicators: Methodology and user guide*. OECD Publishing.

Pesaran, M. H., Shin, Y., & Smith, R. J. (2001). Bounds testing approaches to the analysis of level relationships. *Journal of Applied Econometrics*, *16*(3), 289–326.

Rambachan, A., & Roth, J. (2023). A more credible approach to parallel trends. *Review of Economic Studies*, *90*(5), 2555–2591.

Rogge, K. S., & Reichardt, K. (2016). Policy mixes for sustainability transitions: An extended concept and framework for analysis. *Research Policy*, *45*(8), 1620–1635.

Smith, M. A., Cain, M., & Allen, M. R. (2021). Further improvement of warming-equivalent emissions calculation. *npj Climate and Atmospheric Science*, *4*, Article 19.

Stechemesser, A., Koch, N., Mark, E., Dilger, E., Klösel, P., Menicacci, L., Nachtigall, D., Pretis, F., Ritter, N., Schwarz, M., Vossen, H., & Wenzel, A. (2024). Climate policies that achieved major emission reductions: Global evidence from two decades. *Science*, *385*(6711), 884–892.

Stock, J. H., & Watson, M. W. (2020). *Introduction to econometrics* (4th ed.). Pearson.

Torney, D., & O'Gorman, R. (2019). A laggard in good times and bad? The limited impact of EU membership on Ireland's climate change and environmental policy. *Irish Political Studies*, *34*(4), 575–594.

Webb, M. D. (2023). Reworking wild bootstrap-based inference for clustered errors. *Canadian Journal of Economics*, *56*(3), 839–858.

Young, A. (2019). Channeling Fisher: Randomization tests and the statistical insignificance of seemingly significant experimental results. *Quarterly Journal of Economics*, *134*(2), 557–598.

Yue, S., Pilon, P., Phinney, B., & Cavadias, G. (2002). The influence of autocorrelation on the ability to detect trend in hydrological series. *Hydrological Processes*, *16*(9), 1807–1829.
:::

::: {custom-style="Paper Meta"}
[AUTHOR INPUT REQUIRED: add DOIs to the references above, as required by APA 7th edition; DOIs have not been inserted to avoid introducing unverified identifiers.]
:::

PAGEBREAK

# Appendix A. Acronyms and Symbols {.unnumbered}

TAB acronyms=A1 | Acronyms and symbols

| Acronym | Meaning | Note |
|:---|:---|:---|
| ACRES | Agri-Climate Rural Environment Scheme | Agri-environment scheme from 2023 (M10) |
| ADF | Augmented Dickey–Fuller | Unit-root test (null: non-stationary) |
| AEOS | Agri-Environment Options Scheme | Agri-environment scheme 2010–2018 (M04) |
| AIC / AICc | (Corrected) Akaike Information Criterion | Lag selection; AICc corrects for small samples |
| AR(1) | First-order autoregressive process | Error structure under the UDmax null |
| AR5 | IPCC Fifth Assessment Report | Source of GWP100 values |
| ARDL | Autoregressive distributed lag | Policy-mix time-series model |
| BDGP | Beef Data and Genomics Programme | Part of M08 |
| BEEP-S | Beef Environmental Efficiency Programme – Sucklers | Part of M08 |
| BIC | Bayesian Information Criterion | Selects the number of breaks |
| CAP | Common Agricultural Policy | EU farm policy; 2005 decoupling |
| CH₄ / N₂O / CO₂e | Methane / nitrous oxide / CO₂ equivalent | – |
| CI | Confidence interval | 90% unless stated |
| CPI | Consumer price index | Deflator |
| CRF / CRF3 | Common Reporting Format / sector 3 (agriculture) | Outcome boundary |
| CRT | Common Reporting Tables | UNFCCC inventory submission format |
| CSO | Central Statistics Office (Ireland) | Livestock, milk, prices, CPI, GNI* |
| CUSUM | Cumulative sum of recursive residuals | Parameter stability test |
| DAFM | Department of Agriculture, Food and the Marine | Source of scheme participation statistics |
| DiD | Difference-in-differences | Regional design |
| EF | Emission factor | e.g. kg CH₄ per dairy cow per year |
| EPA | Environmental Protection Agency (Ireland) | Inventory compiler |
| GHG | Greenhouse gas | – |
| GISCO | Geographic Information System of the Commission | Regional boundaries |
| GLAS | Green Low-Carbon Agri-Environment Scheme | M07 |
| GNI* | Modified gross national income | Robustness control |
| GWP / GWP100 / GWP* | Global warming potential (100-year) / warming-equivalent metric | – |
| HAC | Heteroskedasticity and autocorrelation consistent | Newey–West covariance |
| I × *s* × *e* × B × *w* | Implementation × coverage × eligibility × bindingness × content weight | Policy score |
| IO | Intensity offset | Share of scale growth cancelled by intensity |
| IPCC | Intergovernmental Panel on Climate Change | – |
| ITS | Interrupted time series | Segmented regression |
| KPSS | Kwiatkowski–Phillips–Schmidt–Shin | Stationarity test |
| LESS | Low Emission Slurry Spreading | Excluded from the M09 baseline |
| LMDI | Logarithmic Mean Divisia Index | Exact decomposition |
| LU / LSU | Livestock unit / Eurostat LSU coefficients | – |
| M / P / S / G | Mitigation index / production-pressure index / net signal / strategy signal | G is not part of P or S |
| MDE | Minimum detectable effect | 80% power |
| NAP | Nitrates Action Programme | M02, M09 |
| NO / NE / NA | Not occurring / not estimated / not applicable | Treated as missing |
| NUTS | Nomenclature of Territorial Units for Statistics | – |
| OLS | Ordinary least squares | – |
| OR | Offset ratio | Defined only if the mitigation effect < 0 |
| REPS | Rural Environment Protection Scheme | M01 |
| RESET | Regression Equation Specification Error Test | Functional form |
| RI | Randomisation inference | Five-region DiD |
| SBLAS | Sustainable Beef and Lamb Assurance Scheme | M11 |
| SCEP | Suckler Carbon Efficiency Programme | Part of M08 |
| SDAS | Sustainable Dairy Assurance Scheme | M06 |
| SE / SD | Standard error / standard deviation | – |
| SHA-256 | Secure Hash Algorithm, 256-bit | File provenance |
| S.I. | Statutory Instrument | Irish secondary legislation |
| SSR | Sum of squared residuals | – |
| TAMS II | Targeted Agricultural Modernisation Scheme II | P05 |
| TWFE | Two-way fixed effects | – |
| UDmax | Unweighted double maximum | Test for any break |
| UNFCCC | United Nations Framework Convention on Climate Change | – |
| WCB | Wild cluster bootstrap | Webb weights |

# Appendix B. Full Robustness Grid {.unnumbered}

Bootstrap *p*-values in {{tab:robustgrid}} use *B* = 299, so the baseline *p*-value differs slightly from the *B* = 999 value reported in the main text.

TAB robustgrid=B1 | Robustness grid for the long-run multipliers

| Variant | *n* | θ~M~ | *p* (θ~M~ < 0) | θ~P~ | *p* (θ~P~ > 0) |
|:---|---:|---:|---:|---:|---:|
| Baseline | 28 | 0.223 | 0.903 | 0.460 | 0.050 |
| No deterministic trend | 28 | 0.122 | 0.947 | 0.436 | 0.043 |
| Fixed lags ARDL(1,1,1) | 28 | 0.226 | 0.837 | 0.507 | 0.110 |
| Equal bindingness (*B* = 1) | 28 | 0.101 | 0.793 | 0.196 | 0.090 |
| Drop Nitrates Action Programme from M | 28 | −0.814 | 0.030 | 0.788 | 0.080 |
| NAP weighted by climate relevance 0.5 | 28 | 0.173 | 0.730 | 0.424 | 0.110 |
| Strategies added to P (P + G) | 28 | 0.242 | 0.893 | 0.455 | 0.023 |
| Quota abolition *B* = 0.75 | 28 | 0.266 | 0.880 | 0.500 | 0.063 |
| SDAS *B* = 0.50 | 28 | 0.223 | 0.887 | 0.438 | 0.080 |
| Event markers E01, E02 scored in M (*B* = 0.25) | 28 | −0.191 | 0.033 | 0.483 | 0.087 |
| Extended controls (GNI*, 2018 and 2022 indicators) | 28 | 0.077 | 0.653 | 0.220 | 0.247 |
| Milk-to-feed price ratio as control | 28 | 0.214 | 0.823 | 0.594 | 0.067 |
| Static model (*p* = 0) | 28 | 0.113 | 0.777 | 0.394 | 0.003 |
| Pre-ceiling sample (to 2021) | 25 | 0.180 | 0.837 | 0.436 | 0.093 |
| CH₄-only outcome | 28 | 0.218 | 0.840 | 0.573 | 0.053 |
| N₂O-only outcome | 28 | 0.152 | 0.823 | 0.345 | 0.047 |
| First differences (static) | 28 | −0.014 | 0.413 | 0.143 | 0.013 |
| Leave out P01 Coupled livestock premia | 28 | −0.039 | – | 1.235 | 0.043 |
| Leave out P02 Milk quota increases | 28 | 0.134 | – | 0.348 | 0.060 |
| Leave out P03 Nitrates derogation | 28 | 0.271 | – | 0.467 | 0.070 |
| Leave out P04 EU milk quota abolition | 28 | 0.431 | – | 0.512 | 0.120 |
| Leave out P05 TAMS II Dairy Equipment Scheme | 28 | 0.279 | – | 0.454 | 0.070 |

# Appendix C. ARDL Lag-Selection Grid {.unnumbered}

TAB laggrid=C1 | ARDL lag-selection grid (common sample 1997–2024, *n* = 28)

| *p* | *q*~M~ | *q*~P~ | Parameters *k* | AICc |
|---:|---:|---:|---:|---:|
| **1** | **0** | **0** | **7** | **−131.82** (selected) |
| 1 | 1 | 0 | 8 | −128.05 |
| 1 | 0 | 1 | 8 | −127.94 |
| 1 | 1 | 1 | 9 | −123.90 |
| 1 | 2 | 0 | 9 | −123.63 |
| 1 | 0 | 2 | 9 | −123.57 |
| 1 | 2 | 1 | 10 | −119.01 |
| 1 | 1 | 2 | 10 | −118.96 |
| 1 | 2 | 2 | 11 | −113.46 |
| 0 | 0 | 2 | 8 | −112.54 |
| 0 | 1 | 1 | 8 | −110.37 |
| 0 | 1 | 2 | 9 | −109.48 |
| 0 | 0 | 1 | 7 | −108.75 |
| 0 | 2 | 2 | 10 | −107.13 |
| 0 | 2 | 1 | 9 | −106.92 |
| 0 | 0 | 0 | 6 | −104.02 |
| 0 | 1 | 0 | 7 | −103.33 |
| 0 | 2 | 0 | 8 | −99.40 |

# Appendix D. Independent Workflow Verification {.unnumbered}

TAB verification=D1 | Independent workflow verification (30 of 30 checks pass)

| Stage | Check | Result |
|:---|:---|:---|
| 1 Load | SHA-256 of every loaded file matches the provenance sheet | 53 files re-hashed; no mismatch |
| 1 Load | Only documented provisional inputs are loaded | Only `pressure_codebook_coder2_PROVISIONAL` |
| 2 Livestock | CSO tables cover disjoint years | 1991–2004 / 2005–2014 / 2015–2026 |
| 2 Livestock | Panel dairy cows equal CSO State totals | Maximum difference 0 |
| 2 Livestock | Five constant-boundary units sum to the State | Dairy 0.014%, cattle 0.004%, sheep 0.003% |
| 2 Livestock | 1990 livestock left missing | NaN (never imputed) |
| 2 Livestock | LU = 1.0·dairy + Eurostat LSU + 0.1·sheep | LSU per non-dairy head 0.632–0.682 |
| 3 Prices | Chain-link overlaps fit | Maximum deviation 2.88% across 20 links |
| 3 Prices | Linked indices and CPI equal 100 in 2020 | Exact |
| 3 Prices | Real price = nominal / CPI × 100 | Exact |
| 4 Emissions | CRF3 = Agriculture − 1.A.4.c.ii − 1.A.4.c.iii | 19,760.0 (1990); 19,631.2 (2024) kt CO₂e |
| 4 Emissions | CRF3 = sum of 5 categories (≤ 0.0001%) | Gap 0 |
| 4 Emissions | CRF3 = CO₂ + CH₄ + N₂O (≤ 0.0001%) | Gap 2 × 10⁻¹⁴ % |
| 5 CRT | 34 workbooks, 1990–2023, no gaps | Complete |
| 5 CRT | Panel split equals CRT Table 3 rows | 1990–2023 |
| 5 CRT | 2024 split left missing | NaN (never imputed) |
| 5 CRT | CRT cattle CH₄ vs Eurostat | 1990–2020 ≤ 0.004%; 2021–23 ≤ 0.21% |
| 5 CRT | Table 3.D unit is kg N | kg / 1,000 = Eurostat t N exactly, 2000–05 |
| 5 CRT | Panel mineral N 1990–1999 = CRT | 379,311 t (1990); 442,916 t (1999) |
| 5 CRT | Manure N = CRT rates × CSO head counts; 2024 missing | 2023: 108.4 / 48.1 / 7.52 kg N per head |
| 6 Panel | 35 unique years, 1990–2024 | Pass |
| 6 Panel | No weather variable | Pass |
| 7 Indices | M, P and G recomputed independently (I × *s* × *e* × B × *w*) | P~2024~ 0.2812; M~2024~ 0.6933; G~2024~ 0.0877 |
| 8 LMDI | Annual effects sum exactly to ΔCRF3 | Residual 1.9 × 10⁻¹¹ kt |
| 9 ARDL | θ~M~, θ~P~ reproduced by an independent OLS | ARDL(1,0,0): θ~M~ 0.2227, θ~P~ 0.4598, *n* = 28 |
| 9 ARDL | `key_results.json` = `results.xlsx` | Pass |
| 10 Ceiling | 2030 target = 0.75 × CRF3~2018~ | 15,546.2 kt CO₂e |
| 11 Outputs | 34 sheets; 7 figures in PNG and PDF | Pass |
| 11 Outputs | Provisional inputs listed in the JSON | Coder-2 placeholder scores (kappa only) |

# Appendix E. Unit-Root Tests {.unnumbered}

TAB unitroots=E1 | Unit-root tests

| Variable | Form | ADF statistic | ADF *p* | KPSS statistic | KPSS *p* |
|:---|:---|---:|---:|---:|---:|
| ln CRF3 | Level | −3.13 | 0.100 | 0.185 | 0.022 |
| ln CRF3 | First difference | −3.22 | 0.019 | 0.168 | > 0.10 |
| M | Level | −3.98 | 0.009 | 0.072 | > 0.10 |
| M | First difference | −3.01 | 0.034 | 0.087 | > 0.10 |
| P | Level | −6.62 | < 0.001 | 0.156 | 0.042 |
| P | First difference | −4.51 | < 0.001 | 0.103 | > 0.10 |
| ln real milk price | Level | −3.12 | 0.101 | 0.218 | 0.010 |
| ln real milk price | First difference | −6.62 | < 0.001 | 0.346 | > 0.10 |
| ln real fertiliser price | Level | −2.96 | 0.143 | 0.064 | > 0.10 |
| ln real fertiliser price | First difference | −5.89 | < 0.001 | 0.500 | 0.042 |
