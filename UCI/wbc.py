import numpy as np
import pandas as pd

DATA_PATH = "http://archive.ics.uci.edu/ml/machine-learning-databases/" \
            "breast-cancer-wisconsin/breast-cancer-wisconsin.data"

# create the column names
columnNames = [
    'Sample code number',
    'Clump Thickness',
    'Uniformity of Cell Size',
    'Uniformity of Cell Shape',
    'Marginal Adhesion',
    'Single Epithelial Cell Size',
    'Bare Nuclei',
    'Bland Chromatin',
    'Normal Nucleoli',
    'Mitoses',
    'Class'
]

data = pd.read_csv(DATA_PATH, names=columnNames)

# use standard missing value to replace "?"
data = data.replace(to_replace="?", value=np.nan)
# then drop the missing value
data = data.dropna(how='any')

wbc = data.values
wbc = np.array(wbc)
wbc = wbc.astype(int)
# wbc = wbc[:, 1:11]
x = wbc[:, 1:10]
y = wbc[:, 10]
y = y - 3
