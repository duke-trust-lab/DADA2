# formal_A3_r3_20261117T010055_05_86e6

condition: A3  
model_returned: gpt-6-astra  
reasoning_effort: medium  
prompt_version: v1.0  
status: completed

## hypotheses

### hypotheses[1]

#### title

1. Preparation or assay differences account for much of the apparent pig activity deficit

#### question_and_explanation

Does the difference persist when comparable mature proteins are tested under matched conditions? CTX-01 reports lower pig activity but provides neither effect size nor assay conditions. Different processing and glycosylation annotations (CTX-03), unknown construct identity (CTX-06), and unequal amounts of properly folded, zinc-loaded protein could produce an apparent species difference without intrinsically different catalytic chemistry.

#### supporting_evidence_ids

- CTX-01
- CTX-03
- CTX-06

#### conflicting_evidence_ids

_(none)_

#### evidence_notes

These records establish important uncertainties, not that preparation caused the difference. Confident predicted dimers in STRUCT-02 do not establish folding, assembly, or zinc occupancy in the experimental preparations.

#### alternative_explanation

Pig ADA2 has intrinsically different substrate recognition or catalytic behavior even when preparation, processing, and assay conditions are controlled.

#### proposed_test

Verify the actual constructs and pig sequence, then compare independently prepared human and pig mature ADA2 from the same expression and purification workflow. Measure adenosine-to-inosine conversion across substrate concentrations and a shared range of assay conditions. In parallel, compare protein amount, processing, glycosylation, folding, oligomerization, and zinc occupancy. If a preparation difference emerges, test whether correcting it rescues activity.

#### predicted_outcome_if_true

The activity gap shrinks substantially under matched conditions or tracks a correctable difference in protein quality, processing, zinc occupancy, or assay conditions.

#### falsifying_outcome

A reproducible pig deficit persists across independent preparations with comparable mature protein amounts, folding, assembly, processing, and zinc occupancy and across the tested assay conditions.

#### controls_and_feasibility

Include human ADA2 as a positive control, substrate-only and matched purification blanks, product standards, and independent preparations. Confirm product formation rather than relying solely on an indirect signal. Expression, chromatography, and biochemical characterization are supported by CTX-08 and CTX-09; proteomic and metabolomic core access is described in CTX-10, with cost and turnaround unspecified.

#### next_decision

If matching or correcting preparations rescues pig activity, standardize that variable before pursuing mutations. If the deficit persists, prioritize intrinsic structural and substrate-selectivity tests. If protein quality remains unequal, resolve that uncertainty before interpreting species effects.

#### added_value_from_computation

This hypothesis comes primarily from the background and general biochemical knowledge. STRUCT-02 makes gross incompatibility with a dimeric fold less compelling as a sequence-level explanation, but does not replace experimental quality controls. The models omit glycans and cannot adjudicate preparation effects.

#### confidence

moderate

### hypotheses[2]

#### title

2. Local sequence differences alter catalytic behavior without destroying the overall fold

#### question_and_explanation

Do sequence differences near the model-shifted regions corresponding to human positions 281 and 347 cause the free-adenosine deficit? STRUCT-08 identifies local predicted differences and nearby substitutions, while STRUCT-03 suggests broadly similar individual chains. Altered substrate access or conformational coupling is a general-knowledge mechanism, not an observation here; neither region has yet been shown to contact the active site.

#### supporting_evidence_ids

- CTX-01
- STRUCT-03
- STRUCT-05
- STRUCT-08

#### conflicting_evidence_ids

_(none)_

#### evidence_notes

STRUCT-08 provides candidate regions, not evidence of catalytic effects. Distances to the active site, interface, and glycosylation sites are not provided. STRUCT-03 and STRUCT-04 also support considering a modest predicted dimer rearrangement as an alternative. The largest terminal and insertion-region deviations are less secure because of alignment and confidence limitations (STRUCT-06, STRUCT-07).

#### alternative_explanation

The local shifts are functionally neutral; the activity gap instead reflects dimer geometry, another sequence difference, or unequal folding, processing, glycans, zinc occupancy, or protein amount.

#### proposed_test

After validating the construct alignment, locate the STRUCT-08 candidates relative to the catalytic site and interface. Make reciprocal species-residue substitutions in the two candidate regions, initially testing the regions separately. Compare adenosine concentration-response kinetics with both wild types, alongside folding, assembly, processing, and zinc occupancy. Use a solution structural comparison if altered dimer arrangement remains a plausible explanation.

