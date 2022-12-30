from model.RandIndex import RandIndex
from database import Database
from model.VCMNN import VCMNN
from model.AVCMNN import AVCMNN
from model.nmi import nmi
from tools.utils import *
import warnings
warnings.filterwarnings("ignore")
X,y=Database.loadIris()
k,num=25,3
kstart,kend=20,50
secidx=VCMNN(X,k,num)
AR,RI,MI,HI=RandIndex(np.array(secidx),np.array(flatten(y)))
NMI=nmi(np.array(secidx),np.array(flatten(y)))
print('VCMNN result(k={0},num={1}): ARI={2:.4f}\tNMI={3:.4f}'.format(k,num,AR,NMI))
fiannnmiindex,finalnmi,finalari=AVCMNN(X,y,kstart,kend)
print('AVCMNN result(kstart={0},kend={1}): ARI={2:.4f}\tNMI={3:.4f}'.format(kstart,kend,finalari,finalnmi))