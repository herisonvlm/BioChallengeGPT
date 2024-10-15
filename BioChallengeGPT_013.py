# --- Challenge 013 – DNA Sequence Reversal --- #

# --- Step 1: Function to reverse the DNA sequence --- #
def reverse_dna(dna_seq):
    return dna_seq[::-1]

# --- Step 2: Enter a DNA sequence --- #
dna_sequence = input(str("Enter a DNA sequence: ")).strip().upper() # As example: ACGTACGTA

# --- Step 3: Reverse the sequence --- #
reversed_sequence = reverse_dna(dna_sequence)

# --- Step 4: Print the reversed sequence --- #
print("Reversed DNA sequence:", reversed_sequence)