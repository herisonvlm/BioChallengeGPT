# --- Challenge 026 – Translation to protein until it encounters the stop codon --- #

rna_codon= {
    'AUG':'M', 'GCU':'A', 'GCC':'A', 'GCA':'A', 'GCG':'A',
    'UGU':'C', 'UGC':'C', 'GAU':'D', 'GAC':'D', 'GAA':'E', 'GAG':'E',
    'UUU':'F', 'UUC':'F', 'GGU':'G', 'GGC':'G', 'GGA':'G', 'GGG':'G',
    'CAU':'H', 'CAC':'H', 'AUU':'I', 'AUC':'I', 'AUA':'I', 'AAA':'K',
    'AAG':'K', 'UUA':'L', 'UUG':'L', 'CUU':'L', 'CUC':'L', 'CUA':'L',
    'CUG':'L', 'AUG':'M', 'AAU':'N', 'AAC':'N', 'CCU':'P', 'CCC':'P',
    'CCA':'P', 'CCG':'P', 'CAA':'Q', 'CAG':'Q', 'CGU':'R', 'CGC':'R',
    'CGA':'R', 'CGG':'R', 'AGA':'R', 'AGG':'R', 'UCU':'S', 'UCC':'S',
    'UCA':'S', 'UCG':'S', 'AGU':'S', 'AGC':'S', 'ACU':'T', 'ACC':'T',
    'ACA':'T', 'ACG':'T', 'GUU':'V', 'GUC':'V', 'GUA':'V', 'GUG':'V',
    'UGG':'W', 'UAU':'Y', 'UAC':'Y', 'UAA':'_', 'UAG':'_', 'UGA':'_'
}

# --- Step 1: Function to Translate RNA to Protein --- # 
def rna_to_protein(rna_seq):
    protein = ''
    for n in range(0, len(rna_seq), 3):
        codon = rna_seq[n:n + 3]
        if len(codon) < 3:
            break
        aa = rna_codon.get(codon, '')
        if codon == '_':
            break
        protein += aa
    return protein

# --- Main Block --- #
rna_sequence = str(input('Enter a RNA Sequence: ')).strip().upper() # As example: AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA
print(rna_to_protein(rna_sequence))
