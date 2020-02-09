import pandas as pd
import io
import requests


def sports_articles():
    file_url = "https://raw.githubusercontent.com/ZixiaoShen/Datasets/master/UCI/" \
               "C2_F59_S1000_Sports_articles/sports_articles.csv"
    s = requests.get(file_url).content
    df = pd.read_csv(io.StringIO(s.decode('utf-8')))
    x_df = df.drop(columns='Label')
    x = x_df.values

    y_df = df.iloc[:, 0]
    class_mapping = {'objective': 0, 'subjective': 1}
    y = y_df.map(class_mapping).values
    return x, y


if __name__ == '__main__':
    X, Y = sports_articles()
    n_samples, n_features = X.shape
    n_class = len(set(Y))
    print("Number of Samples:", n_samples)
    print("Number of Features:", n_features)
    print("Number of Classes:", n_class)
