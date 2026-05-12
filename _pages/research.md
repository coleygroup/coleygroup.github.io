---
title: "Coley Research Group - Research"
layout: research
excerpt: "Coley Research Group -- Research"
sitemap: false
permalink: /research
---

# Research


### Overview 
---
We work at the interface of chemistry and machine learning to develop models that understand how molecules behave, interact, and react and use that knowledge to engineer new ones. Much of our work focuses on improving computational strategies for small molecule drug discovery, molecular optimization, synthesis planning, and structure elucidation. A long-term goal of our work is to enable autonomous molecular discovery, where hypotheses are proposed algorithmically and tested via experiments with minimal human intervention.

<div style="text-align: center">
<img style="width: 40%;" src="{{ site.url }}{{ site.baseurl }}/images/researchpic/discovery-1.png" alt="Chemical discovery overview"/>
</div>

Small molecules are the predominant modality for medicines, chemical probes, organocatalysts, and specialty monomers among others. They are typically discovered through an iterative process of designing candidate compounds, synthesizing them, and testing their performance, where each repeat of the cycle requires weeks or months. The rate at which this process yields successful compounds can be limited by bottlenecks and mispredictions at all three stages and is plagued by inefficiencies, including underutilization of available data resulting in inadequate predictions of compound performance, compound selection based on intuition or synthetic ease rather than information content, and frequent manual intervention subject to human bias. For example, the hit-to-lead and lead optimization stages of small molecule drug discovery, while only part of the overall pipeline, require several years and millions of dollars for each clinical candidate. Even longer timescales are required to bring a new material to market.

The discovery of these molecules—and scientific discovery more generally—is a problem of inference from incomplete and imperfect information, for which techniques in artificial intelligence are well-suited. However, there are a number of bottlenecks in our current approach to molecular discovery (a few are summarized below in red); overcoming them will require a number of methodological advances (a few are summarized below in blue).

<div style="text-align: center">
<img style="width: 100%;" src="{{ site.url }}{{ site.baseurl }}/images/researchpic/autonomous-workflow-1024x269.png" alt="Autonomous discovery workflow diagram"/>
</div>

