__author__ = 'TramAnh'

from train import load_data
import numpy as np
import cPickle as pickle
from pybrain.datasets.supervised import SupervisedDataSet as SDS
from scipy.stats.stats import pearsonr
from sklearn.metrics import mean_squared_error as MSE
from math import sqrt
import matplotlib.pyplot as plt

MAXLENGTH = 297

output_predictions_file = 'predictions.txt'

def test_fn(testfile, hiddennodes):
    # load model
    model_file = 'Serialized/model_{0}_nodes.pkl'.format(str(hiddennodes))
    net = pickle.load( open( model_file, 'rb' ))
    print 'Finish loading model'

    # Load test data
    x_test, y_test = load_data(testfile)
    y_test_dummy = np.zeros( y_test.shape )
    input_size = x_test.shape[1]
    target_size = y_test.shape[1]

    assert( net.indim == input_size )
    assert( net.outdim == target_size )

    # prepare dataset
    ds = SDS( input_size, target_size )
    ds.setField( 'input', x_test )
    ds.setField( 'target', y_test_dummy )

    # predict
    print 'Activating ds'
    p = net.activateOnDataset( ds )

    r_score = calculate_correlation(y_test, p)
    return r_score

def calculate_correlation(y_test, p):
    r = []
    for i in range(len(p)):
        r_score = pearsonr(y_test[i], p[i])
        r.append(r_score[0])        # pearsonr returns correlation and 2-tailed p-value. Only need correlation
    return r



if __name__=='__main__':
    test_fn()