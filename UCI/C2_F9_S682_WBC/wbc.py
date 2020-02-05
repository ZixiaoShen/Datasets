import numpy as np
import pandas as pd


def wbc():
    data_path = "http://archive.ics.uci.edu/ml/machine-learning-databases/" \
                "breast-cancer-wisconsin/breast-cancer-wisconsin.data"
    data = pd.read_csv(data_path)
    data = data.replace(to_replace="?", value=np.nan)
    data = data.dropna(how='any')

    wbc_data = data.values
    wbc_data = wbc_data.astype(int)
    x = wbc_data[:, 1:10]
    y = wbc_data[:, 10]
    y = y - 3
    return x, y


if __name__ == '__main__':
    X, Y = wbc()
    n_samples, n_features = X.shape
    n_class = len(set(Y))
    print("Number of Samples:", n_samples)
    print("Number of Features:", n_features)
    print("Number of Classes:", n_class)
