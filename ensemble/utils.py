__author__ = 'TramAnh'

import numpy as np
from sklearn.preprocessing import scale
from Levenshtein import distance

# encoder = {'c': -0.5, 't': -0.17, 'a':0.16, 'g':0.50}
# encoder = {'c': 1.0, 't': 2.0, 'a':3.0, 'g':4.0}
encoder = {'c': -1.0, 't': -0.5, 'a':0.5, 'g':1.0}


def __find_mutations_each(seq1, seq2):
    assert (len(seq1)==len(seq2))
    mut = {i for i in range(len(seq1)) if seq1[i]!=seq2[i]}     # set
    return mut

def find_mutation_pos(arr):
    '''~
    Param data: 2d list of sequences
    Take in data of 2 columns wildtype and mutant
    Return a set of all positions that ever have mutations occured
    '''
    a = set()

    x, y = arr
    for i in range(len(x)):
        a |= __find_mutations_each(x[i], y[i])   # |= is union operation
    return a

def load_data(arr):
    # [wt, mt] = arr      # wt and mt are list of sequence (in string)

    def convert(wt):
        x_matrix = []
        for line in wt:
            temp = []
            for char in line:
                temp.append(encoder[char.lower()])
            x_matrix.append(temp)
        return x_matrix

    # Convert to numpy matrix
    x_matrix, y_matrix = [np.asarray(convert(x)) for x in arr]

    return x_matrix, y_matrix

def calculate_accuracy(arr1, arr2):
    '''arr1 and arr2 are mutant and predicted array of sequence. In string
        Return array of accuracy score'''
    def accuracy(str1, str2):

        error = distance(str1, str2)/float(len(str1))
        return 1-error
    accuracy_arr = map(accuracy, arr1, arr2)
    return accuracy_arr