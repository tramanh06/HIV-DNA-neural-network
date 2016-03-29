
import csv
from Bio.Seq import Seq
from Bio.Alphabet import generic_rna

infile = '../results_log/prediction.csv'

dna_seq = []

with open(infile, 'rb') as f:
    for line in f:
        dna_seq.append(line.strip())

out_aa = []
for i, dna in enumerate(dna_seq):
    sample = Seq(dna, generic_rna)
    conv = sample.translate(to_stop=True).__str__()

    if len(conv) < 225/3:
        print 'Stop codon detected'
    else:
        out_aa.append([i, conv])

        