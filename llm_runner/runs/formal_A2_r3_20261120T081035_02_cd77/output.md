# formal_A2_r3_20261120T081035_02_cd77

condition: A2  
model_returned: gpt-6-astra  
reasoning_effort: medium  
prompt_version: v1.0  
status: completed

## hypotheses

### hypotheses[1]

#### title

1. Preparation, maturation, or assay conditions account for much of the apparent activity difference

#### question_and_explanation

Does pig ADA2 have less correctly matured, folded, metal-loaded, or dimeric protein in the tested preparation rather than intrinsically weaker catalysis? CTX-01 reports lower activity without effect size or assay details. Signal-peptide and glycosylation annotations differ, but actual processing and glycan occupancy are unknown (CTX-03). Preparation-dependent loss of functional enzyme is a general biochemical possibility, not an observed pig ADA2 defect.

#### supporting_evidence_ids

- CTX-01
- CTX-02
- CTX-03
- CTX-06

#### conflicting_evidence_ids

_(none)_

#### evidence_notes

The missing construct and assay information makes this the first explanation to test, not an established mechanism. Glycosylation-site annotations do not establish the glycosylation of either recombinant preparation.

#### alternative_explanation

Pig ADA2 has an intrinsic sequence-dependent catalytic defect that persists after preparation quality and assay conditions are matched.

#### proposed_test

Verify the actual constructs and pig sequence, then compare independently prepared human and pig ADA2 produced with matched expression, tags, and purification. Measure adenosine-to-inosine conversion across substrate concentrations and a shared pH range. Quantify protein amount, mature termini, glycans, folding, oligomeric state, and zinc occupancy. Where a preparation difference is found, change that factor independently and retest activity.

#### predicted_outcome_if_true

The species gap substantially decreases after correcting a preparation difference or using conditions suitable for both proteins. Activity tracks the amount of intact, properly assembled protein or its maturation state rather than species alone.

#### falsifying_outcome

A reproducible activity gap persists across independent, comparably processed and folded preparations with matched protein amount, oligomeric state, zinc occupancy, and assay conditions. This would weaken preparation-based explanations.

#### controls_and_feasibility

Include no-enzyme and mock-purification controls, a human ADA2 reference, product standards, and checks for time and enzyme-concentration linearity. Glycan manipulation requires folding and recovery controls. Expression, purification, HPLC/FPLC, and mass-spectrometry access are described in CTX-08, CTX-09, and CTX-10; specific service availability is not provided.

#### next_decision

If matching preparation rescues activity, standardize production and repeat other functional comparisons before mutagenesis. If the gap persists, prioritize intrinsic kinetic and substrate-selectivity experiments. If a single preparation feature correlates with activity, test its causal contribution before attributing the difference to sequence.

#### added_value_from_computation

This experiment comes primarily from the background and general biochemical knowledge. SURF-05 and SURF-07 specifically prevent interpreting the calculated negative active-site potential as evidence of a pig catalytic defect: zinc was removed and glycans were absent.

#### confidence

moderate

### hypotheses[2]

#### title

2. Pig ADA2 has altered substrate handling, with DNA-associated deamination potentially preserved

#### question_and_explanation

After preparation effects are excluded, does pig ADA2 handle free adenosine poorly while retaining activity toward deoxyadenosine within DNA? Lower free-adenosine activity is reported in CTX-01, and DNA-associated deamination is reported for ADA2 in CTX-04. Differential substrate recognition or catalytic dynamics is a general mechanistic possibility; no supplied evidence identifies a causal active-site substitution or demonstrates pig DNA editing.

#### supporting_evidence_ids

- CTX-01
- CTX-02
- CTX-04

#### conflicting_evidence_ids

_(none)_

#### evidence_notes

The records motivate testing substrate selectivity but do not establish it. SURF-05 is explicitly uninformative about species-specific catalytic chemistry and is neither supporting nor conflicting evidence.

#### alternative_explanation

Pig ADA2 is generally catalytically impaired across substrates. Alternatively, apparent DNA editing reflects free nucleoside contamination or a copurifying enzyme rather than modification of DNA.