For a slightly-outdated comprehensive overview of autonomous discovery in the chemical sciences, including a discussion of key challenges, please read our 2019 review article and perspective in Angewandte Chemie or on arxiv: [part one](https://arxiv.org/abs/2003.13754), [part two](https://arxiv.org/abs/2003.13755). Our work falls under the broader umbrella of "[AI for Science](https://www.nature.com/articles/s41586-023-06221-2)".

<br/>

### Current Research Directions
---

#### Computer-aided molecular design and optimization, including generative AI
One of the most important questions one must answer when searching for a molecule that achieves a certain property profile is ‘what should we make next?’ out of the vastness of [chemical space](https://www.sciencedirect.com/science/article/abs/pii/S2589597420302884). Molecules are generally proposed through one of two complementary approaches: virtual screening, where one has a fixed list of candidates, and generative modeling, where one uses algorithms to propose novel molecular structures. Exhaustive virtual screening with a computational oracle (e.g., docking for structure-based drug design) is a viable approach to hit finding, but is not straightforward to apply to the tens of billions of molecules in modern virtual libraries. We work on various methods for selecting and proposing molecular structures during iterative rounds of optimization, both for from discrete libraries and using generative models. The former uses techniques in model-guided optimization (Bayesian optimization) to navigate large discrete design spaces of candidate molecular structures. A thread of particular interest is the development of synthesizability-constrained generative models that propose molecular structures that are synthetically accessible and/or using information about synthesizability as the basis for the downselection of candidates. Sample efficiency is also a primary concern for these moodels, as in silico benchmarks may involve the ‘testing’ of hundreds of thousands of molecules, which is severely misaligned with what is practical, experimentally. Finally, we have sought to better integrate principles of medicinal chemistry and noncovalent interactions into generative design to overcome yet another failure mode of generative models, which is the relatively poor quality of ligands they generate in 3D pocket-conditioned generative tasks.

_Selected publications (screening/selection/non-generative):_
<ul style="font-size: smaller">
<li>Fromer, J., Volkova, A.D., Coley, C.W. "Optimal compound downselection to promote diversity and parallel chemistry". <i>J. Chem. Inf. Model.</i> (2024)</li>
<li>Fromer, J., Coley, C.W. "An algorithmic framework for synthetic cost-aware decision making in molecular design". <i>Nat. Comp. Sci.</i> (2024)</li>
<li>Levin, I., Fortunato, M.E., Tan, K.L., Coley, C.W. "Computer-aided evaluation and exploration of chemical spaces constrained by reaction pathways". <i>AIChE J.</i> (2023)</li>
<li>Fromer, J.C., Graff, D.E., Coley, C.W. "Pareto optimization to accelerate multi-objective virtual screening". <i>Patterns</i> (2024)</li>
<li>Graff, D. E., Aldeghi, M., Marrone, J. A., Jordan, K. E., Pyzer-Knapp, E. O., Coley, C. W. “Self-focusing virtual screening with active design space pruning”. <i>J. Chem. Inf. Model.</i> (2022)</li>
<li>Graff, D. E., Shakhnovich, E. I., Coley, C. W. “Accelerating high-throughput virtual screening through molecular pool-based active learning”. <i>Chem. Sci.</i> (2021)</li>
</ul>

_Selected publications (generative design):_
<ul style="font-size: smaller">
<li>Adams, K., Abeywardane, K., Fromer, J., Coley, C.W. “ShEPhERD: Diffusing shape, electrostatics, and pharmacophores for bioisosteric drug design”. <i>ICLR [Oral]</i> (2025)</li>
<li>Gao, W., Luo, S., Coley, C.W. “Generative artificial intelligence for navigating synthesizable chemical space”. <i>Proc. Natl. Acad. Sci. U. S. A.</i> (2024)</li>
<li>Luo, S., Gao, W., Wu, Z., Peng, J. Coley, C.W., Ma, J. “Projecting molecules into synthesizable chemical spaces”. <i>ICML</i> (2024)</li>
<li>Gao, W., Mercado, R., Coley, C. W. "Amortized tree generation for bottom-up synthesis planning and synthesizable molecular design". <i>ICLR</i> (2022)</li>
<li>Adams, K., Coley, C. W. "Equivariant shape-conditioned generation of 3D molecular for ligand-based drug design". <i>ICLR</i> (2023)</li>
<li>Gao, W., Fu, T., Sun, J. Coley, C. W. "Sample efficiency matters: A benchmark for practical molecular optimization". <i>NeurIPS</i> (2022)</li>
<li>Gao, W., Coley, C. W. "The synthesizability of molecules proposed by generative models". <i>J. Chem. Inf. Model.</i> (2020)</li>
</ul>
<br/>

#### Data-driven predictive chemistry, including retrosynthetic planning and reaction outcome prediction
Computational assistance is only useful insofar as it can produce actionable suggestions for experimental validation. The synthesis and testing of new molecules is a common requirement for validation of functional physical matter. Despite significant progress in methodology development, few reactions have achieved widespread use as part of the synthetic chemistry toolbox. Newly discovered reactions may be too narrowly applicable or require excessive optimization to be practical. Overcoming both of these barriers to adoption requires an expansion of substrate scope and straightforward guidelines for how the reaction should be carried out to achieve maximal yield, selectivity, etc. We approach this problem from a statistical modelling perspective, leveraging the collective chemical knowledge reflected in the patent and journal literature to identify robust synthetic and biological transformations, including enzyme catalysis. This builds on our ongoing efforts in ‘[predictive chemistry](https://pubs.rsc.org/en/content/articlelanding/2023/sc/d2sc05089g)’, which encompasses computer-aided synthesis planning, reaction outcome prediction, and related tasks. Our work in this area also explores the intersection of structure-based representation learning and descriptor-based approaches that have become prevalent in physical organic chemistry. A particular challenge is transforming these methods from being qualitative to quantitative, and retrospective to prospective. To support our more ambitious goals of extrapolation, we also develop models that are designed to predict mechanistic pathways with the expectation that a grounding in mechanistic understand may help models generalize to previously-unseen reaction types.

Several data-driven chemistry tools for synthesis planning are available in the open source [ASKCOS](https://arxiv.org/abs/2501.01835) software suite, which has seen use by 35,000+ chemists and is deployed at 15+ pharmaceutical and chemical companies. Try out the public deployment at [askcos.mit.edu](https://askcos.mit.edu) or spin up your own deployment using [these directions](https://gitlab.com/mlpds_mit/askcosv2/askcos-docs/-/wikis/home).

_Selected publications (retrosynthesis-focused):_
<ul style="font-size: smaller">
<li>Tu, Z., Choure, S.J., Fong, M.H., Roh, J., Levin, I., Yu, K., Joung, J.F., Morgan, N., Li, S.C-., Sun, X., Lin, H., Murnin, M., Liles, J.P., Struble, T.J., Fortunato, M.E., Liu, M., Green, W.H., Jensen, K.F., Coley, C.W. “ASKCOS: an open source software suite for synthesis planning”. <i>Acc. Chem. Res.</i> (2025)</li>
<li>Roh, J., Joung, J.F., Yu, K., Tu, Z., Bartholomew, G.L., Santiago-Reyes, O.A., Fong, M.H., Sarpong, R., Reisman, S.E., Coley, C.W. “Higher-level strategies for computer-aided retrosynthesis”. <i>chemrxiv:10.26434/chemrxiv-2025-21zvt</i> (2025)</li>
<li>Yu, K., Roh, J., Li, Z., Gao, W., Wang, R., Coley, C.W. “Double-ended synthesis planning with goal-constrained bidirectional search”. <i>NeurIPS [Spotlight]</i> (2024)</li>
<li>Levin, I., Liu, M., Voigt, C.A., Coley, C.W. "Merging enzymatic and synthetic chemistry with computational synthesis planning". <i>Nat. Commun.</i> (2022)</li>
<li>Tu, Z., Coley, C. W. "Permutation invariant graph-to-sequence model for template-free retrosynthesis and reaction prediction". <i>J. Chem. Inf. Model.</i> (2022)</li>
</ul>

_Selected publications (outcome prediction-focused):_
<ul style="font-size: smaller">
<li>Joung, J.F., Fong, M.H., Casetti, N., Liles, J.P., Dassanayake, N.S., Coley, C.W. “Electron flow matching for generative reaction mechanism prediction obeying conservation laws”. <i>arxiv:2502.12979</i> (2025)</li>
<li>Joung, J.F., Fong, M.H., Roh, J., Tu, Z., Bradshaw, J., Coley, C.W. “Reproducing reaction mechanisms with machine learning models trained on a large-scale mechanistic dataset”. <i>Angew. Chem.</i> (2024)</li>
<li>Raghavan, P., Rago, A.J., Verma, P., Hassan, M.M., Goshu, G.M., Dombrowski, A.W., Pandey, A., Coley, C.W.**, Wang, Y.** “Incorporating synthetic accessibility in drug design: Predicting reaction yields of Suzuki cross-couplings by leveraging AbbVie’s 15-year parallel library data set”. <i>J. Am. Chem. Soc.</i> (2024)</li>
<li>Raghavan, P., Haas, B.C., Ruos, M.E., Schleinitz, J., Doyle, A.G., Reisman, S.E., Sigman, M.S., Coley, C.W. "Dataset design for building models of chemical reactivity". <i>ACS Cent. Sci.</i> (2023)</li>
<li>Stuyver, T., Coley, C.W. "Machine learning-guided computational screening of new bio-orthogonal click reactions". <i>Eur. J.</i> (2023)</li>
<li>Stuyver, T., Coley C. W. "Quantum chemistry-augmented neural networks for reactivity prediction: Performance, generalizability and interpretability". <i>J. Chem. Phys.</i> (2022)</li>
<li>Goldman, S., Das, R., Yang, K. K., Coley C. W. "Machine learning modeling of family wide enzyme-substrate specificity screens". <i>PLOS Comp. Bio.</i> (2022)</li>
</ul>
<br/>


#### Computational metabolomics and structural elucidation
Small molecule metabolites mediate myriads of biological and environmental phenomena across host-microbiome interactions, plant chemistry, cancer biology, and various other processes. Mass spectrometry is often used as an analytical technique to investigate the small molecules present in a sample, measuring both their masses and fragmentation spectra. However, the complexity and high dimensionality of spectral data makes it difficult to identify unknown metabolites and their roles, with a large majority of detected metabolites remaining unidentified in public data. We are developing a suite of new computational methodologies for higher accuracy annotation of small molecule metabolites from mass spectrometry data that integrate chemistry-informed priors with modern deep learning advancements. These include a variety of _forward_ models as well as _inverse_ models that try to solve the structure-to-spectrum and spectrum-to-structure tasks, respectively. The latter includes methods that treat elucidation as a conditional molecular design task that is therefore amenable to many of the optimization-based and generative approaches we develop in the context of small molecule drug design as well.

_Selected publications:_
<ul style="font-size: smaller">
<li>Wang, R., Manjrekar, M., Mahjour, B., Avila-Pacheco, J., Provenzano, J., Reynolds, E., Lederbauer, M., Mashin, E., Goldman, S.L., Wang, M., Weng, J.-K., Plata, D.L., Clish, C.B., Coley, C.W. “Neural spectral prediction for structure elucidation with tandem mass spectrometry” <i>bioRxiv:2025.05.28.656653</i> (2025)</li>
<li>Bohde, M., Manjrekar, M., Wang, R., Ji, S., Coley, C.W. “DiffMS: Diffusion generation of molecules conditioned on mass spectra”. <i>ICML</i> (2025)</li>
<li>Wang, R., Wang, R.-X., Manjrekar, M., Coley, C.W. “Neural graph matching improves retrieval augmented generation in molecular machine learning”. <i>ICML</i> (2025)</li>
<li>Goldman, S., Xin, J. Provenzano, J., Coley, C.W. "MIST-CF: Chemical formula inference from tandem mass spectra". <i>J. Chem. Inf. Model.</i> (2023)</li>
<li>Goldman, S., Li, J. Coley, C.W. "Generating molecular fragmentation graphs with autoregressive neural networks". <i>Anal. Chem.</i> (2023)</li>
<li>Goldman, S., Bradshaw, J., Xin, J., Coley, C.W. "Prefix-tree decoding for predicting mass spectra from molecules". <i>NeurIPS</i> (2023)</li>
<li>Goldman, S., Wohlwend, J., Stražar, M., Haroush, G., Xavier, R.J., Coley, C.W. "Annotating metabolite mass spectra with domain-inspired chemical formula transformers". <i>Nat. Mach. Intell.</i> (2023)</li>
</ul>
<br/>

#### Molecular representation learning and property prediction with chemistry-tailored neural models

The use of machine learning models for chemical discovery problems has overwhelmingly been limited to off-the-shelf models that do not readily transfer to this domain. Problems in chemistry and biology rarely have large quantities of clean, annotated data, and the structure of model inputs (e.g., molecules, proteins) are not inherently numeric or character-based as in more familiar image-or text-processing tasks. While statistical inference techniques have been successfully applied to self-contained chemical prediction tasks (e.g., developing structure-property relationship models, predicting links in knowledge graphs of biological activity), there are significant obstacles to applying them more broadly related to molecular representation, model generalizability, and data availability, among others. Our work in this area involves the integration of domain expertise and prior knowledge into neural models to improve accuracy, uncertainty estimation, and generalization, especially in low data environments. >2D molecular representations that can understand both stereochemistry and conformational flexibility are of particular interest. Beyond small molecules, we also think about representation learning for molecular ensembles (e.g., polymers) and porous materials (e.g., zeolites).

_Selected publications:_
<ul style="font-size: smaller">
<li>Gao, W., Raghavan, P., Shprints, R., Coley, C.W. "Revealing the relationship between publication bias and chemical reactivity with contrastive learning". <i>JACS</i> (2025)</li>
<li>Adams, K., Coley, C.W. “The impact of conformer quality on learned representations of molecular conformer ensembles”. <i>arxiv:2502.13220</i> (2025)</li>
<li>Graff, D.E., Pyzer-Knapp, E.O., Jordan, K.E., Shakhnovich, E.I., Coley, C.W. “Evaluating the roughness of structure-property relationships using pretrained molecular representations”. <i>Digit. Dis.</i> (2023)</li>
<li>Aldeghi, M., Graff, D. E., Frey, N., Morrone, J. A., Pyzer-Knapp, E. O., Jordan, K. E, Coley, C. W. “Roughness of molecular property landscapes and its impact on modellability”. <i>J. Chem. Inf. Model.</i> (2022)</li>
<li>Adams, K., Pattanaik, L., Coley, C.W. "Learning 3D representations of molecular chirality with invariance to bond rotations". <i>ICLR</i> (2022)</li>
<li>Pattanaik, L., Ganea, O. E., Coley, I., Jensen, K. F., Green, W. H., Coley, C. W. "Message passing networks for molecules with tetrahedral chirality". <i>NeurIPS ML4Molecules</i> (2020)</li>
<li>Aldeghi, M., Coley, C. W. "A graph representation of molecular ensembles for polymer property prediction". <i>Chem. Sci.</i> (2022)</li>
<li>Zhang, X., Wang, L., Helwig, J., Luo, Y., Fu, C., Xie, Y., ..., Adams, K., ..., Coley, C.W., Qian, X., Qian, X., Smidt, T., Ji, S. "Artificial intelligence for science: Quantum, atomistic, and continuum systems". <i>arxiv</i> (2023)</li>
<li>Soleimany, A. P., Amini, A., Goldman, S., Rus, D., Bhatia, S., Coley, C. W. "Evidential deep learning for guided molecular property prediction and discovery". <i>ACS Cent. Sci.</i> (2021)</li>
<li>Hirschfeld, L., Swanson, K., Yang, K., Barzilay, R., Coley, C. W. "Uncertainty quantification using neural networks for molecular property prediction". <i>J. Chem. Inf. Model.</i> (2020)</li></ul>
<br/>

#### Laboratory automation and pursuit of “autonomous” self-driving labs
As computational design strategies are increasingly able to make use of available information to propose new hypotheses, we are increasingly limited by our ability to validate them. More bluntly, synthesis is the bottleneck for many molecular discovery workflows. Current platform technologies for synthesis and screening are often misaligned with rational design approaches; the next generation of laboratory hardware should be specifically tailored to supply the data required by the current and future state-of-the-art machine learning and computational discovery algorithms. We customize our own automated laboratory platforms for the generation of high-fidelity experimental data suitable for training and validation. Our intent is to integrate automated laboratory hardware with our computational models to autonomously conduct reaction and molecule screening campaigns, inching closer to a true ‘closed-loop’ vision beyond the proofs of concept the field has seen to date. Even if we are far from true autonomy, automated platforms are able to explore larger design spaces with better time- and material-efficiency than traditional manual experimentation.

_Selected publications:_
<ul style="font-size: smaller">
<li>Wu, G., Wang, R., Coley, C.W. “Optimization of robotic liquid handling as a capacitated vehicle routing problem” <i>arxiv:2506.02795</i> (2025)
</li>
<li>Ai, Q., Meng, F., Wang, R., Klein, J.C., Godfrey, A.G., Coley, C.W. “Schedule optimization for chemical library synthesis” <i>Digit. Dis.</i> (2025)</li>
<li>Mahjour, B.A., Lu, J., Fromer, J.C., Casetti, N., Coley, C.W. “Ideation and evaluation of novel multicomponent reactions via mechanistic network analysis and automation”. <i>chemrxiv:10.26434/chemrxiv-2024-qfjh9</i> (2024)</li>
<li>Wu, G., Jin, T., Alexander-Katz, A., Coley, C.W. “Autonomous discovery of functional random heteropolymer blends through evolutionary formulation optimization”. <i>chemrxiv:10.26434/chemrxiv-2024-nh0xn</i> (2024)</li>
<li>Gao, W., Raghavan, P., Coley, C. W. "Autonomous platforms for data-driven organic synthesis". <i>Nat. Commun.</i> (2022)</li>
<li>Wierenga, R.P., Golas, S., Ho, W., Coley, C.W., Elsvelt, K.M. "PyLabRobot: An open-source hardware agnostic interface for liquid-handling robots and accessories". <i>Device</i> (2023)</li>
</ul>
<br/>

#### Data sharing and standardization
The development of data-driven methods relies on data. At present, most procedural details about chemical reactions are reported in unstructured supporting information documents as Word files exported to PDFs. Information is not fully captured by current databasing efforts including, even basic details of quantitative amounts. The state of data sharing for other molecular property prediction tasks is better, but efforts to standardize data splits, evaluations, and pre-processing pipelines are essential. In addition to our commitment to developing open source software for the research threads listed above, we help lead the [Open Reaction Database](https://open-reaction-database.org/) and contribute to the [Therapeutics Data Commons](https://tdcommons.ai/).

_Selected publications:_
<ul style="font-size: smaller">
<li>Fan, V., Qian, Y., Wang, A., Wang, A., Coley, C.W., Barzilay, R. “OpenChemIE: An information extraction toolkit for chemistry literature”. <i>J. Chem. Inf. Model.</i> (2024)</li>
<li>Mercado, R., Kearnes, S.M., Coley, C.W. "Data sharing in chemistry: Lessons learned and a case for mandating structured reaction data". <i>J. Chem. Inf. Model.</i> (2023)</li>
<li>Kearnes, S. M., Maser, M. R., Wleklinski, M., Kast, A., Doyle, A. G., Dreher, S. D., Hawkins, J. M., Jensen, K. F. Coley, C. W. "The Open Reaction Database". <i>J. Am. Chem. Soc.</i> (2021)</li>
<li>Maloney, M.P., Coley, C.W., Genheden, S., Carson, N., Helquist, P., Norrby, P.-O., Wiest, O. "Negative data in data sets for machine learning training". <i>J. Org. Chem.</i> (2023)</li>
<li>Huang, K., Fu, T., Gao, W., Zhao, Y., Roohani, Y., Leskovec, J., Coley, C. W., Xiao, C., Sun, J., Zitnik, M. "Therapeutics Data Commons: Machine learning datasets and tasks for therapeutics". <i>NeurIPS</i> (2021)</li>
<li>Huang, K., Fu, T., Gao, W., Zhao, Y., Roohani, Y., Leskovec, J., Coley, C. W., Xiao, C., Sun, J., Zitnik, M. "Artificial intelligence foundation for therapeutic science". <i>Nature Chem. Bio.</i> (2022)</li>
</ul>
<br/>
