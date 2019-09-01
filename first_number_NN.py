import numpy as np
import itertools
import sys
import pprint as pp


class Hidden:

    def __init__(self, bias, weight):
        self.bias = bias
        self.weight = weight


def dense_layer(current, layer):
    print(layer.weight.shape)
    w = list(np.asarray([list(layer.weight)]).transpose())
    pp.pprint(w)

    current = np.asarray([list(current)])

    #y = np.matmul(w, current)
    #print(y)



def main():
    # definitions
    data = np.random.randint(0, 5, (500, 5))
    labels = data[:500, 0]
    hidden = [Hidden(np.random.rand(), np.random.rand(5, 1)) for _ in range(5)]

    # going through dataset
    for current in data:
        # going through each layer in network
        for layer in hidden:
            print('current: {}\nlayer: {}'.format(current, layer.weight))
            dense_layer(current, layer)
            sys.exit(0)




if __name__ == '__main__':
    main()
    '''
    x = np.array([[1, 2, 3]])
    y = np.array([[1], [2], [3]])
    z = np.matmul(x.transpose(), y.transpose())
    print(z)
    '''