from model.VCMNN import VCMNN
from model.AVCMNN import AVCMNN
from tools.RandIndex import RandIndex
from database import Database
from tools.utils import *
from sklearn.metrics import normalized_mutual_info_score as nmi
if __name__=='__main__':
    X,y=Database.loadIris()
    y=flatten(y)
    vcmnnIdx=VCMNN(X,25,3)
    AR1, RI1, MI1, HI1=RandIndex(vcmnnIdx,y)
    NMI1=nmi(vcmnnIdx,y)
    avcmnIdx,parameters=AVCMNN(X)
    AR2, RI2, MI2, HI2=RandIndex(avcmnIdx,y)
    NMI2=nmi(avcmnIdx,y)
    print('VCMNN result:ARI={},NMI={}'.format(AR1,NMI1))
    print('AVCMNN result:ARI={},NMI={}'.format(AR2,NMI2))