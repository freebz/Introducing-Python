# C.2 과학과 파이썬

# C.3 NumPy

# C.3.1 배열 만들기(1): array()

import numpy as np

b = np.array( [2, 4, 6, 8] )
b
# array([2, 4, 6, 8])


b.ndim
# 1


b.size
# 4


b.shape
# (4,)


# C.3.2 배열 만들기(2): arange()

import numpy as np
a = np.arange(10)
a
# array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
a.ndim
# 1
a.shape
# (10,)
a.size
10


a = np.arange(7, 11)
a
# array([ 7,  8,  9, 10])


a = np.arange(7, 11, 2)
a
# array([7, 9])


f = np.arange(2.0, 9.8, 0.3)
f
# array([2. , 2.3, 2.6, 2.9, 3.2, 3.5, 3.8, 4.1, 4.4, 4.7, 5. , 5.3, 5.6,
#        5.9, 6.2, 6.5, 6.8, 7.1, 7.4, 7.7, 8. , 8.3, 8.6, 8.9, 9.2, 9.5,
#        9.8])


g = np.arange(10, 4, -1.5, dtype=np.float)
g
# array([10. ,  8.5,  7. ,  5.5])


# C.3.3 배열 만들기(3): zeros(), ones(), random()

a = np.zeros((3,))
a
# array([0., 0., 0.])
a.ndim
# 1
a.shape
# (3,)
a.size
# 3


b = np.zeros((2, 4))
b
# array([[0., 0., 0., 0.],
#        [0., 0., 0., 0.]])
b.ndim
# 2
b.shape
# (2, 4)
b.size
# 8


import numpy as np
k = np.ones((3, 5))
k
# array([[1., 1., 1., 1., 1.],
#        [1., 1., 1., 1., 1.],
#        [1., 1., 1., 1., 1.]])


m = np.random.random((3, 5))
m
# array([[0.07033508, 0.93857735, 0.15129157, 0.91425712, 0.43635069],
#        [0.30535056, 0.97924896, 0.79299033, 0.19462538, 0.77823159],
#        [0.71663894, 0.44873556, 0.01167547, 0.59423867, 0.08834878]])


# C.3.4 배열 모양 바꾸기: reshape()

a = np.arange(10)
a
# array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
a = a.reshape(2, 5)
a
# array([[0, 1, 2, 3, 4],
#        [5, 6, 7, 8, 9]])
a.ndim
# 2
a.shape
# (2, 5)
a.size
# 10



a = a.reshape(5, 2)
a
# array([[0, 1],
#        [2, 3],
#        [4, 5],
#        [6, 7],
#        [8, 9]])
a.ndim
# 2
a.shape
# (5, 2)
a.size
# 10


a.shape = (2, 5)
a
# array([[0, 1, 2, 3, 4],
#        [5, 6, 7, 8, 9]])


a = a.reshape(3, 4)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: cannot reshape array of size 10 into shape (3,4)


# C.3.5 항목 얻기: []

a = np.arange(10)
a[7]
# 7
a[-1]
# 9


a.shape = (2, 5)
a
# array([[0, 1, 2, 3, 4],
#        [5, 6, 7, 8, 9]])
a[1,2]
# 7


l = [ [0, 1, 2, 3, 4], [5, 6, 7, 8, 9] ]
l
# [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]]
l[1,2]
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: list indices must be integers or slices, not tuple
l[1][2]
# 7


a = np.arange(10)
a = a.reshape(2, 5)
a
# array([[0, 1, 2, 3, 4],
#        [5, 6, 7, 8, 9]])


a[0, 2:]
# array([2, 3, 4])


a[-1, :3]
# array([5, 6, 7])

a[:, 2:4] = 1000
a
# array([[   0,    1, 1000, 1000,    4],
#        [   5,    6, 1000, 1000,    9]])


# C.3.6 배열 연산

from numpy import *
a = arange(4)
a
# array([0, 1, 2, 3])
a *= 3
a
# array([0, 3, 6, 9])


plain_list = list(range(4))
plain_list
# [0, 1, 2, 3]
plain_list = [num * 3 for num in plain_list]
plain_list
# [0, 3, 6, 9]


from numpy import *
a = zeros((2, 5)) + 17.0
a
# array([[17., 17., 17., 17., 17.],
#        [17., 17., 17., 17., 17.]])


import numpy as np
a = np.array([[1,2], [3,4]])
b = a @ a
b
# array([[ 7, 10],
#        [15, 22]])


# C.3 선형 대수

import numpy as np
coefficients = np.array([ [4, 5], [1, 2] ])
dependents = np.array( [20, 13] )


answers = np.linalg.solve(coefficients, dependents)
answers
# array([-8.33333333, 10.66666667])


4 * answers[0] + 5 * answers[1]
# 20.0
1 * answers[0] + 2 * answers[1]
# 13.0


product = np.dot(coefficients, answers)
product
# array([20., 13.])


np.allclose(product, dependents)
# True
