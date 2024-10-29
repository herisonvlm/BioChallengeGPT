# --- Challenge 018 – Most Frequent Motif in a DNA Sequence --- #

# --- Step 1: Find Motifs of Size 'n' and Count Them --- # 
def find_motif(dna_seq, motif_length):
    motifs_count = {}
    for n in range(len(dna_seq) - motif_length + 1):
        motif = dna_seq[n:n + motif_length]
        if motif in motifs_count:
            motifs_count[motif] += 1
        else:
            motifs_count[motif] = 1
    
    return motifs_count

# --- Step 2: Count the Most Frequent Motifs --- # 
def find_most_frequent_motifs(motifs_count):
    max_count = max(motifs_count.values())
    frequent_motifs = []

    for motif, count in motifs_count.items():
        if count == max_count:
            frequent_motifs.append((motif, count))
    
    return frequent_motifs

# --- Step 3: Input of DNA Sequence and Motif Length --- #
dna_sequence = str(input('Enter a DNA Sequence: ')).strip().upper() # As example: TCGATCGATCGTTAGCGTATCGTAGCGTACGTTAGCGTACG
motif_length = int(input('Enter the Motif Length: ')) # As example: 3

# --- Main Block --- #
motifs_count = find_motif(dna_sequence, motif_length)
most_frequent_motifs = find_most_frequent_motifs(motifs_count)
print('Most frequent motif:')
for motif, count in most_frequent_motifs:
    print(f'{motif}: {count}')