#### proposed_test

Using the quality-controlled preparations from hypothesis 1, compare concentration-dependent free-adenosine turnover, DNA binding, and formation of deoxyinosine in DNA as separate measurements. Establish that the product is associated with purified DNA before analytical digestion. Assess DNA integrity separately so that cutting is not mistaken for editing. Free deoxyadenosine can provide an additional substrate comparison to distinguish sugar preference from DNA-context effects.

#### predicted_outcome_if_true

Pig ADA2 remains weak on free adenosine but shows reproducible DNA-associated deamination with a smaller species deficit. Concentration-dependent measurements distinguish impaired apparent substrate utilization from a lower maximal turnover rate.

#### falsifying_outcome

Pig ADA2 loses DNA-associated deamination to a similar or greater extent than free-adenosine turnover, or the apparent DNA product disappears after removal of free nucleosides and contaminants. Comparable activity on all substrates after quality matching would instead favor hypothesis 1.

#### controls_and_feasibility

Use human ADA2, no-enzyme, mock-purification, substrate-only, and DNA-processing blanks; include an independently validated catalytically impaired ADA2 control with checked folding. Confirm comparable protein amount, processing, glycans, assembly, and stability under each assay condition. HPLC and mass-spectrometry access support product analysis (CTX-09, CTX-10), although a validated DNA-editing assay is not documented.

#### next_decision

If DNA editing is relatively preserved, prioritize substrate-recognition studies and then cellular relevance. If both activities are reduced, investigate a shared catalytic or assembly defect rather than substrate specialization. If only binding survives, pursue the noncatalytic-function hypothesis below.

#### added_value_from_computation

The substrate-selectivity hypothesis comes from CTX-01 and CTX-04 plus general enzymology. The surface calculations do not nominate a credible catalytic mutation; their zinc omission argues against selecting active-site mutations from these maps.

#### confidence

low

### hypotheses[3]

#### title

3. Pig ADA2 retains DNA binding or partner-dependent cellular effects despite altered surface electrostatics

#### question_and_explanation

Could pig ADA2 retain a noncatalytic interaction function even if free-adenosine turnover is intrinsically low? Calculated pig surfaces are less positive in several regions, suggesting altered rather than necessarily absent polyanion interactions (SURF-01 through SURF-04). The strongest exploratory candidate contains human Arg395 aligned to pig Trp392 (SURF-03). Electrostatic contributions to binding are a general scientific rationale. This hypothesis addresses preserved function; surface charge alone does not explain weak free-adenosine catalysis.

#### supporting_evidence_ids

- CTX-04
- SURF-01
- SURF-02
- SURF-03
- SURF-04
- SURF-06

#### conflicting_evidence_ids

_(none)_

#### evidence_notes

No pig binding or cellular-function measurement is supplied. SURF-03 uses sparse sampling and a protonation-sensitive region; SURF-07 documents missing glycans, missing zinc, and only one pH. Thus, neither binding specificity nor preservation of function follows from these calculations.

#### alternative_explanation

The modeled differences are preparation or protonation artifacts, or they affect only nonspecific electrostatic adsorption. Any cellular difference could instead reflect secretion, uptake, stability, glycosylation, or unequal protein exposure.

#### proposed_test

First compare human and pig DNA binding across ionic strengths, using unrelated polyanion competitors. After verifying the construct correspondence, test reciprocal human R395W and pig W392R substitutions for effects on binding and free-adenosine turnover separately. If pig binding is retained, compare localization and a TLR9-linked response in a common ADA2-deficient cellular background, including a validated catalytically impaired control to ask whether the response requires catalysis.

#### predicted_outcome_if_true

Pig ADA2 retains measurable binding, potentially weaker or more salt-sensitive than human ADA2. Reciprocal substitutions shift binding in opposite directions without necessarily changing free-adenosine turnover. A cellular response persists with pig ADA2 and with catalytically impaired ADA2 at comparable cellular exposure.

#### falsifying_outcome

