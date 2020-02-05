import pandas as pd
import numpy as np
import io
import requests


def ionosphere():
    file_url = "https://raw.githubusercontent.com/ZixiaoShen/Datasets/master/UCI/" \
               "C2_F34_S351_Ionosphere/ionosphere.data"
    s = requests.get(file_url).content
    df = pd.read_csv(io.StringIO(s.decode('utf-8')), header=None)
    x_df = df.drop(columns=34)
    y_df = df[34]

    class_mapping = {'g': 1, 'b': 0}
    y = y_df.map(class_mapping)
    x = np.array(x_df)
    y = np.array(y)
    return x, y


if __name__ == '__main__':
    X, Y = ionosphere()
    n_samples, n_features = X.shape
    n_class = len(set(Y))
    print("Number of Samples:", n_samples)
    print("Number of Features:", n_features)
    print("Number of Classes:", n_class)
