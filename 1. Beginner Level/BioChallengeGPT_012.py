# --- Challenge 012 – Stop Codon Analysis --- #

# --- Step 2: Count stop codons --- #
def count_stop_codons(rna_sequence):
    stop_codons = {"UAA", "UAG", "UGA"}
    count_stop_codons = 0
    for n in range(0, len(rna_sequence), 3):
        codon = rna_sequence[n:n + 3]
        if codon in stop_codons:
            count_stop_codons += 1
    return count_stop_codons

# --- Step 1: Enter a RNA sequence --- #
rna_seq = input(str('Enter a RNA sequence: ')).strip().upper() # As example: AUGUAAUAGCUGA

# --- Main block --- #
stop_codon_count = count_stop_codons(rna_seq)
print(f'Number of stop codon found: {stop_codon_count}')


