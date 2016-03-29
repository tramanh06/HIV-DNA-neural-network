__author__ = 'TramAnh'

from Bio.Seq import Seq
from Bio.Alphabet import generic_rna

def dna_to_aa(sequence):
    ''' Convert DNA to Amino Acid sequence.
        Return [has_stop_codon, converted_amino_acid]
    '''
    if len(sequence) != 225:
        print len(sequence)

    sample = Seq(sequence, generic_rna)
    amino_acid = sample.translate(stop_symbol='-')


    codon = amino_acid.
    if len(amino_acid) < 225/3:
        'Stop codon detected'
        codon = True

    return codon, amino_acid
