# --- Challenge 022 – Different Sequences --- #

# --- Step 1: Function to Analyse Sequences --- #
def analyse_sequences(sequences):    
    first_sequence = sequences[0]
    for seq in sequences[1:]:
        if seq != first_sequence:
            return "Different sequences"
    return "All the sequences are the same"

# --- Step 2: Input of Sequences --- #
entry = [
    "ATCGTAC",
    "ATCGTAC",
    "ATCGTAC"
]

# --- Main block --- #
result = analyse_sequences(entry)
print(result)