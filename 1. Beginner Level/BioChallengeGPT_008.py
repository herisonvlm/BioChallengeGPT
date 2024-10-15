# --- Challenge 008 – Filtering Sequences by Length --- #

# --- Step 1: Create a List of DNA Sequences --- #
dna_sequences = ["ATCG", "A", "ATCGTA", "GCTA", "AT"]

# --- Step 2: Create a function that filters the sequences --- #
def filter_sequences(sequences, min_length):
    filtered_sequences = []
    for s in sequences:
        if len(s) >= min_length:
            filtered_sequences.append(s)
    return filtered_sequences


# --- Main block --- #
filtered_results = filter_sequences(dna_sequences, 3)
print('Original sequences:', dna_sequences)
print('Filtered sequences (minimum length 3):', filtered_results)