# ---             Challenge 001 – Simple DNA sequence analyzer             --- #
# Download Biopython Library
# pip install biopython


# Import
from Bio import SeqIO


# ---                       Step 1:                       --- #
# ---        Reading sequences from a FASTA file          --- #
def ReadFastaAndWriteResults(file_name, output_file):
    with open(output_file, 'w') as file:
        for i, record in enumerate(SeqIO.parse(file_name, "fasta")):
            seq = str(record.seq)  # Get the sequences as a string

            #  Capital nucleotides
            if not seq.isupper():
                print(f"Warning: The sequence {i + 1} is not capitalized and will be converted.")
                seq = seq.upper()  # Convert to uppercase

            # Call to the ProcessSequence function
            ProcessSequence(seq, record, i + 1, file)


# ---          Step 2:          --- #
# --- Calculate Sequence Length --- #
def Length(seq):
    return len(seq)


# ---                Step 3:                 --- #
# --- Counting Nucleotides in a DNA Sequence --- #
def NucleotideCount(seq):
    nucleotides = {'A': 0, 'C': 0, 'T': 0, 'G': 0}
    for base in seq:
        if base in nucleotides:
            nucleotides[base] += 1
    return nucleotides


# ---                Step 4:                 --- #
# --- Processes each sequence simultaneously --- #
def ProcessSequence(seq, record, seqnumber, file):
    nucleotide_counts = NucleotideCount(seq)
    sequence_length = Length(seq)
    file.write(f'Sequence {seqnumber}:\n')
    file.write(f'Nucleotide counts: {nucleotide_counts}\n')
    file.write(f'Sequence length: {sequence_length}\n')
    file.write(f'Original sequence: {record.seq}\n\n')


# ---                Main block                --- #
if __name__ == "__main__":
    fasta_file = "/content/sample_DNAs.fasta"
    output_file = 'my_results.txt'
    ReadFastaAndWriteResults(fasta_file, output_file)
    print('Results were written in:', output_file)