"""Build llm_runner/evidence/surface_evidence_A2.md from the surface track's draft evidence records.

Usage (from the llm_runner folder):  python runner/build_surface_evidence.py
Edit the records in evidence/surface_evidence_records_DRAFT.csv, not the generated .md file.
"""
import csv
from pathlib import Path

HERE = Path(__file__).resolve().parent
EVID = HERE.parent / "evidence"
RECORDS = EVID / "surface_evidence_records_DRAFT.csv"
OUT = EVID / "surface_evidence_A2.md"

HEADER = """# Surface evidence package (electrostatic surface potential calculations)

Method summary: The AlphaFold 3 top-ranked human (UniProt Q9NZK5, residues 30-511) and pig (P58780, residues 25-510) ADA2 dimer models (seed 101, templates on) were prepared with PDB2PQR at pH 7.4 and the electrostatic potential was calculated with APBS at ionic strengths of 0 M and 0.15 M. Per-residue surface potential (kT/e; positive means a more positive surface) was sampled 3 A outward from each atom, keeping only points at least 2.5 A from every atom, and averaged over chains A and B. Residues use UniProt numbering. Human and pig residues were paired with the human-pig residue correspondence from the sequence track.

Depends on: the AlphaFold 3 models from the structure track; the human-pig residue correspondence (draft). These are calculations, not measurements of DNA binding, glycosaminoglycan binding, specificity or activity. Zinc ions and glycans were not included in the calculation.

Status: DRAFT until checked by a second person.
"""

FIELDS = [("Residues", "mapped_residues"), ("Observation", "observation"), ("Value", "value_units"),
          ("Method", "method"), ("Uncertainty", "uncertainty"), ("Limitations", "limitations"),
          ("Interpretation (not an observation)", "interpretation")]


def main():
    with open(RECORDS, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    parts = [HEADER]
    for r in rows:
        parts.append(f"## {r['id']}  ({r['species']}; {r['type']})")
        for label, key in FIELDS:
            v = (r.get(key) or "").strip()
            if v:
                parts.append(f"{label}: {v}")
        parts.append("")
    OUT.write_text("\n".join(parts), encoding="utf-8")
    print(f"wrote {len(rows)} records; {OUT.stat().st_size} characters")


if __name__ == "__main__":
    main()
