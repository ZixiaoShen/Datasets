import urllib.request
import numpy as np

import urllib.request
wine_url = "http://archive.ics.uci.edu//ml//machine-learning-databases//wine//wine.data"
raw_data = urllib.request.urlopen(wine_url)
raw_wine = np.loadtxt(raw_data, delimiter=",")

X = raw_wine[:, 1:14]
Y = raw_wine[:, 0].astype('int')
n_samples, n_feature = X.shape  # number of samples and number of features
