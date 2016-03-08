__author__ = 'TramAnh'

import train
import test
import numpy as np
from multiprocessing import Pool

score=[]

def mapper(hiddennodes):
    print 'Running hiddennode=%d' %(hiddennodes)
    # train.train_fn(hiddennodes)
    score_test = test.test_fn(hiddennodes)
    # score.append([hiddennodes, score_test])
    print 'Hidden nodes= {0}    Score_test= {1}'.format(hiddennodes, score_test)
    return hiddennodes, score_test

pool = Pool(8)
out= pool.map(mapper, range(3,11))

print 'out= %s' %(out)
score.append(out)

# np.savetxt('NN_Score.txt', score)
