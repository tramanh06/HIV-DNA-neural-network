__author__ = 'TramAnh'

from Bio.Seq import Seq
from Bio.Alphabet import generic_rna
import numpy as np

def dna_to_aa(sequence):
    ''' Convert DNA to Amino Acid sequence.
        Return [has_stop_codon, converted_amino_acid]
    '''
    if len(sequence) != 225:
        print len(sequence)

    sample = Seq(sequence, generic_rna)
    amino_acid = sample.translate(to_stop=True).__str__()

    codon = False
    if len(amino_acid) < 225/3:
        'Stop codon detected'
        codon = True

    return codon, amino_acid

def confusion_matrix(wt, mt, predicted):
    '''
    Take in wildtype, mutant and predicted sequence.
    String type.
    Compute a confusion matrix of
                predicted
                NC          C
    actual  NC
            C
    '''

    if 'stop codon' in predicted:
        return

    # Make sure same length
    assert(len(wt) == len(mt))
    assert(len(mt) == len(predicted))

    tp, fp_nc, fp_c, tn, fn = [0] * 5

    for i in range(len(wt)):
        w = wt[i].lower()
        m = mt[i].lower()
        p = predicted[i].lower()

        if m == w:
            if p == w:
                tp += 1
            else:
                fn += 1
        else:   # case m != w
            if p == m:  # change correctly
                tn += 1
            elif p == w:
                fp_nc += 1
            else:
                fp_c += 1

    MAXLENGTH = len(wt)
    tp = tp/float(MAXLENGTH)
    fn = fn/float(MAXLENGTH)
    fp_c = fp_c/float(MAXLENGTH)
    fp_nc = fp_nc/float(MAXLENGTH)
    tn = tn/float(MAXLENGTH)

    matrix = [[tp, fn], [[fp_nc, fp_c], tn]]

    return matrix

