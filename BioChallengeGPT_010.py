# --- Challenge 010 – GC Content Analysis --- #

# ---  Step 1: Define sequence --- #
dna_sequence = "ATCGATCGGCCG"

# --- Step 2: Function to calculate GC content --- #
def calculate_GC(sequence):
    count_G = sequence.count("G")
    count_C = sequence.count("C")

    total_nucleotides = len(sequence)

    if total_nucleotides == 0:
        return 0.0
    
    GC_percentage = ((count_G + count_C) / total_nucleotides) * 100
    return GC_percentage


# --- Main Block --- #
gc_content = calculate_GC(dna_sequence)
print(f"GC content: {gc_content:.2f}%")