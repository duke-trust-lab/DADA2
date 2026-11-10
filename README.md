# ADA2: human vs pig comparison

Project to find which differences between human and pig ADA2 could explain the reported difference in their activity on free adenosine, and what other ADA2 functions might be preserved in pig. Two parts feed an LLM-based hypothesis experiment:

1. **Structure prediction** (AlphaFold 3): matched human and pig dimers, compared with the human crystal structure 3LGD.
2. **LLM runner**: runs five conditions (A0 to A4), each giving the model a different set of evidence, and saves every input and output for review.

All structural results are predictions. Confidence scores describe how reliable a prediction is. They do not measure binding, activity, or the effect of a mutation. LLM output is a suggestion for the team to review, not a finding.

**Status, decisions, open questions and handoff items: see [NOTES.md](NOTES.md).**

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
└── llm_runner/                LLM experiment (conditions A0 to A4)
    ├── LLM_team_runs.ipynb    start here
    ├── runner/                runner code and the A3 evidence builder
    ├── prompts/  context/  evidence/   shared inputs; keep identical across conditions
    ├── config.json            model and settings
    └── runs_pilot/            saved pilot runs
```

## Quick start

**LLM runs** (needs an OpenAI API key):
1. `pip install -r llm_runner/requirements.txt`
2. Copy `llm_runner/.env.example` to `llm_runner/.env` and add your key. `.env` is git-ignored; never commit it.
3. Open `llm_runner/LLM_team_runs.ipynb`, edit the settings cell, and run it. It runs in pilot mode only. See `llm_runner/README.md` for the formal-batch rules.

**AlphaFold analysis:**
1. `pip install -r structure_prediction/requirements.txt`
2. Put the AlphaFold Server downloads in `structure_prediction/af3_outputs/` (not stored in git), then run `structure_prediction/AF3_results_comparison.ipynb`. The saved tables in `af3_results/` already hold the results.
