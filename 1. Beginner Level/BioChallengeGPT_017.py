# --- Challenge 017 – Hamming Distance Between DNA Sequences --- #

# --- Step 1: Input of DNA Sequences and Calculate Hamming Distance --- #
while True:
    seq1 = str(input('Enter the first DNA sequence: ')).strip().upper() # As example: GATTACA
    seq2 = str(input('Enter the second DNA sequence: ')).strip().upper() # As example: GACTATA
    if len(seq1) != len(seq2):
        print('Error: Sequences must be the same length.')
    else:
        distance = 0
        for n in range(len(seq1)):
            if seq1[n] != seq2[n]:
                distance += 1
        print(f'Hamming distance: {distance}')
        break