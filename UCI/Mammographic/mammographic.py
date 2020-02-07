import pandas as pd
import io
import requests
import numpy as np


def mammographic():
    file_url = "https://raw.githubusercontent.com/ZixiaoShen/Datasets/master/UCI/" \
                "Mammographic/mammographic.csv"
    s = requests.get(file_url).content
    df = pd.read_csv(io.StringIO(s.decode('utf-8')), header=None)

    data = df.replace(to_replace="?", value=np.nan)
    data = data.dropna(how='any')
    array = data.values.astype(float)
    x = array[:, 0:5]
    y = array[:, 5].astype(int)
    return x, y


if __name__ == '__main__':
    X, Y = mammographic()
    n_samples, n_features = X.shape
    n_class = len(set(Y))
    print("Number of Samples:", n_samples)
    print("Number of Features:", n_features)
    print("Number of Classes:", n_class)
