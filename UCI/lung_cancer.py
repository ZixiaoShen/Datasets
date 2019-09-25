import pandas as pd
import numpy as np

file_path = '/Users/shenzixiao/Dropbox/DATA/UCI/Lung Cancer/lung-cancer.data'

data = pd.read_csv(file_path, header=None)

data = data.replace(to_replace="?", value=np.nan)
data = data.dropna(how='any')

lung_cancer = data.values
X = lung_cancer[:, 1:]
Y = lung_cancer[:, 0]

X = X.astype('int')
Y = Y.astype('int')
n_samples, num_F = X.shape
