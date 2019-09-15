import scipy.io

mat = scipy.io.loadmat('/Users/shenzixiao/Dropbox/DATA/ASU/BiologicalData/colon.mat')
X = mat['X']  # data
x = X.astype(float)
y = mat['Y']
y = y[:, 0]
n_samples, n_features = X.shape  # number of samples and number of features
