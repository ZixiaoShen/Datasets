import pandas as pd
import numpy as np
import io
import requests

file_url = "https://raw.githubusercontent.com/ZixiaoShen/Datasets/master/UCI/Parkinsons/parkinsons.csv"

s = requests.get(file_url).content
df = pd.read_csv(io.StringIO(s.decode('utf-8')), header=None)

data = df.values
parkinsons = data[1:, 1:]
parkinsons = parkinsons.astype('float')
x1 = parkinsons[:, 0:16]
x2 = parkinsons[:, 17:]
X = np.hstack((x1, x2)).astype('float')
Y = parkinsons[:, 16].astype('int')
n_samples, num_F = X.shape
