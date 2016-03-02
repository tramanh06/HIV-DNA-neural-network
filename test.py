__author__ = 'TramAnh'

from train import load_data
import numpy as np
import cPickle as pickle
from pybrain.datasets.supervised import SupervisedDataSet as SDS
from sklearn.metrics import mean_squared_error as MSE
from math import sqrt

MAXLENGTH = 297
test_file = 'test.csv'
model_file = 'model.pkl'
output_predictions_file = 'predictions.txt'

def test_fn():
    # load model
    net = pickle.load( open( model_file, 'rb' ))
    print 'Finish loading model'

    # Load test data
    x_test, y_test = load_data('test.csv')
    x_test = x_test /4.0
    y_test = y_test /4.0

    y_test_dummy = np.zeros( y_test.shape )
    print x_test
    print y_test
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

    mse = MSE( y_test, p )
    rmse = sqrt( mse )

    print "testing RMSE:", rmse

    np.savetxt( output_predictions_file, p, fmt = '%.6f' )