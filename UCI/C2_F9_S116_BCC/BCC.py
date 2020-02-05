import pandas as pd
import io
import requests


def breast_cancer_coimbra():
    file_url = "https://raw.githubusercontent.com/ZixiaoShen/Datasets/master/UCI/" \
                "C2_F9_S116_BCC/dataR2.csv"
    s = requests.get(file_url).content
    df = pd.read_csv(io.StringIO(s.decode('utf-8')))

    data = df.values
    x = data[:, 0:9]
    y = data[:, 9].astype('int')
    return x, y


if __name__ == '__main__':
    X, Y = breast_cancer_coimbra()
    n_samples, n_features = X.shape
    n_class = len(set(Y))
    print("Number of Samples:", n_samples)
    print("Number of Features:", n_features)
    print("Number of Classes:", n_class)
