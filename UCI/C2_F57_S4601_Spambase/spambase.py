import pandas as pd
import io
import requests


def spambase():
    file_url = "https://raw.githubusercontent.com/ZixiaoShen/Datasets/master/UCI/" \
               "C2_F57_S4601_Spambase/Spambase.csv"
    s = requests.get(file_url).content
    df = pd.read_csv(io.StringIO(s.decode('utf-8')), header=None)

    data = df.values
    x = data[:, 0:57]
    x = x.astype('float')
    y = data[:, 57].astype('int')
    return x, y


if __name__ == '__main__':
    X, Y = spambase()
    n_samples, n_features = X.shape
    n_class = len(set(Y))
    print("Number of Samples:", n_samples)
    print("Number of Features:", n_features)
    print("Number of Classes:", n_class)
