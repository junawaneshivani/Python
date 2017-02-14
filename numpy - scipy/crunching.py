
# fast number crunching with python

import numpy as np

a1 = np.array([1,2,3])		# parameter can be list(mutable)
a2 = np.array((1,2,3))		# parameter can be tuple(immutable)


print (a1 + a2)
print (a1 - a2)
print (a1 * a2)
print (a1 / a2)
print (a1 % a2)
print (a1 ** 2)

# how is numpy array different from a list ?
# in a numpy arry all the elements have to be of the same type.
# u can also explicitly state the type of array
# a = np.array([1,2,3],float)   OR
# a = np.array([1,2,3],np.float)
