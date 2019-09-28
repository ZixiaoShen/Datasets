# import urllib.request
# import numpy as np
#
# import urllib.request
#
file_path = "https://github.com/ZixiaoShen/Datasets/blob/master/UCI/PIMA/pima-indians-diabetes.data"
#
# raw_data = urllib.request.urlopen(file_path)
# raw_wine = np.loadtxt(raw_data, delimiter=",")


import pandas as pd
import io
import requests
# url = "https://raw.githubusercontent.com/hunkim/DeepLearningZeroToAll/master/data-03-diabetes.csv"
s = requests.get(file_path).content
c = pd.read_csv(io.StringIO(s.decode('utf-8')), header=None)

