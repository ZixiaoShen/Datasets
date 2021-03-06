import pandas as pd
import numpy as np
import io
import requests


def pima():
    file_url = "https://raw.githubusercontent.com/ZixiaoShen/Datasets/master/UCI/" \
               "C2_F8_S768_PIMA/pima-indians-diabetes.data"
    s = requests.get(file_url).content
    df = pd.read_csv(io.StringIO(s.decode('utf-8')), header=None)
    df.columns = ['No_pregnant', 'Plasma_glucose', 'Blood_pres',
                  'Skin_thick', 'Serum_insu', 'BMI', 'Diabetes_func', 'Age', 'Class']
    x = np.array(df.drop(['Class'], axis=1))
    y = np.array(df['Class'])
    return x, y


if __name__ == '__main__':
    X, Y = pima()
    n_samples, n_features = X.shape
    n_class = len(set(Y))
    print("Number of Samples:", n_samples)
    print("Number of Features:", n_features)
    print("Number of Classes:", n_class)
