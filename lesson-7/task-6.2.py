import numpy as np

A = np.array([[1, 2, -1], [3, -4, 0], [8, -5, 2], [2, 0 , -5], [11, 4, -7]])
B = np.array([1, 7, 12, 7, 15])
s = np.linalg.lstsq(A, B)
print(s)
# (array([ 1.13919353, -0.90498444, -0.9009803 ]), array([0.71523211]), 3, array([15.2817306 ,  9.59852942,  3.65197794]))

n = np.dot(A, [ 1.13919353, -0.90498444, -0.9009803 ])
print(n)
# [ 0.23020495  7.03751835 11.83650984  6.78328856 15.21805317]