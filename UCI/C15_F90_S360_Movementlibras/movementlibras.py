import pandas as pd
import io
import requests


def movementlibras():
    file_url = "https://raw.githubusercontent.com/ZixiaoShen/Datasets/master/UCI/" \
               "C15_F90_S360_Movementlibras/Movementlibras.csv"
    s = requests.get(file_url).content
    df = pd.read_csv(io.StringIO(s.decode('utf-8')), header=None)

    data = df.values
    x = data[:, 0:90]
    x = x.astype('float')
    y = data[:, 90].astype('int')
    return x, y


if __name__ == '__main__':
    X, Y = movementlibras()
    n_samples, n_features = X.shape
    n_class = len(set(Y))
    print("Number of Samples:", n_samples)
    print("Number of Features:", n_features)
    print("Number of Classes:", n_class)
