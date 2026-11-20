# ADA2: human vs pig comparison

Project to find which differences between human and pig ADA2 could explain the reported difference in their activity on free adenosine, and what other ADA2 functions might be preserved in pig. Three parts feed an LLM-based hypothesis experiment:

1. **Structure prediction** (AlphaFold 3): matched human and pig dimers, compared with the human crystal structure 3LGD.
2. **Surface electrostatics** (PDB2PQR and APBS): the electrostatic potential on the surface of the predicted human and pig dimers.
3. **LLM runner**: runs five conditions (A0 to A4), each giving the model a different set of evidence, and saves every input and output for review.

All structural results are predictions. Confidence scores describe how reliable a prediction is. They do not measure binding, activity, or the effect of a mutation. LLM output is a suggestion for the team to review, not a finding.

**Status, decisions, open questions and handoff items: see [NOTES.md](NOTES.md).**

## What was done, and what code did it

The project combines data downloaded from public websites, results from web tools, and Python code that processes them. The AlphaFold job files, the shared background text and the prompts were written by the team.

### 1. Data downloaded from websites

| What | Where it came from | Saved in |
|---|---|---|
| Human ADA2 and pig ADA2 protein sequences (FASTA) | UniProt (entries Q9NZK5 and P58780), REST download | `data/sequences/` |
| Sequence annotations (signal peptide, glycosylation sites, zinc ligands, domains) | UniProt, JSON download | `data/annotations/` |
| Human crystal structures 3LGD and 3LGG (with a transition-state analogue) | RCSB Protein Data Bank, assembly files | `data/structures/` |

`data/source_manifest.json` records the web address, download time and checksum of each file, so the downloads can be traced and checked. The UniProt and RCSB files were fetched once on 2026-10-15 and are not edited.

### 2. Results from web tools and programs (not Python)

