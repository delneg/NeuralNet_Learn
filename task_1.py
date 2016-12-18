from neuron import Neuron as n
from neuron import linear_activation, binary_activation, binary_activation_bipolar, binary_activation_reversed
from neuron import test_data as d
from neuron import dimension_test


def var_4():
    n1 = n([-1, 1, 1], 0.5, linear_activation)
    n2 = n([1, -1, 1], 0.5, linear_activation)
    n3 = n([-1, -1], 0.5)

    def f(i):
        r1 = n1.calc(i)
        r2 = n2.calc(i)
        r3 = n3.calc([r1, r2])
        return r3

    dimension_test(3, f)


def var_2():
    n1 = n([1, 1, -1], -2.5)
    n2 = n([1, -1, -1], -2.5)
    n3 = n([-1, 1, -1], -2.5)
    n4 = n([1, 1, 1], 2.5, binary_activation_reversed)

    def f(i):
        r = n4.calc([n1.calc(i), n2.calc(i), n3.calc(i)])
        return r

    dimension_test(3, f, True)


def var_3():
    n1 = n([1, -1, 0, 0], -0.5)
    n2 = n([-1, 0, 0, 1], -0.5)
    n3 = n([1, 1], 1.5, binary_activation_reversed)

    def f(i):
        r = n3.calc([n1.calc(i), n2.calc(i)])
        return r

    dimension_test(4, f, True)

var_3()
