__author__ = 'TramAnh'

import train
import test
import postprocessing
import numpy as np

score=[]
for hiddennodes in range(4, 6):
    print 'Running hiddennode=%d' %(hiddennodes)
    train.train_fn(hiddennodes)
    score_test = test.test_fn()
    score.append([hiddennodes, score_test])
    print score[hiddennodes]

np.savetxt('NN_Score.txt', score)
