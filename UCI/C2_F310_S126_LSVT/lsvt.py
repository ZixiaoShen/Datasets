import pandas as pd
import io
import requests


def lsvt():
    file_url = "https://raw.githubusercontent.com/ZixiaoShen/Datasets/master/UCI/" \
               "C2_F310_S126_LSVT/LSVT.csv"
    s = requests.get(file_url).content
    df = pd.read_csv(io.StringIO(s.decode('utf-8')))

    x_df = df.iloc[:, 0:-1]
    y_df = df.iloc[:, -1]

    x = x_df.values
    y = y_df.values - 1
    return x, y


if __name__ == '__main__':
    X, Y = lsvt()
    n_samples, n_features = X.shape
    n_class = len(set(Y))
    print("Number of Samples:", n_samples)
    print("Number of Features:", n_features)
    print("Number of Classes:", n_class)
