__author__ = 'TramAnh'

import numpy as np
from sklearn.preprocessing import scale

encoder = {'c': -0.5, 't': -0.17, 'a':0.16, 'g':0.50}

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

    # Convert to numpy matrix
    x_matrix, y_matrix = [np.asarray(convert(x)) for x in arr]

    return x_matrix, y_matrix
