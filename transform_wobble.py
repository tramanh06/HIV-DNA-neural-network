__author__ = 'TramAnh'

import csv
import random

wobble_base = {}
wobble_base['b']= ('c', 'g', 't')
wobble_base['d']= ('a', 'g', 't')
wobble_base['h']= ('a', 'c', 't')
wobble_base['k']= ('g', 't')
wobble_base['m']= ('a', 'c')
wobble_base['n']= ('a', 'c', 't', 'g')
wobble_base['r']= ('a', 'g')
wobble_base['s']= ('g', 'c')
wobble_base['v']= ('a', 'c', 'g')
wobble_base['w']= ('a', 't')
wobble_base['y']= ('c', 't')

valid = ('a', 'c', 't', 'g')

def convert(sequence):
    temp = ''
    for char in sequence:
        char = char.lower()
        if char in valid:
            temp += char
        else:
            new = random.choice(wobble_base[char])
            temp += new
            print 'convert %s to %s' %(char, new)
    return temp

with open('Data/trainvaltest.csv','rb') as f:
    arr = []
    csvreader = csv.reader(f)
    for line in csvreader:
        if 'seq_ND' in line:
            continue
        string1 = convert(line[0])
        string2 = convert(line[1])
        arr.append([string1, string2])

# write to file
with open('Data/wobble_data/trainvaltest.csv', 'wb') as writef:
    csvwriter = csv.writer(writef)
    csvwriter.writerows(arr)

