# ---            Challenge 003 – DNA to RNA Transcription           --- #

# ---           Step 1           --- #
# ---      Input sequences       --- #
dna_seq = str(input("Enter a DNA sequence: ")).strip().upper()

# ---           Step 2          --- #
# --- Validation of nucleotides --- #
for n in range(len(dna_seq)):
    if dna_seq[n] not in 'ATCG':
      print('Error! The sequence must only contain A, T, C, and G.')
      break
    else:
      # ---           Step 3          --- #
      # ---         DNA to RNA        --- #
      rna_seq = dna_seq.replace('T', 'U')
print(f'The corresponding RNA sequence is: {rna_seq}')