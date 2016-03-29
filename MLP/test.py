__author__ = 'TramAnh'

from train import load_data
import numpy as np
import cPickle as pickle
from pybrain.datasets.supervised import SupervisedDataSet as SDS
from scipy.stats.stats import pearsonr
from sklearn.metrics import mean_squared_error as MSE
from math import sqrt
import matplotlib.pyplot as plt
import csv

MAXLENGTH = 297

output_predictions_file = 'predictions.txt'

def test_fn(testfile, hiddennodes):
    # load model
    model_file = '../Serialized/model_{0}_nodes.pkl'.format(str(hiddennodes))
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

    p_decoded, dna_converted = decode_whole(p)
    r_score = calculate_correlation(y_test, p_decoded)

    # Write converted predicted sequence to file
    with open('../results_log/prediction.csv', 'wb') as f:
        for item in dna_converted:
            print>>f, item

    return r_score


def calculate_correlation(y_test, p):
    r = []
    for i in range(len(p)):
        r_score = pearsonr(y_test[i], p[i])
        r.append(r_score[0])        # pearsonr returns correlation and 2-tailed p-value. Only need correlation
    return r

def decode_whole(p):
    '''
    Decode from real sequence to threshold sequence
    :param p: predicted sequence (in list of sequence)
    :return: list of threshold values
    '''
    arr = []
    texts = []
    for seq in p:
        decoded_inlist, decoded_intext = decode_each(seq)
        arr.append(decoded_inlist)
        texts.append(decoded_intext)

    return arr, texts

def decode_each(x):
    'param x is a list of numbers'
    # assert (type(x) is float)
    arr = []
    temp = ''
    for each in x:
        if each <= 0.25:
            temp += 'a'
            arr.append(0.25/2)
        elif each <= 0.5:
            temp += 't'
            arr.append((0.25+0.5)/2)
        elif each <= 0.75:
            temp += 'c'
            arr.append((0.5+0.75)/2)
        else:
            temp += 'g'
            arr.append((0.75+1)/2)
    return arr, temp

if __name__=='__main__':
    test_fn()