__author__ = 'TramAnh'

import pandas as pd
import numpy as np
import csv

# Read in PR.txt
f = open('../PR.txt', 'r')
flag = False
no_drug_lst = []
drug_lst = []
for line in f:
    if flag == False:
        flag = True
    else:
        tokens = line.split("\t")
        if tokens[-1].strip():
            ptid = int(tokens[1])
            drug = tokens[6]
            seq = tokens[-1].strip()
            if drug == 'None':
                no_drug_lst.append([ptid, drug, seq])
            else:
                drug_lst.append([ptid, drug, seq])

# Put into df to merge
no_drug_df = pd.DataFrame(no_drug_lst, columns=['ptid', 'Drug', 'seq'])
drug_df = pd.DataFrame(drug_lst, columns=['ptid', 'Drug', 'seq'])
merged = pd.merge(no_drug_df, drug_df, on='ptid', how='inner', suffixes=('_ND', '_D'))

merged.to_csv('alldata.csv', sep="\t", index=False, quoting=csv.QUOTE_NONE)

trainvaltest = merged[['seq_ND','seq_D']]

# Split to train and test

num_sample = len(trainvaltest)
test_ratio = 0.15
trainval = trainvaltest[:int((1-test_ratio)*num_sample)]
test = trainvaltest[int((1-test_ratio)*num_sample):]

trainval.to_csv('trainval.csv', index=False, header=False)
test.to_csv('test.csv', index=False, header=False)


