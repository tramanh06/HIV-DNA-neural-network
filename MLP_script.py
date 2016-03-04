__author__ = 'TramAnh'

import train
import test
import postprocessing
import numpy as np

score=[]
for hiddennodes in range(3, 10):
    print 'Running hiddennode=%d' %(hiddennodes)
    train.train_fn(hiddennodes)
    test.test_fn()
    score.append([hiddennodes, postprocessing.postproc_fn()])
    print score[hiddennodes]

np.savetxt('NN_Score.txt', score)
