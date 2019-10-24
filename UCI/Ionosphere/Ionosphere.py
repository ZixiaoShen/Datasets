import pandas as pd
import numpy as np
import io
import requests

file_url = "https://raw.githubusercontent.com/ZixiaoShen/Datasets/master/UCI/Ionosphere/ionosphere.data"
s = requests.get(file_url).content
df = pd.read_csv(io.StringIO(s.decode('utf-8')), header=None)

X = df.drop(columns=34)
Y = df[34]

class_mapping = {'g': 1, 'b': 0}
y = Y.map(class_mapping)

x = np.array(X)
y = np.array(y)

n_samples, num_F = x.shape
