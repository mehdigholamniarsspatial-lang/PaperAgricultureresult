"""Step 6 – discussion, policy implications, limitations and next steps."""
from dash import html

from ..components import page_header, section, card, callout, kpi, kpi_row, details
from ..data_store import KEY

REFS = [
    'Abadie, A. (2021). Using synthetic controls: Feasibility, data requirements, and methodological aspects. Journal of Economic Literature, 59(2), 391–425. https://doi.org/10.1257/jel.20191450',
    "Abadie, A., Diamond, A., & Hainmueller, J. (2010). Synthetic control methods for comparative case studies: Estimating the effect of California's tobacco control program. Journal of the American Statistical Association, 105(490) , 493–505.",
    'Andersson, J. J. (2019). Carbon taxes and CO₂ emissions: Sweden as a case study. American Economic Journal: Economic Policy, 11(4), 1–30. https://doi.org/10.1257/pol.20170144',
    'Ang, B. W. (2015). LMDI decomposition approach: A guide for implementation. Energy Policy, 86, 233–238.',
    'Ang, B. W., & Liu, F. L. (2001). A new energy decomposition method: Perfect in decomposition and consistent in aggregation. Energy, 26(6), 537–548.',
    'Augustenborg, C. A., Lentz, P., & Pender, A. (2026). Barriers to environmental policy implementation: Stakeholder perceptions in the context of Ireland. Journal of Environmental Policy & Planning, 28(3), 531–553.',
    'Bai, J., & Perron, P. (2003). Computation and analysis of multiple structural change models. Journal of Applied Econometrics, 18(1), 1–22.',
    'Balaine, L., Dillon, E. J., Läpple, D., & Lynch, J. (2020). Can technology help achieve sustainable intensification? Evidence from milk recording on Irish dairy farms. Land Use Policy, 92, Article 104437. https://doi.org/10.1016/j.landusepol.2019.104437',
    'Balaine, L., Läpple, D., Buckley, C., & Dillon, E. (2022). Reconciling socio-economic and environmental sustainability in agri-food development. EuroChoices, 21(2), 52–57.',
    'Batáry, P., Dicks, L. V., Kleijn, D., & Sutherland, W. J. (2015). The role of agri-environment schemes in conservation and environmental management. Conservation Biology, 29(4), 1006–1016. https://doi.org/10.1111/cobi.12536',
    'Bloom, H. S. (1995). Minimum detectable effects: A simple way to report the statistical power of experimental designs. Evaluation Review, 19(5), 547–556.',
    "Callaway, B., Goodman-Bacon, A., & Sant'Anna, P. H. C. (2024). Difference-in-differences with a continuous treatment (NBER Working Paper No. 32117). National Bureau of Economic Research.",
    'Cameron, A. C., Gelbach, J. B., & Miller, D. L. (2008). Bootstrap-based improvements for inference with clustered errors. Review of Economics and Statistics, 90(3), 414–427.',
    'Candel, J. J. L., & Biesbroek, R. (2016). Toward a processual understanding of policy integration. Policy Sciences . https://doi.org/10.1007/s11077-016-9248-y',
    'Card, D. (1992). Using regional variation in wages to measure the effects of the federal minimum wage. ILR Review, 46(1), 22–37.',
    'Climate Action and Low Carbon Development (Amendment) Act 2021, No. 32 of 2021 (Ireland). https://www.irishstatutebook.ie/eli/2021/act/32/',
    'Climate Change Advisory Council. (2025). Annual review 2025: Summary for all. https://www.climatecouncil.ie/councilpublications/annualreviewandreport/CCAC-AR-2025-SfA-final.pdf',
    'Cohen, J. (1968). Weighted kappa: Nominal scale agreement with provision for scaled disagreement or partial credit. Psychological Bulletin, 70(4), 213–220.',
    'Crippa, M., Solazzo, E., Guizzardi, D., Monforti-Ferrario, F., Tubiello, F. N., & Leip, A. (2021). Food systems are responsible for a third of global anthropogenic GHG emissions. Nature Food, 2(3), 198–209. https://doi.org/10.1038/s43016-021-00225-9',
    "Cullen, P., Hynes, S., Ryan, M., & O'Donoghue, C. (2021). More than two decades of agri-environment schemes: Has the profile of participating farms changed? Journal of Environmental Management, 292, Article 112826. https://doi.org/10.1016/j.jenvman.2021.112826",
    "Dai, X.-W., Sun, Z., & Müller, D. (2021). Driving factors of direct greenhouse gas emissions from China's pig industry from 1976 to 2016. Journal of Integrative Agriculture . https://doi.org/10.1016/S2095-3119(20)63425-6",
    "Daugbjerg, C., & Swinbank, A. (2016). Three decades of policy layering and politically sustainable reform in the European Union's agricultural policy. Governance . https://doi.org/10.1111/gove.12171",
    'Davidson, R., & MacKinnon, J. G. (2000). Bootstrap tests: How many bootstraps? Econometric Reviews, 19(1), 55–68.',
    'DeBoe, G., Deconinck, K., Henderson, B., & Lankoski, J. (2020). Reforming agricultural policies will help to improve environmental performance. EuroChoices, 19(1), 30–35. https://doi.org/10.1111/1746-692X.12247',
    'Department of Agriculture, Fisheries and Food. (2010). Food Harvest 2020: A vision for Irish agri-food and fisheries.',
    'Department of Agriculture, Food and the Marine. (2015). Food Wise 2025. https://www.gov.ie/en/department-of-agriculture-food-and-the-marine/publications/food-wise-2025/',
    'Department of Agriculture, Food and the Marine. (2021a). Food Vision 2030: A world leader in sustainable food systems.',
    'Department of Agriculture, Food and the Marine. (2021b, August 3). Launch of "Food Vision 2030—A world leader in sustainable food systems". https://www.gov.ie/en/department-of-agriculture-food-and-the-marine/press-releases/launch-of-food-vision-2030-a-world-leader-in-sustainable-food-systems/',
    'Department of the Taoiseach. (2022, July 28). Government announces sectoral emissions ceilings, setting Ireland on a pathway to turn the tide on climate change. https://www.gov.ie/en/department-of-the-taoiseach/press-releases/government-announces-sectoral-emissions-ceilings-setting-ireland-on-a-pathway-to-turn-the-tide-on-climate-change/',
    'Diebold, F. X., & Chen, C. (1996). Testing structural stability with endogenous breakpoint: A size comparison of analytic and bootstrap procedures. Journal of Econometrics, 70(1), 221–241.',
    'Donnellan, T., Hanrahan, K., Breen, J. P., & Gillespie, P. (2013). Climate change and agricultural policy coherence: Agricultural growth and GHG emissions in Ireland [Conference paper]. Agricultural Economics Society Annual Conference, Warwick, United Kingdom.',
    'Ellerman, A. D., & Wing, I. S. (2003). Absolute versus intensity-based emission caps. Climate Policy, 3(Suppl. 2), S7–S20. https://doi.org/10.1016/j.clipol.2003.09.013',
    "Environmental Protection Agency. (2026a). Ireland's provisional greenhouse gas emissions 1990–2025 [Data workbook]. Environmental Protection Agency.",
    "Environmental Protection Agency. (2026b). Ireland's final greenhouse gas emissions 1990–2024. https://www.epa.ie/publications/monitoring--assessment/climate-change/air-emissions/EPA-Final-GHG-Emissions-Report-1990-2024.pdf",
    'Eskander, S. M. S. U., & Fankhauser, S. (2020). Reduction in greenhouse gas emissions from national climate legislation. Nature Climate Change, 10, 750–756.',
    'European Commission. (2022). Commission Implementing Decision (EU) 2022/696 of 29 April 2022 granting a derogation requested by Ireland pursuant to Council Directive 91/676/EEC concerning the protection of waters against pollution caused by nitrates from agricultural sources (notified under document C(2022) 2596). Official Journal of the European Union, L 129, 37–45. https://eur-lex.europa.eu/eli/dec_impl/2022/696/oj/eng',
    'European Court of Auditors. (2021). Common Agricultural Policy and climate: Half of EU climate spending but farm emissions are not decreasing (Special Report No. 16/2021). Publications Office of the European Union. https://op.europa.eu/webpub/eca/special-reports/cap-and-climate-16-2021/en/',
    'European Environment Agency. (2025, November 6). Greenhouse gas emissions from agriculture in Europe [Indicator]. https://www.eea.europa.eu/en/analysis/indicators/greenhouse-gas-emissions-from-agriculture',
    'European Environment Agency. (2026). Greenhouse gas emissions—Trends and drivers in the EU agricultural sector (EEA Report No. 09/2026). Publications Office of the European Union. https://doi.org/10.2800/9890535',
    'Eurostat. (2016). Handbook on prices and volume measures in national accounts. Publications Office of the European Union.',
    'Fellmann, T., Witzke, P., Weiss, F., Van Doorslaer, B., Drabik, D., Huck, I., Salputra, G., Jansson, T., & Leip, A. (2018). Major challenges of integrating agriculture into climate change mitigation policy frameworks. Mitigation and Adaptation Strategies for Global Change, 23(3), 451–468. https://doi.org/10.1007/s11027-017-9743-2',
    "Finn, J. A., & Ó hUallacháin, D. (2012). A review of evidence on the environmental impact of Ireland's Rural Environment Protection Scheme (REPS). Biology and Environment: Proceedings of the Royal Irish Academy, 112B, 1–24. https://doi.org/10.3318/BIOE.2011.19",
    'Fisher, R. A. (1935). The design of experiments. Oliver & Boyd.',
    'Gelman, A., & Carlin, J. (2014). Beyond power calculations: Assessing Type S (sign) and Type M (magnitude) errors. Perspectives on Psychological Science, 9(6), 641–651.',
    'Gerber, P., Vellinga, T., Opio, C., & Steinfeld, H. (2011). Productivity gains and greenhouse gas emissions intensity in dairy systems. Livestock Science, 139(1–2) , 100–108.',
    'Goldsmith-Pinkham, P., Sorkin, I., & Swift, H. (2020). Bartik instruments: What, when, why, and how. American Economic Review, 110(8), 2586–2624.',
    'Greening, L. A., Greene, D. L., & Difiglio, C. (2000). Energy efficiency and consumption—The rebound effect—A survey. Energy Policy, 28(6–7), 389–401.',
    'Hall, P., Horowitz, J. L., & Jing, B.-Y. (1995). On blocking rules for the bootstrap with dependent data. Biometrika, 82(3), 561–574.',
    'Hamed, K. H., & Rao, A. R. (1998). A modified Mann–Kendall trend test for autocorrelated data. Journal of Hydrology, 204(1–4), 182–196.',
    'Hasler, B., Termansen, M., Nielsen, H. Ø., Daugbjerg, C., Wunder, S., & Latacz-Lohmann, U. (2022). European agri-environmental policy: Evolution, effectiveness, and challenges. Review of Environmental Economics and Policy, 16(1), 105–125. https://doi.org/10.1086/718212',
    'Henderson, B., & Lankoski, J. (2021). Assessing the environmental impacts of agricultural policies. Applied Economic Perspectives and Policy, 43(4), 1487–1502. https://doi.org/10.1002/aepp.13081',
    'Herrero, M., Henderson, B., Havlík, P., Thornton, P. K., Conant, R. T., Smith, P., Wirsenius, S., Hristov, A. N., Gerber, P., Gill, M., Butterbach-Bahl, K., Valin, H., Garnett, T., & Stehfest, E. (2016). Greenhouse gas mitigation potentials in the livestock sector. Nature Climate Change, 6(5), 452–461. https://doi.org/10.1038/nclimate2925',
    'Hertel, T. W., Ramankutty, N., & Baldos, U. L. C. (2014). Global market integration increases likelihood that a future African Green Revolution could increase crop land use and CO₂ emissions. Proceedings of the National Academy of Sciences of the United States of America . https://doi.org/10.1073/pnas.1403543111',
    'Himics, M., Fellmann, T., Barreiro-Hurlé, J., Witzke, H.-P., Pérez Domínguez, I., Jansson, T., & Weiss, F. (2018). Does the current trade liberalization agenda contribute to greenhouse gas emission mitigation in agriculture? Food Policy, 76, 120–129. https://doi.org/10.1016/j.foodpol.2018.01.011',
    'Howlett, M., & del Río, P. (2015). The parameters of policy portfolios: Verticality and horizontality in design spaces and their consequences for policy mix formulation. Environment and Planning C: Government and Policy, 33(5), 1233–1245. https://doi.org/10.1177/0263774X15610059',
    'Howlett, M., & Rayner, J. (2013). Patching vs packaging in policy formulation: Assessing policy portfolio design. Politics and Governance, 1(2), 170–182.',
    'Huitema, D., Jordan, A., Massey, E., Rayner, T., van Asselt, H., Haug, C., Hildingsson, R., Monni, S., & Stripple, J. (2011). The evaluation of climate policy: Theory and emerging practice in Europe. Policy Sciences, 44(2), 179–198. https://doi.org/10.1007/s11077-011-9125-7',
    'Intergovernmental Panel on Climate Change. (2022). Climate change 2022: Mitigation of climate change. Contribution of Working Group III to the Sixth Assessment Report of the Intergovernmental Panel on Climate Change (P. R. Shukla, J. Skea, R. Slade, A. Al Khourdajie, R. van Diemen, D. McCollum, M. Pathak, S. Some, P. Vyas, R. Fradera, M. Belkacemi, A. Hasija, G. Lisboa, S. Luz, & J. Malley, Eds.). Cambridge University Press. https://doi.org/10.1017/9781009157926',
    'Jansson, T., Nordin, I., Wilhelmsson, F., Witzke, P., Manevska-Tasevska, G., Weiss, F., & Gocht, A. (2021). Coupled agricultural subsidies in the EU undermine climate efforts. Applied Economic Perspectives and Policy, 43(4), 1503–1519. https://doi.org/10.1002/aepp.13092',
    'Jongeneel, R., & Gonzalez-Martinez, A. R. (2022). The role of market drivers in explaining the EU milk supply after the milk quota abolition. Economic Analysis and Policy, 73, 194–209. https://doi.org/10.1016/j.eap.2021.11.020',
    'Kiefer, N. M., & Vogelsang, T. J. (2005). A new asymptotic theory for heteroskedasticity-autocorrelation robust tests. Econometric Theory, 21(6), 1130–1164.',
    'Koch, N., Naumann, L., Pretis, F., Ritter, N., & Schwarz, M. (2022). Attributing agnostically detected large reductions in road CO₂ emissions to policy mixes. Nature Energy, 7, 844–853. https://doi.org/10.1038/s41560-022-01095-6',
    "Lanigan, G., Black, K., Donnellan, T., Crosson, P., Beausang, C., Hanrahan, K., Buckley, C., Lahart, B., Herron, J., Redmond, J., Shalloo, L., Krol, D., Forrestal, P., Farrelly, N., O'Brien, D., Lenehan, J. J., Hennessy, M., O'Donovan, M., Wall, D., … Richards, K. (2023). MACC 2023: An updated analysis of the greenhouse gas abatement potential of the Irish agriculture and land-use sectors between 2021 and 2030. Teagasc. https://teagasc.ie/wp-content/uploads/media/website/environment/climate-action/climate-centre/MACC-2023.pdf",
    'Läpple, D., Carter, C. A., & Buckley, C. (2022). EU milk quota abolition, dairy expansion, and greenhouse gas emissions. Agricultural Economics, 53(1), 125–142.',
    'Lawlor, D. A., Tilling, K., & Davey Smith, G. (2016). Triangulation in aetiological epidemiology. International Journal of Epidemiology, 45(6), 1866–1886.',
    'Leahy, S., Clark, H., & Reisinger, A. (2020). Challenges and prospects for agricultural greenhouse gas mitigation pathways consistent with the Paris Agreement. Frontiers in Sustainable Food Systems, 4, Article 69. https://doi.org/10.3389/fsufs.2020.00069',
    'Li, H., & Maddala, G. S. (1996). Bootstrapping time series models. Econometric Reviews, 15(2), 115–158.',
    'Lopez Bernal, J., Cummins, S., & Gasparrini, A. (2017). Interrupted time series regression for the evaluation of public health interventions: A tutorial. International Journal of Epidemiology, 46(1), 348–355. https://doi.org/10.1093/ije/dyw098',
    'von Lüpke, H., Azevedo-Ramos, C., Laraswati, D., Maryudi, A., Ayu, C., Wijaya, N., Sopaheluwakan, R., Kübler, D., & Fischer, R. (2026). Coherence between climate and land use policies of the European Union, Brazil, and Indonesia: A primer to analyze potential GHG leakage. Environmental Policy and Governance, 36(4), 871–886. https://doi.org/10.1002/eet.70084',
    'Marsh, D., & McConnell, A. (2010). Towards a framework for establishing policy success. Public Administration, 88(2), 564–583.',
    'Munafò, M. R., & Davey Smith, G. (2018). Robust research needs many lines of evidence. Nature, 553, 399–401.',
    'Myhre, G., Shindell, D., Bréon, F.-M., Collins, W., Fuglestvedt, J., Huang, J., Koch, D., Lamarque, J.-F., Lee, D., Mendoza, B., Nakajima, T., Robock, A., Stephens, G., Takemura, T., & Zhang, H. (2013). Anthropogenic and natural radiative forcing. In T. F. Stocker, D. Qin, G.-K. Plattner, M. Tignor, S. K. Allen, J. Boschung, A. Nauels, Y. Xia, V. Bex, & P. M. Midgley (Eds.), Climate change 2013: The physical science basis. Contribution of Working Group I to the Fifth Assessment Report of the Intergovernmental Panel on Climate Change (pp. 659–740). Cambridge University Press.',
    'Nabuurs, G.-J., Mrabet, R., Abu Hatab, A., Bustamante, M., Clark, H., Havlík, P., House, J., Mbow, C., Ninan, K. N., Popp, A., Roe, S., Sohngen, B., & Towprayoon, S. (2022). Agriculture, forestry and other land uses (AFOLU). In P. R. Shukla, J. Skea, R. Slade, A. Al Khourdajie, R. van Diemen, D. McCollum, M. Pathak, S. Some, P. Vyas, R. Fradera, M. Belkacemi, A. Hasija, G. Lisboa, S. Luz, & J. Malley (Eds.), Climate change 2022: Mitigation of climate change. Contribution of Working Group III to the Sixth Assessment Report of the Intergovernmental Panel on Climate Change . Cambridge University Press. https://doi.org/10.1017/9781009157926.009',
    'Newey, W. K., & West, K. D. (1987). A simple, positive semi-definite, heteroskedasticity and autocorrelation consistent covariance matrix. Econometrica, 55(3), 703–708.',
    'Nilsson, M., Zamparutti, T., Petersen, J. E., Nykvist, B., Rudberg, P., & McGuinn, J. (2012). Understanding policy coherence: Analytical framework and examples of sector–environment policy interactions in the EU. Environmental Policy and Governance, 22(6), 395–423.',
    "O'Brien, D., Brennan, P., Humphreys, J., Ruane, E., & Shalloo, L. (2014). An appraisal of carbon footprint of milk from commercial grass-based dairy farms in Ireland according to a certified life cycle assessment methodology. The International Journal of Life Cycle Assessment, 19(7), 1469–1481. https://doi.org/10.1007/s11367-014-0755-9",
    'OECD, European Commission, & Joint Research Centre. (2008). Handbook on constructing composite indicators: Methodology and user guide. OECD Publishing.',
    'Organisation for Economic Co-operation and Development. (2019). Enhancing climate change mitigation through agriculture. OECD Publishing. https://doi.org/10.1787/e9a79226-en',
    'Organisation for Economic Co-operation and Development. (2022). Agricultural policy monitoring and evaluation 2022: Reforming agricultural policies for climate change mitigation. OECD Publishing. https://doi.org/10.1787/7f4542bf-en',
    "Pe'er, G., Bonn, A., Bruelheide, H., Dieker, P., Eisenhauer, N., Feindt, P. H., Hagedorn, G., Hansjürgens, B., Herzon, I., Lomba, Â., Marquard, E., Moreira, F., Nitsch, H., Oppermann, R., Perino, A., Röder, N., Schleyer, C., Schindler, S., Wolf, C., … Lakner, S. (2020). Action needed for the EU Common Agricultural Policy to address sustainability challenges. People and Nature, 2(2), 305–316. https://doi.org/10.1002/pan3.10080",
    'Pesaran, M. H., Shin, Y., & Smith, R. J. (2001). Bounds testing approaches to the analysis of level relationships. Journal of Applied Econometrics, 16(3), 289–326.',
    'Pfeiffer, L., & Lin, C.-Y. C. (2014). Does efficient irrigation technology lead to reduced groundwater extraction? Empirical evidence. Journal of Environmental Economics and Management, 67(2), 189–208. https://doi.org/10.1016/j.jeem.2013.12.002',
    'Pretis, F. (2022). Does a carbon tax reduce CO₂ emissions? Evidence from British Columbia. Environmental and Resource Economics, 83(1), 115–144. https://doi.org/10.1007/s10640-022-00679-w',
    'Rambachan, A., & Roth, J. (2023). A more credible approach to parallel trends. Review of Economic Studies, 90(5), 2555–2591.',
    'Regina, K., Budiman, A., Greve, M. H., Grønlund, A., Kasimir, Å., Lehtonen, H., Petersen, S. O., Smith, P., & Wösten, H. (2016). GHG mitigation of agricultural peatlands requires coherent policies. Climate Policy, 16(4), 522–541. https://doi.org/10.1080/14693062.2015.1022854',
    'Rogge, K. S., & Reichardt, K. (2016). Policy mixes for sustainability transitions: An extended concept and framework for analysis. Research Policy, 45(8), 1620–1635.',
    'Schoenefeld, J., & Jordan, A. (2017). Governing policy evaluation? Towards a new typology. Evaluation, 23(3), 274–293. https://doi.org/10.1177/1356389017715366',
    'Smith, M. A., Cain, M., & Allen, M. R. (2021). Further improvement of warming-equivalent emissions calculation. npj Climate and Atmospheric Science, 4, Article 19.',
    "Sorrell, S. (2009). Jevons' paradox revisited: The evidence for backfire from improved energy efficiency. Energy Policy, 37(4), 1456–1469.",
    'Stechemesser, A., Koch, N., Mark, E., Dilger, E., Klösel, P., Menicacci, L., Nachtigall, D., Pretis, F., Ritter, N., Schwarz, M., Vossen, H., & Wenzel, A. (2024). Climate policies that achieved major emission reductions: Global evidence from two decades. Science, 385(6711), 884–892.',
    'Stock, J. H., & Watson, M. W. (2020). Introduction to econometrics (4th ed.). Pearson.',
    "Torney, D., & O'Gorman, R. (2019). A laggard in good times and bad? The limited impact of EU membership on Ireland's climate change and environmental policy. Irish Political Studies, 34(4), 575–594.",
    'Velthof, G. L., Lesschen, J. P., Webb, J., Pietrzak, S., Miatkowski, Z., Pinto, M., Kros, J., & Oenema, O. (2014). The impact of the Nitrates Directive on nitrogen emissions from agriculture in the EU-27 during 2000–2008. Science of the Total Environment, 468–469, 1225–1233. https://doi.org/10.1016/j.scitotenv.2013.04.058',
    'Webb, M. D. (2023). Reworking wild bootstrap-based inference for clustered errors. Canadian Journal of Economics, 56(3), 839–858.',
    'Young, A. (2019). Channeling Fisher: Randomization tests and the statistical insignificance of seemingly significant experimental results. Quarterly Journal of Economics, 134(2), 557–598.',
    'Yue, S., Pilon, P., Phinney, B., & Cavadias, G. (2002). The influence of autocorrelation on the ability to detect trend in hydrological series. Hydrological Processes, 16(9), 1807–1829.',
]


