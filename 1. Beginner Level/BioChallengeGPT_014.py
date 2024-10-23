# --- Challenge 014 – DNA Sequence Complement --- #

# --- Step 1: Request user input --- #
sequence = input("Enter the DNA sequence: ").upper() # As example: ATCG

# --- Step 2: Function to Calculate DNA complement --- #
def dna_complement(sequence):
    complement = ''
    for n in sequence:
        if n == 'A':
            complement += 'T'
        elif n == 'T':
            complement += 'A'
        elif n == 'C':
            complement += 'G'
        elif n == 'G':
            complement += 'C'
    return complement

# --- Main block --- #
complement = dna_complement(sequence)
print(f'Original sequence: {sequence}')
print(f'Complement: {complement}')