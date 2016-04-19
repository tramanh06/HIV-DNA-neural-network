__author__ = 'TramAnh'

import csv
import random

wobble_base = {}
wobble_base['b']= ('t') #('c', 'g', 't')       # t
wobble_base['d']= ('g') #('a', 'g', 't')       # g
wobble_base['h']= ('c') #('a', 'c', 't')       # c
wobble_base['k']= ('t') #('g', 't')            # t
wobble_base['m']= ('c') #('a', 'c')            # c
wobble_base['n']= ('t') #('a', 'c', 't', 'g')  # t
wobble_base['r']= ('a') #('a', 'g')            # a
wobble_base['s']= ('g') #('g', 'c')            # g
wobble_base['v']= ('a') #('a', 'c', 'g')       # a
wobble_base['w']= ('a') #('a', 't')            # a
wobble_base['y']= ('c') #('c', 't')            # c

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
            # print 'convert %s to %s' %(char, new)
    return temp

with open('../Data/trainvaltest.csv','rb') as f:
    arr = []
    csvreader = csv.reader(f)
    for line in csvreader:
        if 'seq_ND' in line:
            continue
        string1 = convert(line[0])
        string2 = convert(line[1])
        arr.append([string1, string2])

# write to file
with open('../Data/wobble_data/trainvaltest.csv', 'wb') as writef:
    csvwriter = csv.writer(writef)
    csvwriter.writerows(arr)

