import numpy as np

image = np.array([[[255,100],[200,150],[120,86]],
 [[55,120],[100,250],[220,186]],
 [[255,10],[220,150],[220,186]]
])

image = image.reshape(image.shape[0],image.shape[1],image.shape[2],1)
x = np.array([[0,5,20,30,12]])
def normalize(x):
    X_norm = np.linalg.norm(x)
    return x/X_norm

print(normalize(x))
