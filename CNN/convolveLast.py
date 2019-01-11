
import numpy as np
from scipy import signal
from scipy import ndimage

def convolve(array, window, padding=0, stride=1, bias=0):
    A = len(array)
    F = len(window)
    dim = (A - F + 2*padding) // stride
    dim = dim + 1
    window = window.reshape((F*F, 1))
    result = np.zeros((dim, dim))
    array = pad(padding, array)
    i, j = 0, 0
    for row in range(0, dim):
        for col in range(0, dim):
            i = row*stride
            j = col*stride
            tmp = array[i:i+F, j:j+F]
            tmp = tmp.reshape((F*F, 1))
            tmp = tmp * window
            tmp = tmp.sum() +  bias
            result[row][col] = tmp
    return result

def pad(padding, array):
    if padding == 0:
        return array
    dim = len(array) + 2*padding
    res = np.zeros((dim, dim))
    for i in range(padding, padding+len(array)):
        for j in range(padding, padding+len(array)):
            res[i][j] = array[i-padding][j-padding]
    return res

def pooling(func, array, window, stride=1):
    A = len(array)
    F = window
    dim = ((A - F) // stride) + 1
    result = np.zeros((dim, dim))
    i, j = 0, 0
    for row in range(0, dim):
        for col in range(0, dim):
            i = row*stride
            j = col*stride
            tmp = array[i:i+F, j:j+F]
            tmp = pooler(func, tmp)
            result[row][col] = tmp
    return result

def pooler(func, arr):
      L = len(arr)
      arr = arr.reshape((L*L, 1))
      return func(arr)


if __name__ == "__main__":
    r = np.array([       # our input

        [1, 1, 2, 1, 0],
        [0, 2, 2, 2, 2],
        [1, 0, 2, 1, 0],
        [1, 1, 1, 2, 2],
        [1, 2, 1, 0, 2],

    ])

    f1r = np.array([[0, 0, -1],         # our filter matrix
                    [1, -1, 1],
                    [0, -1, 0]
                    ])
    res = convolve(r, f1r, padding=1, stride=1, bias=0)
    # res = ndimage.correlate(r, f1r, mode='constant')
    res1 = pooling(np.max, res, 2, 1)
    res1 = res1.flatten()
    print(res1) # result



