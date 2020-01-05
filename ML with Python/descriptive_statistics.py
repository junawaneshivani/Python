import pandas as pd

filename = "pima-indians-diabetes.data.csv"
data = pd.read_csv(filename)
print(data.shape)
# print(data.head(20))

print(data.dtypes)

'''
The describe() function on the Pandas
DataFrame lists 8 statistical properties of each attribute. They are:
 Count.
 Mean.
 Standard Deviation.
 Minimum Value.
 25th Percentile.
 50th Percentile (Median).
 75th Percentile.
 Maximum Value.
'''

print(data.describe())

'''On classification problems you need to know how balanced the class values are. Highly imbalanced
problems (a lot more observations for one class than another) are common and may need special
handling in the data preparation stage of your project.'''
class_counts = data.groupby('Outcome').size()
print(class_counts)

# Pearson's Correlation Coefficient
'''assumes a normal distribution of the attributes involved. A correlation of -1
or 1 shows a full negative or positive correlation respectively. Whereas a value of 0 shows no
correlation at all. Some machine learning algorithms like linear and logistic regression can suffer
poor performance if there are highly correlated attributes in your dataset. As such, it is a good
idea to review all of the pairwise correlations of the attributes in your dataset. You can use the
corr() function on the Pandas DataFrame to calculate a correlation matrix.'''
pd.set_option('display.width', 100)
pd.set_option('precision', 3)
correlations = data.corr(method='pearson')
print(correlations)


'''Skew refers to a distribution that is assumed Gaussian (normal or bell curve) that is shifted or
squashed in one direction or another. Knowing that an attribute has a skew may allow you to perform data preparation
to correct the skew and later improve the accuracy of your models. The skew result show a positive (right) or negative (left) skew. Values closer to zero show
less skew.'''
skew = data.skew()
print(skew)