import scipy.io

# mat = scipy.io.loadmat('/Users/shenzixiao/Dropbox/DATA/ASU/TextData/BASEHOCK.mat')
mat = scipy.io.loadmat('D:/CloudFiles/Dropbox/DATA/ASU/TextData/BASEHOCK.mat')

X = mat['X']
X = X.astype(float)
Y = mat['Y']
Y = Y[:, 0]
n_samples, n_features = X.shape
