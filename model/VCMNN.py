from tools.utils import *
from scipy.spatial.distance import pdist
from scipy.spatial.distance import squareform
from database.Database import *
def kCMNN(data,k):
    D = pdist(data)
    Simi = squareform(D)
    for i in range(Simi.shape[0]):
        Simi[i, i] = math.inf
    sdismat, index = newSort(Simi, axis=1)
    index=index[:,:k]
    ag=np.zeros(shape=(index.shape[0],index.shape[0]))
    for i in range(1,index.shape[0]):
        for j in range(i+1,index.shape[0]):
            #Judge whether point_i and point_j are mutual k-nearest neighbors
            if find(index[j,:],i)!=[] and find(index[i,:],j)!=[]:
                ag[i,j]=1
    one = 0
    # Classify data that are k-nearest neighbors
    idx = np.zeros((len(data),))
    for i in range(ag.shape[0]):
        for j in range(ag.shape[1]):
            if ag[i, j] == 1:
                if idx[i] == 0:
                    one = one + 1
                idx[i] = one
                idx[j] = idx[i]
    return index,idx
def VCMNN(data,k,num):
    index,idx=kCMNN(data,k)
    secidx=idx
    #Count the number of different categories and sort them
    uidx=unique(idx)
    numIdx=np.zeros((len(uidx),))
    for i in range(len(uidx)):
        numIdx[i]=len(find(idx,uidx[i]))
    value,index2=newSort(numIdx,axis=0,reverse=True)
    # minority groups
    microidx2=index2[num:]
    for i in range(len(microidx2)):
        arowList=find(secidx,microidx2[i])
        # K-nearest neighbor of all data points
        kNeighbors = index[arowList, :k]
        a=secidx[unique(kNeighbors)]
        a=np.delete(a,find(a,microidx2[i]),axis=0)
        if len(a)==0:
            result=index2[0]
        else:
            uniqea = unique(a)
            cc = histcNoGraph(a, uniqea)
            max_num, max_index = newMax(cc)
            result=uniqea[max_index]
        for pj in arowList:
            kNeighbors=index[pj,:k]
            a=secidx[unique(kNeighbors)]
            a=np.delete(a,find(a,microidx2[i]),axis=0)
            #Assigned to the first nearest neighbor by default
            if len(a)==0:
                secidx[pj]=result
                continue
            uniqea=unique(a)
            cc=histcNoGraph(a,uniqea)
            max_num,max_index=newMax(cc)
            secidx[pj]=uniqea[max_index]
        '''
        #Finding k-Nearest Neighbors of All Data Points in a Group
        a=secidx[unique(index[arowList,:k])]
        #Remove the location of its own element
        a=np.delete(a,find(a,microidx2[i]),axis=0)
        if a==[]:
            continue
        #Classify all data in a group in a minority group into a majority group
        uniqea=unique(a)
        cc=histcNoGraph(a,unique(a))
        if len(cc)==0:
            continue
        max_num,max_index=newMax(cc)
        secidx[find(secidx,microidx2[i])]=uniqea[max_index]
        '''
    secidx=secidx+np.ones(shape=(len(secidx),))
    return secidx
