# Surface electrostatics track

Project: ADA2 human vs pig comparison. Status as of the Nov 10, 2026 team meeting.
Track: surface electrostatics (PDB2PQR + APBS). Owner: Sienna.

Project-wide decisions, open questions and handoff items are in [`../NOTES.md`](../NOTES.md).

All results here are calculations. A positive surface potential is a possible interaction clue only. It does not measure DNA or GAG binding, specificity, or catalytic activity.

## 1. Summary

Human and pig ADA2 dimers were prepared with PDB2PQR and their electrostatic potential was calculated with APBS at pH 7.4 and two ionic strengths (0 M and 0.15 M). Per-residue surface potential was extracted and compared between species using the human-pig residue correspondence. At 0.15 M the human surface is more positive than the pig surface. The largest aligned difference is human Arg395 (+11.2 kT/e) vs pig Trp392 (-0.6 kT/e). The residue ranking is stable between the two ionic strengths. The evidence records are in `../llm_runner/evidence/surface_evidence_records_DRAFT.csv` (SURF-01 to SURF-07).

## 2. Layout

```
surface_analysis/
├── README.md                  this file
├── requirements.txt           numpy, pandas, scipy
├── scripts/
│   ├── renumber_pqr.py        renumber a .pqr to UniProt numbers (coordinates unchanged)
│   ├── surface_findings.py    per-residue surface potential from a .pqr + APBS .dx
│   └── compare.py             human vs pig lists and salt check (0 M vs 0.15 M)
├── inputs/                    .pqr files (original and UniProt-renumbered), APBS settings
├── apbs_outputs/              APBS .dx maps (see note on file size below)
└── results/
    ├── human_0M_residues.csv, human_150_residues.csv
    ├── pig_0M_residues.csv,   pig_150_residues.csv
    ├── human_salt_check.csv,  pig_salt_check.csv
    └── human_pig_aligned_surface_potential.csv
```

If the `.dx` maps are larger than about 50 MB each, they are not stored in git. Keep them in the shared drive and list their location here.

## 3. Settings

| Item | Setting |
|---|---|
| Structures | AlphaFold 3 top models, seed 101, templates on: `../structure_prediction/shared_models/HUM_ADA2_mature30-511_dimer_Zn_s101_model0.cif` and `PIG_ADA2_mature25-510_dimer_Zn_s101_model0.cif` (to confirm with the structure track) |
| Segments | Human UniProt 30-511, pig UniProt 25-510, two chains each |
| Charges and radii | PDB2PQR, pH 7.4 (AMBER-style names such as HID, HIP, CYX) |
| Ionic strength | 0 M (no mobile ions) and 0.15 M |
| Not included | Zinc (present in the AlphaFold models but removed by PDB2PQR), glycans |
| Surface sampling | One point 3 A outward from each atom, kept only if at least 2.5 A from every atom; potential at the nearest grid point; averaged per residue, then over chains A and B |

## 4. Numbering

The `.pqr` files from PDB2PQR number residues 1..N within each chain. `renumber_pqr.py` converts them to UniProt numbers so all results match the sequence track and the evidence records.

- human UniProt = file number + 29
- pig UniProt = file number + 24
- 3LGD author numbering = human UniProt - 26

The offsets were checked against the UniProt sequences for every surface residue (human 441/441, pig 460/460).

## 5. How to reproduce

From inside `surface_analysis/`:

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

## 6. Limitations

- pH 7.4 only. A second pH was optional and has not been run.
- Zinc was removed during PDB2PQR preparation, so the active site appears artificially negative.
- Human His391 was assigned as positively charged (HIP); its value depends on that choice.
- Surface sampling is approximate. Residues sampled at only one point are less reliable.
- Regions R2 (389-400) and R3 (460-500) were chosen after looking at the data and are exploratory.
