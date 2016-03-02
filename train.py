__author__ = 'TramAnh'

import numpy as np
import csv
import cPickle as pickle
from math import sqrt
from pybrain.datasets.supervised import SupervisedDataSet as SDS
from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.structure import SigmoidLayer


def encoding(seq):
    splitted = ()
    for each_char in seq:
        encoded_char = encode_char(each_char.lower())
        if encoded_char:
            splitted = splitted + (encoded_char,)
        else: #encode_char() return None
            return None

    if len(splitted)<MAXLENGTH:
        padding_length = MAXLENGTH - len(splitted)
        splitted = splitted + (0,)*padding_length

    return splitted

def encode_char(x):
    if x=='a':
        return 1
    elif x=='t':
        return 2
    elif x=='c':
        return 3
    elif x=='g':
        return 4
    else:
        return None

# load data

MAXLENGTH = 297

def load_data(filename):
    x_data = []
    y_data = []
    with open(filename, 'rb') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if not encoding(row[0].strip()) or not encoding(row[1].strip()):
                continue
            else:
                x = encoding(row[0].strip())
                y = encoding(row[1].strip())
                x_data.append(x)
                y_data.append(y)

    return np.array(x_data), np.array(y_data)

def train_fn(hiddennodes):
    trainval_file = 'trainval.csv'
    output_model_file = 'model.pkl'

    hidden_size = hiddennodes
    epochs = 600

    x_train, y_train = load_data(trainval_file)

    input_size = x_train.shape[1]
    target_size = y_train.shape[1]

    # Normalize
    x_train = x_train /4.0
    y_train = y_train /4.0

    # print 'in train.py'
    # print x_train
    # print y_train

    # prepare dataset

    ds = SDS( input_size, target_size )
    ds.setField( 'input', x_train )
    ds.setField( 'target', y_train )

    # init and train

    net = buildNetwork(input_size, hidden_size, target_size, bias = True, hiddenclass=SigmoidLayer,
                       outclass=SigmoidLayer)
    trainer = BackpropTrainer(net,ds)

    # print "training for {} epochs...".format( epochs )
    #
    # for i in range(epochs):
    #     mse = trainer.train()
    #     rmse = sqrt( mse )
    #     print "training RMSE, epoch {}: {}".format( i + 1, rmse )

    print 'Training..'
    trainer.trainUntilConvergence(verbose = True, validationProportion = 0.15, maxEpochs = 1000, continueEpochs = 10 )
    pickle.dump( net, open( output_model_file, 'wb' ))