#### predicted_outcome_if_true

Humanizing a pig candidate region increases free-adenosine activity, while the reciprocal human change reduces it, without corresponding losses or gains in protein quality or abundance. Kinetic changes would distinguish altered apparent substrate dependence from altered maximal turnover, although neither alone proves a microscopic mechanism.

#### falsifying_outcome

Reciprocal changes have no reproducible effect despite verified protein quality, or apparent rescue is explained entirely by improved folding, zinc occupancy, or assembly. This would weaken these specific candidates, not exclude all sequence-based mechanisms.

#### controls_and_feasibility

Use verified alignments, wild-type proteins, independent mutant preparations, matched mature constructs and tags, direct product measurements, and quality controls from hypothesis 1. Do not assign pig mutation coordinates from unverified numbering. Recombinant work is supported by CTX-08 and CTX-09; specific solution-structure access and scheduling would need confirmation.

#### next_decision

If reciprocal effects occur without quality changes, dissect the responsible substitutions and test their effect on other substrates. If effects track assembly, redirect toward a dimer-mediated mechanism. If candidates are neutral, stop expanding this mutational panel and reassess other differences rather than targeting uncertain terminal shifts.

#### added_value_from_computation

STRUCT-08 specifically prioritizes the regions around human 281 and 347; STRUCT-05 supports their reproducibility across model runs. STRUCT-07 discourages prioritizing the larger but less reliable terminal and insertion-region shifts. STRUCT-04 makes direct template use alone a less likely explanation for the predicted dimer difference. None establishes a catalytic mechanism.

#### confidence

low

### hypotheses[3]

#### title

3. Pig ADA2 retains DNA-associated functions despite weak activity on free adenosine

#### question_and_explanation

Is the deficit selective for free adenosine rather than a loss of all ADA2 functions? CTX-04 reports DNA interaction, DNA-associated deoxyadenosine-to-deoxyinosine conversion, and lysosome/TLR9 effects for ADA2, but does not establish these functions in pig. Pig ADA2 might retain DNA binding and possibly DNA editing or downstream cellular effects even if free-substrate turnover is poor. This functional hypothesis can coexist with an intrinsic sequence mechanism.

#### supporting_evidence_ids

- CTX-01
- CTX-04

#### conflicting_evidence_ids

_(none)_

#### evidence_notes

No supplied record measures pig DNA binding, DNA editing, or TLR9 effects. The models contain no DNA or glycans and therefore provide no direct support for these functions. The disease resemblance in CTX-07 motivates testing preserved function but does not identify it.

#### alternative_explanation

Pig ADA2 has broadly impaired catalysis but retains only nonspecific DNA association. Apparent DNA editing could instead reflect contaminating enzymes or free nucleosides, and cellular differences could reflect uptake, processing, protein amount, or glycosylation rather than substrate selectivity.

#### proposed_test

Using the matched preparations from hypothesis 1, measure DNA binding, DNA-associated deoxyinosine formation, and DNA cleavage separately, alongside free-adenosine turnover. Establish that any detected deoxyinosine originated in purified DNA rather than a free-nucleoside pool. If a DNA-associated activity is retained, compare human and pig ADA2 add-back in an ADA2-deficient cellular system, measuring uptake, lysosomal localization, and a TLR9-dependent response.

#### predicted_outcome_if_true

Pig retains DNA binding and, for the stronger substrate-selectivity hypothesis, DNA editing despite its free-adenosine deficit. Comparable cellular effects after controlling delivery would support preserved downstream function. Binding alone would support only preserved association, not editing or cleavage.

#### falsifying_outcome

Pig DNA editing is impaired along with free-adenosine turnover under matched conditions, weakening catalytic substrate selectivity. Failure to detect pig binding also weakens preserved DNA association. Signals that follow contaminants or free nucleosides rather than ADA2 and DNA contradict an ADA2-mediated editing interpretation.

#### controls_and_feasibility

Include human ADA2, no-protein and matched purification controls, protein-dose comparisons, DNA integrity measurements, and independent preparations. Use competition and salt-dependence tests to assess nonspecific association. For cells, control viability, uptake, localization, and TLR9 dependence. Validate pig recognition before using the ADA2 aptamer described in CTX-08. Chromatography, mass spectrometry, and imaging access are described in CTX-09 and CTX-10; DNA-editing assay validation remains necessary.

