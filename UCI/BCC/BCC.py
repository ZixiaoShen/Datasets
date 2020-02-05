import pandas as pd
import io
import requests


# def phoneme():
file_url = "https://raw.githubusercontent.com/ZixiaoShen/Datasets/master/UCI/" \
            "BCC/dataR2.csv"
s = requests.get(file_url).content
df = pd.read_csv(io.StringIO(s.decode('utf-8')), header=None)

    # data = df.values
    # data = data[1:, :]
    # x = data[:, 0:5]
    # x = x.astype('float')
    # y = data[:, 5].astype('int')
    # return x, y


# if __name__ == '__main__':
#     X, Y = phoneme()
#     n_samples, n_features = X.shape
#     n_class = len(set(Y))
#     print("Number of Samples:", n_samples)
#     print("Number of Features:", n_features)
#     print("Number of Classes:", n_class)
