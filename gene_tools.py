from Bio.Seq import Seq
from Bio.SeqUtils import CodonUsage

# Returns the complement strand of a DNA sequence
def to_complement(sequence):
	complementary_nucleotides = {'A': 'T', 'G': 'C',
				   				 'T': 'A', 'C': 'G'}
	return ''.join(complementary_nucleotides[i] for i in sequence)

# Returns the transcribed (RNA) version of a sequence
def transcribe(sequence):
	return sequence.replace('T','U')

# Translates a mRNA sequence into their corresponding amino acid structure with the help the *biopython* library
def translate(sequence):
	three_letter_aminos = {
	    'A': 'Ala', 'R': 'Arg', 'N': 'Asn', 'D': 'Asp', 'C': 'Cys',
	    'Q': 'Gln', 'E': 'Glu', 'G': 'Gly', 'H': 'His', 'I': 'Ile',
	    'L': 'Leu', 'K': 'Lys', 'M': 'Met', 'F': 'Phe', 'P': 'Pro',
	    'S': 'Ser', 'T': 'Thr', 'W': 'Trp', 'Y': 'Tyr', 'V': 'Val', '*': 'Stop'
	}
	translated = Seq(sequence).translate() # Returns the single-letter key values of each amino acid
	three_letter_translation = ' '.join(three_letter_aminos[i] for i in translated) # Iterates through each letter and gives it a corresponding 3-Letter Amino Acid
	return three_letter_translation
	

# Simulate different types of mutations 
def mutate():
	pass
