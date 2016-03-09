__author__ = 'TramAnh'

''' Split to train and test '''

from filter_input_data import filter, write_csv

filename = 'Data/trainvaltest.csv'

unseen_ratio = 0.15
test_ratio = 0.15

' Filter out noise sequence in trainvaltest.csv'
trainvaltest = filter(filename)

' Split data '
num_sample = len(trainvaltest)
traintest_mark = int((1-test_ratio-unseen_ratio)*num_sample)
testunseen_mark = int((1-unseen_ratio)*num_sample)

train = trainvaltest[:traintest_mark]
test = trainvaltest[traintest_mark:testunseen_mark]
unseen = trainvaltest[testunseen_mark:]

'Write to csv'
write_csv('Data/train_cleaned.csv', train)
write_csv('Data/test_cleaned.csv', test)
write_csv('Data/unseen_cleaned.csv', unseen)


