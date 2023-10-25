"""
DNA to Protein Translation Tool:
Takes a DNA sequence and translates it into the corresponding 
amino acid sequence using the genetic code table.

Steps:
1 entrada de cadena ADN (txt)
2 lectura de la cadena
3 traductor de adn a aminoacido(bases)
4 traduccion a aminoacidos
5 impresion de la cadena de aminoacidos

"""


genetic_code = {
    'TTT': 'Phe', 'TTC': 'Phe', 'TTA': 'Leu', 'TTG': 'Leu',
    'TCT': 'Ser', 'TCC': 'Ser', 'TCA': 'Ser', 'TCG': 'Ser',
    'TAT': 'Tyr', 'TAC': 'Tyr', 'TAA': 'Stop', 'TAG': 'Stop',
    'TGT': 'Cys', 'TGC': 'Cys', 'TGA': 'Stop', 'TGG': 'Trp',
    'CTT': 'Leu', 'CTC': 'Leu', 'CTA': 'Leu', 'CTG': 'Leu',
    'CCT': 'Pro', 'CCC': 'Pro', 'CCA': 'Pro', 'CCG': 'Pro',
    'CAT': 'His', 'CAC': 'His', 'CAA': 'Gln', 'CAG': 'Gln',
    'CGT': 'Arg', 'CGC': 'Arg', 'CGA': 'Arg', 'CGG': 'Arg',
    'ATT': 'Ile', 'ATC': 'Ile', 'ATA': 'Ile', 'ATG': 'Met',
    'ACT': 'Thr', 'ACC': 'Thr', 'ACA': 'Thr', 'ACG': 'Thr',
    'AAT': 'Asn', 'AAC': 'Asn', 'AAA': 'Lys', 'AAG': 'Lys',
    'AGT': 'Ser', 'AGC': 'Ser', 'AGA': 'Arg', 'AGG': 'Arg',
    'GTT': 'Val', 'GTC': 'Val', 'GTA': 'Val', 'GTG': 'Val',
    'GCT': 'Ala', 'GCC': 'Ala', 'GCA': 'Ala', 'GCG': 'Ala',
    'GAT': 'Asp', 'GAC': 'Asp', 'GAA': 'Glu', 'GAG': 'Glu',
    'GGT': 'Gly', 'GGC': 'Gly', 'GGA': 'Gly', 'GGG': 'Gly',
}

def codon_to_aminoacid(codon):
    """Converts a single codon from the corresponding amino acid
    
    Parameters:
        codon (str) : Three letters codon
    
    Returns:
        str : amino acid name
    """
    if not isinstance(codon, str):
        print("Codon must be a string")
        return None
    if len(codon) != 3:
        print("Codon length must be of size 3")
        return None
    if codon not in genetic_code:
        print(f"Invalid Codon {codon}")
        return None
    return genetic_code[codon]


def adn_to_aminoacids(adn_strand):
    """Converts a DNA strand of any size into a amino acids string

    Parameters:
        adn_strand (str) : DNA strand to be converted
    
    Returns:
        str : amino acids string
    """

    amino_acids = []
    index = 0
    while index < len(adn_strand) - 3:
        codon = adn_strand[index:index+3]
        one_amino_acid = codon_to_aminoacid(codon)
        if one_amino_acid is not None:
            amino_acids.append(one_amino_acid)
            index += 3
        else:
            index += 1
    return amino_acids



# DEMO

SAMPLE1 = "ATGCGAATGGGTAAG"
EXPECTED_OUTPUT1 = "Met Arg Asn Gly Lys"

real_result = adn_to_aminoacids(SAMPLE1)
print(real_result)
