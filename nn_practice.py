import numpy as np
import itertools
import sys
import pprint as pp
import random
import matplotlib.pyplot as plt


# class definitions
# not being used
class Model:
    def __init__(self, bias, weight):
        self.bias = bias
        self.weight = weight

    def __call__(self, inputs):
        print(f'inputs: {inputs}')
        print(f'weight: {self.weight}')
        print(f'output: {np.matmul(inputs, self.weight)}')

        # change 5 to size of layer
        return [np.matmul(inputs, self.weight) + self.bias] * 5


learning_rate = .0001
n = 100
epoch = 100


def sigmoid(x):
    return 1/(1 + np.exp(-x))


def sig_div(x):
    return np.exp(-x) / (1 + np.exp(-x))**2


# change in error
def error_change(target, predicted):
    return target - predicted


def sse(data, labels, w, b):
    return np.sum(((data * w + b) - labels)**2)


def main():
    # creating random data with outputs (labels) being the square of the value
    np.random.seed(1)
    data = np.random.random_sample(100) * 10
    labels = data * data

    # setting weights and bias
    w1 = np.random.rand()
    w2 = np.random.rand()
    b = np.random.rand()

    for i in range(epoch):
        for j in range(n):
            output = (data[j] * w1) + b

            # backpropagation
            w1 = w1 + learning_rate * error_change(labels[j], output) * data[j]
            b = b + learning_rate * error_change(labels[j], output) * 1

        error = sse(data, labels, w1, b)
        print(f'iteration: {i} --- error: {error}')

    # plotting graph of data and trained network
    print(f'weight: {w1} -- bias: {b}')
    func = np.linspace(0, 10, 100)
    plt.plot(list(data), list(labels), 'ro')
    plt.plot(list(func), list(func * w1 + b))
    plt.ylabel('some numbers')
    plt.show()


if __name__ == '__main__':
    main()

    '''
    nodes = np.array([[1, 2, 3]] * 3)
    print(f'node: {nodes}')
    weight = np.array([[1, 1, 1], [2, 2, 2], [3, 3, 3]])
    print(f'weight: {weight}')

    print(np.matmul(weight, nodes))
'''