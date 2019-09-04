import urllib.request
import numpy as np

import urllib.request
wine_url = "http://archive.ics.uci.edu//ml//machine-learning-databases//wine//wine.data"
raw_data = urllib.request.urlopen(wine_url)
raw_wine = np.loadtxt(raw_data, delimiter=",")
