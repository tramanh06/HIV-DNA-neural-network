from utils import dna_to_aa
import csv

predictfile = '../results_log/prediction.csv'       # in DNA
actualfile = '../Data/alignment/test_aligned.csv'   # WT, MT in DNA

def alert(has_stop):
    if has_stop:
        print 'Stop codon detected'

if __name__== '__main__':
    predict_dna = []
    predict_aa = []
    actual_wt_dna = []
    actual_wt_aa = []
    actual_mt_dna = []
    actual_mt_aa = []

    with open(predictfile, 'rb') as f:
        for line in f:
            dna = line.strip()
            predict_dna.append(dna)
            has_stop, aa = dna_to_aa(dna)     # dna_to_aa returns [has_stop_codon, aa]
            alert(has_stop)
            predict_aa.append(aa)

    with open(actualfile, 'rb') as f:
        csvreader = csv.reader(f)
        for line in csvreader:
            wt = line[0]
            mt = line[1]
            actual_wt_dna.append(wt)
            actual_mt_dna.append(mt)

            # Convert to Amino Acid
            has_stop, wt_aa = dna_to_aa(wt)
            alert(has_stop)
            actual_wt_aa.append(wt_aa)

            has_stop, mt_aa = dna_to_aa(mt)
            alert(has_stop)
            actual_mt_aa.append(mt_aa)

    with open('summary.csv', 'wb') as f:
        csvwriter = csv.writer(f)
        headers = ['Wildtype (DNA)', 'Mutant (DNA)', 'Predicted (DNA)',
                   'Wildtype (AA)', 'Mutant (AA)', 'Predicted (AA)']
        csvwriter.writerow(headers)

        num_seq = len(predict_dna)
        for i in range(num_seq):
            row = [actual_wt_dna[i], actual_mt_dna[i], predict_dna[i],
                   actual_wt_aa[i], actual_mt_aa[i], predict_aa[i]]
            csvwriter.writerow(row)


