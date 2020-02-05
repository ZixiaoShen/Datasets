import pandas as pd
import numpy as np
import io
import requests


def statlog_heart():
    file_url = "https://raw.githubusercontent.com/ZixiaoShen/Datasets/master/UCI/" \
               "C2_F13_S270_Statlog_heart/Statlog_heart.csv"

    s = requests.get(file_url).content
    df = pd.read_csv(io.StringIO(s.decode('utf-8')), header=None)
    x_df = df.drop(columns=13)
    y_df = df[13]

    x = np.array(x_df)
    y = np.array(y_df)
    return x, y


if __name__ == '__main__':
    X, Y = statlog_heart()
    n_samples, n_features = X.shape
    n_class = len(set(Y))
    print("Number of Samples:", n_samples)
    print("Number of Features:", n_features)
    print("Number of Classes:", n_class)
