from sklearn.datasets import load_breast_cancer
wdbc = load_breast_cancer()

X = wdbc.data
Y = wdbc.target
n_samples, num_F = X.shape
