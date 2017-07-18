# -*- coding:utf-8 -*-

from numpy import *
import operator

def createDataSet():
    group = array([[1.0,1.1], [1.0,1.0], [0,0], [0,0.1]])
    labels = ['A','A','B','B']
    return group,labels

def classify0(index , dataSet , labels , k):
    dataSetSize = dataSet.shape[0]
    diffMat = tile(index, (dataSetSize,1)) - dataSet
    sqDiffMat = diffMat **2
    sqDistances = sqDiffMat.sum(axis = 1)
    distances = sqDistances ** 0.5
    sortedDistIndicies = distances.argsort()
    classCount = {}
    for i in range(k):
        votelLabel = labels[sortedDistIndicies[i]]
        classCount[votelLabel] = classCount.get(votelLabel ,0) +1
    sortedClassCount = sorted(classCount.items(),key= operator.itemgetter(1), reverse= True)
    return sortedClassCount[0][0]
