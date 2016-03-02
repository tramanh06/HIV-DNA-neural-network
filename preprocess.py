__author__ = 'TramAnh'

import csv

with open('trainval.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter="\t")
    for row in reader:


