import pandas as pd
import numpy as np
import io
import requests


def yeast():
    file_url = "https://raw.githubusercontent.com/ZixiaoShen/Datasets/master/UCI/" \
               "C10_F8_S1484_Yeast/yeast.csv"
    s = requests.get(file_url).content
    df = pd.read_csv(io.StringIO(s.decode('utf-8')), header=None)
    df = df.drop(columns=0)
    x_df = df.drop(columns=9)
    y_df = df[9]
    x = np.array(x_df)
    class_mapping = {'MIT': 0, 'NUC': 1, 'CYT': 2, 'ME1': 3, 'EXC': 4,
                     'ME2': 5, 'ME3': 6, 'VAC': 7, 'POX': 8, 'ERL': 9}
    y = y_df.map(class_mapping)
    y = np.array(y)
    return x, y


if __name__ == '__main__':
    X, Y = yeast()
    n_samples, n_features = X.shape
    n_class = len(set(Y))
    print("Number of Samples:", n_samples)
    print("Number of Features:", n_features)
    print("Number of Classes:", n_class)
