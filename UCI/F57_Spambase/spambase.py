import pandas as pd
import io
import requests


def spambase():
    file_url = "https://raw.githubusercontent.com/ZixiaoShen/Datasets/master/UCI/F57_Spambase/Spambase.csv"
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
    print(n_samples)
    print(n_features)
