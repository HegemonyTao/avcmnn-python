# VCMNN and adaptive VCMNN (i.e., AVCMNN) algorithms implemented in python

This project is implemented in python version of [An adaptive mutual K-nearest neighbors clustering algorithm based on maximizing mutual information]((https://www.sciencedirect.com/science/article/pii/S003132032200752X)) , and [the original project](https://github.com/mlyizhang/avcmnn) is implemented in matlab.

## Install

The code is written in python, you can access it as follows:

```
git clone https://github.com/HegemonyTao/avcmnn-python.git
cd avcmnn-python
python -m pip install --user -r requirements.txt
```

## Usage

You can directly run the main function in the root directory to obtain the Adjusted Rand Index (ARI) and Normalized Mutual Information (NMI) of VCMNN and AVCMNN algorithms on the iris dataset. Note that the AVCMNN algorithm may run slowly

```python
cd avcmnn-python
python main.py
```

Alternatively, you can use it in the root directory by following the steps below:

### Import package and database

```python
from model.RandIndex import RandIndex
from database import Database
from model.VCMNN import VCMNN
from model.AVCMNN import AVCMNN
from model.nmi import nmi
from tools.utils import *
X,y=Database.loadIris()
```

### Clustering with VCMNN

```python
k,num=25,3#Recommended value, can be set by yourself
secidx=VCMNN(X,k,num)
#Calculate ARI and NMI
AR,RI,MI,HI=RandIndex(np.array(secidx),np.array(flatten(y)))
NMI=nmi(np.array(secidx),np.array(flatten(y)))
print('VCMNN result(k={0},num={1}): ARI={2:.4f}\tNMI={3:.4f}'.format(k,num,AR,NMI))
```

### Clustering with AVCMNN

```python
kstart,kend=20,50 #Recommended value, can be set by yourself
fiannnmiindex,finalnmi,finalari=AVCMNN(X,y,kstart,kend)
print('AVCMNN result(kstart={0},kend={1}): ARI={2:.4f}\tNMI={3:.4f}'.format(kstart,kend,finalari,finalnmi))
```

### Recommended parameters for different data sets

| Datasets         | k    | num  |
| ---------------- | ---- | ---- |
| iris             | 25   | 3    |
| ecoli            | 110  | 8    |
| sonar            | 32   | 2    |
| seeds            | 21   | 3    |
| libras movements | 19   | 15   |
| banknote         | 50   | 2    |
| heart            | 31   | 2    |
| yeast            | 50   | 8    |
| wpbc             | 6    | 2    |
| glass            | 69   | 6    |





