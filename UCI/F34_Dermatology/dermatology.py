import pandas as pd
import numpy as np
import io
import requests


def dermatology():
    file_url = "https://raw.githubusercontent.com/ZixiaoShen/Datasets/master/UCI/Dermatology/dermatology.data"
    s = requests.get(file_url).content
    df = pd.read_csv(io.StringIO(s.decode('utf-8')), header=None)

    data = df.replace(to_replace="?", value=np.nan)
    data = data.dropna(how='any')
    dermatology = data.values
    # dermatology = dermatology.astype('int')

    x = dermatology[:, 0:34]
    x = x.astype(int)
    y = dermatology[:, 34].astype(int)
    return x, y


if __name__ == '__main__':
    X, Y = dermatology()
    n_samples, n_features = X.shape
    n_class = len(set(Y))
    print("Number of Samples:", n_samples)
    print("Number of Features:", n_features)
    print("Number of Classes:", n_class)
