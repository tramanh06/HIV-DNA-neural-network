__author__ = 'TramAnh'

from mainmodel import MainModel

if __name__=='__main__':
    model = MainModel(5)
    model.train(trainfile='../Data/alignment/train_aligned.csv')
    model.test(testfile='../Data/alignment/test_aligned.csv')
