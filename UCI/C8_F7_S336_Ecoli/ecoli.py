import pandas as pd
import io
import requests


def ecoli():
    file_url = "https://raw.githubusercontent.com/ZixiaoShen/Datasets/master/UCI/" \
                "C8_F7_S336_Ecoli/ecoli.csv"
    s = requests.get(file_url).content
    df = pd.read_csv(io.StringIO(s.decode('utf-8')), header=None)
    df = df.drop(columns=0)
    x = df.iloc[:, 0:7].values
    y_df = df.iloc[:, 7]

    class_mapping = {'cp': 0, 'im': 1, 'imS': 2, 'imL': 3, 'imU': 4, 'om': 5,
                     'omL': 6, 'pp': 7}
    y = y_df.map(class_mapping).values
    return x, y


if __name__ == '__main__':
    X, Y = ecoli()
    n_samples, n_features = X.shape
    n_class = len(set(Y))
    print("Number of Samples:", n_samples)
    print("Number of Features:", n_features)
    print("Number of Classes:", n_class)
