import numpy as np
#sigmoid function formula
# s = 1/(1+e^-1)

def sigmoidFunc(input):
    return 1/(1+np.exp(-input))

def creating_weights(input_rows):
    return np.random.randn(input_rows,1),1



#Input
X = np.array([[1],[2]])

#weight creating
w,b =creating_weights(X.shape[0])

#create sigmoid by multiplying T of inputs and weights plus with bias (b)
result = sigmoidFunc((X.T *w) +b)
print(result)


