from sklearn import datasets

iris = datasets.load_iris()
X = iris.data
Y = iris.target
n_samples, num_F = X.shape  # number of samples and number of features
