# formal_A0_r1_20261117T005618_00_3736

condition: A0  
model_returned: gpt-6-astra  
reasoning_effort: medium  
prompt_version: v1.0  
status: completed

## hypotheses

### hypotheses[1]

#### title

1. Unequal protein maturation or assay conditions produce an apparent species difference

#### question_and_explanation

Does the reported activity gap reflect unequal amounts of properly folded, processed, zinc-containing ADA2 rather than different intrinsic chemistry? CTX-01 reports lower pig activity without assay conditions or an effect size. Signal-peptide and glycosylation annotations differ between species, but actual recombinant processing is unknown (CTX-03). Preparation-dependent changes could affect secretion, stability or dimer assembly. If this explanation is correct, pig ADA2 may retain substantial free-adenosine activity when comparably prepared; preservation of DNA-related functions would still require separate testing.

#### supporting_evidence_ids

- CTX-01
- CTX-02
- CTX-03
- CTX-06

#### conflicting_evidence_ids

_(none)_

#### evidence_notes

These records establish unresolved preparation variables, not a demonstrated preparation defect. CTX-02 establishes zinc involvement and human dimerization, not pig zinc occupancy or assembly. The pig reference sequence may not match the experimental construct (CTX-06). No supplied observation directly contradicts this hypothesis.

#### alternative_explanation

Correctly matured pig ADA2 has intrinsically weaker free-adenosine catalysis because of sequence-dependent differences in substrate recognition or catalytic dynamics.

#### proposed_test

First verify the experimental construct sequences and reproduce the comparison using independent human and pig preparations made in the same expression system with matched tag handling. Quantify intact mature protein and characterize processing, glycosylation, folding, oligomeric state and zinc content. Measure adenosine-to-inosine initial rates across substrate concentrations and a shared range of assay conditions. If a preparation difference is identified, correct that variable and repeat the activity comparison.

#### predicted_outcome_if_true

Activity tracks a preparation or condition variable, and correcting it substantially narrows the species gap. A condition-dependent gap would weaken the claim of universally low pig activity, although it could still reflect an intrinsic difference in condition preference.

#### falsifying_outcome

The gap persists across independent preparations and shared conditions despite comparable intact protein amounts, maturation, folding, assembly and zinc content. Failure to rescue activity after correcting an identified defect would weaken that defect as the explanation.

#### controls_and_feasibility

Include no-enzyme and mock-purification controls, product standards, independent preparations, and verification of initial-rate linearity with time and protein amount. Use matched treatment controls for any processing or glycan intervention and recheck folding afterward. Protein production and chromatography are supported by CTX-08 and CTX-09; mass-spectrometry cores are available under CTX-10, although access and turnaround are unspecified.

#### next_decision

If correction removes the gap, standardize preparations before assigning biological meaning to the original result, then compare DNA-related activities. If the gap persists with adequate quality controls, prioritize intrinsic substrate-selectivity tests. If protein quality remains unequal, resolve that uncertainty before interpreting species-specific kinetics.

#### added_value_from_computation

No computational evidence was provided. The preparation-first design comes from the missing information in CTX-01, the processing annotations in CTX-03 and construct uncertainty in CTX-06. Effects of maturation, metal occupancy and folding on measured enzyme activity are general biochemical reasoning, not demonstrated findings for these pig preparations.

#### confidence

moderate

### hypotheses[2]

#### title

2. Pig ADA2 has altered substrate preference while retaining DNA-associated functions

#### question_and_explanation

Does pig ADA2 handle free adenosine poorly while retaining DNA binding and possibly DNA-associated deamination? CTX-04 reports ADA2–DNA interactions and conversion of DNA deoxyadenosine to deoxyinosine, motivating a direct comparison with free-substrate activity. Sequence-dependent substrate recognition or access could selectively alter free-adenosine activity without abolishing these other functions. No supplied alignment or pig structure identifies a responsible residue.

#### supporting_evidence_ids

- CTX-01
- CTX-02
- CTX-04

#### conflicting_evidence_ids

_(none)_

#### evidence_notes

