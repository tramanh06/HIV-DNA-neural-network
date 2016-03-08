__author__ = 'TramAnh'

from train import load_data
import numpy as np
import cPickle as pickle
from pybrain.datasets.supervised import SupervisedDataSet as SDS
from sklearn.metrics import mean_squared_error as MSE
from math import sqrt
import matplotlib.pyplot as plt

MAXLENGTH = 297
test_file = 'test.csv'

output_predictions_file = 'predictions.txt'

def test_fn(hiddennodes):
    # load model
    model_file = 'model_{0}_nodes.pkl'.format(str(hiddennodes))
    net = pickle.load( open( model_file, 'rb' ))
    print 'Finish loading model'

    # Load test data
    x_test, y_test = load_data('test.csv')
    # x_test = x_test /4.0
    # y_test = y_test /4.0


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

    print p
    print 'Length of test output p {0}'.format(len(p))
    # mse = MSE( y_test, p )
    # rmse = sqrt( mse )
    #
    # print "testing RMSE:", rmse

    # np.savetxt( output_predictions_file, p, fmt = '%.6f' )

    print 'To debug'
    similarity_score = compare_ytest_p(y_test, p)

    return similarity_score

def compare_ytest_p(y_test, p):
    # Calculate similarity (in number) between y_test and p
    score = 0

    for i, row in enumerate(p):
        p_decoded = []
        for each in row:
            decoded_x = decode(each)
            p_decoded.append(decoded_x)
        score_temp =  similarity(p_decoded, y_test[i])
        if (score_temp <0.80):
            print 'Score below 0.80'
            print 'Score= {0}'.format(score_temp)
            temp_ytest = y_test[i]
            # plot_low_score(y_test[i], row, temp)
        score += score_temp

    average_score = score / len(p)

    print 'Average score = {0}'.format(average_score)
    return average_score

def plot_low_score(desired, predicted, p_encode):
    x_axis = range(1, MAXLENGTH+1)
    plt.figure(1)
    # plt.subplot(211)
    plt.plot(x_axis, desired, 'bo', x_axis, p_encode, 'ro')
    plt.show()

# TODO: determine threshold so it can tolerate fluctuation
def decode(x):
    if x > 0.85:
        return 1
    elif x>0.65:
        return 0.75
    elif x>0.35:
        return 0.5
    elif x>0.15:
        return 0.25
    else:
        return 0

def similarity(a, b):
    '''
    Calculate similarity between 2 strings
    :param a: array containing encoded sequences
    :param b: array containing encoded sequences
    :return: score of similarity between the 2 array sequences
    '''
    assert(len(a)==len(b))

    # print 'length a=%d' %(len(a))
    # print 'length b=%d' %(len(b))
    score = 0
    for i in range(len(a)):
        if a[i]==b[i]:
            score += 1
    return float(score)/len(a)


if __name__=='__main__':
    test_fn()