#### next_decision

If editing is retained, prioritize substrate recognition and DNA-linked cellular rescue. If binding alone is retained, test a noncatalytic interaction role without claiming editing. If neither is retained, deprioritize preserved DNA function and examine broader catalytic impairment or other partners. Advance to animal studies only after resolving the biochemical and cellular alternatives.

#### added_value_from_computation

This hypothesis comes from CTX-04 and general knowledge that macromolecular substrate recognition can differ from free-substrate recognition. The supplied computations do not establish DNA-binding surfaces, DNA editing, lysosomal delivery, or TLR9 regulation and do not justify a specific DNA-interface mutation.

#### confidence

low

## overall_note

Start with matched-preparation replication: CTX-01 is an unverified draft observation with no reported effect size or assay details, and the collaborators' pig construct may differ from the modeled reference. The hypotheses are not mutually exclusive. Structural predictions prioritize conditional experiments, not conclusions about activity; preserved DNA binding, editing, cleavage, and cellular signaling must be tested separately.

## context_provided_to_model

- condition: A3
- prompt version: v1.0
- background / literature records (shared by all conditions): CTX-01 to CTX-11 (11 records)
- structure evidence: STRUCT-01 to STRUCT-08 (8 records)
- full input hash (sha256, first 12): 95c2c4bc389a
- shared context hash (sha256, first 12): 2a75a6c9f881
- evidence hash (sha256, first 12): 8873f0094138

The exact text sent to the model (also saved as `input.txt`):

<details><summary>system prompt</summary>

~~~~~~text
You are helping a research team decide which laboratory experiments are most worth doing next. You will be given a biological question, background information with labelled literature observations (IDs starting CTX), and possibly additional computational evidence records (IDs starting SEQ, SURF or STRUCT).

Rules:
1. Use only the information provided in this conversation. Do not browse, retrieve, or claim access to other sources. You may use general scientific knowledge to reason, but you must say when an idea comes from general knowledge rather than from a provided record.
2. When you rely on a provided observation, cite its ID exactly as written (for example CTX-02 or STRUCT-05). Never invent an ID, a number, a residue, or a measurement. If a value is not provided, say it is not provided.
3. Keep observations and interpretations separate. A prediction or a computed score is not a measured biological result. Computational confidence scores are not measurements of activity or binding.
4. Always consider alternative explanations, including differences in protein preparation, folding, processing, glycosylation, protein amount, and assay conditions, in addition to sequence or structural explanations.
5. Each proposed experiment must be able to distinguish the hypothesis from a plausible alternative and must state what result would weaken or contradict the hypothesis. Name controls. Do not give detailed assay protocols; the experimental team will choose these.
6. If the evidence is too weak to support a specific hypothesis, say so and propose fewer hypotheses. Proposing fewer than the maximum is acceptable.
7. Be concise. Do not pad answers.

Return your answer only in the JSON format requested.
~~~~~~

</details>

<details><summary>user message (task, background information and evidence)</summary>

~~~~~~text
Below is the shared background information, followed by any computational evidence available for this task.

=== BACKGROUND INFORMATION ===
Question
Which differences between human and pig ADA2 could explain the reported difference in their activity on free adenosine, and what other functions might be preserved in pig ADA2? We want hypotheses that lead to experiments that distinguish between explanations.

Plain-language definitions
- Protein: a chain of amino acids that folds into a 3D shape. A residue is one amino acid at a position in the chain. A substitution replaces one residue with another.
- Orthologs: corresponding proteins in different species. Human and pig ADA2 are orthologs. Positions must be aligned before they are compared, because insertions and deletions shift the numbering.
- Enzyme and substrate: an enzyme speeds up a chemical reaction; the substrate is the molecule it acts on. The active site is where the chemistry occurs.
- Dimer: two copies of the protein assembled together. The interface is where they meet.
- Signal peptide: a leading segment that routes a protein for secretion and is normally removed.
- Glycans: sugar chains attached to a protein after it is made. They are not specified by the amino acid sequence alone.
- Binding, editing, and cutting DNA are different events and need different measurements. Binding to a negatively charged molecule such as DNA could be helped by a positively charged protein surface, but charge alone does not establish specific binding or function.

