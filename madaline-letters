import numpy as np
import math

neurons = []
weights = []

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

# training set
training_set = np.array(
    [[1, 0, 0, 1,
      0, 1, 1, 0,
      0, 1, 1, 0,
      1, 0, 0, 1],
     [1, 0, 0, 1,
      0, 1, 1, 0,
      0, 1, 0, 0,
      1, 0, 0, 0],
     [1, 1, 1, 1,
      0, 0, 1, 0,
      0, 1, 0, 0,
      1, 1, 1, 1]])

# test set - it is the same as training set
test_set1 = np.array(
    [[1, 0, 0, 1,
      0, 1, 1, 0,
      0, 1, 1, 0,
      1, 0, 0, 1],
     [1, 0, 0, 1,
      0, 1, 1, 0,
      0, 1, 0, 0,
      1, 0, 0, 0],
     [1, 1, 1, 1,
      0, 0, 1, 0,
      0, 1, 0, 0,
      1, 1, 1, 1]])

# create vectorised arrays for training and test sets
array_vectorise(training_set, neurons)
neurons = split(neurons, 16)
array_vectorise(test_set1, weights)
weights = split(weights, 16)

# function for letter checking
def check_letter(letter):
    if letter == "X":
        print("X letter: ")
        X = sum([a * b for a, b in zip(neurons[0], weights[0])])
        Y = sum([a * b for a, b in zip(neurons[0], weights[1])])
        Z = sum([a * b for a, b in zip(neurons[0], weights[2])])
        print("X: ", X)
        print("Y: ", Y)
        print("Z: ", Z)
    elif letter == "Y":
        print("Y letter: ")
        X = sum([a * b for a, b in zip(neurons[1], weights[0])])
        Y = sum([a * b for a, b in zip(neurons[1], weights[1])])
        Z = sum([a * b for a, b in zip(neurons[1], weights[2])])
        print("X: ", X)
        print("Y: ", Y)
        print("Z: ", Z)
    elif letter == "Z":
        print("Z letter: ")
        X = sum([a * b for a, b in zip(neurons[2], weights[0])])
        Y = sum([a * b for a, b in zip(neurons[2], weights[1])])
        Z = sum([a * b for a, b in zip(neurons[2], weights[2])])
        print("X: ", X)
        print("Y: ", Y)
        print("Z: ", Z)

# check letters:
check_letter("X")
check_letter("Y")
check_letter("Z")
