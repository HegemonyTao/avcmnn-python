import os
import scipy
NOWFILEPATH=os.path.dirname(__file__)
def loadDataSet(filename):
    filename=NOWFILEPATH+'\\'+filename
    data=scipy.io.loadmat(filename)
    return data['data'],data['label']
def loadBalance():
    return loadDataSet('balance.mat')
def loadBanknote():
    return loadDataSet('banknote.mat')
def loadEcoli():
    return loadDataSet('ecoli.mat')
def loadGalss():
    return loadDataSet('glass.mat')
def loadHeart():
    return loadDataSet('heart.mat')
def loadIris():
    return loadDataSet('iris.mat')
def loadMovementLibras():
    return loadDataSet('movement_libras.mat')
def loadSeeds():
    return loadDataSet('seeds.mat')
def loadSonar():
    return loadDataSet('sonar.mat')
def loadYeast():
    return loadDataSet('Yeast.mat')
