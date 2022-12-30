from tools.utils import *
from scipy.spatial.distance import pdist
from scipy.spatial.distance import squareform
def VCMNN(data,k,num):
    #caculate distance
    D=pdist(data)
    Simi=squareform(D)
    for i in range(Simi.shape[0]):
        Simi[i,i]=math.inf
    sdismat,index=newSort(Simi,axis=1)
    index=index[:,:k]
    ag=np.zeros(shape=(index.shape[0],index.shape[0]))
    for i in range(1,index.shape[0]):
        for j in range(i+1,index.shape[0]):
            if find(index[j,:],i)!=[] and find(index[i,:],j)!=[]:
                ag[i,j]=1
    one=-1
    idx=np.zeros((len(data),))
    for i in range(ag.shape[0]):
        for j in range(ag.shape[1]):
            if ag[i,j]==1:
                if idx[i]==0:
                    one=one+1
                idx[i]=one
                idx[j]=idx[i]
    idx=idx.T
    secidx=idx
    uidx=unique(idx)
    numIdx=np.zeros((len(uidx),))
    for i in range(len(uidx)):
        numIdx[i]=len(find(idx,uidx[i]))
    value,index2=newSort(numIdx,axis=0,reverse=True)
    # minority groups
    microidx2=index2[num:]
    for i in range(len(microidx2)):
        arowList=find(secidx,microidx2[i])
        if arowList==[]:
            continue
        a=secidx[unique(index[arowList,:k])]
        a=np.delete(a,find(a,microidx2[i]),axis=0)
        if a==[]:
            continue
        uniqea=unique(a)
        cc=histcNoGraph(a,unique(a))
        if len(cc)==0:
            continue
        max_num,max_index=newMax(cc)
        secidx[find(secidx,microidx2[i])]=uniqea[max_index]
    secidx=secidx+np.ones(shape=(len(secidx),))
    return secidx
