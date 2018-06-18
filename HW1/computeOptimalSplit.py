#!/usr/bin/python

import csv
import math

def computeOptimalSplit(xfile, yfile):
    xlines = opencsvfile(xfile)
    ylines = opencsvfile(yfile)

    nodes = []
    for i in range(len(xlines)):
        nodes += [datanode(xlines[i], ylines[i])]

    entropyOfNodes(nodes)

def entropyOfNodes(nodelist):
    numtrue = reduce( lambda x: x.result == 1, nodelist )
    numfalse = reduce( lambda x: x.result == 0, nodelist )
    return computeEntropy(numtrue, numfalse)
            
#Computes entropy of True/False selection
# Arguments - number of true elements, number of false elements
def computeEntropy(numtrue, numfalse):
    total = numtrue + numfalse
    return -((numtrue/total)*math.log2(numtrue/total) + \
           (numfalse/total)*math.log2(numfalse/total))

#Open file and return it as a list of lists (row,colums)
def opencsvfile(filename):
    with open(filename) as csvfile:
        csvreader = csv.reader(csvfile)    
        return list(csvreader)


class datanode:
    def __init__(self, featattr, result):
        self.averages = featattr.split(",")[0:9]
        self.stdevs = featattr.split(",")[10:19]
        self.maxattrs = featattr.split(",")[20:29]
        self.result = int(result)


#print("Entropy: ", computeEntropy(3,4))
computeOptimalSplit("testX.csv", "testY.csv")

