import pandas as pd
import numpy as np

file_path = '/Users/shenzixiao/Dropbox/DATA/UCI/Dermatology/dermatology.data'
data = pd.read_csv(file_path, header=None)

data = data.replace(to_replace="?", value=np.nan)
data = data.dropna(how='any')
dermatology = data.values

X = dermatology[:, 0:34]
X = X.astype('float')
Y = dermatology[:, 34].astype('int')
n_samples, num_F = X.shape
