__author__ = 'TramAnh'

import train
import test
import numpy as np
from multiprocessing import Pool
import matplotlib.pyplot as plt

''' Controller to train NN model '''

score=[]
testfile = 'Data/test_cleaned.csv'
trainfile = 'Data/train_cleaned.csv'

def plot_histogram(r, hiddennodes):
    plt.subplot(240+hiddennodes-2)
    plt.hist(r, bins=20)
    plt.title("hiddennodes=%s" %hiddennodes)
    plt.ylim(0,25)

def mapper(hiddennodes):
    print 'Running hiddennode=%d' %(hiddennodes)
    train.train_fn(hiddennodes, trainfile)
    r_score = test.test_fn(testfile, hiddennodes)
    print 'Length of samples= %s'%len(r_score)
    print 'Hidden nodes= {0}    Score_test= {1}'.format(hiddennodes, r_score)
    return hiddennodes, r_score

# Run in parallel
pool = Pool(8)
out= pool.map(mapper, range(3,11))      # out = [[hiddennodes, [score1, score2,..]], [hiddennodes, [score1, score2,...]]]

# Plot histogram
plt.figure(1)
for i in out:
    nodes = i[0]
    plot_histogram(i[1], nodes)
plt.show()

print 'out= %s' %(out)
score.append(out)

# np.savetxt('NN_Score.txt', score)
