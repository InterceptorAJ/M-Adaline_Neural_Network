import numpy as np
import math

# empty arrays
neurons = []
test1 = []
test2 = []
test3 = []

# split an array into sub-arrays
def split(arr, size):
    arrs = []
    while len(arr) > size:
        pice = arr[:size]
        arrs.append(pice)
        arr = arr[size:]
    arrs.append(arr)
    return arrs

# main function
def array_vectorise(arg1, arg2):
    for array in arg1:
        for i in array:
            if i == 1:
                a = np.count_nonzero(array == 1)
                i = 1 / math.sqrt(a)
                arg2.append(i)
            else:
                arg2.append(0)

# training set - it is a set of 10 numbers from 0 to 9
training_set = np.array(
    [[1, 1, 1,
      1, 0, 1,
      1, 0, 1,
      1, 0, 1,
      1, 1, 1],
     [0, 1, 0,
      1, 1, 0,
      0, 1, 0,
      0, 1, 0,
      0, 1, 0],
     [0, 1, 0,
      1, 0, 1,
      0, 1, 0,
      1, 0, 0,
      1, 1, 1],
     [1, 1, 1,
      0, 0, 1,
      0, 1, 0,
      0, 0, 1,
      1, 1, 1],
     [1, 0, 0,
      1, 0, 0,
      1, 1, 1,
      0, 0, 1,
      0, 0, 1],
     [1, 1, 1,
      1, 0, 0,
      1, 1, 1,
      0, 0, 1,
      1, 1, 1],
     [1, 1, 1,
      1, 0, 0,
      1, 1, 1,
      1, 0, 1,
      1, 1, 1],
     [1, 1, 1,
      0, 0, 1,
      0, 1, 0,
      1, 0, 0,
      1, 0, 0],
     [1, 1, 1,
      1, 0, 1,
      1, 1, 1,
      1, 0, 1,
      1, 1, 1],
     [1, 1, 1,
      1, 0, 1,
      1, 1, 1,
      0, 0, 1,
      1, 1, 1]])

# first test set - it is a set of 10 numbers from 0 to 9
test_set1 = np.array(
    [[1, 1, 1,
      1, 0, 1,
      1, 0, 1,
      1, 0, 1,
      1, 1, 1],
     [0, 1, 0,
      1, 1, 0,
      0, 1, 0,
      0, 1, 0,
      0, 1, 0],
     [0, 1, 0,
      1, 0, 1,
      0, 1, 0,
      1, 0, 0,
      1, 1, 1],
     [1, 1, 1,
      0, 0, 1,
      0, 1, 0,
      0, 0, 1,
      1, 1, 1],
     [1, 0, 0,
      1, 0, 0,
      1, 1, 1,
      0, 0, 1,
      0, 0, 1],
     [1, 1, 1,
      1, 0, 0,
      1, 1, 1,
      0, 0, 1,
      1, 1, 1],
     [1, 1, 1,
      1, 0, 0,
      1, 1, 1,
      1, 0, 1,
      1, 1, 1],
     [1, 1, 1,
      0, 0, 1,
      0, 1, 0,
      1, 0, 0,
      1, 0, 0],
     [1, 1, 1,
      1, 0, 1,
      1, 1, 1,
      1, 0, 1,
      1, 1, 1],
     [1, 1, 1,
      1, 0, 1,
      1, 1, 1,
      0, 0, 1,
      1, 1, 1]])

#second test set - it is a set of two. One is blank page (0) and second is filled page (1)
test_set2 = np.array(
    [[0, 0, 0,
      0, 0, 0,
      0, 0, 0,
      0, 0, 0,
      0, 0, 0],
     [1, 1, 1,
      1, 1, 1,
      1, 1, 1,
      1, 1, 1,
      1, 1, 1]])

#third test set - it is a set of two. One is "X" letter and the second is inverted 1 number
test_set3 = np.array(
    [[1, 0, 1,
      0, 1, 0,
      0, 1, 0,
      0, 1, 0,
      1, 0, 1],
     [1, 0, 1,
      0, 0, 1,
      1, 0, 1,
      1, 0, 1,
      1, 0, 1]])

# vectorising of training and test sets
array_vectorise(training_set, neurons)
neurons = split(neurons, 15)
array_vectorise(test_set1, test1)
weights = split(test1, 15)
array_vectorise(test_set2, test2)
weights1 = split(test2, 15)
array_vectorise(test_set3, test3)
weights2 = split(test3, 15)

# func for training set and first test set
def check_number():
    for i in range(0,10):
        for k in range(0,10):
            count = sum([a*b for a,b in zip(neurons[k], weights[i])])
            print(i,k, " : ", round(count,2))
# check_number()


# func for training set and second test set
def check_number1():
    for i in range(0,2):
        for k in range(0,10):
            count = sum([a*b for a,b in zip(neurons[k], weights1[i])])
            print(i,k, " : ", round(count,2))
# check_number1()


# func for training set and third test set
def check_number2():
    for i in range(0,2):
        for k in range(0,10):
            count = sum([a*b for a,b in zip(neurons[k], weights2[i])])
            print(i,k, " : ", round(count,2))
# check_number2()
