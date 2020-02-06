import pandas as pd
import io
import requests


def hcv_egy():
    file_url = "https://raw.githubusercontent.com/ZixiaoShen/Datasets/master/UCI/" \
                "C4_F28_S1385_HCV_Egy/HCV_Egy_Data.csv"
    s = requests.get(file_url).content
    df = pd.read_csv(io.StringIO(s.decode('utf-8')))

    x_df = df.iloc[:, 0: -1]
    y_df = df.iloc[:, -1]

    x = x_df.values
    y = y_df.values
    return x, y


if __name__ == '__main__':
    X, Y = hcv_egy()
    n_samples, n_features = X.shape
    n_class = len(set(Y))
    print("Number of Samples:", n_samples)
    print("Number of Features:", n_features)
    print("Number of Classes:", n_class)
