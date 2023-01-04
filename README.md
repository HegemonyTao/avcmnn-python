# VCMNN and adaptive VCMNN (i.e., AVCMNN) algorithms implemented in python

This project is implemented in python version of [An adaptive mutual K-nearest neighbors clustering algorithm based on maximizing mutual information](https://www.sciencedirect.com/science/article/pii/S003132032200752X) .

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
from model.VCMNN import VCMNN
from model.AVCMNN import AVCMNN
from tools.RandIndex import RandIndex
from database import Database
from tools.utils import *
from sklearn.metrics import normalized_mutual_info_score as nmi
X,y=Database.loadIris()
y=flatten(y)
```

### Clustering with VCMNN

```python
vcmnnIdx=VCMNN(X,25,3)#Recommended value, can be set by yourself
AR1, RI1, MI1, HI1=RandIndex(vcmnnIdx,y)
#Calculate ARI and NMI
NMI1=nmi(vcmnnIdx,y)
print('VCMNN result:ARI={},NMI={}'.format(AR1,NMI1))
```

### Clustering with AVCMNN

```python
avcmnIdx,parameters=AVCMNN(X)
AR2, RI2, MI2, HI2=RandIndex(avcmnIdx,y)
NMI2=nmi(avcmnIdx,y)
print('AVCMNN result:ARI={},NMI={}'.format(AR2,NMI2))
```

### Recommended parameters for different data sets

| Datasets | k    | num  |
| -------- | ---- | ---- |
| Iris     | 25   | 3    |
| Heart    | 31   | 2    |
| Glass    | 69   | 6    |
| Sonar    | 32   | 2    |

## Comparison with the algorithm performance in the paper

<table>
   <tr>
      <td>Datasets</td>
      <td>KPI</td>
      <td>VCMNN（paper）</td>
      <td>AVCMNN（paper）</td>
      <td>VCMNN（exp）</td>
      <td>AVCMNN（exp）</td>
   </tr>
   <tr>
      <td>Iris</td>
      <td>ARI</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>0.9609</td>
   </tr>
   <tr>
      <td></td>
      <td>NMI</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>0.953</td>
   </tr>
   <tr>
      <td>Heart</td>
      <td>ARI</td>
      <td>0.3085</td>
      <td>0.1723</td>
      <td>0.5899</td>
      <td>0.2739</td>
   </tr>
   <tr>
      <td></td>
      <td>NMI</td>
      <td>0.2661</td>
      <td>0.2515</td>
      <td>0.4866</td>
      <td>0.2563</td>
   </tr>
   <tr>
      <td>Glass</td>
      <td>ARI</td>
      <td>0.6757</td>
      <td>0.3477</td>
      <td>0.6882</td>
      <td>0.2414</td>
   </tr>
   <tr>
      <td></td>
      <td>NMI</td>
      <td>0.7587</td>
      <td>0.5998</td>
      <td>0.7636</td>
      <td>0.4131</td>
   </tr>
   <tr>
      <td>Sonar</td>
      <td>ARI</td>
      <td>0.3186</td>
      <td>0.2876</td>
      <td>0.297</td>
      <td>0.0084</td>
   </tr>
   <tr>
      <td></td>
      <td>NMI</td>
      <td>0.3732</td>
      <td>0.3705</td>
      <td>0.32493</td>
      <td>0.015</td>
   </tr>
</table>