Literature observations (draft; each needs verification)
CTX-01. Recombinant pig ADA2 is reported to have much lower activity on adenosine than human ADA2. Source: Tarrant and colleagues, Development of a Yucatan Mini-Pig Model for Deficiency of Adenosine Deaminase 2, 2026 conference abstract (DOI 10.70962/cis2026abstract.48). The abstract gives the direction of the difference but not the effect size, assay conditions, or raw data.
CTX-02. ADA2 (adenosine deaminase 2) converts adenosine to inosine. A zinc ion participates in the catalytic machinery. Human ADA2 forms a homodimer. Sources: UniProt Q9NZK5; Zavialov and colleagues, J Biol Chem 2010 (structures PDB 3LGD, and 3LGG with the transition-state analogue coformycin).
CTX-03. ADA2 is secreted. UniProt annotates a signal peptide at human positions 1-29 and pig positions 1-24. UniProt annotates four N-linked glycosylation sites in human ADA2 (N127, N174, N185, N378) and three in pig ADA2 (N122, N171, N375). Whether a given recombinant protein carries the signal peptide or these glycans depends on how it was prepared. Source: UniProt Q9NZK5 and P58780.
CTX-04. A 2024 study reported ADA2 interactions with DNA, conversion of deoxyadenosine to deoxyinosine within DNA, and effects involving lysosomes and the DNA-sensing receptor TLR9. This does not establish that every ADA2-DNA interaction occurs outside cells or explains the disease. Source: Greiner-Tollersrud and colleagues, Cell Reports 2024 (DOI 10.1016/j.celrep.2024.114899).
CTX-05. Deficiency of ADA2 (DADA2), caused by disease-causing changes in both copies of the ADA2 gene, can involve inflammation, blood vessel problems, abnormal blood-cell production, and immune problems. How ADA2's molecular activities relate to these symptoms is still being investigated.
CTX-06. Both human and pig reference sequences are UniProt reviewed entries (human Q9NZK5, 511 amino acids; pig P58780, 510 amino acids). The pig sequence is not confirmed to match the collaborators' Yucatan mini-pig or their recombinant construct. A human experimental structure exists (3LGD); no experimental pig structure was identified in the supplied materials.
CTX-07. The collaborating laboratory (at Duke) studies inherited disorders of purine metabolism and, in particular, deficiency of ADA2 (DADA2) in human patients: its genetics, diagnosis, and how it causes immune deficiency, auto-inflammatory, or autoimmune disease. With an industry collaborator it has made a minipig model of ADA2 deficiency and is characterizing the inflammatory disease that loss of ADA2 causes in these pigs, which resembles DADA2 in humans. The longer-term aim of the collaboration is to understand the fundamental biological function of ADA2, which may lead to an understanding of how the disease arises and possibly to specific therapy. Source: the laboratory's written reply to the team's request for its tools and methods.
CTX-08. Laboratory capabilities reported by the laboratory. People: six PhD scientists and a couple of skilled technicians, with broad expertise in biochemistry, enzymology, genetics, immunology, and cell biology. One member specializes in developing DNA and RNA aptamers and has developed an aptamer specific for ADA2, which is being used to study where ADA2 is located in living monocytes and macrophages. Two further members are expected to join in January: one with expertise in protein expression, purification, and structure analysis by NMR and other techniques, and one with extensive expertise in mass spectrometry for metabolomic and proteomic studies; these two are expected to test hypotheses about ADA2's function and molecular partners. Equipment: the laboratory states that it has, or has access to, the equipment needed to over-express, purify, and characterize recombinant human and pig ADA2 and otherwise pursue this research. Source: the same written reply. The reply does not list specific instruments; see CTX-09 to CTX-11 for the written equipment and facilities descriptions. Neither source gives limits on what the laboratory cannot do.
CTX-09. In-house equipment, as listed in the laboratories' equipment description (from a grant proposal; the description says the laboratories hold all major and minor equipment needed for the studies in that proposal, together with the Duke core facilities). Listed: PCR machines, digital PCR, qRT-PCR, thermocycler, UV transilluminator with gel imaging, 3 spectrophotometers, DNA and protein electrophoresis equipment, 2 tissue-culture incubators, biosafety cabinets, HPLC and FPLC, 4 refrigerators, 5 ultra-low (-80 C) freezers, 3 -20 C freezers, 2 liquid nitrogen freezers, tabletop centrifuges, pH meters, and microscopes including a high-resolution Keyence BZ-X series fluorescence microscope. Shared rooms: cold room, darkroom, autoclave, dishwasher. Together with CTX-08, the laboratory can over-express, purify, and characterize recombinant human and pig ADA2. Source: Tarrant and Hershfield laboratories, Equipment (grant proposal section).
CTX-10. Duke core facilities available to the laboratories, as described in the facilities section of the same proposal. Flow cytometry and cell sorting (several analyzers and sorters, up to 12 fluorochromes at once, P2 biohazard containment for sorting). Animal pathology (macroscopic pathology, histopathology, clinical pathology). Genomics and computational biology (sequencing and genomic technologies, bioinformatics). Light microscopy (21 microscopes including 9 confocal, 1 TIRF, 1 multiphoton with fluorescence lifetime, 1 laser capture microdissection; 6 image-analysis workstations). Molecular genomics (10x Genomics single-cell RNA and ATAC sequencing, Visium and Xenium spatial assays, DNA methylation and SNP arrays, Taqman genotyping). Metabolomics and proteomics: 13 mass spectrometers (Waters, Agilent, Sciex, Thermo Fisher) including 4 triple-quadrupole instruments and a GC/MS, with targeted panels of more than 300 metabolites in seven classes (acylcarnitines, amino acids and biogenic amines, acyl CoAs, organic acids, ceramides, sphingomyelins, and 36 nucleotides and purine/pyrimidine pathway intermediates) plus untargeted GC/MS. Electron microscopy (sample preparation, imaging, and immuno-EM). These are shared core services, so access, cost, and turnaround are not stated. Source: Tarrant and Hershfield laboratories, Facilities and Other Resources (grant proposal section).
CTX-11. Facilities, clinical testing, and animals, from the same facilities section. The laboratories occupy about 1,700 sq ft in the Sands Research Building at Duke, sharing space with immunology and biochemistry. The principal investigator directs the CLIA/CAP-certified Purine Metabolic and Immunodeficiency laboratory that performs ADA1 and ADA2 testing. The ADA2-deficient swine colony is not currently housed at Duke: the pigs are bred and housed at the collaborating vendor, and weaned minipigs are planned to be transferred to Duke's accredited animal resources facility (DLAR), which has surgical suites and MRI, CT, X-ray, ultrasound, optical, histological, and pathological imaging. Planned animal work is challenge studies with a baculovirus (AcMNPV) pseudotyped with VSV-G and other TLR agonists, for up to three months before endpoints, with procedures such as bone marrow biopsy and catheter placement. Source: Tarrant and Hershfield laboratories, Facilities and Other Resources (grant proposal section).

