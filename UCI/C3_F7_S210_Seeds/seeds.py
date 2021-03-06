import pandas as pd
import io
import requests


def seeds():
    file_url = "https://raw.githubusercontent.com/ZixiaoShen/Datasets/master/UCI/" \
               "C3_F7_S210_Seeds/seeds.csv"
    s = requests.get(file_url).content
    df = pd.read_csv(io.StringIO(s.decode('utf-8')), header=None)

    data = df.values
    x = data[:, 0:7]
    x = x.astype('float')
    y = data[:, 7].astype('int')
    return x, y


if __name__ == '__main__':
    X, Y = seeds()
    n_samples, n_features = X.shape
    n_class = len(set(Y))
    print("Number of Samples:", n_samples)
    print("Number of Features:", n_features)
    print("Number of Classes:", n_class)
