# Project notes

Working notes for the team: what has been decided, what is still open, and what is needed next. Anything marked **[CONFIRM]** or **DRAFT** has not been checked by a second person. Update this file as items are settled.

## 1. Where things stand

| Area | Status |
|---|---|
| AlphaFold 3 (human and pig dimers) | 12 jobs run (60 models) on AlphaFold Server and compared with 3LGD. Results in `structure_prediction/af3_results/`, summary in `structure_prediction/README.md`. |
| Human-pig position map | Draft only (`structure_prediction/human_pig_position_map_DRAFT.csv`). Yang's alignment is meant to be the official version. |
| LLM runner | Built and tested with the real model (`gpt-6-astra`). Pilot done for A0 and A3 (one repeat each). A1 (sequence) and A2 (surface) evidence are still placeholders. `config.json` is not frozen, so formal runs are blocked. |
| Lab context for the LLM | Lab expertise and capabilities added to the shared context as CTX-07 and CTX-08, from the lab's written reply. Needs verification by a team member. |
| Review | Medical-team review form and evidence-record/hypothesis templates mentioned in the starter packet are not in the repo. |

## 2. Key findings so far (AlphaFold 3, predictions only)

- Both species are predicted as confident dimers (ipTM about 0.9, pTM about 0.95, no clashes) with intact zinc sites (Zn to ligand about 2.2 A, matching 3LGD).
- Human matches the crystal structure closely (dimer RMSD about 0.45 A).
- Pig has the same single-chain fold (about 0.75 A from human) but the two chains sit slightly differently (chain B about 2 A off after fitting chain A, versus about 0.6 A for human).
- This holds with PDB templates turned off, so it is not a template artifact. It is larger than seed-to-seed variation (about 0.3 to 0.6 A).
- The largest local human-pig differences are near residues 151-159, the N-terminus, and residues 281 and 347. The spike near residue 156 is where pig pLDDT is lowest (about 68), so treat it as uncertain.
- Zinc raised human confidence slightly (ipTM 0.89 to 0.92) but did not change accuracy against 3LGD. Only one human no-zinc run exists.
- Sequence facts (draft; Yang to re-verify): 506 aligned positions, 355 identical (70.2%). Catalytic residues (human E359, H384) and all four annotated zinc ligands (H112, H114, H356, D441) are identical in pig. The substrate-binding region (human 204-211) has two differences (S205K, E208K). Human has four N-glycosylation sequons (N127, N174, N185, N378); pig has three, and the N185 sequon is lost.
- The active site and zinc site being conserved means a simple swap in the catalytic pocket is unlikely to explain the activity difference. This is a clue, not a conclusion.

## 3. Decisions needed from Dr. Bent

Choices already made are provisional. If a different choice is made, the affected AlphaFold jobs must be rerun.

1. **Segments to model.** Used: each species with its own UniProt signal peptide removed (human 30-511, 482 aa; pig 25-510, 486 aa). This was a proposal, not specified by the project. Alternatives: full-length, or the lab's actual construct. Do the lab's recombinant proteins keep the signal peptide, or carry tags or linkers?
2. **Zinc.** One Zn2+ per chain in the baseline, plus a no-zinc sensitivity check. Is that right?
3. **Glycans.** Left out of the baseline (human has 4 sequons, pig 3). Leave out, or run a glycan variant?
4. **Templates.** AlphaFold Server uses PDB templates by default (the top pig template was 3LGD). Both settings were run and agree closely. Which should be the reported baseline?
5. **DNA.** Is an ADA2-DNA system in scope? If so, which oligo, and who extracts the exact sequence and conditions from Greiner-Tollersrud 2024 (Cell Reports, DOI 10.1016/j.celrep.2024.114899)? No DNA run has been done because the system is unverified.
6. **Lab information.** The lab's actual human and pig construct sequences and assay conditions (substrate, concentrations, pH, buffer, temperature, incubation time).

## 4. Other open items and blockers

- **Earlier AlphaFold runs.** Previous AlphaFold inputs and outputs are not in the shared folder. Locate them or declare them lost. [CONFIRM which analyses were run earlier, and on which platform.]
- **Alignment.** Replace the draft position map with Yang's alignment, and confirm the numbers with him.
- **Residue checks.** Check pLDDT and PAE at residues 151-160, 281 and 347. Distance of 281/347 to the active site, zinc site, interface and glycosylation sites has not been computed.
- **Sharing structures.** `structure_prediction/shared_models/` holds the top human and pig models for Sienna. Agree segments and chain names with her.
- **Not run:** full-length (signal peptide kept) control, glycan variants, DNA.
- **AlphaFold platform.** Confirm AlphaFold Server versus a local install, and the daily job limit. Output terms are non-commercial and exclude docking or screening use.
- **Job file format.** The JSON job files in `structure_prediction/af3_inputs/` were written from memory of the AlphaFold Server format; if an upload is rejected, enter the same sequences and ions manually.

## 5. LLM experiment

- **Design:** five conditions: A0 (no evidence), A1 (sequence), A2 (surface), A3 (structure), A4 (all). Same shared context and system prompt in all conditions. The formal batch is 5 conditions x 3 repeats in random order.
- **Model:** `gpt-6-astra`. The API accepted reasoning effort low, medium and high and the JSON-schema output. Prices are not set, so cost is not logged.
- **Pilot (A0 and A3):** both runs completed, with no invented evidence IDs. A3 proposed a hypothesis about residues 281 and 347 that A0 could not; both runs flagged that specific assays must be confirmed with the lab. A second identical round showed the main ideas repeat while wording and some confidence labels change. Details: `llm_runner/runs_pilot/README.md`. Pilot runs are rehearsals and must not be counted in the study.
- **Before formal runs:** finalize the DRAFT prompt, context and evidence (rename away from DRAFT, set a prompt version, set `frozen: true`); have a second person verify every CTX and STRUCT record; receive the A1 and A2 packages. The runner refuses formal runs until these are done.
- **Lab context (CTX-07, CTX-08):** the lab reported expertise in biochemistry, enzymology, genetics, immunology and cell biology, an ADA2-specific aptamer, and recombinant protein capability, with NMR and mass-spectrometry expertise joining in January. It did not list specific instruments or limits, so the model is told not to assume any capability not stated.
- **Optional prompt change (not made):** add a rule telling the model to propose only experiments the lab can run, citing CTX-08. This is a prompt-design decision for Sienna and Dr. Bent.

## 6. Before pushing to GitHub

- `.env` (holds the API key) is git-ignored. Check `git status` shows no `.env` before the first commit, and rotate the key if it was ever shared.
- `structure_prediction/af3_outputs/` is git-ignored (about 0.9 GB; the largest single files are about 10 MB zips, but the folder is too large to be useful in git). Share it through the team drive instead.
- `docs/` holds the team's starter packet, timeline and status slides, which name team members and assign tasks. Check that the repository's visibility suits that, or leave `docs/` out.
- AlphaFold output terms are non-commercial. `structure_prediction/shared_models/` and `af3_results/` derive from those outputs; check the terms before making the repository public.
- LLM outputs in `llm_runner/runs_pilot/` are saved model responses; keep them with the repository so results can be traced to their exact inputs.
