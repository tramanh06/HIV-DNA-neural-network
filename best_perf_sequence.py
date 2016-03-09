__author__ = 'TramAnh'


import cPickle as pickle

top_perf = pickle.load( open('top_perf.pkl', 'rb'))

read_file = open( 'Data/test_cleaned.csv', 'rb')
write_file = open('Data/top_perf.txt', 'wb')

for i, line in enumerate(read_file):
    if i in top_perf:
        write_file.write(line)

