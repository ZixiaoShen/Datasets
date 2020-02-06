import pandas as pd
import io
import requests


def fertility():
    file_url = "https://raw.githubusercontent.com/ZixiaoShen/Datasets/master/UCI/" \
                "C2_F9_S100_Fertility/Fertility.csv"
    s = requests.get(file_url).content
    df = pd.read_csv(io.StringIO(s.decode('utf-8')), header=None)
    x_df = df.iloc[:, 0:9]
    y_df = df.iloc[:, 9]
    x = x_df.values
    class_mapping = {'N': 0, 'O': 1}
    y = y_df.map(class_mapping).values
    return x, y


if __name__ == '__main__':
    X, Y = fertility()
    n_samples, n_features = X.shape
    n_class = len(set(Y))
    print("Number of Samples:", n_samples)
    print("Number of Features:", n_features)
    print("Number of Classes:", n_class)
