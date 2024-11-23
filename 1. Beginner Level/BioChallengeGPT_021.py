# --- Challenge 021 – Counting Nucleotides in Specific Regions of a DNA Sequence --- #

# --- Step 1: Function to extract subsequences --- #
def extract_subsequence(seq, start, end):
    if start < 0 or end > len(seq) or start >= end:
        return None

    subsequence = seq[start:end]
    return subsequence

# --- Step 2: Function to count nucleotides in a range --- #
def count_nucleotides(sub_seq):
    nucleotide_count = {'A': 0, 'T': 0, 'C': 0, 'G': 0}
    for n in sub_seq:
        if n in nucleotide_count:
            nucleotide_count[n] += 1
    return nucleotide_count

# --- User Input --- #
user_seq = input('Enter a DNA Sequence: ').strip().upper() # As example: ATGCGATACG
start_position = int(input('Enter the Start Position [starting from 0]: ')) # As example: 2
end_position = int(input('Enter the End Position: ')) # As example: 7

# --- Main Block --- #
new_sequence = extract_subsequence(user_seq, start_position, end_position)

# --- Check if the subsequence is valid before counting nucleotides --- #
if new_sequence is None:
    print('Invalid START or END positions!')
else:
    nucleotides_counted = count_nucleotides(new_sequence)
    print(f'Nucleotide counts in the region ({start_position}, {end_position}):')
    for nucleotide, frequence in nucleotides_counted.items():
        print(f'{nucleotide}: {frequence}')