# --- Challenge 006 – Amino Acid Count in a Protein Sequence --- #

# --- Step 1: Create a Protein Sequence --- #
protein_sequence = "MKTAFCLGAFG"

# --- Step 2: Count Amino Acids --- #
def count_amino(sequence):
    count = {}
    for amino in sequence:
        if amino in count:
            count[amino] += 1
        else:
            count[amino] = 1
    return count

final_count = count_amino(protein_sequence)


# --- Main block --- #
print('Original sequence:', protein_sequence)
print('Amino acyds count:', final_count)