import pandas as pd
import io
import requests


def absenteeism():
    file_url = \
        "https://raw.githubusercontent.com/ZixiaoShen/Datasets/master/UCI/" \
        "C19_F20_S740_Absenteeism/Absenteeism_at_work.csv"
    s = requests.get(file_url).content
    df = pd.read_csv(io.StringIO(s.decode('utf-8')), header=None)
    df = df.drop([0])
    data = df.values
    x = data[:, 0:20]
    x = x.astype(int)
    y = data[:, 20].astype(int)
    return x, y


if __name__ == '__main__':
    X, Y = absenteeism()
    n_samples, n_features = X.shape
    n_class = len(set(Y))
    print("Number of Samples:", n_samples)
    print("Number of Features:", n_features)
    print("Number of Classes:", n_class)
