# --- Challenge 024 – GC Content by Sliding Window --- #

# --- Step 1: Function to Calculate GC content --- #
def gc_content_by_window(sequence, k):
    for i in range(len(sequence) - k + 1):
        window = sequence[i:i+k]
        gc = window.count('G') + window.count('C')
        percentage = (gc / k)* 100
        print(f'Window {window} → GC%: {percentage}')

# Step 2: Input of Sequence and K-mer --- #
seq = str(input('Enter a DNA sequence: ')) # As example: ATGCGCGTAC
k_value = int(input('Enter a K-mer Value: ')) # As example: 4

# --- Main Block --- #
gc_content_by_window(seq, k_value)