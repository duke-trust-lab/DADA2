# renumber_pqr.py
# Change the residue numbers in a .pqr file to UniProt numbering.
# Coordinates, charges and radii are NOT changed, so the old .dx files still match.
#
# Usage:
#   python renumber_pqr.py human.pqr human_uniprot.pqr 29
#   python renumber_pqr.py pig.pqr   pig_uniprot.pqr   24
#
# Offsets: human UniProt = file number + 29 ; pig UniProt = file number + 24

import sys

in_file = sys.argv[1]
out_file = sys.argv[2]
offset = int(sys.argv[3])

count = 0
with open(in_file) as f, open(out_file, "w") as out:
    for line in f:
        if line.startswith("ATOM") or line.startswith("HETATM"):
            # In this file format the residue number sits in characters 23-26
            old_num = int(line[22:26])
            new_num = old_num + offset
            line = line[:22] + str(new_num).rjust(4) + line[26:]
            count += 1
        out.write(line)

print("Renumbered", count, "atoms. Saved:", out_file)
