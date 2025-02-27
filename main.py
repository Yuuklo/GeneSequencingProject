import pandas as pd
import seaborn as sb
import random
import gene_tools

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
		    "COMPLEMENT (DNA)" : gene_tools.to_complement(sequence), 
		    "TRANSCRIBED (mRNA)" : gene_tools.transcribe(sequence), 
		    "COMPLEMENT (mRNA)" : gene_tools.transcribe(gene_tools.to_complement(sequence)),
		    "AMINO ACID SEQUENCE" : gene_tools.translate(gene_tools.transcribe(sequence))
		    })
	return dna_chart

# Program Start
data = create_dictionary(100, 20)
df = pd.DataFrame(data).head(1)

print(df)

