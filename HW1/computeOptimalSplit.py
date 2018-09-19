#!/usr/bin/python

import csv
import math

def buildOptimalTree(xfile, yfile):
    tree = decisionnode(nodes)
    nodes = readNodesFromCSV(xfile, yfile)
    return tree

def readNodesFromCSV(xfile, yfile)
    xlines = opencsvfile(xfile)
    ylines = opencsvfile(yfile)

    nodes = []
    for i in range(len(xlines)):
        nodes += [datanode(xlines[i], ylines[i][0])]

    return nodes

def computeOptimalSplit(nodes):

    originalentropy = entropyOfNodes(nodes)
    print ("DEBUG: entropy of nodes: ", originalentropy)
    print ("DEBUG: nodes: ", list(map( lambda x: x.result, nodes)))

    nodes.sort( key = lambda x: x.averages[0] )

    minentropy = 1
    bestfeature = 0
    bestthreshold = 0
    #Feature vector has 10 characteristics
    for characteristic in range(10):
        nodes.sort( key = lambda x: x.averages[characteristic] )
#        print ("DEBUG: all nodes char:", list(map( lambda x: x.averages[characteristic], nodes)))
        #Get all possible threshold splits for the feature
        (threshold, entropy, numnode) = findThreshold(nodes, characteristic)
        print ("INFO:\t gain of splitting against feature:", characteristic, "is: ", originalentropy - entropy, "with threshold:", threshold, " node: ", numnode)

        if (entropy < minentropy):
            minentropy = entropy
            bestfeature = characteristic
            bestthreshold = threshold
    
    print ("INFO: Returning split feature:", bestfeature, "on threshold:", bestthreshold, "gain:", originalentropy - minentropy)
    return (bestfeature, bestthreshold)
        
#Finds threshold for a sorted list of nodes, given characteristic
def findThreshold(nodes, characteristic):
    minentropy = 1
    minthreshold = 0
    numnode = 0
    for i, node in enumerate (nodes[1:]):
        totalnodes = len(nodes)
        lastfeaturevalue = nodes[i].averages[characteristic] 
        featurevalue = node.averages[characteristic] 
#        print ("DEBUG: lastfeaturevalue:", lastfeaturevalue, " featurevalue: ", featurevalue)

        #Look for min entropy
        if (lastfeaturevalue != featurevalue):
            threshold = (lastfeaturevalue + featurevalue)/2
            entropy = entropyOfNodes(nodes[:i+1])*i/totalnodes + entropyOfNodes(nodes[i+1:]) * (totalnodes - (i+1))/totalnodes
#            print ("DEBUG:\t\t char:", characteristic, "threshold:", threshold, "entropy:", entropy)
            if (entropy < minentropy):
                minthreshold = threshold
                minentropy = entropy
                numnode = i
    return (minthreshold, minentropy, numnode)

#Computes entropy of a list of nodes
def entropyOfNodes(nodelist):
    numtrue = len( list( filter( ( lambda x: (x.result == 1) ), nodelist )))
    numfalse = len( list( filter( ( lambda x: (x.result == 0) ), nodelist )))
    return computeEntropy(numtrue, numfalse)
            
#Computes entropy of True/False selection
# Arguments - number of true elements, number of false elements
def computeEntropy(numtrue, numfalse):
#    print ("DEBUG: numtrue:",numtrue, "numfalse", numfalse)
    total = numtrue + numfalse
    if (numtrue != 0) and (numfalse != 0):
        return -((numtrue/total)*math.log2(numtrue/total) + \
               (numfalse/total)*math.log2(numfalse/total))
    else:
        return 0

#Open file and return it as a list of lists (row,colums)
def opencsvfile(filename):
    with open(filename) as csvfile:
        csvreader = csv.reader(csvfile)    
        return list(csvreader)

def validatetree(tree, xfile, yfile):
    nodes = readNodesFromCSV(xfile, yfile)
    for node in nodes:
        decision = predictFromNode(node, tree)

class datanode:
    def __init__(self, featattr, result):
        featattr = list(map(lambda x: float(x), featattr))
        self.averages = featattr[0:10]
        self.stdevs = featattr[10:20]
        self.maxattrs = featattr[20:30]
        self.result = int(result)

class decisionnode:
    def __init__(self, nodes):
        self.feature, self.threshold = computeOptimalSplit(nodes)
        firsthalf  = list( filter(lambda x: x.averages[self.feature] < self.threshold, nodes))
        secondhalf = list( filter(lambda x: x.averages[self.feature] >= self.threshold, nodes))
        (self.truenode, self.falsenode) = (None, None)

        #Leaf node if all data has same value
        if (firsthalf == [] or secondhalf == []):
            self.nodes = nodes
        else:
            #Find which child node is more true
            firsthalfpercenttrue = sum( list( map(lambda x: x.result, firsthalf ) ) ) / len(firsthalf)
            secondhalfpercenttrue = sum( list( map(lambda x: x.result, secondhalf ) ) ) / len(secondhalf)
    
            if firsthalfpercenttrue > secondhalfpercenttrue:
                self.falsenode = decisionnode(secondhalf)
                self.truenode = decisionnode(firsthalf)
            else:
                self.truenode = decisionnode(secondhalf)
                self.falsenode = decisionnode(firsthalf)

    def predictFromDataNode(self, datanode):
        if (self.nodes != []):
            if (datanode.averages[self.feature] > self.threshold):
                self.lessnode.predictFromDataNode(datanode)
            else:
                self.morenode.predictFromDataNode(datanode)
        else:
            prediction = 


#print("Entropy: ", computeEntropy(3,4))
buildOptimalTree("testX.csv", "testY.csv")

