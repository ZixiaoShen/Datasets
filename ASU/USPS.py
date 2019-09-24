import scipy.io

mat = scipy.io.loadmat('/Users/shenzixiao/Dropbox/DATA/ASU/'
                       'HandWrittenImageData/USPS.mat')

X = mat['X']  # data
x = X.astype(float)
y = mat['Y']
y = y[:, 0]
n_samples, num_F = X.shape  # number of samples and number of features

