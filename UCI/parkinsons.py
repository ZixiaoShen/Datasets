import pandas as pd
import numpy as np

file_path = '/Users/shenzixiao/Dropbox/DATA/UCI/Parkinsons/parkinsons.csv'
data = pd.read_csv(file_path)
parkinsons = data.values

x1 = parkinsons[:, 1:17]
x2 = parkinsons[:, 18:]
X = np.hstack((x1, x2)).astype('float')
Y = parkinsons[:, 17].astype('int')
n_samples, num_F = X.shape
