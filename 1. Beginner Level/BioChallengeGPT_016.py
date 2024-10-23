# --- Challenge 016 – Find Repeated Subsequences --- #

# --- Step 1: DNA sequence input --- #
dna_sequence = str(input("Enter a DNA sequence: ")).strip().upper() # As example: ATCGATCGATCGATCGGCTAAGCTAGCTGATCG
repeated_sequence_length = int(input('Length of the subsequence: ')) # As example: 4

count = {}

# --- Step 2: Function to find subsequences --- #
def find_subsequences(dna_seq, sub_length):
    for p in range(len(dna_seq) - sub_length + 1):
        subsequence = dna_seq[p:p + sub_length]
        if subsequence in count:
            count[subsequence] += 1
        else:
            count[subsequence] = 1

# --- Main block --- #
find_subsequences(dna_sequence, repeated_sequence_length)
for subseq, cnt in count.items():
    if cnt > 1:
        print(f"{subseq}: {cnt}")