from sklearn.cluster import KMeans
from model.nmi import nmi
from model.VCMNN import *
from model.RandIndex import RandIndex
def AVCMNN(data,label,kstart,kend):
    label = np.array(flatten(label))
    N=data.shape[0]
    relation=np.zeros(shape=(N,N))
    for k in range(2,51):
        model=KMeans(n_clusters=k)
        model.fit(data)
        idx=model.predict(data)
        for i in range(N):
            for j in range(i+1,N):
                if idx[i]==idx[j]:
                    relation[i,j]=relation[i,j]+1
    list=np.zeros(shape=(N,5))
    listval=np.zeros(shape=(N,3))
    for i in range(N):
        valu,loc=newSort(relation[i,:],axis=0,reverse=True)
        list[i,:]=loc[:5]
        listval[i,:]=valu[:3]
    firstcol=np.array([[i for i in range(N)]])
    coocurrence=np.concatenate([firstcol.T,list],axis=1)
    co=coocurrence[:,:2]
    dele=[]
    for i in range(len(listval)):
        if listval[i,1]<20:
            dele.append(i)
    co=np.delete(co,dele,axis=0)
    co2=[]
    for i in range(len(co)):
        co2.append(co[i,:])
    co2=np.array(co2)
    for i in range(10000):
        delrec=[]
        for i in range(co2.shape[1]):
            for j in range(i+1,co2.shape[1]):
                if len(intersect(co2[i],co2[j]))>=1:
                    co2[i]=unique(np.concatenate([co2[i],co2[j]],axis=0))
                    co2=np.delete(co2,[j],axis=0)
                    delrec=delrec.append(j)
        if len(delrec)==0:
            break
        co2=np.delete(co2,delrec,axis=0)
    co2id=np.zeros(shape=(max(N,max(list[:,0])),))
    for k in range(len(co2)):
        for j in range(len(co2[k])):
            co2id[int(co2[k,j])]=k
    co2id[find(co2id,0)]=co2id[[int(item) for item in list[find(co2id,0),1]]]
    differentcenter=np.zeros(shape=(22,))
    differentcenterari=np.zeros(shape=(22,))
    NMI=[]
    NMIself=[]
    AR1=[]
    AR2=[]
    totalcorrect=[]
    for center in range(2,21):
        for k in range(kstart,kend+1):
            idx=VCMNN(data,k,center)
            finalidx=idx
            correct=[]
            for i in range(len(idx)):
                for j in range(len(co2)):
                    if find(co2[j],i)!=[]:
                        ta=tabulate(finalidx[[int(item) for item in co2[j]]])
                        ma,mb=newMax(ta[:,1])
                        finalidx[i]=ta[mb,0]
                        if finalidx[i]!=idx[i]:
                            correct.append(i)
                        break
            co2id=co2id+np.ones(shape=(co2id.shape[0],))
            NMI.append(nmi(label,idx))
            NMIself.append(nmi(co2id,idx))
            AR,RI,MI,HI=RandIndex(label,idx)
            AR1.append(AR)
            AR, RI, MI, HI = RandIndex(co2id, idx)
            AR2.append(AR)
            totalcorrect.append(len(correct))
        vacorr,loccorr=newSort(np.array(totalcorrect),axis=0)
        mini=find(vacorr<=np.mean(vacorr),True)
        a,b=newMax(np.array(NMIself)[loccorr[mini]])
        differentcenter[center]=NMI[loccorr[b]]
        differentcenterari[center]=AR1[loccorr[b]]
    fiannnmiindex = a
    finalnmi = max(differentcenter)
    finalari = max(differentcenterari)
    return fiannnmiindex,finalnmi,finalari