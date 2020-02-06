import pandas as pd
import numpy as np
import io
import requests


def ilpd():
    file_url = "https://raw.githubusercontent.com/ZixiaoShen/Datasets/master/UCI/" \
                "ILPD/ILPD.csv"
    s = requests.get(file_url).content
    df = pd.read_csv(io.StringIO(s.decode('utf-8')), header=None)

    y = df.iloc[:, -1].values
    x_df = df.iloc[:, 0:-1]

    df_str = x_df.iloc[:, 1]
    class_mapping = {'Male': 0, 'Female': 1}
    df1 = df_str.map(class_mapping)
    x_df.iloc[:, 1] = df1
    x = x_df.values
    return x, y


if __name__ == '__main__':
    X, Y = ilpd()
    n_samples, n_features = X.shape
    n_class = len(set(Y))
    print("Number of Samples:", n_samples)
    print("Number of Features:", n_features)
    print("Number of Classes:", n_class)
