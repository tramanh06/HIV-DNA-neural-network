__author__ = 'TramAnh'

import csv

def get_sequences(filename, arr):
    with open(filename, 'rb') as f:
        csvreader = csv.reader(f)
        for line in csvreader:
            arr.append(line)

def write_fasta(outfile, arr):
    with open(outfile, 'wb') as f:
        for i, line in enumerate(arr):
            f.write('>{0}W\n'.format(i))
            f.write(line[0].strip()+'\n')
            f.write('>{0}M\n'.format(i))
            f.write(line[1].strip()+'\n')

# trainfile = 'Data/train_cleaned.csv'
# testfile = 'Data/test_cleaned.csv'
file = '../Data/wobble_data/trainvaltest.csv'
outfile = '../Data/wobble_data/fasta_4alignment.txt'

arr=[]
# get_sequences(trainfile, arr)
get_sequences(file, arr)

write_fasta(outfile, arr)



