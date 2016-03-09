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
    r_score, top_score = test.test_fn(testfile, hiddennodes)       # r_score is list of r score for each sample
    # score.append([hiddennodes, score_test])R
    # print 'Length of samples= %s'%len(r_score)
    # print 'Hidden nodes= {0}    Score_test= {1}'.format(hiddennodes, r_score)
    return hiddennodes, r_score, top_score

plt.figure(1)
pool = Pool(8)
out= pool.map(mapper, range(3,11))  # Return out in format [nodes, r_score, top_score]

top_intersect = set()
for i in out:
    print 'Hiddenlayer= %s' %(i[0])
    print 'Top perf sequeces= {0}'.format(i[2])
    if not top_intersect:
        top_intersect = set(i[2])
    else:
        top_intersect.intersection(i[2])

print "Intersect top results= {0}".format(top_intersect)
print "Length intersection=%s" %(len(top_intersect))

import cPickle as pickle
pickle.dump( top_intersect, open( 'top_perf.pkl', 'wb'))





# Plot histogram for each configuration
# for i in out:
#     nodes = i[0]
#     plot_histogram(i[1], nodes)

# plt.show()

# print 'out= %s' %(out)
# score.append(out)
# np.savetxt('NN_Score.txt', score)
