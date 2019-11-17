import pandas as pd
import numpy as np
import io
import requests


def parkinsons():
    file_url = "https://raw.githubusercontent.com/ZixiaoShen/Datasets/master/UCI/Parkinsons/parkinsons.csv"
    s = requests.get(file_url).content
    df = pd.read_csv(io.StringIO(s.decode('utf-8')), header=None)

    data = df.values
    parkinson = data[1:, 1:]
    parkinson = parkinson.astype('float')
    x1 = parkinson[:, 0:16]
    x2 = parkinson[:, 17:]
    x = np.hstack((x1, x2)).astype('float')
    y = parkinson[:, 16].astype('int')
    return x, y


if __name__ == '__main__':
    X, Y = parkinsons()
    n_samples, n_features = X.shape
    print(n_samples)
    print(n_features)