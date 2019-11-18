import pandas as pd
import io
import requests


def satimage():
    file_url = "https://raw.githubusercontent.com/ZixiaoShen/Datasets/master/UCI/F7_Appendicitis/Appendicitis.csv"
    s = requests.get(file_url).content
    df = pd.read_csv(io.StringIO(s.decode('utf-8')), header=None)

    data = df.values
    x = data[:, 0:7]
    x = x.astype('float')
    y = data[:, 7].astype('int')
    return x, y


if __name__ == '__main__':
    X, Y = satimage()
    n_samples, n_features = X.shape
    print(n_samples)
    print(n_features)
