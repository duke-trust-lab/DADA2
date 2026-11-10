# Structure evidence package (AlphaFold 3 predictions)

Method summary: Human (UniProt Q9NZK5, residues 30-511) and pig (P58780, residues 25-510) ADA2, each with its UniProt-annotated signal peptide removed, were modelled as homodimers (two copies plus one Zn2+ per chain; no glycans, no DNA) on AlphaFold Server (AlphaFold 3). Twelve jobs were run: three seeds per species with zinc and templates, one no-zinc job per species, and two no-template jobs per species; each job returns five models. Predictions were compared with the human crystal structure 3LGD (chains A and B, UniProt 29-510) by superposing C-alpha atoms on residues matched by sequence position. Pig positions were mapped to human positions using a draft pairwise alignment. pLDDT is AlphaFold's per-residue local confidence (0-100); PAE is its expected position error (A); ipTM and pTM (0-1) describe confidence in the chain interface and overall fold.

Depends on: UniProt reference sequences; the draft human-pig position map; the human crystal structure 3LGD. These are predictions, not measurements of activity or binding.

Status: DRAFT until checked by a second person.

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
