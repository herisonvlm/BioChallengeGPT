# --- Challenge 020 – Stop Codon Identification --- #

# --- Step 1: Funcion to Find Stop Codons --- #
def find_stop_codons(rna_seq):
    stop_codon_positions = []
    stop_codons = ['UAA', 'UAG', 'UGA']
    for i in range(0, len(rna_seq) - 2, 3):
        codon = rna_seq[i:i + 3]
        if codon in stop_codons:
            stop_codon_positions.append(i)

    return stop_codon_positions

# --- User Input --- #
rna_seq = str(input('Enter a RNA sequence: ')).strip().upper() # As example: AUGCGCUAAUGCGGUAGCGGAUGA

# --- Main Block --- #
stop_codons = find_stop_codons(rna_seq)
print(f'Stop codons found at positions {stop_codons}')