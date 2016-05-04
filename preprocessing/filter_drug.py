__author__ = 'TramAnh'

import sys
import csv
# print 'Hello world from command line! {0}'.format(sys.argv)
import pandas as pd

def main(argv):
    drug = argv
    datapath = '../Data/alldata_DrugSeq_pair.csv'
    df = pd.read_csv(datapath, sep='\t')
    drugdf = df[df['Drug_D']==drug][['seq_ND','seq_D']]
    drugdf.to_csv(drug+'.csv',index=False, quoting=csv.QUOTE_NONE)

if __name__=='__main__':
    main(sys.argv[1])