import pandas as pd
import io
import requests


# def appendicitis():
file_url = "https://raw.githubusercontent.com/ZixiaoShen/Datasets/master/UCI/" \
           "C2_F7_S440_Wholesale/Wholesale.csv"
s = requests.get(file_url).content
df = pd.read_csv(io.StringIO(s.decode('utf-8')))

    # data = df.values
    # x = data[:, 0:7]
    # x = x.astype('float')
    # y = data[:, 7].astype('int')
    # return x, y


# if __name__ == '__main__':
#     X, Y = appendicitis()
#     n_samples, n_features = X.shape
#     n_class = len(set(Y))
#     print("Number of Samples:", n_samples)
#     print("Number of Features:", n_features)
#     print("Number of Classes:", n_class)
