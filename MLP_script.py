__author__ = 'TramAnh'

import train
import test
import numpy as np
from multiprocessing import Pool
import matplotlib.pyplot as plt
score=[]
testfile = 'Data/test_cleaned.csv'

def plot_histogram(r, hiddennodes):
    plt.subplot(240+hiddennodes-2)
    plt.hist(r, bins=20)
    plt.title("hiddennodes=%s" %hiddennodes)
    plt.ylim(0,25)

def mapper(hiddennodes):
    print 'Running hiddennode=%d' %(hiddennodes)
    # train.train_fn(hiddennodes)
    r_score = test.test_fn(testfile, hiddennodes)
    # score.append([hiddennodes, score_test])R
    print 'Length of samples= %s'%len(r_score)
    print 'Hidden nodes= {0}    Score_test= {1}'.format(hiddennodes, r_score)
    return hiddennodes, r_score

plt.figure(1)
pool = Pool(8)
out= pool.map(mapper, range(3,11))

bad = set(range(35))
for i in out:
    r_score = i[1]
    bad_score = [i for i, x in enumerate(r_score) if x < 0.05]
    print bad_score
    bad = bad.intersection(bad_score)

print 'Bad performance position: {0}'.format(bad)

