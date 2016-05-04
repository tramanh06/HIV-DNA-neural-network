__author__ = 'TramAnh'

from mainmodel import MainModel
from multiprocessing import Pool
import matplotlib.pyplot as plt

def plot_histogram(r, hiddennodes):
    plt.subplot(140+hiddennodes-2)
    plt.hist(r, bins=20)
    plt.title("hiddennodes=%s" %hiddennodes)
    # plt.ylim(0,10)

def mapper(hiddennodes):
    print 'Running hiddennodes %s' %(hiddennodes)
    model = MainModel(hiddennodes)
    print 'Training..'
    model.train(trainfile='../Data/wobble_data/train_aligned.csv')
    print 'Testing..'
    score = model.test(testfile='../Data/wobble_data/test_aligned.csv')
    return hiddennodes, score

if __name__=='__main__':
    # Parallel run
    # plt.figure(1)
    # pool = Pool(4)
    # out= pool.map(mapper, range(3,7))
    #
    # for i in out:
    #     nodes = i[0]
    #     plot_histogram(i[1], nodes)
    #
    # plt.show()

    mapper(6)