import pandas as pd
import io
import requests


def spectfheart():
    file_url = "https://raw.githubusercontent.com/ZixiaoShen/Datasets/master/UCI/F44_Spectfheart/Spectfheart.csv"
    s = requests.get(file_url).content
    df = pd.read_csv(io.StringIO(s.decode('utf-8')), header=None)

    data = df.values
    x = data[:, 1:]
    x = x.astype('int')
    y = data[:, 0].astype('int')
    return x, y


if __name__ == '__main__':
    X, Y = spectfheart()
    n_samples, n_features = X.shape
    n_class = len(set(Y))
    print("Number of Samples:", n_samples)
    print("Number of Features:", n_features)
    print("Number of Classes:", n_class)
