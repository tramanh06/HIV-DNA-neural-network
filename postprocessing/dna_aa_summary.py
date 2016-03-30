from utils import dna_to_aa, confusion_matrix
import csv
from Levenshtein import distance

predictfile = '/Users/TramAnh/Dropbox/NTU/BII_Parttime_work/HIV/ForSight Results/3rd_set/set3_converted.txt'       # in DNA
actualfile = '/Users/TramAnh/Dropbox/NTU/BII_Parttime_work/HIV/ForSight Results/test_aligned.csv'   # WT, MT in DNA
outfile = '/Users/TramAnh/Dropbox/NTU/BII_Parttime_work/HIV/ForSight Results/3rd_set/summary.csv'


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

    stats_dna = []
    stats_aa = []

    dist_dna = []
    dist_aa = []

    CODON_MSG = 'Contains stop codon'

    # Analyse prediction
    with open(predictfile, 'rb') as f:
        for line in f:
            dna = line.strip()
            predict_dna.append(dna)
            has_stop, aa = dna_to_aa(dna)     # dna_to_aa returns [has_stop_codon, aa]
            alert(has_stop)
            if has_stop:
                aa = CODON_MSG
            predict_aa.append(aa)

    # Analyse clinical data
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
            if has_stop:
                wt_aa = CODON_MSG
            actual_wt_aa.append(wt_aa)

            has_stop, mt_aa = dna_to_aa(mt)
            alert(has_stop)
            if has_stop:
                mt_aa = CODON_MSG
            actual_mt_aa.append(mt_aa)

    # Calculate confusion matrix
    for i in range(len(actual_wt_dna)):
        stats_dna.append(confusion_matrix(wt=actual_wt_dna[i],
                                          mt=actual_mt_dna[i],
                                          predicted=predict_dna[i]).__str__())
        stats_aa.append(confusion_matrix(wt=actual_wt_aa[i],
                                         mt=actual_mt_aa[i],
                                         predicted=predict_aa[i]).__str__())

        dist_dna.append(distance(actual_mt_dna[i].lower(), predict_dna[i].lower()))
        dist_aa.append(distance(actual_mt_aa[i].lower(), predict_aa[i].lower()))

    # Calculate Levenstein distance


    with open(outfile, 'wb') as f:
        csvwriter = csv.writer(f)
        headers = ['Wildtype (DNA)', 'Mutant (DNA)', 'Predicted (DNA)', 'ConfMatrix (DNA)', 'Distance (DNA)',
                   'Wildtype (AA)', 'Mutant (AA)', 'Predicted (AA)', 'ConfMatrix (AA)', 'Distance (AA)']
        csvwriter.writerow(headers)

        num_seq = len(predict_dna)
        for i in range(num_seq):
            row = [actual_wt_dna[i], actual_mt_dna[i], predict_dna[i], stats_dna[i], dist_dna[i],
                   actual_wt_aa[i], actual_mt_aa[i], predict_aa[i], stats_aa[i], dist_aa[i]]
            csvwriter.writerow(row)


