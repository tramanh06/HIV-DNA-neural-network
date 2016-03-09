__author__ = 'TramAnh'

bad = [0, 17, 26]

read_file = open( 'Data/test_cleaned.csv', 'rb')
write_file = open('Data/bad_perf.txt', 'wb')

for i, line in enumerate(read_file):
    if i in bad:
        write_file.write(line)

