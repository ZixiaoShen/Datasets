import pandas as pd
import io
import requests


# def page_blocks():
file_url = "https://raw.githubusercontent.com/ZixiaoShen/Datasets/master/UCI/F10_page_blocks/page_blocks.csv"
# file_url = "https://raw.githubusercontent.com/ZixiaoShen/Datasets/master/UCI/F10_page_blocks/page-blocks.data"
s = requests.get(file_url).content
df = pd.read_csv(io.StringIO(s.decode('utf-8')), header=None)

data = df.values
# x = data[:, 0:9]
# x = x.astype('float')
# y = data[:, 9].astype('int')
    # return x, y

#
# if __name__ == '__main__':
#     X, Y = page_blocks()
#     n_samples, n_features = X.shape
#     print(n_samples)
#     print(n_features)
