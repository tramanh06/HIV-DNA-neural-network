__author__ = 'TramAnh'

import train
import test
import postprocessing
import numpy as np

score={}
for i in range(3, 10):
    print 'Running hiddennode=%d' %(i)
    train.train_fn(i)
    test.test_fn()
    score[i] = postprocessing.postproc_fn()
    print score[i]

np.savetxt('NN_Score.txt', score)
