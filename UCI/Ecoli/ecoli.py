import pandas as pd
import io
import requests


# def breast_tissue():
file_url = "https://raw.githubusercontent.com/ZixiaoShen/Datasets/master/UCI/" \
            "Ecoli/ecoli.csv"
s = requests.get(file_url).content
df = pd.read_csv(io.StringIO(s.decode('utf-8')), header=None)
    # data = df.values
    # x = data[:, 2:]
    # x = x.astype('float')
    # y_df = df['Class']
    #
    # class_mapping = {'car': 0, 'fad': 1, 'mas': 2, 'gla': 3, 'con': 4, 'adi': 5}
    # y = y_df.map(class_mapping).values
    # return x, y


# if __name__ == '__main__':
#     X, Y = breast_tissue()
#     n_samples, n_features = X.shape
#     n_class = len(set(Y))
#     print("Number of Samples:", n_samples)
#     print("Number of Features:", n_features)
#     print("Number of Classes:", n_class)
