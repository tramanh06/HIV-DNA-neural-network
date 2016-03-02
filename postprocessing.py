__author__ = 'TramAnh'

import csv


def decode(x):
    if x > 0.75:
        return 'G'
    elif x>0.5:
        return 'C'
    elif x>0.25:
        return 'T'
    else:
        return 'A'

def similarity(a, b):
    # assert(len(a)==len(b))
    # print 'length a=%d' %(len(a))
    # print 'length b=%d' %(len(b))
    score = 0
    for i in range(len(a)):
        if a[i]==b[i]:
            score += 1
    return float(score)/len(a)

def postproc_fn():
    f = open('predictions.txt', 'rb')
    p_sequences = []
    for line in f:
        nums = line.split()
        temp = ''
        for num in nums:
            temp = temp + decode(float(num))
        p_sequences.append(temp)

    # Compare with test.csv
    similar = []
    with open('test.csv', 'rb') as testfile:
        reader = csv.reader(testfile,)
        for i, row in enumerate(reader):
            print i
            d = row[1]
            o = p_sequences[i]
            similar.append(similarity(d, o))

    mean = sum(similar)/len(similar)
    print 'Mean similarity= %f' %(mean)