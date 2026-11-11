# Surface electrostatics track

Project: ADA2 human vs pig comparison. Status as of the Nov 11, 2026 push.
Track: surface electrostatics (PDB2PQR + APBS). Owner: Sienna (GitHub: sienna-wangxy).

Project-wide decisions, open questions and handoff items are in [`../NOTES.md`](../NOTES.md).

All results here are calculations. A positive surface potential is a possible interaction clue only. It does not measure DNA or GAG binding, specificity, or catalytic activity.

## 1. Summary

Human and pig ADA2 dimers were prepared with PDB2PQR, and their electrostatic potential was calculated with APBS at pH 7.4 and two ionic strengths (0 M and 0.15 M). Per-residue surface potential was extracted and compared between species using the human-pig residue correspondence from the sequence track.

At 0.15 M the human surface is more positive than the pig surface (16 vs 6 residues above +3 kT/e). The largest aligned difference is human Arg395 (+11.2 kT/e) vs pig Trp392 (-0.6 kT/e). The residue ranking is stable between the two ionic strengths (Spearman 0.95 human, 0.97 pig).

The evidence records are in [`../llm_runner/evidence/surface_evidence_records_DRAFT.csv`](../llm_runner/evidence/surface_evidence_records_DRAFT.csv) (SURF-01 to SURF-07). They are a draft until checked by a second person.

## 2. What was done

1. Took the AlphaFold 3 human and pig dimer models from `../structure_prediction/shared_models/` (seed 101, model 0) and prepared them with PDB2PQR at pH 7.4.
2. Ran APBS for each species at 0 M (no mobile ions) and 0.15 M ionic strength: four maps in total.
3. Wrote `surface_findings.py` to read each map and report the surface potential of every residue. Only sample points in the solvent are used, so buried atoms do not distort the values.
4. Wrote `renumber_pqr.py` to convert the structure files to UniProt numbering, so the results match the sequence track and the evidence records. The offsets were checked on every surface residue.
5. Wrote `compare.py` to list the most positive residues per species and to compare 0 M with 0.15 M (salt sensitivity check).
6. Paired human and pig residues using the sequence track's correspondence table (199 aligned positions sampled in both species) and built `human_pig_aligned_surface_potential.csv`.
7. Compared four regions chosen in advance or from the data, and wrote seven evidence records.

| Region | Human (UniProt) | Pig (UniProt) | Human mean at 0.15 M (kT/e) | Pig mean at 0.15 M (kT/e) | Basis |
|---|---|---|---|---|---|
| R1 N-terminal | 30-50 | 25-45 | +2.30 | +0.56 | Prior |
| R2 | 389-400 | 386-397 | +6.83 | +0.45 | Exploratory |
| R3 C-terminal | 460-500 | 457-497 | +0.71 | -0.33 | Exploratory |
| R4 zinc site | His114 | His109 | -20.34 | -19.73 | Prior; null result |

Segments 151-156 and 509-510 (human) were excluded because their human-pig alignment is uncertain.

## 3. Layout

```
surface_analysis/
├── README.md                  this file
├── requirements.txt           numpy, pandas, scipy
├── scripts/
│   ├── renumber_pqr.py        renumber a .pqr to UniProt numbers (coordinates unchanged)
│   ├── surface_findings.py    per-residue surface potential from a .pqr + APBS .dx
│   └── compare.py             human vs pig lists and salt check (0 M vs 0.15 M)
├── inputs/                    .pqr files (original and UniProt-renumbered), APBS settings
├── apbs_outputs/              APBS .dx maps (NOT in git; see below)
└── results/
    ├── human_0M_residues.csv, human_150_residues.csv
    ├── pig_0M_residues.csv,   pig_150_residues.csv
    ├── human_salt_check.csv,  pig_salt_check.csv
    └── human_pig_aligned_surface_potential.csv
```

### APBS maps (.dx)

The four `.dx` maps are about 120 MB each, above GitHub's 100 MB file limit, so they are not stored in git (`.gitignore` excludes `surface_analysis/apbs_outputs/*.dx`).

They are in the team Google Drive: [surface_analysis APBS outputs](https://drive.google.com/drive/folders/14SJNDJQ06nd5agIgDJKuUiG-YzEs2stP)

Files: `human_0M.dx`, `human_150.dx`, `pig_0M.dx`, `pig_150.dx`. Download them into `surface_analysis/apbs_outputs/` to rerun the scripts.

## 4. Settings

| Item | Setting |
|---|---|
| Structures | AlphaFold 3 top models, seed 101, templates on: `HUM_ADA2_mature30-511_dimer_Zn_s101_model0.cif` and `PIG_ADA2_mature25-510_dimer_Zn_s101_model0.cif` |
| Segments | Human UniProt 30-511, pig UniProt 25-510, two chains each |
| Charges and radii | PDB2PQR, pH 7.4 (AMBER-style names such as HID, HIP, CYX) |
| Ionic strength | 0 M (no mobile ions) and 0.15 M |
| Not included | Zinc (present in the AlphaFold models but removed by PDB2PQR), glycans |
| Surface sampling | One point 3 A outward from each atom, kept only if at least 2.5 A from every atom; potential at the nearest grid point; averaged per residue, then over chains A and B |

## 5. Numbering

PDB2PQR numbers residues 1..N within each chain. `renumber_pqr.py` converts them to UniProt numbers:

- human UniProt = file number + 29
- pig UniProt = file number + 24
- 3LGD author numbering = human UniProt - 26

Checked against the UniProt sequences for every surface residue (human 441/441, pig 460/460). All results and evidence records use UniProt numbers.

## 6. How to reproduce

Download the `.dx` maps first (see section 3). Then, from inside `surface_analysis/`:

```bash
pip install -r requirements.txt

# 1. renumber to UniProt
python scripts/renumber_pqr.py inputs/human.pqr inputs/human_uniprot.pqr 29
python scripts/renumber_pqr.py inputs/pig.pqr   inputs/pig_uniprot.pqr   24

# 2. per-residue surface potential (writes <label>_residues.csv in the current folder)
python scripts/surface_findings.py inputs/human_uniprot.pqr apbs_outputs/human_0M.dx  human_0M
python scripts/surface_findings.py inputs/human_uniprot.pqr apbs_outputs/human_150.dx human_150
python scripts/surface_findings.py inputs/pig_uniprot.pqr   apbs_outputs/pig_0M.dx    pig_0M
python scripts/surface_findings.py inputs/pig_uniprot.pqr   apbs_outputs/pig_150.dx   pig_150

# 3. human vs pig lists and salt check
python scripts/compare.py
```

Then move the new CSV files into `results/`.

## 7. Limitations

- pH 7.4 only. A second pH was optional and has not been run.
- Zinc was removed during PDB2PQR preparation, so the active site appears artificially negative.
- Human His391 was assigned as positively charged (HIP); its value depends on that choice.
- Surface sampling is approximate. Residues sampled at only one point are less reliable.
- Regions R2 and R3 were chosen after looking at the data and are exploratory.

## 8. Open items

- Second-person check of SURF-01 to SURF-07.
- Visual check in PyMOL that human Arg395 and His391 form one exposed surface patch.
- Replace the placeholder `../llm_runner/evidence/surface_evidence_A2.md` with the checked package after team agreement.