CTX-01 supports only the reported direction of the free-adenosine difference. CTX-04 motivates alternative functional measurements but does not establish any DNA activity in pig ADA2. There is no direct evidence for altered pig substrate preference and no supplied contradictory result.

#### alternative_explanation

Pig ADA2 is broadly catalytically impaired rather than substrate-selective. Apparent preservation of DNA activity could instead arise from nonspecific binding, contaminating enzymes, free nucleosides in the DNA preparation or unequal protein quality.

#### proposed_test

Using quality-matched preparations, compare concentration-dependent activity on free adenosine, free deoxyadenosine and defined deoxyadenosine-containing DNA. Independently measure DNA binding, deoxyinosine formation within recovered DNA and DNA strand integrity. Including free deoxyadenosine distinguishes a sugar-dependent preference from a preference for DNA context. Assess whether DNA-associated activity is relatively spared compared with the free-adenosine deficit.

#### predicted_outcome_if_true

Pig ADA2 shows a reproducibly different substrate-activity profile, with DNA-associated deamination relatively preserved despite weak free-adenosine activity. Preserved binding alone would support retained interaction capacity, but not preserved DNA editing or the full substrate-selectivity hypothesis.

#### falsifying_outcome

All catalytic activities fall proportionately after protein-quality normalization, supporting general impairment rather than altered substrate preference. Failure to detect pig DNA binding or DNA-associated deamination while the human controls work would contradict preservation of the corresponding function. A signal confined to free nucleosides would not establish DNA editing.

#### controls_and_feasibility

Include human ADA2, no-enzyme, mock-purification and substrate-only controls; independent protein batches; nucleic-acid competition controls for binding; and confirmation that substrate DNA lacks free nucleosides. Separate DNA-associated products from soluble products and assess strand integrity independently: binding, editing and cutting are not interchangeable. Control protein amount, folding, processing, glycans, assembly, zinc and assay conditions. Chromatography and mass-spectrometry access support feasibility (CTX-09, CTX-10), but assay development and core availability remain unspecified.

#### next_decision

If DNA editing is relatively spared, pursue verified sequence alignment and substrate-recognition candidates before designing substitutions. If only binding is preserved, prioritize noncatalytic interaction studies. If neither is preserved, investigate general catalytic impairment. Following biochemical evidence of preservation, test pig versus human rescue of DNA-associated localization or TLR9 responses in an ADA2-deficient cellular system, controlling protein uptake and abundance; biochemical preservation alone does not establish cellular rescue.

#### added_value_from_computation

No computational evidence was provided. CTX-04 changes the experiment from an adenosine-only assay to separate binding, DNA-editing and strand-integrity measurements. The free-deoxyadenosine comparator and substrate-recognition mechanism are general biochemical reasoning. CTX-08 supports later localization work, but the existing ADA2 aptamer's recognition of pig ADA2 must be validated rather than assumed.

#### confidence

low

## overall_note

Prioritize matched-preparation replication, then the substrate-panel experiment. All literature observations are supplied as drafts requiring verification; the activity difference lacks an effect size and assay details. Two hypotheses are proposed because no computational evidence supports residue-specific mechanisms. Similar inflammatory disease in ADA2-deficient pigs (CTX-07) motivates functional comparison but does not identify which molecular activity is preserved.

## context_provided_to_model

- condition: A0
- prompt version: v1.0
- background / literature records (shared by all conditions): CTX-01 to CTX-11 (11 records)
- computational evidence: none
- full input hash (sha256, first 12): 568fb971e171
- shared context hash (sha256, first 12): 2a75a6c9f881
- evidence hash (sha256, first 12): 02e0642a5ec6

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
No computational evidence is provided for this task.

=== TASK ===
Propose up to 3 hypotheses that could explain the reported difference between human and pig ADA2 activity on free adenosine, and what other ADA2 functions might be preserved in pig ADA2. For each hypothesis, follow the required JSON fields: the explanation, supporting and conflicting evidence IDs, a plausible alternative explanation, a proposed test, predicted and falsifying outcomes, controls and feasibility, the next decision the team would make after each outcome, and what (if anything) in the provided evidence changed your proposed experiment. If an idea comes from the background information alone or from general knowledge, say so in the last field.
~~~~~~

</details>
