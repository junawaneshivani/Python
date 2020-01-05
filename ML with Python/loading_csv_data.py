
import csv
import numpy as np
import pandas as pd

file_name = 'pima-indians-diabetes.data.csv'

# importing with csv module
with open(file_name) as raw_data:
    reader = csv.reader(raw_data, delimiter=',', quoting=csv.QUOTE_NONE)
    X = list(reader)
    data = np.array(X[1:]).astype('float') # excluding the header
    print(data.shape)


# importing with numpy
# with open(file_name) as raw_data:
#     data = np.loadtxt(raw_data, delimiter=',') # this function assumes no header, so will error out
#     print(data.shape)

# load csv from URL using numpy
# from urllib.request import urlopen
# url = 'https://goo.gl/vhm1eU'
# raw_data = urlopen(url)
# data = np.loadtxt(raw_data, delimiter=',')
# print(data.shape)

# load csv using pandas
data = pd.read_csv(file_name)
# data = pd.read_csv(url) # load csv from url pandas
print(data.shape)