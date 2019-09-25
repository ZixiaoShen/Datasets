import pandas as pd
import numpy as np

file_path = '/Users/shenzixiao/Dropbox/DATA/UCI/Arrhythmia/arrhythmia.data'
# file_path = 'D:/CloudFiles/Dropbox/DATA/UCI/Arrhythmia/arrhythmia.data'

df = pd.read_csv(file_path, header=None)

df = df.replace(to_replace="?", value=np.nan)
df = df.dropna(how='any')

data = np.array(df).astype('float')

X = data[:, 0:279]
Y = data[:, 279].astype('int')
n_samples, num_F = X.shape