def layout():
    k = KEY
    return html.Div([
        page_header("Step 6 · Conclusions", "Expansion acted through scale; mitigation left little to offset",
                    "Production-oriented policy is associated with higher Irish agricultural emissions and works through herd size and nitrogen use. "
                    "The mitigation portfolio, mostly voluntary and intensity-oriented, shows no detectable effect on total emissions — so expansion "
                    "had little mitigation to offset."),
        kpi_row(kpi(f"+{k['offset']['pressure_effect_pct']:.1f}%", "2024 emissions due to production pressure since 2000",
                    f"90% CI {k['offset']['pressure_lo']:.1f}–{k['offset']['pressure_hi']:.1f}%", tone="tone-orange"),
                kpi(f"θ_P = {k['ardl']['theta_P']:.2f}", "long-run pressure association", f"+{k['ardl']['pct_per_0p1_P']:.1f}% per +0.1 in P; p = {k['ardl']['p_boot_P']:.3f}"),
                kpi(f"{k['lmdi']['P4_intensity_offset']:.2f}", "share of post-quota growth cancelled by intensity gains"),
                kpi("16–23%", "fewer livestock units needed by 2030", "unless intensity falls far faster", tone="tone-red")),
        section("Discussion",
                html.Div(className="grid-3", children=[
                    card(html.H3("Expansion with little to offset"),
                         html.P("Three pieces of evidence point the same way: scale and yield growth after 2014 outran intensity gains more than three to "
                                f"one; the policy-mix model links higher pressure to higher long-run emissions (+{k['ardl']['pct_per_0p1_P']:.1f}% per 0.1) and "
                                "changes in P track the activity component of the decomposition; and the same model finds no emission-reducing effect of "
                                "mitigation. This matches the farm-level finding that productivity lowered intensity while total farm emissions rose "
                                "(Läpple et al., 2022), the EU verdict that climate-labelled CAP spending did not cut farm emissions (European Court of "
                                "Auditors, 2021; Pe'er et al., 2020) and the ranking of output-linked support as the most harmful form of support "
                                "(DeBoe et al., 2020; Henderson & Lankoski, 2021). The size of the pressure footprint depends on the comparison year: "
                                f"relative to 2000 it is small ({k['offset']['pressure_effect_pct']:+.1f}%); relative to the post-decoupling low of 2005 "
                                "the rebuilding of P corresponds to a long-run effect of about 12%.")),
                    card(html.H3("Timing: 2010, not 2015"),
                         html.P("The trend changed in 2010–2012. Expansion began under the quota increases and Food Harvest 2020; abolition continued it "
                                "rather than starting it. Analyses that treat 2015 as the single turning point understate the soft-landing years. This "
                                "reconciles Ireland with the EU-wide finding that post-quota supply was price-inelastic and few member states expanded "
                                "(Jongeneel & Gonzalez-Martinez, 2022): Irish expansion was prepared under the quota increases and a national growth "
                                "strategy, not triggered by abolition alone.")),
                    card(html.H3("Why mitigation did not register"),
                         html.P("Most instruments were voluntary or incentive-based schemes acting on intensity, and the main binding one was designed for "
                                "water quality — consistent with the limited outcome evidence for voluntary schemes (Hasler et al., 2022; Cullen et al., "
                                "2021; Finn & Ó hUallacháin, 2012) and the modest climate co-benefit of nitrates rules (Velthof et al., 2014). An "
                                "intensity-only portfolio can lower emissions per litre while totals rise (Ellerman & Wing, 2003). The positive M "
                                "association is best read as reverse timing. Two fragile results qualify the null: dropping the Nitrates Action Programme "
                                "turns the rest of M significantly negative, and the voluntary sub-index is negative "
                                + f"(θ = {k['subindex']['voluntary']['theta']:.2f}, p = {k['subindex']['voluntary']['p_boot_one_sided']:.2f})".replace("-", "−")
                                + f". Effects larger than |θ| ≈ {k['power']['MDE_M']:.2f} would very likely have been detected; smaller ones cannot be excluded.")),
                ]),
                callout("read", "Relation to stakeholder-identified barriers",
                        "Of the five barriers in Augustenborg et al. (2026), policy incoherence is supported (P and M rose together 2005–2020 and P has a "
                        "detectable association with emissions) — the layering described by Howlett & Rayner (2013) and documented for the CAP by "
                        "Daugbjerg & Swinbank (2016). Competing political priorities are consistent with the regime change around Food Harvest 2020. "
                        "Capacity, financial and planning constraints cannot be separated with these data.")),
        section("Policy implications",
                html.Div(className="grid-2", children=[
                    card(html.H3("1 · Coherence before additionality"),
                         html.P("Pressure has a detectable association with emissions, acting through scale, and the mitigation portfolio does not. Adding "
                                "further intensity-oriented instruments is unlikely, on its own, to close the gap while expansion incentives remain. Growth "
                                "instruments — derogations, capacity grants, volume targets — should be assessed for their emission consequences, as the "
                                "OECD (2022) urges for the wider incentive structure.")),
                    card(html.H3("2 · Targets on totals, not only intensity"),
                         html.P(f"An intensity offset of {k['lmdi']['P4_intensity_offset']:.2f} means efficiency gains cancelled only about a third of scale "
                                "growth. Policy framed around emissions per litre can succeed on its own terms while total emissions rise.")),
                    card(html.H3("3 · The arithmetic of the 2030 ceiling"),
                         html.P("On recent trends, compliance implies roughly 16–23% fewer livestock units by 2030 unless intensity falls far faster than "
                                "ever observed. This should be stated explicitly in sectoral planning.")),
                    card(html.H3("4 · Measure the net signal"),
                         html.P("The common I × s × e × B scale lets governments track whether new instruments raise mitigation faster than concurrent "
                                "sectoral policy raises pressure. It transfers to other land-based sectors facing growth and decarbonisation mandates at once.")),
                ]),
                callout("caution", "These are interpretations of the evidence, not estimated policy effects.", "")),
        section("Limitations",
                html.Ul(className="refs", children=[
                    html.Li("Policy coding: M is the authors' coding under the INPACT rule; several eligibility shares are low-confidence; the second coding "
                            "of P and G is a placeholder, so the kappa values do not yet measure reliability. Results are sensitive to coding (equal "
                            "bindingness θ_P = 0.20; dropping the NAP turns θ_M significantly negative), so the codebook is published in full."),
                    html.Li(f"Short national series: n = {k['ardl']['n']} in the ARDL; the bounds test does not confirm a level relationship, so the "
                            "long-run multipliers are indicative; estimates are conditional associations, not causal effects."),
                    html.Li("No untreated comparator: quota abolition and CAP reform applied across the EU, so neither a synthetic control nor a "
                            "cross-country DiD is available; the regional design's parallel-trends assumption fails."),
                    html.Li("Five clusters: randomisation inference and the wild cluster bootstrap cannot create information five units do not contain."),
                    html.Li("Inventory data: the LMDI and regional emissions end in 2023; methodology changes appear as intensity changes."),
                    html.Li("Omitted drivers: no weather control; GNI* enters only one variant and is collinear with quota abolition."),
                    html.Li("The statutory ceiling includes agricultural fuel, so applying it to CRF3 is an approximation."),
                ])),
        section("Next steps",
                html.Div(className="grid-2", children=[
                    card(html.H3("Data"), html.Ul([html.Li("INPACT export for the mitigation index M"),
                                                   html.Li("Independent, blind second coding of the revised P and G codebook"),
                                                   html.Li("DAFM scheme statistics to refine the low-confidence eligibility and coverage shares"),
                                                   html.Li("CRT 2026 submission to extend the LMDI and regional emissions to 2024")])),
                    card(html.H3("Design"), html.Ul([html.Li("County-level panel from the Census of Agriculture and DAFM derogation statistics for a "
                                                             "continuous-treatment design (Callaway et al., 2024)"),
                                                     html.Li("Transfer the common-scale approach to other jurisdictions where land-based sectors face "
                                                             "growth and decarbonisation mandates at once"), html.Li("Manuscript prepared for submission to Climate Policy (29 October 2026)")])),
                ])),
        section("References", details(f"Show the {len(REFS)} references cited in the manuscript", html.Ol([html.Li(r) for r in REFS], className="refs"))),
        html.Div(className="footer-note", children=[
            html.P("All numbers on this site come from a full re-run of ireland_agri_ghg_analysis.ipynb (seed 20261019, 29 October 2026) with the "
                   "revised policy codebook and reproduce the submission manuscript exactly. Data: EPA, Ireland's CRT 2025 submission to the UNFCCC, "
                   "CSO and Eurostat."),
        ]),
    ])
