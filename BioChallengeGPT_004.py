### --- Challenge 004 – Nucleotide Frequency Analysis --- ###

# ---             Step 1             --- #
# --- Receive Multiple DNA Sequences --- #
sequences = []
while True:
    sequence = str(input("Enter a DNA sequence [or press Enter to finish]: ")).strip().upper()
    if sequence == "":
        break
    valid_sequence = True
    for nucleotide in sequence:
        if nucleotide not in "ATCG":
            valid_sequence = False
            break
    if valid_sequence:
        sequences.append(sequence)
print()
# ---        Step 2       --- #
# --- Calculate Frequency --- #
for pos, seq in enumerate(sequences):
    nucleotides_frequency = {'A': 0, 'T': 0, 'C': 0, 'G': 0}
    for nucleotide in seq:
        if nucleotide in nucleotides_frequency:
            nucleotides_frequency[nucleotide] += 1

    print(f'Frequency in sequence {sequences[pos]}:')
    for nucleotide, frequence in nucleotides_frequency.items():
        print(f'{nucleotide}:{frequence}')
    print()