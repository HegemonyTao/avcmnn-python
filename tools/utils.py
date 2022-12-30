import math
import numpy as np
def flatten(y):
    result=[]
    for i in range(len(y)):
        for j in range(len(y[i])):
            result.append(y[i,j])
    return result
def newSort(data,axis=0,reverse=False):
    if len(data.shape)==1:
        sortedData=np.sort(data)
        if reverse:
            sortedData=sortedData.tolist()
            sortedData.sort(reverse=True)
            sortedData=np.array(sortedData)
    else:
        sortedData=np.sort(data,axis=axis)
        if reverse:
            sortedData=np.sort(-data,axis=axis)
            sortedData=-sortedData
    index=getIndex(data,sortedData,axis)
    return sortedData,index
def getIndex(oldData,newData,axis):
    indexList=[]
    if len(oldData.shape)==1:#单维数组
        for i in range(len(newData)):
            for j in range(len(oldData)):
                if newData[i]==oldData[j] and j not in indexList:
                    indexList.append(j)
                    break
        indexList=np.array(indexList)
    else:
        if axis==0:#列排序
            for i in range(len(newData[0])):
                innerIndex=[]
                for j in range(len(newData)):
                    for k in range(len(oldData)):
                        if newData[j,i]==oldData[k,i] and k not in innerIndex:
                            innerIndex.append(k)
                            break
                indexList.append(innerIndex)
            indexList=np.array(indexList)
            indexList=indexList.T
        else:
            for i in range(len(newData)):
                innerIndex=[]
                for j in range(len(newData[i])):
                    for k in range(len(oldData[i])):
                        if newData[i,j]==oldData[i,k] and k not in innerIndex:
                            innerIndex.append(k)
                            break
                indexList.append(innerIndex)
            indexList=np.array(indexList)
    return indexList
def find(array,item):
    resultIndex=[]
    for i in range(len(array)):
        if array[i]==item:
            resultIndex.append(i)
    return resultIndex
def unique(array):
    uniqueList=[]
    if len(array.shape)==1:
        for i in range(len(array)):
            if array[i] not in uniqueList:
                uniqueList.append(array[i])
    else:
        for i in range(len(array)):
            for j in range(len(array[i])):
                if array[i,j] not in uniqueList:
                    uniqueList.append(array[i,j])
    uniqueList.sort()
    return np.array(uniqueList)
def histcNoGraph(array,bins):
    result=np.zeros(shape=(len(bins),))
    for i in range(len(array)):
        for j in range(len(bins)):
            if array[i]==bins[j]:
                result[j]+=1
    return result
def newMax(array):
    maxValue=-math.inf
    maxIndex=-1
    for i in range(len(array)):
        if array[i]>maxValue:
            maxValue=array[i]
            maxIndex=i
    return maxValue,maxIndex
def intersect(array1,array2):
    result=[]
    for item1 in array1:
        for item2 in array2:
            if item1==item2 and item1 not in result:
                result.append(item1)
    return result
#only for X are positive integers
def tabulate(X):
    maxX=max(X)
    lengthX=len(X)
    resultList=[]
    def counts(X,value):
        result=0
        for item in X:
            if item==value:
                result+=1
        return result
    for i in range(1,int(maxX)+1):
        nowCounts=counts(X,i)
        resultList.append([i,nowCounts,nowCounts/lengthX])
    return np.array(resultList)
def nchoosek(n,k):
    up=1
    down=1
    for i in range(k):
        up*=n-i
        down*=(i+1)
    return up/down

