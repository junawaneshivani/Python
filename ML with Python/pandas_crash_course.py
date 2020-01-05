
import pandas as pd
import numpy as np

# Series is 1d array
my_array = np.array([1, 2, 3])
row_names = ["a", "b", "c"]
my_series = pd.Series(my_array, index=row_names)
print(my_series)

print(my_series[0])
print(my_series["a"])

# DataFrame is 2d array
my_array = np.array([[1, 2, 3], [4, 5, 6]])
row_names = ["a", "b"]
col_names = ["one", "two", "three"]
my_df = pd.DataFrame(my_array, index=row_names, columns=col_names)
print(my_df)

print(my_df.one)
print(my_df["one"])

# Snippet from Machine learning mastery with python book
"""
There is a lot of documentation for Pandas, I think because it is such a 
exible tool. Generally,
the cookbook examples will be most useful to you here as they will give you ideas on dierent
ways to slice and dice your data.
 Pandas documentation page (user guide). Note the table of contents of the left hand side,
it's very extensive.
http://pandas.pydata.org/pandas-docs/stable/
 Pandas cookbook providing many short and sweet examples.
http://pandas.pydata.org/pandas-docs/stable/cookbook.html
 Pandas API Reference.
http://pandas.pydata.org/pandas-docs/stable/api.html
"""