Known unknowns
- The exact human and pig recombinant constructs (signal peptide, tags, linkers), expression system, purification, and glycosylation state.
- Assay conditions: substrate, concentrations, pH and buffer, temperature, incubation time.
- Whether pig ADA2 is secreted and dimerizes in the lab's preparations.
- Assay-specific details of what the laboratory will run (instrument settings, scheduling, and cost and turnaround of core services).

Alternative explanations to consider
- Different chemistry: sequence changes might alter how the active site handles free adenosine while other activities stay similar.
- Different interactions: the proteins might differ in how they bind DNA or another partner, or in how the two copies assemble.
- Different preparation or conditions: protein amount, folding, processing, attached sugars, or assay conditions could contribute to the reported difference.

=== COMPUTATIONAL EVIDENCE ===
# Structure evidence package (AlphaFold 3 predictions)

Method summary: Human (UniProt Q9NZK5, residues 30-511) and pig (P58780, residues 25-510) ADA2, each with its UniProt-annotated signal peptide removed, were modelled as homodimers (two copies plus one Zn2+ per chain; no glycans, no DNA) on AlphaFold Server (AlphaFold 3). Twelve jobs were run: three seeds per species with zinc and templates, one no-zinc job per species, and two no-template jobs per species; each job returns five models. Predictions were compared with the human crystal structure 3LGD (chains A and B, UniProt 29-510) by superposing C-alpha atoms on residues matched by sequence position. Pig positions were mapped to human positions using a draft pairwise alignment. pLDDT is AlphaFold's per-residue local confidence (0-100); PAE is its expected position error (A); ipTM and pTM (0-1) describe confidence in the chain interface and overall fold.

