# --- Challenge 023 – Identify a Subsequence --- #

# --- Step 1: Function to Read Sequence and Motif --- #
def find_motif(sequence, motif):
    if motif in sequence:
        print("Motif found!")
    else:
        print("Motif not found.")

# --- Step 2: Input of Sequence and Motif --- #
sequence = input("Enter the Sequence: ") # As example: ATGCTAGCTAG   
motif = input("Enter the Motif: ") # As example: CTAG

# --- Main Block --- #
find_motif(sequence, motif)