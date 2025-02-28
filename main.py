import pandas as pd
import seaborn as sb
import random
import gene_tools as gt

# Generates a random sequence that is n nucleotide units long
def generate_random_sequence(sequence_length):
	nucleotides = ['A','T','G','C']
	return ''.join(random.choice(nucleotides) for _ in range(sequence_length))

# Works in tangent with generate_random_sequence() to produce a dictionary of n random DNA sequences
def create_dictionary(number_of_sequences, sequence_length):
	dna_chart = []

	for i in range(number_of_sequences):
		sequence = generate_random_sequence(sequence_length)
		dna_chart.append({
			"ID" : f"Seq_{i+1}", "SEQUENCE" : sequence, 
		    "COMPLEMENT (DNA)" : gt.to_complement(sequence), 
		    "TRANSCRIBED (mRNA)" : gt.transcribe(sequence), 
		    "COMPLEMENT (mRNA)" : gt.transcribe(gt.to_complement(sequence)),
		    "AMINO ACID SEQUENCE" : gt.find_coding_regions(gt.translate(gt.transcribe(sequence)))
		    })
	return dna_chart

# Program Start
data = create_dictionary(100, 30)
df = pd.DataFrame(data)

print(df.head(50))

