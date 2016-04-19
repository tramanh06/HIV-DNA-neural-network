__author__ = 'TramAnh'

import csv
from submodel import SubModel
from utils import find_mutation_pos
from utils import calculate_accuracy

class MainModel():

    def __init__(self, hiddennodes):
        self.hiddennodes = hiddennodes
        self.MutateClassifier = SubModel(hiddennodes=self.hiddennodes, type='mutate')
        # self.NomutateClassifier = SubModel(hiddennodes=self.hiddennodes, type='nomutate')

    def train(self, trainfile):
        arr = self.__get_data(trainfile)

        # Get mutation positions
        self.mut_pos = find_mutation_pos(arr)

        mut_arr, nomut_arr = self.__split_data(arr=arr, mut_pos=self.mut_pos)

        print "debug"

        # self.MutateClassifier.train(arr=mut_arr)
        # self.NomutateClassifier.train(arr=nomut_arr)

    def test(self, testfile):
        arr = self.__get_data(testfile)

        mut_arr, nomut_arr = self.__split_data(arr=arr, mut_pos=self.mut_pos)

        p_mut = self.MutateClassifier.test(arr=mut_arr)
        # p_nomut = self.NomutateClassifier.test(arr=nomut_arr)

        # p_dna = self.__merge_predicted(p_mut, p_nomut, self.mut_pos)
        self.__model_evaluation(arr=mut_arr, p_dna=p_mut)

    def __merge_predicted(self, p_mut, p_nomut, mut_pos):
        '''
        Merge mutation and nomutation array into 1
        '''
        mut_pos = sorted(mut_pos)   # to make sure positions in order
        def merge(mut, nomut):
            j=0
            for i in mut_pos:
                nomut = nomut[:i]+mut[j]+nomut[i:]
                j+=1
            return nomut
        merged = map(merge, p_mut, p_nomut)
        return merged

    def __model_evaluation(self, arr, p_dna):
        # TODO calculate confusion matrix score
        x_data, y_data = arr

        # print predicted data
        print "\n".join(p_dna)
        accuracy = calculate_accuracy(y_data, p_dna)
        print 'Accuracy'
        print accuracy

    def __get_data(self, infile):
        '''Parse data to 2 arrays (i,e, mut and wt)'''
        x_data, y_data = [], []

        with open(infile, 'rb') as f:
            csvreader = csv.reader(f)
            for line in csvreader:
                x_data.append(line[0])
                y_data.append(line[1])

        return x_data, y_data

    def __split_data(self, arr, mut_pos):
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

