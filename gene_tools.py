import pandas as pd
import codon_chart as cc

# Returns the complement strand of a DNA sequence
def to_complement(sequence):
	complementary_nucleotides = {'A': 'T', 'G': 'C',
				   				 'T': 'A', 'C': 'G'}
	return ''.join(complementary_nucleotides[i] for i in sequence)

# Returns the transcribed (RNA) version of a sequence
def transcribe(sequence):
	return sequence.replace('T','U')

# Translates a mRNA sequence into their corresponding amino acid structure
def translate(sequence):
	codons = [sequence[i:i+3] for i in range(0, len(sequence), 3)] # Traversing the mRNA sequence to find Codons in threes
	codon_chart = cc.table
	amino_acids = []
	for codon in codons:
		for amino_acid, codon_list in codon_chart.items():
			if codon in codon_list:
				amino_acids.append(amino_acid)
	return to_three_letter_acids(amino_acids)

# Iterates through each letter and appends it's corresponding 3-letter amino acid name
def to_three_letter_acids(amino_acids):
	amino_chart = cc.amino_table
	amino_acid_sequence = []
	for acid in amino_acids:
		if acid in amino_chart:
			if acid == '*':
				pass # STOP Codon does not get printed
			else:
				amino_acid_sequence.append(amino_chart[acid])
	return '-'.join(amino_acid_sequence)



# Reads a translated amino acid sequence and trims off the non-coding proteins
def find_coding_regions(translation):
	# The translate() function built inside the biopython function denotes the letter 'M' as a START CODON and an asterisk '*' as the STOP CODON.
	# Therefore, finding the coding regions of a translated sequence will involve trimming based off the indices of M and *.
	coding_regions = [] 
	...

# Simulate different types of mutations 
def mutate():
	pass
