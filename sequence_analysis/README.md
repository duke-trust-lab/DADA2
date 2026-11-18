# Sequence evidence and cross-track integration

Owner: Canyang Xu. Numerical results were executed in Google Colab on 9 November 2026. Cross-track integration was checked on 18 November against commit 054513cf82598d5c2ad58202e249f59ec8eb59f2. This delivery does not represent a new scientific run, LLM batch or experimental validation.

## Start here

- [English notebook](Sequence_Complete_English.ipynb): six visual demonstration pages, executed analysis, SEQ records and integration audit. English presentation edits preserve numerical results; the presentation edits themselves were not rerun in Colab.
- [A1 evidence](../llm_runner/evidence/sequence_evidence_A1.md): eight source-linked records, replacing the sequence placeholder. Paths beginning `evidence/` and `integration/` in these records are relative to this directory.
- [Structured records](sequence_evidence_records.csv): observations, methods, sources, uncertainties and interpretation boundaries.
- [Team Drive delivery](https://drive.google.com/drive/folders/1QBWAr7v-QA-mco5CveIvQVOdQy6t6S7v): complete downloadable package, standalone interactive views and laboratory-resource source review.

## Results and reproducibility

The full-length comparison contains 356 identical residues, 149 substitutions and 11 gap columns across 516 columns (505 paired positions). Nine recorded QC assertions pass. Inputs, alignment, parameter settings, environment, annotation provenance, complete bidirectional mappings, structure mappings and figures are under `evidence/`. `evidence/output_checksums.json` preserves the cloud-run file hashes. The notebook contains frozen source data for rerunning the analysis in Colab.

Human catalytic residues E359/H384 and zinc ligands H112/H114/H356/D441 are conserved. Exploratory candidates are N185/T182, S205/K202 and E208/K205, selected by explicit annotation/property rules. These are cross-species differences, not validated functional effects or clinical variants. No ESM-2 scores are included.

## Reconciliation with the structural track

Seven human positions differ between the draft and representative sequence maps: 151–155, 509–510. All are uncertain under the sequence sensitivity checks; 156 is also uncertain even where the two selected maps agree. See `integration/draft_mapping_discrepancies.csv`. Do not interpret alternate gap placements as experimentally established structural differences.

The draft sequence summary used 506 pairs and 355 identities; this analysis uses 505 pairs and 356 identities. The original draft map, STRUCT records and archived formal runs remain unchanged. Draft-map-dependent structural RMSDs and local deviations need a sensitivity check before revised structural evidence is frozen. This PR does not recompute those metrics.

The supplied mature human/pig shared models passed 1,936 chain-residue identity checks against the reference sequences. For these files, full-length UniProt position is model label_seq_id +29 (human) or +24 (pig). Experimental PDB author numbers require the separate SIFTS map. These checks do not independently validate unseen PQR files or APBS results. Priority residues around human 281/347 and surface-track regions are listed in `integration/team_priority_residues.csv`.

## Runner status and next action

A1 can now be built without a sequence placeholder. A4 includes the identical A1 text, but still contains the surface placeholder at this reviewed revision. A0/A3 shared context, prompt, configuration, structure evidence and archived outputs are unchanged. Their six saved input hashes reproduce exactly. No paid API calls are made by the validation script.

Run from the repository root:

```sh
python3 sequence_analysis/verify_integration.py
python3 llm_runner/runner/llm_runner.py dry-run
```

Pranshul and the team should resolve draft-map sensitivity and freeze A2 before A4 formal execution. Do not silently revise old A3 inputs; version changed evidence and preserve run lineage. The existing A0/A3 runs preceded this handoff, and their outputs were available during integration; this timing must remain visible in study reporting.

Lab equipment is already represented in frozen CTX-09–CTX-11. Resource-review notes stay outside A1 so common background does not differ across conditions. The existing hypothesis ledger is a traceability index, not a completed biological or claim-level review. New sequence claims should be checked using the review template.
