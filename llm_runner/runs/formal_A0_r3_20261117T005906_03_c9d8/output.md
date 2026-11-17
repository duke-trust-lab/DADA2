# formal_A0_r3_20261117T005906_03_c9d8

condition: A0  
model_returned: gpt-6-astra  
reasoning_effort: medium  
prompt_version: v1.0  
status: completed

## hypotheses

### hypotheses[1]

#### title

1. Protein preparation or assay conditions account for much of the activity difference

#### question_and_explanation

Does pig ADA2 remain less active when equivalent preparations are compared? The reported difference lacks effect size and assay details (CTX-01). Different signal-peptide annotations and glycosylation-site annotations (CTX-03), together with uncertainty about the actual pig construct (CTX-06), make processing and preparation important first explanations. As a general biochemical possibility, unequal amounts of correctly folded, processed protein could mimic an intrinsic catalytic difference. Under this hypothesis, both free-adenosine activity and other functions could remain intact in appropriately prepared pig ADA2.

#### supporting_evidence_ids

- CTX-01
- CTX-03
- CTX-06

#### conflicting_evidence_ids

_(none)_

#### evidence_notes

These records establish uncertainty, not a demonstrated preparation defect. Annotated glycosylation sites do not establish glycan occupancy in the tested proteins. No supplied observation rules out an intrinsic species difference.

#### alternative_explanation

Pig ADA2 has intrinsically different substrate recognition or catalytic behavior even when folding, processing, protein amount, and assay conditions are matched.

#### proposed_test

Verify the actual expression constructs, then compare independently prepared human and pig ADA2 made in the same expression system with comparable tag handling and purification. Measure adenosine disappearance and inosine formation across substrate concentrations and a shared range of assay conditions. In parallel, assess protein amount, integrity, mature termini, glycosylation, folding, oligomeric state, and zinc occupancy. If one preparation feature tracks activity, vary that feature independently rather than attributing causality to the initial comparison.

#### predicted_outcome_if_true

The activity gap substantially narrows after correcting preparation differences or choosing conditions that support both proteins. Activity tracks protein quality, processing, or assay conditions more strongly than species identity.

#### falsifying_outcome

A reproducible activity gap persists across independent preparations after protein quality, processing, amount, zinc occupancy, assembly, and assay conditions have been assessed and comparably controlled.

#### controls_and_feasibility

Include no-enzyme and mock-purification controls, product standards, a human ADA2 reference preparation, and independent protein batches. Normalize to quantified intact protein and report remaining uncertainty about the catalytically competent fraction. Expression, purification, chromatography, and relevant core characterization are supported by CTX-08, CTX-09, and CTX-10; specific scheduling and costs are not provided.

#### next_decision

If matching preparations removes the gap, identify the responsible preparation variable before pursuing species-specific mutations. If the gap persists, prioritize intrinsic kinetics and assembly tests. If results vary by batch without an identifiable cause, improve preparation reproducibility before interpreting biological differences.

#### added_value_from_computation

No computational evidence was supplied. This experiment comes from the background uncertainties; CTX-03 specifically adds processing and glycosylation checks, and CTX-06 adds construct verification. The causal effects proposed for folding, zinc occupancy, and assay conditions are general biochemical reasoning.

#### confidence

low

### hypotheses[2]

#### title

2. Pig ADA2 has altered substrate preference, with DNA-associated activity potentially preserved

#### question_and_explanation

Could pig ADA2 handle free adenosine poorly while retaining activity on deoxyadenosine within DNA? Lower free-adenosine activity is reported in CTX-01, whereas DNA interactions and DNA-associated deamination were reported for ADA2 in CTX-04. A species-dependent change in substrate recognition is therefore testable, but neither a responsible substitution nor preserved pig DNA activity is established.

#### supporting_evidence_ids

- CTX-01
- CTX-02
- CTX-04

#### conflicting_evidence_ids

_(none)_

#### evidence_notes

CTX-04 motivates a second substrate class; it does not demonstrate that pig ADA2 binds or edits DNA. There is no supplied alignment or pig structure supporting a particular residue-level mechanism.

#### alternative_explanation

Pig ADA2 has a general loss of catalytic competence rather than selective loss of free-adenosine activity. Alternatively, apparent DNA activity could arise from contaminants or free nucleosides rather than modification within DNA.

#### proposed_test

Using quality-matched preparations, compare concentration-dependent free-adenosine kinetics with separate measurements of DNA binding, DNA-associated deoxyadenosine-to-deoxyinosine conversion, and DNA cleavage. Verify that any conversion product derives from the DNA fraction rather than free nucleosides. Include free deoxyadenosine as an additional comparator to help distinguish nucleoside chemistry from recognition of a DNA context.

#### predicted_outcome_if_true

Pig ADA2 shows a smaller deficit relative to human ADA2 for DNA-associated deamination than for free-adenosine turnover. Preserved DNA binding alone would support retained interaction capacity, but would not establish preserved editing.

