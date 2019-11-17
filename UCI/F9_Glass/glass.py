import pandas as pd
import numpy as np
import io
import requests


def glass():
    file_url = "https://raw.githubusercontent.com/ZixiaoShen/Datasets/master/UCI/Glass/glass.data"

    s = requests.get(file_url).content
    df = pd.read_csv(io.StringIO(s.decode('utf-8')), header=None)

    df = df.drop(columns=0)
    x_df = df.drop(columns=10)
    y_df = df[10]

    x = np.array(x_df)
    y = np.array(y_df)
    return x, y


if __name__ == '__main__':
    X, Y = glass()
    n_samples, n_features = X.shape
    print(n_samples)
    print(n_features)
