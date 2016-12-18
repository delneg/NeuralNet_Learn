from neuron import Neuron as n
from neuron import linear_activation_double_plus_one, modular_activation, linear_activation_double, \
    one_to_one_activation, sqrt_activation, linear_activation, binary_activation, binary_activation_reversed


def var_4(x1, x2):
    n1 = n([1, -1], 0, linear_activation)
    n2 = n([1, -1], 0, linear_activation)
    n3 = n([0.5, 0.5], 0, linear_activation)
    n4 = n([1], 0, binary_activation)
    n5 = n([1], 0, binary_activation)

    def f(i, j):

        r1 = n1.calc([i, j])
        r2 = n2.calc([j, i])
        r3 = n3.calc([i, j])
        r4 = n4.calc([r1])
        r5 = n5.calc([r2])

        return r3, r4, r5

    halfsumm, max_1, max_2 = f(x1, x2)
    print("Mean " + str(x1) + " and " + str(x2) + " = " + str(halfsumm))
    if max_2 > max_1:
        print("Number " + str(x2) + " is greater than " + str(x1))
    else:
        print("Number " + str(x1) + " is greater than " + str(x2))


def var_3(x1, x2):
    n1 = n([1, -1], 0, linear_activation)
    n2 = n([1, -1], 0, linear_activation)
    n3 = n([1, -1], 0, modular_activation)
    n4 = n([1], 0, binary_activation_reversed)
    n5 = n([1], 0, binary_activation_reversed)

    def f(i, j):

        r1 = n1.calc([i, j])
        r2 = n2.calc([j, i])
        r3 = n3.calc([i, j])
        r4 = n4.calc([r1])
        r5 = n5.calc([r2])

        return r3, r4, r5

    difference_module, max_1, max_2 = f(x1, x2)
    print("Difference modulo  " + str(x1) + " и " + str(x2) + " = " + str(difference_module))
    if max_2 > max_1:
        print("Number " + str(x2) + " is smaller than " + str(x1))
    else:
        print("Number " + str(x1) + " is smaller than " + str(x2))


var_3(5, 30)