#### falsifying_outcome

Pig ADA2 loses DNA-associated deamination to a similar or greater extent than free-adenosine turnover under validated, matched conditions. Failure to reproduce DNA-associated conversion with the human reference would make the pig comparison inconclusive rather than falsify it.

#### controls_and_feasibility

Include human ADA2, no-protein and mock-purification controls, independent protein batches, appropriate analytical standards, and checks for contaminating deaminases or nucleases. Measure DNA integrity separately from base conversion. Match protein amount, processing, glycosylation, folding, and assembly, and test shared assay conditions. Purification and mass-spectrometry access are supported by CTX-08 through CTX-10, but a validated DNA-editing assay is not documented.

#### next_decision

If selective preservation is observed, verify it with an orthogonal readout before mapping sequence determinants or testing TLR9-related cellular consequences. If binding is retained without editing, pursue a noncatalytic interaction hypothesis instead. If both catalytic activities are impaired, investigate shared catalytic competence, zinc occupancy, or assembly.

#### added_value_from_computation

No computational evidence was supplied. CTX-04 changes the proposed experiment from a free-nucleoside assay alone to separate binding, editing, and cleavage measurements. Substrate selectivity and the free-deoxyadenosine comparator are general biochemical reasoning, not computed findings.

#### confidence

low

### hypotheses[3]

#### title

3. Altered dimer assembly reduces free-adenosine turnover while leaving interaction functions intact

#### question_and_explanation

Does pig ADA2 assemble differently, and does that account for reduced activity? Human ADA2 is a homodimer (CTX-02), but pig assembly in the laboratory preparations is unknown. General biochemical reasoning suggests that altered assembly could affect catalytic organization without abolishing a separate DNA- or partner-binding surface. Preserved binding or localization could be relevant to functions beyond free-adenosine turnover, but the pig disease phenotype alone does not identify such a function (CTX-07).

#### supporting_evidence_ids

- CTX-01
- CTX-02
- CTX-04

#### conflicting_evidence_ids

_(none)_

#### evidence_notes

The evidence establishes human dimerization, not an assembly defect in pig ADA2 or a requirement for dimerization in catalysis. This hypothesis is less directly supported than the need to control protein preparation.

#### alternative_explanation

Both orthologs form equivalent dimers, and the activity difference comes from local catalytic properties. Alternatively, apparent assembly differences reflect misfolding, aggregation, tags, glycosylation, or protein concentration rather than a native species difference.

#### proposed_test

Measure oligomeric state and free-adenosine turnover across matched protein concentrations and conditions, accounting for concentration-dependent assembly during the activity assay. Where feasible, compare well-characterized assembly states while checking folding and integrity. Measure DNA binding independently. Only if an assembly-dependent activity difference is found, test whether a controlled shift toward the human-like assembly state changes pig turnover without altering protein quality.

#### predicted_outcome_if_true

Pig ADA2 has a different assembly distribution, and its turnover per unit protein tracks the dimer fraction. Favoring the human-like assembly state increases pig activity. DNA binding can remain detectable in a low-turnover state.

#### falsifying_outcome

Both proteins show equivalent assembly under activity-assay conditions yet retain different turnover, or changing the pig dimer fraction leaves turnover unchanged after folding and protein amount are controlled. Loss of DNA binding would contradict the proposed preserved interaction, but not by itself the assembly mechanism.

#### controls_and_feasibility

Use human ADA2 as an assembly reference, independent preparations, matched tags and processing, aggregation and folding checks, and an orthogonal oligomerization measurement. DNA-binding controls should include unrelated nucleic-acid competitors to assess nonspecific association. CTX-08 and CTX-09 support protein characterization and FPLC; the exact available method for absolute oligomeric mass is not specified. Any use of the ADA2 aptamer from CTX-08 requires validating pig recognition first.

#### next_decision

If assembly causally tracks activity, investigate assembly determinants only after verifying and aligning the actual constructs. If assembly is equivalent, deprioritize this mechanism and focus on substrate handling. If DNA binding persists, consider cellular localization and TLR9-response tests with matched uptake, protein amount, and contamination controls; binding alone is not evidence of a preserved TLR9 function.

#### added_value_from_computation

No computational evidence was supplied. CTX-02 motivates the assembly measurement, and CTX-04 motivates an independent interaction readout. The assembly-to-catalysis connection is a general biochemical hypothesis; no interface residues or structural differences can be nominated from the supplied evidence.

#### confidence

low

## overall_note

Prioritize the matched-preparation comparison, incorporating oligomeric-state measurements where practical, before undertaking sequence swaps or animal experiments. The literature observations are explicitly provisional, and the reported activity difference lacks quantitative detail. No supplied sequence analysis or pig experimental structure justifies naming causal residues. DNA binding, DNA editing, DNA cleavage, localization, and TLR9 effects require distinct readouts; none is established as preserved in pig ADA2.

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
