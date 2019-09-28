import pandas as pd
import numpy as np

# file_path = '/Users/shenzixiao/Dropbox/DATA/UCI/PIMA/pima-indians-diabetes.data'
file_path = 'D:/CloudFiles/Dropbox/DATA/UCI/PIMA/pima-indians-diabetes.data'
df = pd.read_csv(file_path, header=None)

df.columns = ['No_pregnant', 'Plasma_glucose', 'Blood_pres', 'Skin_thick',
             'Serum_insu', 'BMI', 'Diabetes_func', 'Age', 'Class']

X = np.array(df.drop(['Class'], axis=1))
Y = np.array(df['Class'])
n_samples, num_F = X.shape
