__author__ = 'TramAnh'

import csv
from submodel import SubModel
from utils import find_mutation_pos

class MainModel():

    def __init__(self, hiddennodes):
        self.hiddennodes = hiddennodes
        self.MutateClassifier = SubModel(hiddennodes=self.hiddennodes, type='mutate')
        self.NomutateClassifier = SubModel(hiddennodes=self.hiddennodes, type='nomutate')

    def train(self, trainfile):
        arr = self.get_data(trainfile)

        # Get mutation positions
        self.mut_pos = find_mutation_pos(arr)

        mut_arr, nomut_arr = self.split_data(arr=arr, mut_pos=self.mut_pos)

        self.MutateClassifier.train(arr=mut_arr)
        self.NomutateClassifier.train(arr=nomut_arr)

    def test(self, testfile):
        arr = self.get_data(testfile)

        mut_arr, nomut_arr = self.split_data(arr=arr, mut_pos=self.mut_pos)

        p_mut = self.MutateClassifier.test(arr=mut_arr)
        p_nomut = self.NomutateClassifier.test(arr=nomut_arr)

        p_dna = self.merge_predicted(p_mut, p_nomut, self.mut_pos)


    def merge_predicted(self, p_mut, p_nomut, mut_pos):
        mut_pos = sorted(mut_pos)   # to make sure
        def merge(mut, nomut):
            j=0
            for i in mut_pos:
                nomut = nomut[:i]+mut[j]+nomut[i:]
                j+=1
        merged = map(merge, p_mut, p_nomut)
        return merged

    def model_evaluation(self, arr, p_dna):
        # TODO calculate confusion matrix score

    def get_data(self, infile):
        '''Parse data to 2 arrays (i,e, mut and wt)'''

        with open(infile, 'rb') as f:
            csvreader = csv.reader(f)
            x_data, y_data = [[x[i] for x in csvreader] for i in range(2)]

        return x_data, y_data

    def split_data(self, arr, mut_pos):
        x_data, y_data = arr

        def split_one(data):
            mut_seqs = [''.join([x[i] for i in mut_pos]) for x in data]
            nomut_seqs = [''.join([x[i] for i in range(len(x)) if i not in mut_pos]) for x in data]
            return mut_seqs, nomut_seqs

        x_mut, x_nomut = split_one(x_data)
        y_mut, y_nomut = split_one(y_data)

        mut_arr = [x_mut, y_mut]
        nomut_arr = [x_nomut, y_nomut]

        return mut_arr, nomut_arr

