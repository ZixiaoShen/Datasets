from sklearn import datasets


def iris():
    iris = datasets.load_iris()
    x = iris.data
    y = iris.target
    return x, y


if __name__ == '__main__':
    X, Y = iris()
    n_samples, n_features = X.shape
    print(n_samples)
    print(n_features)
