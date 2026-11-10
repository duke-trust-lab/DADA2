# pilot_A0_r1_20261110T005204_01_5416

condition: A0  
model_returned: gpt-6-astra  
reasoning_effort: medium  
prompt_version: v0.1_DRAFT  
status: completed

## hypotheses

### hypotheses[1]

#### title

Preparation and maturation differences reduce the functional fraction of pig ADA2

#### question_and_explanation

Does the reported activity gap reflect less correctly processed, folded, zinc-loaded, or assembled pig ADA2 rather than intrinsically weaker catalysis? CTX-01 reports lower activity but provides neither assay conditions nor an effect size. Different signal-peptide and glycosylation annotations make maturation worth examining (CTX-03), but do not establish different glycan occupancy in the preparations. If preparation is responsible, pig ADA2 could retain both adenosine activity and other functions when correctly prepared.

#### supporting_evidence_ids

- CTX-01
- CTX-02
- CTX-03
- CTX-06

#### conflicting_evidence_ids

_(none)_

#### evidence_notes

No supplied observation directly demonstrates defective pig protein preparation. Zinc participation and human dimerization are established background observations (CTX-02); pig zinc occupancy and assembly are unknown. The reference pig sequence may not match the tested construct (CTX-06).

#### alternative_explanation

Properly matured pig ADA2 has intrinsically different substrate handling, so a species difference persists even when preparation and assay conditions are matched.

#### proposed_test

First verify the actual constructs and reproduce the activity comparison using independently prepared human and pig proteins from a matched expression and purification workflow. Measure adenosine-to-inosine conversion across substrate concentrations under identical conditions. Independently quantify protein amount and characterize processing, glycosylation, folding, assembly, and zinc occupancy where feasible. If a specific preparation defect is detected, correct that feature and retest both species. Measure DNA binding separately in matched preparations to assess whether an interaction function remains intact despite low free-adenosine activity.

#### predicted_outcome_if_true

Low pig activity tracks a measurable preparation defect or reduced intact protein fraction, and correcting that feature substantially narrows the activity gap. Detectable pig DNA binding would show preservation of an interaction, not establish DNA editing or cellular function.

#### falsifying_outcome

The activity gap persists across independent preparations with comparable amount, maturation, folding, assembly, and zinc occupancy, and does not respond to correction of any detected preparation differences.

#### controls_and_feasibility

Use human ADA2 processed in parallel, independent preparation batches, protein-free blanks, product-recovery controls, and identical buffer, temperature, incubation, and substrate conditions. Avoid estimating functional protein amount from the activity being compared. Include DNA-binding background controls and distinguish aggregation from binding. CTX-08 supports recombinant protein work broadly; availability of specific glycan, metal, folding, and assembly measurements must be confirmed.

#### next_decision

If correcting a preparation feature rescues activity, standardize that feature before interpreting species differences or starting mutagenesis. If the gap persists, prioritize intrinsic substrate-selectivity tests. If assembly rather than processing differs reproducibly, investigate assembly as a separate mechanism.

#### added_value_from_computation

No computational evidence was supplied. This experiment follows from background uncertainties in CTX-01, CTX-03, and CTX-06. The connection between maturation, functional protein fraction, and apparent enzyme activity is general biochemical reasoning, not a provided measurement.

#### confidence

low

### hypotheses[2]

#### title

Pig ADA2 has intrinsically different substrate selectivity while retaining DNA interaction or editing

#### question_and_explanation

Could species-specific sequence differences impair free-adenosine recognition or catalysis while preserving DNA binding and possibly DNA-associated deamination? Lower free-adenosine activity is reported in CTX-01, and DNA interaction and editing are reported for ADA2 in CTX-04. Neither observation establishes pig DNA activity. No alignment or pig experimental structure is supplied, so no particular substitution or active-site change can yet be nominated.

#### supporting_evidence_ids

- CTX-01
- CTX-02
- CTX-04
- CTX-06

#### conflicting_evidence_ids

_(none)_

#### evidence_notes

The observations motivate a substrate-selectivity test but do not show that the reported activities are conserved in pig. DNA binding, DNA editing, DNA cutting, and lysosomal/TLR9 effects must remain separate endpoints.

#### alternative_explanation

Pig ADA2 has a general catalytic impairment rather than altered substrate selectivity; DNA binding could survive even if both free-substrate and DNA-associated deamination are lost. Preparation differences could also produce the apparent selectivity.

#### proposed_test

