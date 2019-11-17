import urllib.request
import numpy as np
import urllib.request


def wine():
    wine_url = "http://archive.ics.uci.edu//ml//machine-learning-databases//wine//wine.data"
    raw_data = urllib.request.urlopen(wine_url)
    raw_wine = np.loadtxt(raw_data, delimiter=",")

    x = raw_wine[:, 1:14]
    y = raw_wine[:, 0].astype('int')
    return x, y


if __name__ == '__main__':
    X, Y = wine()
    n_samples, n_features = X.shape
    print(n_samples)
    print(n_features)
