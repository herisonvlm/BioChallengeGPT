# --- Challenge 007 – Protein Sequence Comparison --- #

# --- Step 1: Create Protein Sequences --- #
protein_sequence1 = "MKTAFCLG"
protein_sequence2 = "MKTAFCAG"

# --- Step 2: Compare Sequences --- #
def compare_sequences(seq1, seq2):
    differences = []
    for a in range(min(len(seq1), len(seq2))):
        if seq1[a] != seq2[a]:
            differences.append((a, seq1[a], seq2[a]))
    return differences


# --- Main block --- #
results = compare_sequences(protein_sequence1, protein_sequence2)
print("Differences found in indexes:", results)