Depends on: UniProt reference sequences; the draft human-pig position map; the human crystal structure 3LGD. These are predictions, not measurements of activity or binding.


## STRUCT-01  (human; prediction compared with an experimental structure)
Residues: UniProt Q9NZK5 residues 30-511 vs 3LGD residues 4-484 (UniProt 30-510)
Observation: The AlphaFold 3 human ADA2 dimer (2 chains + 2 Zn2+) overlays the human crystal structure 3LGD with C-alpha RMSD 0.43-0.46 A over 962 matched residues (both chains), across 6 jobs. Single-chain RMSD 0.40-0.45 A. Zn2+ to ligand side-chain N/O distances (His112, His114, His356, Asp441) are all within 2.16-2.29 A (the largest ligand distance in each job, across jobs with zinc; 3LGD: 2.15-2.56 A).
Method: Kabsch superposition of C-alpha atoms on residues matched by sequence position; zinc distances to side-chain N/O atoms
Uncertainty: Spread across jobs is 0.03 A. Includes seeds, with and without templates, with and without zinc.
Limitations: Agreement with one crystal structure (3LGD, without bound ligand) shows the prediction is plausible; it does not show activity. 3LGD may be in AlphaFold's training data.
Interpretation (not an observation): The method reproduces the known human dimer and zinc site, so its human-pig comparisons are not obviously unreliable.

## STRUCT-02  (human and pig; prediction)
Residues: whole dimer
Observation: AlphaFold 3 confidence for the top model of each job: human ipTM 0.89-0.93, pTM 0.93-0.95, mean pLDDT 92.8-93.6; pig ipTM 0.91-0.93, pTM 0.94-0.95, mean pLDDT 93.4-93.9. No steric clashes in any model. Mean between-chain PAE: human 5.2-6.5 A, pig 5.6-6.1 A. Zinc raised human ipTM (no zinc 0.89 vs with zinc 0.92-0.93); for pig the difference was small (no zinc 0.92 vs with zinc 0.91-0.93).
Method: AlphaFold Server (AlphaFold 3) summary and full confidence files, top-ranked model per job
Uncertainty: Confidence scores describe the model's own reliability.
Limitations: Confidence is not a measure of binding, catalytic activity or mutation effect. Only one no-zinc job per species.
Interpretation (not an observation): Both species are predicted as confident dimers; zinc matters little for pig confidence.

## STRUCT-03  (pig vs human crystal; prediction compared with an experimental structure)
Residues: pig residues aligned to human 30-510 (draft position map)
Observation: Pig dimers compared with human 3LGD on aligned residues: dimer C-alpha RMSD 1.10-1.28 A; single chain 0.73-0.81 A. After fitting chain A alone, chain B deviates by 1.84-2.29 A for pig versus 0.49-0.71 A for human. Interface residue overlap with 3LGD (Jaccard, 4 A cutoff): human 0.78-0.86, pig 0.72-0.78.
Method: Kabsch superposition on chain A, then distance of matched chain B C-alpha atoms; interface residues = any heavy atom within 4 A of the other chain
Uncertainty: Position map is a draft pending the sequence alignment from the sequence track.
Limitations: No experimental pig structure exists in the supplied files; the human crystal is only a reference. Chain B offset is about 2 A, a modest difference.
Interpretation (not an observation): A single pig chain resembles the human chain, but the two pig chains sit in a somewhat different relative arrangement than the two human chains.

## STRUCT-04  (human and pig; calculation (control))
Residues: whole dimer
Observation: AlphaFold Server uses PDB structure templates by default; for the pig jobs the top template was 3LGD (human ADA2). Repeating human and pig with templates off (2 seeds each) changed the results little. Pig vs 3LGD: dimer RMSD 1.27 A without templates vs 1.14 A with; chain B after chain A fit 2.24 A vs 1.94 A. Human vs 3LGD: 0.44 A vs 0.46 A.
Method: Same inputs and seeds with useStructureTemplate = false
Uncertainty: Two no-template seeds per species.
Limitations: AlphaFold may still reflect human-like structures through its training data and multiple sequence alignments.
Interpretation (not an observation): The slightly different pig chain arrangement persists with templates off, so it is unlikely to come only from using the human crystal structure as a template.

