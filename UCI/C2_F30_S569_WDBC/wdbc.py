from sklearn.datasets import load_breast_cancer


def wdbc():
    wdbc = load_breast_cancer()
    x = wdbc.data
    y = wdbc.target
    return x, y


if __name__ == '__main__':
    X, Y = wdbc()
    n_samples, n_features = X.shape
    n_class = len(set(Y))
    print("Number of Samples:", n_samples)
    print("Number of Features:", n_features)
    print("Number of Classes:", n_class)
