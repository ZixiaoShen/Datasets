import pandas as pd
import io
import requests


def musk():
    file_url = "https://raw.githubusercontent.com/ZixiaoShen/Datasets/master/UCI/" \
               "Musk/clean1.csv"
    s = requests.get(file_url).content
    df = pd.read_csv(io.StringIO(s.decode('utf-8')), header=None)

    x_df = df.iloc[:, 2:-1]
    y_df = df.iloc[:, -1]

    x = x_df.values
    y = y_df.values
    return x, y


if __name__ == '__main__':
    X, Y = musk()
    n_samples, n_features = X.shape
    n_class = len(set(Y))
    print("Number of Samples:", n_samples)
    print("Number of Features:", n_features)
    print("Number of Classes:", n_class)
