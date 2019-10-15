import pandas as pd
import numpy as np
import io
import requests

file_url = "https://raw.githubusercontent.com/ZixiaoShen/Datasets/master/UCI/Dermatology/dermatology.data"

s = requests.get(file_url).content
df = pd.read_csv(io.StringIO(s.decode('utf-8')), header=None)

data = df.replace(to_replace="?", value=np.nan)
data = data.dropna(how='any')
dermatology = data.values
dermatology = dermatology.astype('int')

X = dermatology[:, 0:34]
X = X.astype('float')
Y = dermatology[:, 34].astype('int')
n_samples, n_features = X.shape
