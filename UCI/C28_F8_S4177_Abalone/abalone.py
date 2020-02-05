import pandas as pd
import numpy as np
import io
import requests


def abalone():
    file_url = "https://raw.githubusercontent.com/ZixiaoShen/Datasets/master/UCI/F8_Abalone/abalone.data"

    s = requests.get(file_url).content
    df = pd.read_csv(io.StringIO(s.decode('utf-8')), header=None)
    df_str = df[0]
    df1 = df.drop(columns=0)
    class_mapping = {'M': 0, 'F': 1, 'I': 2}
    df0 = df_str.map(class_mapping)
    df0 = df0.to_frame()

    data0 = df0.values
    data1 = df1.values
    data = np.hstack((data0, data1))
    x = data[:, 0:8]
    x = x.astype('float')
    y = data[:, 8].astype('int')
    return x, y


if __name__ == '__main__':
    X, Y = abalone()
    n_samples, n_features = X.shape
    n_class = len(set(Y))
    print("Number of Samples:", n_samples)
    print("Number of Features:", n_features)
    print("Number of Classes:", n_class)
