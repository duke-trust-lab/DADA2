# compare.py
# Compare the per-residue surface potential tables made by surface_findings.py
#
# Step 1: run surface_findings.py four times first, for example:
#   python surface_findings.py human.pqr human_0M.dx   human_0M
#   python surface_findings.py human.pqr human_150.dx  human_150
#   python surface_findings.py pig.pqr   pig_0M.dx     pig_0M
#   python surface_findings.py pig.pqr   pig_150.dx    pig_150
# Step 2: run this file:
#   python compare.py
#
# If your labels are different, change the four file names below.

import pandas as pd

human_0M = pd.read_csv("human_0M_residues.csv")
human_150 = pd.read_csv("human_150_residues.csv")
pig_0M = pd.read_csv("pig_0M_residues.csv")
pig_150 = pd.read_csv("pig_150_residues.csv")

# ---------- Part 1: human vs pig at the same salt (0.15 M) ----------
# Residue numbers differ between species, so we just list them side by side.
print("===== Human, 0.15 M: top 15 most positive residues =====")
print(human_150.head(15).to_string(index=False))
print()
print("===== Pig, 0.15 M: top 15 most positive residues =====")
print(pig_150.head(15).to_string(index=False))
print()

# ---------- Part 2: salt check (0 M vs 0.15 M, same species) ----------
# Same protein, so residue numbers match and we can merge.
def salt_check(no_salt, salt, name):
    m = no_salt.merge(salt, on=["chain", "res_name", "res_num"], suffixes=("_0M", "_150"))
    m["change"] = (m["potential_150"] - m["potential_0M"]).round(2)

    # Do the top 15 residues stay the same when salt is added?
    top_0M = set(no_salt.head(15)["res_name"] + no_salt.head(15)["res_num"].astype(str))
    top_150 = set(salt.head(15)["res_name"] + salt.head(15)["res_num"].astype(str))
    shared = top_0M & top_150

    print("===== " + name + ": salt check (0 M vs 0.15 M) =====")
    print("Residues in the top 15 under both salt conditions:", len(shared), "of 15")
    print(sorted(shared))
    print()
    print("Top 15 residues at 0.15 M, with their 0 M values:")
    cols = ["chain", "res_name", "res_num", "potential_0M", "potential_150", "change"]
    print(m.sort_values("potential_150", ascending=False).head(15)[cols].to_string(index=False))
    print()

    m.to_csv(name + "_salt_check.csv", index=False)

salt_check(human_0M, human_150, "human")
salt_check(pig_0M, pig_150, "pig")

print("Saved: human_salt_check.csv, pig_salt_check.csv")
