import pandas as pd
import numpy as np
import io
import requests

file_url = "https://raw.githubusercontent.com/ZixiaoShen/Datasets/master/UCI/Dermatology/dermatology.csv"

# s = requests.get(file_url).content
df = pd.read_csv(file_url, header=None)

data = df.values
data = data.replace(to_replace="?", value=np.nan)
data = data.dropna(how='any')
dermatology = data.values

X = dermatology[:, 0:34]
X = X.astype('float')
Y = dermatology[:, 34].astype('int')
n_samples, n_features = X.shape
