__author__ = 'TramAnh'

import csv
from filter_input_data import write_csv
infile = 'Data/alignment/trainval_aligned.csv'

def load_data(infile):
    arr = []
    with open(infile, 'rb') as f:
        csvreader = csv.reader(f)
        for line in csvreader:
            arr.append(line)

    return arr

trainval = load_data(infile)
test_ratio = 0.15
' Split data '
num_sample = len(trainval)
trainval_mark = int((1-test_ratio)*num_sample)

train = trainval[:trainval_mark]
test = trainval[trainval_mark:]

'Write to csv'
write_csv('Data/alignment/train_aligned.csv', train)
write_csv('Data/alignment/test_aligned.csv', test)
