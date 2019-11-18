import pandas as pd
import numpy as np
import io
import requests


def sonar():
    file_url = "https://raw.githubusercontent.com/ZixiaoShen/Datasets/master/UCI/F60_Sonar/sonar.csv"
    s = requests.get(file_url).content
    df = pd.read_csv(io.StringIO(s.decode('utf-8')), header=None)
    x_df = df.drop(columns=60)
    y_df = df[60]

    class_mapping = {'R': 0, 'M': 1}
    y = y_df.map(class_mapping)
    x = np.array(x_df)
    y = np.array(y)
    return x, y


if __name__ == '__main__':
    X, Y = sonar()
    n_samples, n_features = X.shape
    print(n_samples)
    print(n_features)
