import pandas as pd
import numpy as np
import io
import requests

file_url = "https://raw.githubusercontent.com/ZixiaoShen/Datasets/master/UCI/Glass/glass.data"

s = requests.get(file_url).content
df = pd.read_csv(io.StringIO(s.decode('utf-8')), header=None)

df = df.drop(columns=0)
X = df.drop(columns=10)
Y = df[10]

x = np.array(X)
y = np.array(Y)

n_samples, num_F = x.shape
