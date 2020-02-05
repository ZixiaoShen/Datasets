from sklearn import datasets


def iris():
    iris = datasets.load_iris()
    x = iris.data
    y = iris.target
    return x, y


if __name__ == '__main__':
    X, Y = iris()
    n_samples, n_features = X.shape
    n_class = len(set(Y))
    print("Number of Samples:", n_samples)
    print("Number of Features:", n_features)
    print("Number of Classes:", n_class)
