from sklearn.datasets import load_breast_cancer


def wdbc():
    wdbc = load_breast_cancer()
    x = wdbc.data
    y = wdbc.target
    return x, y


if __name__ == '__main__':
    X, Y = wdbc()
    n_samples, n_features = X.shape
    print(n_samples)
    print(n_features)
