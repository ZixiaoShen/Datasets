import numpy as np
import pandas as pd

DATA_PATH = "http://archive.ics.uci.edu/ml/machine-learning-databases/" \
            "breast-cancer-wisconsin/breast-cancer-wisconsin.data"

data = pd.read_csv(DATA_PATH)
data = data.replace(to_replace="?", value=np.nan)
data = data.dropna(how='any')

wbc = data.values
wbc = wbc.astype(int)
X = wbc[:, 1:10]
Y = wbc[:, 10]
Y = Y - 3
n_samples, num_F = X.shape
