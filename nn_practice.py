import numpy as np
import itertools
import sys
import pprint as pp
import random
import matplotlib.pyplot as plt


learning_rate = .001
n = 100
epoch = 100


# sigmoid function
def sigmoid(x):
    # print(1/(1 + np.exp(-x)))
    return 1/(1 + np.exp(-x))


# derivative of sigmoid function
def sig_div(x):
    return np.exp(-x) / (1 + np.exp(-x))**2


# sum of squares error
def sse(data, data2, labels, w1, w2, w21, w22, b):
    return np.sum(((data * w1 + data2 * w21 + (data * w2) + data2 * w22 + b) - labels)**2) / (2 * n)


def main():
    # creating randomized data
    np.random.seed(1)
    data = np.random.random_sample(n) * 100
    data2 = np.random.random_sample(n) * 100
    labels = data * data
    labels2 = data + data2

    # setting weights and bias
    w11 = np.random.rand()
    w12 = np.random.rand()
    w21 = np.random.rand()
    w22 = np.random.rand()
    b = np.random.rand()

    # non-matrix training for layman understanding of backpropagation
    for i in range(epoch):
        for j in range(n):
            '''
            # 1 INPUT, 2 LAYERS
            a = (data[j] * w11) + (data[j]**2 * w12) + b
            output = sigmoid(data[j] * w11) + sigmoid(data[j]**2 * w12) + sigmoid(b)
            # output = sigmoid((data[j] * w1) + (data[j]**2 * w2) + b)

            # backpropagation
            # w1 = w1 - (output - labels[j]) * learning_rate * data[j]
            w11 = w11 - learning_rate * (a - labels[j]) * output * (sigmoid(data[j] * w11))
            # w2 = w2 - (output - labels[j]) * learning_rate * data[j]
            w12 = w12 - learning_rate * (a - labels[j]) * output * (sigmoid(data[j]**2 * w12))
            # b = b - (output - labels[j]) * learning_rate * 1
            b = b - learning_rate * (a - labels[j]) * output * sigmoid(1)
            '''

            # 2 INPUTS, 2 LAYERS
            output = (data[j] * w11 + data2[j] * w21) + (data[j] * w12 + data2[j] * w22) + b
            a = sigmoid(data[j] * w11 + data2[j] * w21) + sigmoid(data[j] * w12 + data2[j] * w22) + sigmoid(b)

            # backpropagation
            '''
            Change in error with respect to w_xy: (predicted - target) *
            activation function derivative of product sum plus bias (after activation function) *
            output of node xy
            Activation function is linear because regression problem, so derivative is 1
            Learning rate applied to change in error
            '''
            w11 = w11 - learning_rate * (output - labels2[j]) * a * (sigmoid(data[j] * w11))
            w12 = w12 - learning_rate * (output - labels2[j]) * a * (sigmoid(data[j] * w12))
            w21 = w21 - learning_rate * (output - labels2[j]) * a * (sigmoid(data2[j] * w21))
            w22 = w22 - learning_rate * (output - labels2[j]) * a * (sigmoid(data2[j] * w22))
            b = b - learning_rate * (output - labels2[j]) * a * sigmoid(1)

        error = sse(data, data2, labels2, w11, w12, w21, w22, b)
        print(f'iteration: {i} --- error: {error} --- weight: {w11}, {w12}, {w21}, {w22}')

    # adding in1 and in2 together
    in1 = 20
    in2 = 10
    print(f'{in1} + {in2} = {(in1 * w11 + in2 * w21) + (in1 * w12 + in2 * w22) + b}')


if __name__ == '__main__':
    main()
