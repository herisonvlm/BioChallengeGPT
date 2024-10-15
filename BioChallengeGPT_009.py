# --- Challenge 009 – Analysis of SNPs in DNA Sequences --- #

# --- Step 1: Define the Sequences --- #

seq1 = "ATCGATCG"
seq2 = "ATGGGTCA"

# --- Step 2: Function to Identify SNPs --- #
def identify_snps(sequence1, sequence2):
    identified_snps = []
    shortest_sequence = min(len(sequence1), len(sequence2))
    for p in range(shortest_sequence):
        if sequence1[p] != sequence2[p]:
            identified_snps.append((p + 1, f"{sequence1[p]} > {sequence2[p]}"))
    return identified_snps

# --- Main block --- #
found_snps = identify_snps(seq1, seq2)
for p, c in found_snps:
  print(f"Position {p}: {c}")