No pig binding is detectable under conditions where human binding is robust, or cellular effects require catalytic activity. Failure of reciprocal substitutions to affect binding despite preserved protein quality weakens the specific Arg395/Trp392 mechanism, though not every possible interaction mechanism.

#### controls_and_feasibility

Include wild-type proteins, no-protein and mock-purification controls, unrelated polyanions, folding and dimerization checks, and matched processing, glycans, and protein amount. For cellular studies, measure uptake and localization and include a TLR9-dependence control. Validate equal species recognition before using the ADA2 aptamer (CTX-08). Cell biology and microscopy capabilities are available (CTX-08 through CTX-10).

#### next_decision

If reciprocal substitutions selectively alter binding, prioritize this patch and test whether binding changes predict cellular effects. If binding survives but editing does not, focus on noncatalytic interaction functions. If neither binding nor cellular effects survive, do not infer preserved DNA-related function from the models.

#### added_value_from_computation

SURF-03 nominates a concrete reciprocal mutation pair rather than an unguided surface screen; SURF-06 motivates ionic-strength comparisons. SURF-02 shows that basic-residue counts alone are insufficient. These calculations prioritize tests but do not demonstrate binding or explain the reported catalytic difference.

#### confidence

low

## overall_note

Start with matched preparations and direct product measurements because CTX-01 lacks an effect size, assay conditions, and raw data, and the literature observations are flagged for verification. Proceed to substrate selectivity and surface-mutant experiments only after confirming the species difference. Similar inflammatory disease in ADA2-deficient pigs (CTX-07) motivates conserved-function studies but does not identify which molecular function is conserved.

## context_provided_to_model

- condition: A2
- prompt version: v1.0
- background / literature records (shared by all conditions): CTX-01 to CTX-11 (11 records)
- surface evidence: SURF-01 to SURF-07 (7 records)
- full input hash (sha256, first 12): 607433a7ae05
- shared context hash (sha256, first 12): 2a75a6c9f881
- evidence hash (sha256, first 12): f41717fa872b

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
# Surface evidence package (electrostatic surface potential calculations)

Method summary: The AlphaFold 3 top-ranked human (UniProt Q9NZK5, residues 30-511) and pig (P58780, residues 25-510) ADA2 dimer models (seed 101, templates on) were prepared with PDB2PQR at pH 7.4 and the electrostatic potential was calculated with APBS at ionic strengths of 0 M and 0.15 M. Per-residue surface potential (kT/e; positive means a more positive surface) was sampled 3 A outward from each atom, keeping only points at least 2.5 A from every atom, and averaged over chains A and B. Residues use UniProt numbering. Human and pig residues were paired with the human-pig residue correspondence from the sequence track.

Depends on: the AlphaFold 3 models from the structure track; the human-pig residue correspondence (draft). These are calculations, not measurements of DNA binding, glycosaminoglycan binding, specificity or activity. Zinc ions and glycans were not included in the calculation.


## SURF-01  (human vs pig; calculation)
Residues: UniProt Human 30–511; pig 25–510 (all surface-sampled residues)
Observation: At 0.15 M, the human dimer has more strongly positive surface residues than the pig dimer. Human: 223 surface residues, mean +0.36 kT/e, 16 above +3 kT/e, 8 below −3 kT/e. Pig: 232 surface residues, mean +0.12 kT/e, 6 above +3 kT/e, 7 below −3 kT/e.
Value: Mean +0.36 vs +0.12 kT/e; residues > +3 kT/e: 16 vs 6
Method: PDB2PQR (pH 7.4; AMBER-type naming in .pqr) + APBS; per-residue surface potential sampled 3 Å outward from each atom, kept only if ≥2.5 Å from every atom; nearest grid point; averaged over chains A and B; surface_findings.py v2
Uncertainty: Counts depend on the +3 kT/e cut-off and on the surface-sampling rule; chain A and B values agree closely for the residues checked.
Limitations: pH 7.4 only; no zinc (removed by PDB2PQR) or glycans; approximate surface sampling.
Interpretation (not an observation): Positive potential is a possible interaction clue only; it does not measure DNA/GAG binding, specificity or activity.

