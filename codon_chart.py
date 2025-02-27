table = {
    'M': ['AUG'],  # Methionine (Start codon)
    '*': ['UAA', 'UAG', 'UGA'],  # Stop codons
    'F': ['UUU', 'UUC'],  # Phenylalanine
    'L': ['UUA', 'UUG', 'CUU', 'CUC', 'CUA', 'CUG'],  # Leucine
    'I': ['AUU', 'AUC', 'AUA'],  # Isoleucine
    'V': ['GUU', 'GUC', 'GUA', 'GUG'],  # Valine
    'S': ['UCU', 'UCC', 'UCA', 'UCG', 'AGU', 'AGC'],  # Serine
    'P': ['CCU', 'CCC', 'CCA', 'CCG'],  # Proline
    'T': ['ACU', 'ACC', 'ACA', 'ACG'],  # Threonine
    'A': ['GCU', 'GCC', 'GCA', 'GCG'],  # Alanine
    'Y': ['UAU', 'UAC'],  # Tyrosine
    'H': ['CAU', 'CAC'],  # Histidine
    'Q': ['CAA', 'CAG'],  # Glutamine
    'N': ['AAU', 'AAC'],  # Asparagine
    'K': ['AAA', 'AAG'],  # Lysine
    'D': ['GAU', 'GAC'],  # Aspartic acid
    'E': ['GAA', 'GAG'],  # Glutamic acid
    'C': ['UGU', 'UGC'],  # Cysteine
    'W': ['UGG'],  # Tryptophan
    'R': ['CGU', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'],  # Arginine
    'G': ['GGU', 'GGC', 'GGA', 'GGG']  # Glycine
    }

amino_table = {
    'M': 'Met',
    'F': 'Phe',
    'L': 'Leu',
    'I': 'Ile',
    'V': 'Val',
    'S': 'Ser',
    'P': 'Pro',
    'T': 'Thr',
    'A': 'Ala',
    'Y': 'Tyr',
    'H': 'His',
    'Q': 'Gln',
    'N': 'Asn',
    'K': 'Lys',
    'D': 'Asp',
    'E': 'Glu',
    'C': 'Cys',
    'W': 'Trp',
    'R': 'Arg',
    'G': 'Gly',
    '*': 'STOP'
}