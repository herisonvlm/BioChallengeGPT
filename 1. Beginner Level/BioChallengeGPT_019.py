# --- Challenge 019 – Detect Repeated Sequences in a Sliding Window --- #

# --- Step 1: Function to Count the Number of Subsequences --- #
def count_subsequences(dna_seq, window_size):
    count_subsequences = {}
    for n in range(len(dna_seq) - window_size + 1):
        subsequence = dna_seq[n:n + window_size]
        if subsequence in count_subsequences:
            count_subsequences[subsequence] += 1
        else:
            count_subsequences[subsequence] = 1
    
    return count_subsequences

# --- Step 2: Function to Find Subsequences --- #
def find_subsequences(count_subsequences):
    repeated_sequences = {}
    for subsequence, count in count_subsequences.items():
        if count > 1:
            repeated_sequences[subsequence] = count

    return repeated_sequences

# --- Step 3: User input --- #
dna_sequence = str(input('Enter a DNA Sequence: ')).strip().upper() # As example: ACGTACGTACGTGCGTACGTTAGCGTAGCGTACGCGTAGCGTACGTACGTTAGCGTACGCGTAGCGTATCGATCGATCGACGCGTACGTTAGCGTACGCGTAGCGTACGATCGTACGCGTAGCGT
window_size = int(input('Enter a number of window sliding: ')) # As example: 5

# --- Main Block --- #
counted_subsequences = count_subsequences(dna_sequence, window_size)
repetead_sequences = find_subsequences(counted_subsequences)
if repetead_sequences:
    print(f'Repeated subsequences of length {window_size}:')
    for subseq, count in repetead_sequences.items():
        print(f'{subseq}: {count}')