## STRUCT-05  (human and pig; calculation)
Residues: whole dimer
Observation: Pairwise C-alpha RMSD between top models of different seeds (same setup): human 0.27-0.29 A, pig 0.22-0.57 A (4 human and 4 pig pairs).
Method: Kabsch superposition of whole dimer C-alpha atoms, with and without swapping chain order
Uncertainty: Three seeds with templates and two without.
Limitations: Top model per seed only; models within a seed share a seed.
Interpretation (not an observation): Run-to-run variation is small (under about 0.6 A), smaller than the overall human-pig difference in STRUCT-06.

## STRUCT-06  (human vs pig; calculation)
Residues: human 30-511 and aligned pig residues
Observation: Predicted human and pig dimers differ by C-alpha RMSD 1.16 A (templates on) and 1.19 A (templates off) over aligned residues. Largest per-residue deviations (human numbering), templates on: 511 (7.1 A), 156 (5.7 A), 157 (3.9 A), 281 (3.6 A), 30 (3.5 A), 151 (3.2 A), 154 (2.9 A), 152 (2.9 A). Templates off: 511 (7.2 A), 156 (5.2 A), 281 (3.9 A), 157 (3.5 A), 151 (3.2 A), 152 (3.0 A), 154 (2.8 A), 158 (2.6 A).
Method: Pig dimer fitted to human dimer on aligned C-alpha atoms; per-residue distance after fitting
Uncertainty: Larger than seed-to-seed variation (STRUCT-05). Residue 511 is the chain end and is poorly defined.
Limitations: Depends on the draft position map. Pig has a 2-residue insertion after human 154 that disturbs the alignment near 151-160.
Interpretation (not an observation): Most of the structure is similar; local differences concentrate at chain ends, near the pig insertion, and at a few interior positions.

## STRUCT-07  (human and pig; prediction)
Residues: human 30-33, 151-160, 511 (pig aligned positions)
Observation: Confidence is lower in the regions with the largest deviations. Residues 151-160: pLDDT human 88.6 (range 88.1-89.3), pig 82.3 (range 80.6-84.4); within-chain PAE human 9.1 (range 8.8-9.6) A, pig 13.7 (range 12.0-14.4) A. Last residue (human 511): pLDDT human 74.7 (range 73.6-75.5), pig 54.6 (range 52.1-55.9). Whole-chain reference: pLDDT human 96.8 (range 96.4-97.0), pig 97.1 (range 96.8-97.2).
Method: pLDDT from model B-factor column (C-alpha); PAE rows of region residues against all chain-A residues; top model per job
Uncertainty: Mean over 6 human and 6 pig jobs; chain A only.
Limitations: Confidence does not say whether a difference is functional.
Interpretation (not an observation): Deviations in these regions are likely flexibility or modelling uncertainty and should not be treated as real structural differences.

## STRUCT-08  (human vs pig; prediction)
Residues: human 281 and 347 (pig 278 and 344)
Observation: Residues 281 and 347 are predicted with high confidence in both species (pLDDT 281: human 96.9 (range 96.8-97.2), pig 97.0 (range 96.7-97.4); 347: human 95.3 (range 95.0-95.7), pig 97.0 (range 96.6-97.2)) yet the models differ there (C-alpha distance, human vs pig: 281 noTemplate: 3.9 A, template: 3.6 A; 347 noTemplate: 2.5 A, template: 2.4 A). Pig differs from human at nearby positions: around 281 V277A, E278K, E282G; around 347 K346S, D347R.
Method: As STRUCT-06 and STRUCT-07
Uncertainty: Deviation is larger than seed-to-seed variation (STRUCT-05). Distance to active site, zinc site, dimer interface and glycosylation sites has NOT yet been computed.
Limitations: A shift in a confident region may still be small in physical terms. Not tested experimentally.
Interpretation (not an observation): These are candidate positions for a real human-pig structural difference, to be checked against position in the structure and the other evidence.

=== TASK ===
Propose up to 3 hypotheses that could explain the reported difference between human and pig ADA2 activity on free adenosine, and what other ADA2 functions might be preserved in pig ADA2. For each hypothesis, follow the required JSON fields: the explanation, supporting and conflicting evidence IDs, a plausible alternative explanation, a proposed test, predicted and falsifying outcomes, controls and feasibility, the next decision the team would make after each outcome, and what (if anything) in the provided evidence changed your proposed experiment. If an idea comes from the background information alone or from general knowledge, say so in the last field.
~~~~~~

</details>
