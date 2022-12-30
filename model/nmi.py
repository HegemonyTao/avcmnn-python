from tools.utils import *
eps=2.2204e-16
def nmi(A,B):
    if len(A)!=len(B):
        raise Exception('length( A ) must == length( B)')
    total=len(A)
    A_ids=unique(A)
    A_class=len(A_ids)
    B_ids=unique(B)
    B_class=len(B_ids)
    idAOccur=np.array(np.tile(np.array([A]),(A_class,1))==np.tile(np.array([A_ids]).T,(1,total)))+0
    idBOccur=np.array(np.tile(np.array([B]),(B_class,1))==np.tile(np.array([B_ids]).T,(1,total)))+0
    idABOccur=np.dot(idAOccur,idBOccur.T)
    Px=np.sum(idAOccur,axis=1)/total
    Py=np.sum(idBOccur,axis=1)/total
    Pxy=idABOccur/total
    MImatrix=Pxy*np.log2((Pxy/np.dot(np.array([Px]).T,np.array([Py])))+eps)
    MI=sum(sum(MImatrix))
    Hx=-sum(Px*np.log2(Px+eps))
    Hy=-sum(Py*np.log2(Py+eps))
    MIhat=2*MI/(Hx+Hy)
    return MIhat