## SURF-02  (human vs pig; calculation)
Residues: UniProt Human 30–50; pig 25–45
Observation: At 0.15 M, surface residues in this segment average +2.30 kT/e in human (17 residues) and +0.56 kT/e in pig (16 residues). Both species have 5 Lys/Arg here. Largest aligned differences: human Met44 +5.40 vs pig Met39 +0.69 kT/e; human Arg49 +2.24 vs pig Gln44 −0.57 kT/e (R→Q substitution).
Value: Region mean +2.30 vs +0.56 kT/e
Method: PDB2PQR (pH 7.4; AMBER-type naming in .pqr) + APBS; per-residue surface potential sampled 3 Å outward from each atom, kept only if ≥2.5 Å from every atom; nearest grid point; averaged over chains A and B; surface_findings.py v2
Uncertainty: Chain A/B: human Met44 +5.32/+5.47; pig Met39 +0.67/+0.71. Residues sampled at 5–18 points.
Limitations: Difference is not explained by Lys/Arg count alone (5 vs 5); cause not determined. Alignment stable for all positions.
Interpretation (not an observation): Positive potential is a possible interaction clue only; it does not measure DNA/GAG binding, specificity or activity.

## SURF-03  (human vs pig; calculation)
Residues: UniProt Human 389–400; pig 386–397
Observation: This is the most positive human surface region found. At 0.15 M, human surface residues here average +6.83 kT/e (5 residues) vs +0.45 kT/e in pig (5 residues). Human Arg395 is +11.19 kT/e; the aligned pig residue Trp392 is −0.57 kT/e, the largest human–pig difference among the 199 aligned positions sampled in both species (11.76 kT/e). Human His391 is +15.02 kT/e. Sequence differences in this segment: R395W, T396A, Y397D, S398A, K400R (human→pig).
Value: Region mean +6.83 vs +0.45 kT/e; Arg395 vs Trp392: +11.19 vs −0.57 kT/e
Method: PDB2PQR (pH 7.4; AMBER-type naming in .pqr) + APBS; per-residue surface potential sampled 3 Å outward from each atom, kept only if ≥2.5 Å from every atom; nearest grid point; averaged over chains A and B; surface_findings.py v2
Uncertainty: Few sample points (Arg395: 1–2 per chain; His391: 2 per chain). Chain A/B: Arg395 +10.33/+12.05; His391 +15.39/+14.64.
Limitations: His391 was assigned as positively charged (HIP) by PDB2PQR at pH 7.4; its value depends on that protonation choice. Pig His388 was not surface-sampled, so His391 has no pig comparison. Region chosen after inspecting the data (exploratory).
Interpretation (not an observation): Positive potential is a possible interaction clue only; it does not measure DNA/GAG binding, specificity or activity.

## SURF-04  (human vs pig; calculation)
Residues: UniProt Human 460–500; pig 457–497
Observation: At 0.15 M, surface residues average +0.71 kT/e in human (19 residues) and −0.33 kT/e in pig (21 residues). Three human Lys positions are non-positive residues in pig: K466T (human +5.62 vs pig +0.94 kT/e), K498E (+0.58 vs −3.47 kT/e), K499E (+1.03 vs −1.62 kT/e). Lys/Arg count in segment: human 8, pig 6; Asp/Glu: human 4, pig 6.
Value: Region mean +0.71 vs −0.33 kT/e
Method: PDB2PQR (pH 7.4; AMBER-type naming in .pqr) + APBS; per-residue surface potential sampled 3 Å outward from each atom, kept only if ≥2.5 Å from every atom; nearest grid point; averaged over chains A and B; surface_findings.py v2
Uncertainty: Chain A/B: human Lys466 +5.58/+5.67; pig Thr463 +0.72/+1.17; pig Glu495 −3.44/−3.50.
Limitations: Region boundaries chosen after inspecting the data (exploratory). Effect size per region is small compared with SURF-03.
Interpretation (not an observation): Positive potential is a possible interaction clue only; it does not measure DNA/GAG binding, specificity or activity.

