
# ---            Challenge 002 – DNA Sequence Similarity Analyzer          --- #

# ---                         Step 1                          --- #
# ---            Request DNA sequences from the user          --- #

seq1 = input("Enter the first DNA sequence (A, T, C, G): ").strip().upper()
seq2 = input("Enter the second DNA sequence (A, T, C, G): ").strip().upper()

# ---                    Step 2                      --- #
# --- Validation of each nucleotide in the sequences --- #
valid_sequences = True
for base in seq1:
    if base not in 'ATCG':
        valid_sequences = False
        break

for base in seq2:
    if base not in 'ATCG':
        valid_sequences = False
        break

if valid_sequences == False:
  print('Error: Sequences must contain only A, T, C and G.')
else:
# ---         Step 3        --- #
# --- Calculate similarity  --- #
    identical_nucleotides = 0
    shortest_seq = min(len(seq1), len(seq2))
    for n in range(shortest_seq):
        if seq1[n] == seq2[n]:
          identical_nucleotides += 1
    similarity = (identical_nucleotides / shortest_seq) * 100
    print(f'The similarity between the sequences is: {similarity:.2f}%')