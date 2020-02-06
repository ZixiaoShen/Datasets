import pandas as pd
import io
import requests


def image_segmentation():
    file_url = "https://raw.githubusercontent.com/ZixiaoShen/Datasets/master/UCI/" \
                "Image_segmentation/Image_segmentation.csv"
    s = requests.get(file_url).content
    df = pd.read_csv(io.StringIO(s.decode('utf-8')), header=None)

    x_df = df.drop(columns=0)
    x = x_df.values
    y_df = df.iloc[:, 0]

    class_mapping = {'BRICKFACE': 0, 'SKY': 1, 'FOLIAGE': 2, 'CEMENT': 3,
                     'WINDOW': 4, 'PATH': 5, 'GRASS': 6}
    y = y_df.map(class_mapping).values
    return x, y


if __name__ == '__main__':
    X, Y = image_segmentation()
    n_samples, n_features = X.shape
    n_class = len(set(Y))
    print("Number of Samples:", n_samples)
    print("Number of Features:", n_features)
    print("Number of Classes:", n_class)