Using quality-matched preparations, compare free-adenosine kinetics and condition dependence alongside independent measurements of DNA binding and formation of deoxyinosine within DNA. Establish that any detected deoxyinosine was generated in DNA rather than from free nucleosides or contaminating enzymes. If pig DNA editing is retained despite weak free-adenosine activity, align the verified constructs before selecting reciprocal sequence swaps to test causality. If only binding is retained, treat that as evidence for preserved interaction rather than preserved catalysis.

#### predicted_outcome_if_true

Pig ADA2 remains less active on free adenosine under matched conditions but retains DNA binding and, for the stronger substrate-selectivity hypothesis, DNA-associated deamination. A reproducible separation between the two catalytic readouts supports substrate-dependent function rather than a uniform loss of catalytic competence.

#### falsifying_outcome

The free-adenosine difference disappears after preparation or condition matching. Alternatively, a comparable loss of both catalytic activities would weaken selective preservation of DNA editing, although DNA binding could still be preserved. Failure to detect pig DNA binding under conditions that detect the human interaction would weaken the interaction-preservation claim.

#### controls_and_feasibility

Use human ADA2, protein-free and mock-purification controls, matched protein amounts, and a validated catalytically impaired control if available. Check DNA integrity separately to distinguish editing from cutting, exclude free-nucleoside contributions, and use binding competition controls to assess nonspecific association. CTX-08 supports broad biochemical expertise but does not confirm a validated DNA-editing assay; analytical capability and assay sensitivity must be established. The ADA2 aptamer in CTX-08 is not evidence that pig ADA2 binds DNA or that the aptamer recognizes pig ADA2.

#### next_decision

If DNA editing is selectively retained, pursue aligned sequence comparisons and reciprocal perturbations. If only DNA binding survives, prioritize interaction-dependent functions without claiming editing. If both catalytic activities decline together, investigate general catalytic competence and assembly. Only after biochemical preservation is established should lysosomal localization or TLR9-related effects be tested with matched delivery and expression controls.

#### added_value_from_computation

No computational evidence was supplied. CTX-04 changes the experiment by motivating separate DNA-binding and DNA-editing measurements rather than treating free-adenosine activity as a proxy for all ADA2 functions. Substrate-selective effects of sequence changes are a general scientific hypothesis, not an observed human–pig difference.

#### confidence

low

## overall_note

Prioritize the matched-preparation comparison because CTX-01 lacks effect size, assay conditions, and raw data, and all literature observations are supplied as drafts needing verification. Two hypotheses are proposed: the evidence does not yet justify a specific residue, structural mechanism, or third independent explanation. The pig disease-model phenotype in CTX-07 motivates studying conserved functions but does not identify which molecular function is preserved.

## context_provided_to_model

- condition: A0
- prompt version: v0.1_DRAFT
- background / literature records (shared by all conditions): CTX-01 to CTX-08 (8 records)
- computational evidence: none
- full input hash (sha256, first 12): fc0f146c1f23
- shared context hash (sha256, first 12): a6539b55b600
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
CTX-08. Laboratory capabilities reported by the laboratory. People: six PhD scientists and a couple of skilled technicians, with broad expertise in biochemistry, enzymology, genetics, immunology, and cell biology. One member specializes in developing DNA and RNA aptamers and has developed an aptamer specific for ADA2, which is being used to study where ADA2 is located in living monocytes and macrophages. Two further members are expected to join in January: one with expertise in protein expression, purification, and structure analysis by NMR and other techniques, and one with extensive expertise in mass spectrometry for metabolomic and proteomic studies; these two are expected to test hypotheses about ADA2's function and molecular partners. Equipment: the laboratory states that it has, or has access to, the equipment needed to over-express, purify, and characterize recombinant human and pig ADA2 and otherwise pursue this research. Source: the same written reply. The reply does not list specific instruments, methods, or constraints, and it gives no limits on what the laboratory cannot do.

Known unknowns
- The exact human and pig recombinant constructs (signal peptide, tags, linkers), expression system, purification, and glycosylation state.
- Assay conditions: substrate, concentrations, pH and buffer, temperature, incubation time.
- Whether pig ADA2 is secreted and dimerizes in the lab's preparations.
- Exactly which experiments the laboratory can and cannot run. CTX-08 gives general expertise and says recombinant protein work is possible, but lists no specific instruments or limits. Do not assume a capability that is not in CTX-07 or CTX-08; if a proposed test needs one, say so.

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
