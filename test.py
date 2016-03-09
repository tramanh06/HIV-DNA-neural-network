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
    model_file = 'Serialized/model_{0}_nodes.pkl'.format(str(hiddennodes))
    output_predictions_decoded = 'Data/results_{0}_nodes.csv'.format(hiddennodes)

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

    print_predicted(x_test, y_test, p, output_predictions_decoded)

    r_score = calculate_correlation(y_test, p)
    return r_score

def calculate_correlation(y_test, p):
    r = []
    for i in range(len(p)):
        r_score = pearsonr(y_test[i], p[i])
        r.append(r_score[0])        # pearsonr returns correlation and 2-tailed p-value. Only need correlation
    return r

def print_predicted(x_test, y_test, p, output_file):
    assert( len(x_test) == len(y_test) )
    assert( len(y_test) == len(p))

    decoded_array = []
    for i in range(len(p)):
        wildtype = x_test[i]
        output = y_test[i]
        predicted = p[i]

        wildtype_decoded = decode(wildtype)
        output_decoded = decode(output)
        p_decoded = decode(predicted)

        out=[wildtype_decoded, output_decoded, p_decoded]
        decoded_array.append(out)

    with open(output_file, 'wb') as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(['wildtype', 'actual final', 'predicted final'])
        csvwriter.writerows(decoded_array)


def decode(list_of_floats):
    out_string = ''
    for each in list_of_floats:
        out_string += decode_char(each)
    return out_string

# TODO: determine threshold so it can tolerate fluctuation
def decode_char(x):
    if x > 0.85:
        return 'G'  # 1
    elif x>0.65:
        return 'C'  # 0.75
    elif x>0.35:
        return 'T'  # 0.5
    elif x>0.15:
        return 'A'  # 0.25
    else:
        return '_'  # _

if __name__=='__main__':
    test_fn()