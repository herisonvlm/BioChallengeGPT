# --- Challenge 005 – Protein Sequence Modification --- #

# --- Step 1: Create a Protein Sequence --- #
protein_seq = "MKTAFCLG"

# --- Step 2: Replace Amino Acids --- #
def modify_protein(sequence):
    substitutions = {"A":"X", "F":"Y"}
    new_protein_sequence = ''
    for amino in sequence:
        if amino in substitutions:
            new_protein_sequence += substitutions[amino]
        else:
            new_protein_sequence += amino
    return new_protein_sequence

    
# --- Main block --- #
modified_protein = modify_protein(protein_seq)
print('Original sequence:', protein_seq)
print('Modified sequence:', modified_protein)