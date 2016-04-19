__author__ = 'TramAnh'

from mainmodel import MainModel

if __name__=='__main__':
    model = MainModel(5)
    model.train(trainfile='../Data/wobble_data/train_aligned.csv')
    model.test(testfile='../Data/wobble_data/test_aligned.csv')
