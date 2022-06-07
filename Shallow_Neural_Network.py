import numpy as np

W1 = np.array([[3,1],[2,4]])
W2 = np.array([3,5])

X = np.array([[1],[2]])
b1 = np.array([[1],[1]])
b2 = np.array([1])

V1 = np.dot(W1,X)+b1
V2 = np.dot(W2,V1)+b2

print(V2)