## SURF-05  (human and pig; calculation)
Residues: UniProt Human His112, His114, His356, Asp441; pig His107, His109, His353, Asp438
Observation: Null result for species comparison: the only sampled ligand position is strongly negative in both species and similar (human His114 −20.34 kT/e; pig His109 −19.73 kT/e at 0.15 M). The other three ligand positions were not surface-sampled in either species.
Value: −20.34 vs −19.73 kT/e
Method: PDB2PQR (pH 7.4; AMBER-type naming in .pqr) + APBS; per-residue surface potential sampled 3 Å outward from each atom, kept only if ≥2.5 Å from every atom; nearest grid point; averaged over chains A and B; surface_findings.py v2
Uncertainty: Single sample point per chain; pig chain A/B −17.94/−21.51.
Limitations: The AlphaFold 3 input models contain one Zn2+ per chain, but PDB2PQR removed the zinc ions (no HETATM records in the .pqr). The active-site potential therefore lacks the metal's positive charge and is expected to be artificially negative. Treat as a preparation artifact, not a biological feature.
Interpretation (not an observation): No species difference observed; not evidence for or against any mechanism.

## SURF-06  (human and pig; calculation)
Residues: UniProt All surface residues; regions R1–R3
Observation: Changing ionic strength from 0 M to 0.15 M lowers potentials (median change human −1.69, pig −1.50 kT/e) but preserves the residue ranking (Spearman correlation 0.95 human, 0.97 pig). The human-more-positive direction holds at 0 M in all three regions: R1 +6.34 vs +2.48, R2 +11.91 vs +2.77, R3 +3.32 vs +1.03 kT/e.
Value: Spearman 0.95 / 0.97; median shift −1.69 / −1.50 kT/e
Method: PDB2PQR (pH 7.4; AMBER-type naming in .pqr) + APBS; per-residue surface potential sampled 3 Å outward from each atom, kept only if ≥2.5 Å from every atom; nearest grid point; averaged over chains A and B; surface_findings.py v2
Uncertainty: Only two ionic strengths tested.
Limitations: 0 M is unphysiological and used only as a robustness check.
Interpretation (not an observation): Robustness check, not a new biological observation.

## SURF-07  (human and pig; method note)
Residues: All
Observation: Calculations used pH 7.4 only, ionic strength 0 and 0.15 M, dimer models (chains A and B) with zinc removed during PDB2PQR preparation and no glycans. Structure files were renumbered to UniProt numbering with renumber_pqr.py (human +29, pig +24; coordinates unchanged, so the APBS maps still apply); the conversion matched every sampled residue (441/441 human, 460/460 pig). Only 199 aligned positions were surface-sampled in both species. Positions 151–156 and 509–510 (human) have uncertain alignment and were excluded from regional comparisons. Source structures: AlphaFold 3 top-ranked models (seed 101, templates on) from structure_prediction/shared_models/: HUM_ADA2_mature30-511_dimer_Zn_s101_model0.cif and PIG_ADA2_mature25-510_dimer_Zn_s101_model0.cif.
Method: PDB2PQR (pH 7.4; AMBER-type naming in .pqr) + APBS; per-residue surface potential sampled 3 Å outward from each atom, kept only if ≥2.5 Å from every atom; nearest grid point; averaged over chains A and B; surface_findings.py v2
Uncertainty: Surface sampling is approximate (nearest grid point, single outward direction); residues sampled at 1 point are less reliable.
Limitations: Second pH not tested. Zinc present in the source models was removed by PDB2PQR; a rerun with zinc kept would remove this limitation.

=== TASK ===
Propose up to 3 hypotheses that could explain the reported difference between human and pig ADA2 activity on free adenosine, and what other ADA2 functions might be preserved in pig ADA2. For each hypothesis, follow the required JSON fields: the explanation, supporting and conflicting evidence IDs, a plausible alternative explanation, a proposed test, predicted and falsifying outcomes, controls and feasibility, the next decision the team would make after each outcome, and what (if anything) in the provided evidence changed your proposed experiment. If an idea comes from the background information alone or from general knowledge, say so in the last field.
~~~~~~

</details>
