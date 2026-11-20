# Sequence evidence package — SEQ v1.0 — 18 November 2026

Owner: Canyang Xu. Numerical analysis executed in Google Colab on 9 November 2026. Integration audit prepared on 18 November. This is a computationally checked package pending team review. All coordinates are full-length UniProt unless explicitly labeled otherwise. No ESM-2 scores are used.

## SEQ-01 — Full precursor sequences

observation: 516 columns contain 356 matches, 149 substitutions and 11 gap columns; 505 columns pair residues.
value_and_units: 68.99% identity including gaps; 70.50% over paired residues
evidence_type: sequence calculation / database annotation
method: Full-length global alignment; Biopython 1.86; BLOSUM62; gap open -10, extend -0.5 including ends; frozen inputs
input_run_files: evidence/inputs/alignment.fasta; evidence/tables/all_differences.csv
uncertainty: Statistics depend on alignment definition. Eleven gap columns are not eleven insertion/deletion events.
limitations: Reference sequences are not confirmed laboratory constructs. No activity, binding or clinical effect was measured.
interpretation_boundary: Sequence identity does not measure functional equivalence.
verification_status: Computational QC passed; team scientific review pending

## SEQ-02 — Human 151–156 and 509–510

observation: Nine baseline optima and sensitivity analyses identify non-unique correspondence at these positions. Tested gap settings (-8,-0.5),(-12,-0.5),(-10,-1) yield 9,9,42 optima.
value_and_units: 8 uncertain human positions
evidence_type: sequence calculation / database annotation
method: Full-length global alignment; Biopython 1.86; BLOSUM62; gap open -10, extend -0.5 including ends; frozen inputs
input_run_files: evidence/tables/alignment_sensitivity.csv; evidence/tables/Human_Pig_Residue_Correspondence.csv
uncertainty: The representative alignment is one optimum. Stability applies only to tested settings.
limitations: Reference sequences are not confirmed laboratory constructs. No activity, binding or clinical effect was measured.
interpretation_boundary: Large structural deviations in these regions cannot be attributed solely to biology; do not force one-to-one mapping.
verification_status: Computational QC passed; team scientific review pending

## SEQ-03 — All 149 substitutions

observation: 61 coarse chemical-class changes; 10 acidic/basic reversals; 39 hydrophobic-category changes; 3 proline and 10 glycine changes; 49 negative BLOSUM62 scores.
value_and_units: Counts overlap
evidence_type: sequence calculation / database annotation
method: Full-length global alignment; Biopython 1.86; BLOSUM62; gap open -10, extend -0.5 including ends; frozen inputs
input_run_files: evidence/tables/all_149_substitutions_annotated.csv
uncertainty: D/E acidic, K/R basic, H separate, others neutral; hydrophobic set AVILMFWY.
limitations: Reference sequences are not confirmed laboratory constructs. No activity, binding or clinical effect was measured.
interpretation_boundary: Flags prioritize inspection; they are not electrostatic potentials, pH-dependent charges or pathogenicity predictions.
verification_status: Computational QC passed; team scientific review pending

## SEQ-04 — Human catalytic, zinc-binding, substrate and disulfide annotations

observation: E359/H384 and H112/H114/H356/D441 are identical in pig. Four individual substrate-binding sites 115/293/326/442 and disulfide endpoints C137/C159 are also identical.
value_and_units: 2/2 catalytic; 4/4 zinc; 4/4 individual binding; 2/2 disulfide endpoints conserved
evidence_type: sequence calculation / database annotation
method: Full-length global alignment; Biopython 1.86; BLOSUM62; gap open -10, extend -0.5 including ends; frozen inputs
input_run_files: evidence/tables/functional_site_summary.csv; evidence/tables/human_feature_provenance.csv
uncertainty: Human annotations have heterogeneous evidence codes. Conservation does not establish pig activity; interval interiors are not disulfide endpoints.
limitations: Reference sequences are not confirmed laboratory constructs. No activity, binding or clinical effect was measured.
interpretation_boundary: Conserved core residues constrain simple substitution explanations but do not exclude differences in dynamics, assembly, processing or assay conditions.
verification_status: Computational QC passed; team scientific review pending

## SEQ-05 — Human N185 / pig T182; other human glycosylation positions

