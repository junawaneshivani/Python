import numpy as np

# define an 1d array
my_list_1 = [1, 2, 3]
my_array_1 = np.array(my_list_1)
print(my_array_1, my_array_1.shape)

# define a 2d array
my_list_2 = [[1, 2, 3], [4, 5, 6]]
my_array_2 = np.array(my_list_2)
print(my_array_2, my_array_2.shape)
print("First row: {}".format(my_array_2[0]))
print("Last row: {}".format(my_array_2[-1]))
print("Specific row and col: {}".format(my_array_2[0, 2]))
print("Whole col: {}".format(my_array_2[:, 2]))

# Arithmetic
print("Addition: {}".format(my_array_1 + my_array_2))
print("Subtraction: {}".format(my_array_1 - my_array_2))
print("Multiplication: {}".format(my_array_1 * my_array_2))
print("Division: {}".format(my_array_1 / my_array_2))


# Snippet from Machine learning mastery with python book
'''
It is a great idea to become familiar with the broader SciPy ecosystem and for that I would
recommend the SciPy Lecture Notes listed below. I think the NumPy documentation is excellent
(and deep) but you probably don't need it unless you are doing something exotic.
 SciPy Lecture Notes.
http://www.scipy-lectures.org/
 NumPy User Guide.
http://docs.scipy.org/doc/numpy/user/
'''