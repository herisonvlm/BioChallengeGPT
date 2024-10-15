# --- Challenge 011 – Nucleotide Composition Classification --- #

# --- Step 1: DNA Sequence Entry --- #
dna_sequence = "AGCTAGCTAG"

# --- Step 2: Count nucleotides --- #
def count_nucleotides(sequence):
    nucleotides_frequence = {"A": 0, "C": 0, "G": 0, "T": 0}
    for nucleotide in sequence:
        if nucleotide in nucleotides_frequence:
            nucleotides_frequence[nucleotide] += 1

    # --- Step 3: Calculate the total number of nucleotides --- #
    total_nucleotides = sum(nucleotides_frequence.values())

    # --- Step 4: Calculate and print percentages --- #
    for nucleotides, count in nucleotides_frequence.items():
        percentage = (count / total_nucleotides) * 100
        print(f"{nucleotides}: {percentage}%")

    # --- Step 5: Classification --- #
    sum_A_G = nucleotides_frequence["A"] + nucleotides_frequence["G"]
    if total_nucleotides > 0 and sum_A_G >= 0.5:
        classification = "Balanced"
    else:
        classification = "Unbalanced"
    print(f"Classification: {classification}")


# --- Main block --- #
count_nucleotides(dna_sequence)
