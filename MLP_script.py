__author__ = 'TramAnh'

import train
import test
import numpy as np
from multiprocessing import Pool
import matplotlib.pyplot as plt
score=[]
testfile = 'Data/train_cleaned.csv'

def mapper(hiddennodes):
    print 'Running hiddennode=%d' %(hiddennodes)
    # train.train_fn(hiddennodes)
    r_score = test.test_fn(testfile, hiddennodes)
    # score.append([hiddennodes, score_test])R
    print 'Length of samples= %s'%len(r_score)
    print 'Hidden nodes= {0}    Score_test= {1}'.format(hiddennodes, r_score)
    return hiddennodes, r_score

pool = Pool(8)
out= pool.map(mapper, range(3,11))

