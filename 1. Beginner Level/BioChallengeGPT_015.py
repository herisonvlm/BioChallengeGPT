# --- Challenge 015 – Analysis of Genetic Variants --- #

# --- Step 1: Function to analyze genetic variants --- #
def analyze_variants(ref_seq, query_seq):
    variants = []
    min_lenght = min(len(ref_seq), len(query_seq))

    for p in range(min_lenght):
        if ref_seq[p] != query_seq[p]:
            variants.append(((p + 1, ref_seq[p], query_seq[p], "(SNP)")))

    if len(ref_seq) > len(query_seq):
        for p in range(min_lenght, len(ref_seq)):
            variants.append(((p + 1), ref_seq[p], "-", "(Deletion)"))
    
    elif len(query_seq) > len(ref_seq):
        for p in range(min_lenght, len(query_seq)):
            variants.append(((p + 1), "-", query_seq[p], "(Insertion)"))

    return variants

# --- Step 2: Input of reference and query sequences --- #
reference_sequence = str(input('Enter a reference sequence: ')).strip().upper() # As example: ATCGGTA
query_sequence = str(input('Enter your query sequence: ')).strip().upper() # As example: ATCAGT

# --- Main block --- #
variants = analyze_variants(reference_sequence, query_sequence)
print("Founded Variants:")
for pos, ref_base, query_base, type in variants:
    print(f"Position {pos}: {ref_base} -> {query_base} {type}")