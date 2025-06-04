# --- Challenge 025 – Count transitions and transversions --- #

# --- Step 1: Function to Count Transitions and Transversions --- #
def count_transitions_transversions(seq1, seq2):
    purines = {'A', 'G'}
    pyrimidines = {'C', 'T'}

    # --- Counters --- #
    transitions = 0
    transversions = 0

    min_lenght = min(len(seq1), len(seq2))
    for s1, s2 in zip(seq1, seq2):
        if s1 == s2:
            continue
        if s1 in purines or s2 in pyrimidines:
            transitions += 1
        else:
            transversions += 1

    print(f'Transitions {transitions}')
    print(f'transversions {transversions}')

# --- Main Block --- #
sequence1 = str(input("Enter the First DNA Sequence: ")).strip().upper() # As example: AGCTAGC
sequence2 = str(input("Enter the Second DNA Sequence: ")).strip().upper() # As example: AGTTGGC
count_transitions_transversions(sequence1, sequence2)