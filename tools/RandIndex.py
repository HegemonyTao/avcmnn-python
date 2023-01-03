from tools.utils import *
def Contingency(Mem1,Mem2):
    Cont=np.zeros(shape=(int(max(Mem1)),int(max(Mem2))))
    for i in range(len(Mem1)):
        Cont[int(Mem1[i])-1,int(Mem2[i])-1]=Cont[int(Mem1[i])-1,int(Mem2[i])-1]+1
    return Cont
def RandIndex(c1,c2):
    C=Contingency(c1,c2)
    n=sum(sum(C))
    nis=sum(np.sum(C,axis=0)**2)
    njs=sum(np.sum(C,axis=1)**2)
    t1=nchoosek(n,2)
    t2=sum(sum(C**2))
    t3=0.5*(nis+njs)
    nc = (n * (n ** 2 + 1) - (n + 1) * nis - (n + 1) * njs + 2 * (nis * njs) / n) / (2 * (n - 1))
    A=t1+t2-t3
    D=-t2+t3
    if t1==nc:
        AR=0
    else:
        AR=(A-nc)/(t1-nc)
    RI=A/t1
    MI=D/t1
    HI=(A-D)/t1
    return AR,RI,MI,HI