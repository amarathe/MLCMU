#!/usr/bin/python

import csv

def computeOptimalSplit(attr, thresh):
    with open('testX.csv') as csvfile:
        csvreader = csv.reader(csvfile)    
        csvlist = list(csvreader)
        print ("Row 1, Col 2: ", csvlist[1][2])   
        print ("Row 3, Col 4: ", csvlist[3][4])   

computeOptimalSplit("","")
