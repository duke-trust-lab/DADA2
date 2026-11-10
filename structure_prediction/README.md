# AlphaFold 3 structure track

Project: ADA2 human vs pig comparison. Status as of the Oct 20, 2026 team meeting.
Track: molecular arrangements (AlphaFold 3 structure prediction).

Project-wide decisions, open questions and handoff items are in [`../NOTES.md`](../NOTES.md).

All structural results here are predictions. Confidence scores describe how reliable a prediction is. They do not measure binding, catalytic activity, or the effect of a mutation.

## 1. Summary

Matched human and pig ADA2 dimer predictions were set up, run on AlphaFold Server, and compared with the human crystal structure 3LGD. Both species are predicted as confident dimers with intact zinc sites. The human prediction reproduces the crystal structure closely. The pig dimer is predicted with a slightly different arrangement of the two chains. This held with PDB templates turned off, so it is not a template artifact. Several decisions still need Dr. Bent, and earlier AlphaFold inputs and outputs are still to be recovered.

## 2. What was done

1. Read the starter packet, timeline, and `source_manifest.json`, and checked the supplied sequences, UniProt annotations, and the 3LGD/3LGG structures.
2. Aligned human (Q9NZK5, 511 aa) and pig (P58780, 510 aa) ADA2 and drafted a position map (`human_pig_position_map_DRAFT.csv`). Yang's alignment is the intended official version.
3. Chose the modeled segments (a proposal, not specified by the project): each species with its own UniProt signal peptide removed. Human 30–511 (482 aa), pig 25–510 (486 aa). Two copies of each, with one Zn2+ per chain.
4. Prepared AlphaFold Server job files in `af3_inputs/` and ran 12 jobs. Each job gives 5 models, so there are 60 models in total.
5. Built a notebook (`AF3_results_comparison.ipynb`) that loads the downloads, tabulates the scores, compares each prediction with 3LGD, measures seed-to-seed variation, and compares human vs pig. Results are saved in `af3_results/`.
6. Collected the open decisions and questions for Dr. Bent in `../NOTES.md`.

### Jobs run

| Setting | Human | Pig |
|---|---|---|
| Dimer + Zn, templates on | seeds 101, 202, 303 | seeds 101, 202, 303 |
| Dimer, no Zn, templates on | seed 101 | seed 101 |
| Dimer + Zn, templates off | seeds 101, 202 | seeds 101, 202 |

Not run: full-length (signal peptide kept) controls, glycans, DNA.

## 3. Results

### 3.1 Sequence observations (from the supplied files; to be verified against Yang's alignment)

- 506 aligned positions, 355 identical (70.2%), 151 differences, 143 of them in the mature region.
- Pig has a 2-residue insertion after human position 154 and a 2-residue C-terminal extension.
- The catalytic residues (human E359, H384) and all UniProt-annotated zinc ligands (human H112, H114, H356, D441) are identical in pig.
- The substrate-binding region (human 204–211) has two differences: S205K and E208K.
- Human has four N-glycosylation sequons (N127, N174, N185, N378). Pig has three, and the N185 sequon is lost. This is a sequence-level observation only.

### 3.2 Prediction confidence

| Group | ipTM | pTM | Between-chain PAE (Å) | Mean pLDDT |
|---|---|---|---|---|
| Human, Zn | 0.92–0.93 | 0.95 | 5.2–5.5 | 93.3–93.6 |
| Human, no Zn | 0.89 | 0.93 | 6.5 | 92.8 |
| Pig, Zn | 0.91–0.93 | 0.94–0.95 | 5.6–6.1 | 93.4–93.9 |
| Pig, no Zn | 0.92 | 0.94 | 5.8 | 93.9 |

No model has a clash. Within each job the five models give nearly the same ipTM (range at most 0.02). Zinc improves the human dimer confidence a little (ipTM 0.89 to 0.92). It makes almost no difference for pig.

### 3.3 Comparison with the human crystal structure 3LGD

| Group | Dimer RMSD (Å) | Chain A alone (Å) | Chain B after chain A fit (Å) | Zn to ligand distance (Å) |
|---|---|---|---|---|
| Human | 0.43–0.46 | 0.40–0.45 | 0.49–0.71 | 2.16–2.29 |
| Pig (aligned residues only) | 1.10–1.28 | 0.73–0.81 | 1.84–2.29 | 2.17–2.32 |

- The human prediction closely reproduces the crystal dimer, and the zinc sites match the crystal (about 2.2 Å).
- The pig single chain is close to the human structure (about 0.75 Å). The two copies sit in a different relative arrangement (chain B about 2 Å off after fitting chain A, versus about 0.6 Å for human).
- Interface overlap with 3LGD: human 0.78–0.86, pig 0.72–0.78 (Jaccard).
- Pig is compared with the human crystal on residues aligned to human. There is no pig crystal structure.

### 3.4 Reproducibility and the template control

- Seed to seed RMSD: human about 0.3 Å, pig about 0.2–0.6 Å.
- AlphaFold Server uses PDB templates by default. For pig, the top template was 3LGD, the human structure. So human and pig were repeated with templates off. Results were essentially unchanged: human dimer RMSD 0.44 vs 0.46 Å, pig 1.27 vs 1.14 Å, and the pig chain B offset stayed (2.2 vs 1.9 Å).

### 3.5 Human vs pig (predicted vs predicted)

- Overall RMSD is 1.16 Å with templates and 1.19 Å without.
- The largest local differences, in both settings, are around residues 151–159 (next to the pig insertion), the N-terminus (about 30–33), and the last residue. Residues 281 and 347 also appear.
- The human–pig difference (about 1.2 Å) is larger than the seed-to-seed spread (about 0.3–0.6 Å).
- Residues 151–159 sit next to an alignment gap, so they need checking against Yang's alignment. The pLDDT and PAE in these regions had not been examined when this was written. See the notebook (section 5) for the pLDDT profile; the region around residue 156 has the lowest pig pLDDT.

## 4. Interpretation (kept separate from observations)

- The active-site and zinc residues are conserved, so a simple swap in the catalytic pocket is unlikely to explain the reported activity difference. This is a clue only.
- The slightly different pig dimer arrangement, and the lost glycosylation site, are candidate clues. They need local confidence checks and expert review before they are treated as real.
- Differences in preparation, processing, glycosylation or assay conditions remain possible explanations.

## 5. Limitations

- Sequences are UniProt references. They may not match the lab's recombinant constructs, which are unknown.
- The segment choice (signal peptide removed) is a proposal and has not been approved.
- Zinc is included, glycans are not, and DNA is not modeled.
- AlphaFold Server is one tool, and the five models per job share a seed. Agreement is not independent confirmation.
- Output terms of use are non-commercial and exclude docking or screening use.
- Earlier AlphaFold inputs and outputs are not yet recovered, and the evidence-record and hypothesis templates are not in the folder.

## 6. Open items and next steps

Questions for Dr. Bent are in `../NOTES.md`: segments, zinc, glycans, templates, DNA scope, lab construct and assay details.

1. Fill in the earlier AlphaFold run details (marked [CONFIRM] in `../NOTES.md`).
2. Confirm the numbers with Yang and replace the draft position map with his alignment.
3. Check pLDDT and PAE in residues 151–160, 281 and 347.
4. Share the structures with Sienna (`shared_models/`), agreeing on segments and chain names.
5. Hold the full-length control and any DNA run until Dr. Bent decides.

## 7. Files

- `af3_inputs/`: AlphaFold Server job files and FASTA files.
- `af3_outputs/`: downloaded AlphaFold zips (12) and their unzipped folders. Large, so **not stored in git** (see below).
- `af3_results/`: score and comparison tables (CSV) and figures.
- `shared_models/`: the top-ranked human and pig dimer models (seed 101) for sharing, with a README on numbering and chain names.
- `AF3_results_comparison.ipynb`: analysis notebook.
- `human_pig_position_map_DRAFT.csv`: draft position map.

### Re-running the analysis

`af3_outputs/` is excluded from git because it is about 0.9 GB. To re-run the notebook, put the AlphaFold Server downloads (the 12 `fold_*` zips or unzipped folders) into `structure_prediction/af3_outputs/`, then run all cells. The saved tables in `af3_results/` are enough to rebuild the LLM evidence package without the raw outputs.

Install: `pip install -r requirements.txt`.