| Step | Tool | What went in and what came out |
|---|---|---|
| Structure prediction | AlphaFold Server (AlphaFold 3, web interface) | Job files in `structure_prediction/af3_inputs/` (two copies of each species' protein plus one zinc ion per chain). 12 jobs were run and 60 models downloaded as zip files into `structure_prediction/af3_outputs/`. |
| Surface preparation and electrostatics | PDB2PQR and APBS (programs run outside this repository) | The top human and pig models were assigned charges at pH 7.4, and the electrostatic potential was calculated at 0 M and 0.15 M ionic strength. The four large map files are on the team Google Drive, not in git. |
| Language model | OpenAI API, model `gpt-6-astra` | The runner sends the prompts and evidence and saves the responses. |

### 3. What Python did

| Step | Code | What it does |
|---|---|---|
| Compare AlphaFold results | `structure_prediction/AF3_results_comparison.ipynb` (numpy, pandas, matplotlib) | Reads the AlphaFold downloads and builds score tables (ipTM, pTM, PAE, pLDDT). Overlays each prediction on the 3LGD crystal structure and measures the difference (RMSD), the zinc-to-ligand distances and the overlap of the chain interface. Measures how much results change between seeds, with and without templates, and compares human against pig on aligned positions. Saves tables and figures in `structure_prediction/af3_results/`. |
| Pair human and pig positions | `structure_prediction/human_pig_position_map_DRAFT.csv` (a data file, not a script) | A draft map from an alignment of the two UniProt sequences, giving the human residue number for each aligned pig residue, so the proteins can be compared position by position. It is to be replaced by the sequence track's official alignment. |
| Turn structure results into model input | `llm_runner/runner/build_structure_evidence.py` | Reads the saved tables and the position map and writes the structure evidence records (STRUCT-01 to STRUCT-08) as `evidence/structure_evidence_A3.md` and a CSV. |
| Renumber structure files | `surface_analysis/scripts/renumber_pqr.py` | Converts residue numbers in the charge-assigned structure files to UniProt numbers, with the coordinates unchanged. |
| Surface potential per residue | `surface_analysis/scripts/surface_findings.py` | Reads each structure and its electrostatics map. Takes a point just outside each atom, keeps it only if it is in open solvent, reads the potential there, and averages it per residue and over both chains. Writes one table per species and ionic strength. |
| Compare human and pig surfaces | `surface_analysis/scripts/compare.py` | Lists the most positive residues in each species and checks that results hold between 0 M and 0.15 M. |
| Turn surface results into model input | `llm_runner/runner/build_surface_evidence.py` | Reads the draft surface records (SURF-01 to SURF-07) and writes them as `evidence/surface_evidence_A2.md`. |
| Run the experiment | `llm_runner/runner/llm_runner.py` and the notebooks | Builds each condition's prompt from the shared context and evidence, calls the OpenAI API with a fixed JSON output format, and saves each run's input, raw response, parsed hypotheses and a readable `output.md`. Checks that every cited evidence ID was actually given to the model, refuses formal runs until the setup is frozen, and can write a blind review sheet. |

### 4. How the pieces connect

```
UniProt + RCSB (data/)  ->  AlphaFold Server  ->  AF3_results_comparison.ipynb  ->  STRUCT records  ->  A3 evidence --+
                                    |                                                                                   |
                                    +-> PDB2PQR + APBS  ->  surface_findings.py  ->  SURF records  ->  A2 evidence ----+--> llm_runner.py --> runs/
                                                                                                    shared context -----+      (hypotheses)
```

Condition A0 gets only the shared context. A2 adds the surface evidence, A3 adds the structure evidence, and A1 (sequence) and A4 (everything) are waiting for the sequence evidence.

## Layout

```
.
├── README.md                  this file
├── NOTES.md                   decisions, open questions, status, handoff
├── data/                      source inputs (do not edit)
│   ├── sequences/             UniProt FASTA (human Q9NZK5, pig P58780)
│   ├── annotations/           UniProt annotations (JSON)
│   ├── structures/            human crystal structures 3LGD and 3LGG
│   └── source_manifest.json
├── docs/                      project documents (starter packet, timeline, status slides)
├── structure_prediction/      AlphaFold 3 track
│   ├── af3_inputs/            AlphaFold Server job files
│   ├── af3_outputs/           raw downloads (NOT in git, ~0.9 GB)
│   ├── af3_results/           score tables and figures
│   ├── shared_models/         top-ranked human and pig models for sharing
│   ├── human_pig_position_map_DRAFT.csv
│   └── AF3_results_comparison.ipynb
├── surface_analysis/          surface electrostatics track
│   ├── scripts/               renumber_pqr.py, surface_findings.py, compare.py
│   ├── inputs/                charge-assigned structure files
│   └── results/               per-residue surface potential tables
└── llm_runner/                LLM experiment (conditions A0 to A4)
    ├── LLM_team_runs.ipynb    start here
    ├── runner/                runner code and the A2 and A3 evidence builders
    ├── prompts/  context/  evidence/   shared inputs; keep identical across conditions
    ├── config.json            model and settings
    ├── runs/                  formal runs (A0, A2, A3) and the hypothesis README
    └── runs_pilot/            rehearsal runs (empty)
```

## Quick start

**LLM runs** (needs an OpenAI API key):
1. `pip install -r llm_runner/requirements.txt`
2. Copy `llm_runner/.env.example` to `llm_runner/.env` and add your key. `.env` is git-ignored; never commit it.
3. Open `llm_runner/LLM_team_runs.ipynb`, edit the settings cell, and run it. It runs in pilot mode only. See `llm_runner/README.md` for the formal-batch rules.

**AlphaFold analysis:**
1. `pip install -r structure_prediction/requirements.txt`
2. Put the AlphaFold Server downloads in `structure_prediction/af3_outputs/` (not stored in git), then run `structure_prediction/AF3_results_comparison.ipynb`. The saved tables in `af3_results/` already hold the results.

## Sequence track handoff

[Sequence analysis and integration](sequence_analysis/README.md) contains the executed English notebook, complete residue mappings, annotated differences, SEQ-01–SEQ-08 evidence and reconciliation with the structural draft map. The A1 evidence file is now populated; A2 and mapping-sensitive A3 review remain team integration items.
