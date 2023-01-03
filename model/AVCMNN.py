from sklearn.cluster import KMeans
from model.VCMNN import *
from sklearn.metrics import normalized_mutual_info_score as nmi
import warnings
warnings.filterwarnings("ignore")
def getCV(data):
    N = data.shape[0]
    relation = np.zeros(shape=(N, N))
    for k in range(2,51):
        model=KMeans(n_clusters=k)
        model.fit(data)
        idx = model.predict(data)
        for i in range(N):
            for j in range(i+1,N):
                if idx[i]==idx[j]:
                    relation[i,j]=relation[i,j]+1
    list = np.zeros(shape=(N, N))
    listval = np.zeros(shape=(N, N))
    for i in range(N):
        valu, loc = newSort(relation[i, :], axis=0, reverse=True)
        list[i, :] = loc
        listval[i, :] = valu
    firstcol = [[i for i in range(N)]]
    firstcol.append(list[:,0].tolist())
    firstcol.append(listval[:,0].tolist())
    co=np.array(firstcol).T
    return co,list
def cleanCO(co):
    dele = []
    for i in range(len(co)):
        if co[i, 2] < 25:
            dele.append(int(co[i,1]))
            dele.append(i)
    dele=unique(np.array(dele)).tolist()
    co = np.delete(co, dele, axis=0)
    return co
def AVCMNN(data):
    co,list=getCV(data)
    co=cleanCO(co)
    length=len(co)
    B=0
    BList=[]
    #get initial clusters B
    for i in range(length):
        for j in range(i+1,length):
            if len(intersect(co[i,:2],co[j,:2]))>=1:
                unionList=union(co[i,:2],co[j,:2])
                BList.append(unionList)
                B+=1
    deleList=[]
    #merge B
    for i in range(100):
        flag=True
        for j in range(B):
            if j in deleList:
                continue
            for k in range(j+1,B):
                if k in deleList:
                    continue
                if len(intersect(BList[j],BList[k]))>=1:
                    BList[j]=union(BList[j],BList[k])
                    deleList.append(k)
                    flag=False
        if flag:
            break
    #get pseudo labels
    idx=np.zeros(shape=len(data))-1
    for i in range(B):
        if i not in deleList:
            for index in BList[i]:
                idx[int(index)]=i
    deleItem=find(idx,-1)
    idx=np.array(idx)
    for item in deleItem:
        for neighbors in list[item]:
            if int(neighbors)==item or idx[int(neighbors)]==-1:
                continue
            idx[item]=idx[int(neighbors)]
            break
    pseudoIdx=idx+np.ones(shape=(idx.shape[0],))
    pseudoLabels=unique(pseudoIdx)
    NMI=[]
    c = []
    idxList=[]
    parameters=[]
    for num in range(2,21):
        for k in range(2,91):
            idx=VCMNN(data,k,num)
            idxList.append(idx)
            wrong = 0
            for label in pseudoLabels:
                Bi=find(pseudoIdx,label)
                for point in Bi:
                    neighbors=idx[[item for item in Bi if item!=point]]
                    counts,index=newMax(histcNoGraph(neighbors,unique(neighbors)))
                    if unique(neighbors)[index]!=idx[point]:
                        wrong+=1
            nowNMI=nmi(pseudoIdx,idx)
            print('num={},k={},nmi={}'.format(num,k,nowNMI))
            parameters.append([num,k])
            c.append(wrong)
            NMI.append(nowNMI)
        vacorr,loccorr=newSort(np.array(c),axis=0)
        mini=find(vacorr<=np.mean(vacorr),True)
        a,b=newMax(np.array(NMI)[loccorr[mini]])
        maxidx=idxList[loccorr[b]]
        maxParameters=parameters[loccorr[b]]
    return maxidx,maxParameters