observation: Human NFT at 185 maps to pig TFT at 182, removing the canonical N-linked sequon at that position. The N at human sites 127,174,378 is retained at mapped pig positions.
value_and_units: 1 of 4 annotated human glycosylation residues substituted
evidence_type: sequence calculation / database annotation
method: Full-length global alignment; Biopython 1.86; BLOSUM62; gap open -10, extend -0.5 including ends; frozen inputs
input_run_files: evidence/tables/glycosylation_motif_comparison.csv; evidence/tables/candidate_sites.csv
uncertainty: No pig glycan occupancy, recombinant glycoform, secretion or stability measurement.
limitations: Reference sequences are not confirmed laboratory constructs. No activity, binding or clinical effect was measured.
interpretation_boundary: Supports a local modification question, not a claim that pig ADA2 is unglycosylated or that this explains lower activity.
verification_status: Computational QC passed; team scientific review pending

## SEQ-06 — Human substrate-binding interval 204–211

observation: Six residues are identical; S205 maps to pig K202 and E208 to pig K205. These are neutral-to-basic and acidic-to-basic category changes.
value_and_units: 2 substitutions / 8 interval residues
evidence_type: sequence calculation / database annotation
method: Full-length global alignment; Biopython 1.86; BLOSUM62; gap open -10, extend -0.5 including ends; frozen inputs
input_run_files: evidence/tables/feature_residue_correspondence.csv; evidence/tables/candidate_sites.csv
uncertainty: An interval annotation does not establish a direct ligand contact for either side chain.
limitations: Reference sequences are not confirmed laboratory constructs. No activity, binding or clinical effect was measured.
interpretation_boundary: Supports a local environment/substrate-handling question, not a measured affinity or catalytic change.
verification_status: Computational QC passed; team scientific review pending

## SEQ-07 — Exploratory shortlist and human experimental geometry

observation: Stable substitutions satisfying either a changed human glycosylation site or a chemical-class change in the binding interval yield exactly N185/T182, S205/K202, E208/K205. Minimum heavy-atom distances to nearest same-chain catalytic/zinc anchor across 3LGD/3LGG A/B are 15.4–15.6,11.8–11.9,8.8–10.4 Å respectively.
value_and_units: 3 candidates; none within 5 Å of the defined anchors
evidence_type: sequence calculation / database annotation
method: Full-length global alignment; Biopython 1.86; BLOSUM62; gap open -10, extend -0.5 including ends; frozen inputs
input_run_files: evidence/tables/candidate_evidence_cards.csv; evidence/tables/catalytic_neighborhood_distances_all_chains.csv
uncertainty: Exploratory selection, not preregistered or a ranking. Human experimental geometry only; not ligand distance. Backbone and side-chain atoms included.
limitations: Reference sequences are not confirmed laboratory constructs. No activity, binding or clinical effect was measured.
interpretation_boundary: These are annotation-led questions, not close-contact mutations. No pig structure prediction or experimental validation is supplied by this track.
verification_status: Computational QC passed; team scientific review pending

## SEQ-08 — Cross-track numbering and structural priority regions

observation: Human 281 maps to pig 278 and human 347 to pig 344. The nearby differences V277/A274, E278/K275, E282/G279, K346/S343 and D347/R344 are stable in the checked alignment. Human 151–156 mapping remains uncertain; human 157–160 must be checked individually rather than labeling the entire window ambiguous.
value_and_units: UniProt precursor coordinates are the cross-track join key
evidence_type: sequence calculation / database annotation
method: Full-length global alignment; Biopython 1.86; BLOSUM62; gap open -10, extend -0.5 including ends; frozen inputs
input_run_files: integration/team_priority_residues.csv; integration/draft_mapping_discrepancies.csv; evidence/tables/Sequence_to_Structure_Residue_Mapping.csv
uncertainty: Mature AF3 model positions require species-specific offsets (+29 human, +24 pig), verified against model residue identities. Experimental PDB author numbering is a separate mapping.
limitations: Reference sequences are not confirmed laboratory constructs. No activity, binding or clinical effect was measured.
interpretation_boundary: Local sequence support does not confirm the magnitude or functional meaning of AlphaFold displacement; draft-map-dependent structural calculations require sensitivity review.
verification_status: Computational QC passed; team scientific review pending
