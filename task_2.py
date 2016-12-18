from neuron import Neuron as n
from neuron import linear_activation_double_plus_one, modular_activation, linear_activation_double, \
    one_to_one_activation, sqrt_activation, linear_activation


def var_4():
    n1 = n([-1], 0, linear_activation_double)
    n2 = n([0.2], 0, one_to_one_activation)
    n3 = n([0.2], 0, one_to_one_activation)
    n4 = n([2, -1.5], 0, linear_activation_double)

    def f(i):
        r1 = n1.calc([i], log=True)
        r2 = n2.calc([r1], log=True)
        r3 = n3.calc([r1], log=True)
        r4 = n4.calc([r2, r3], log=True)
        return r4

    def plot(dots):
        import matplotlib.pyplot as plt
        results = [f(dot) for dot in dots]
        fig = plt.figure()
        plt.plot(dots, results, 'ro')
        fig.suptitle('Task 5, Var 4', fontsize=20)
        plt.grid(True)
        plt.show()

    # print(f(0.5))
    import numpy as np
    plot(np.arange(-10., 10., 0.05))


def var_3():
    n1 = n([2], 0.5, modular_activation)
    n2 = n([2], 0.5, modular_activation)
    n3 = n([1, -0.5], 0.5, linear_activation_double_plus_one)
    n4 = n([1, -0.5], 0.5, linear_activation_double_plus_one)

    def f(i):
        r1 = n1.calc([i], log=True)
        r2 = n2.calc([i], log=True)
        r3 = n3.calc([r1, r2], log=True)
        r4 = n4.calc([r1, r2], log=True)
        return r3, r4

    def plot(dots):
        import matplotlib.pyplot as plt
        results = [f(dot)[0] for dot in dots]
        fig = plt.figure()
        plt.plot(dots, results, 'ro')
        fig.suptitle('Task 5, Var 3', fontsize=20)
        plt.grid(True)
        plt.show()

    # print(f(-1.5))
    import numpy as np
    plot(np.arange(-10., 10., 0.05))


def var_2():
    n1 = n([0.5, -1, 0.2], 0.5, linear_activation)
    n2 = n([1.5], 0.5, sqrt_activation)
    n3 = n([1.5], 0.5, sqrt_activation)

    def f(i, j, k):
        r1 = n1.calc([i, j, k], log=True)
        r2 = n2.calc([r1], log=True)
        r3 = n3.calc([r1], log=True)
        return r2, r3

    def plot(dots):
        import matplotlib.pyplot as plt
        results = [f(dot, 0, 0)[0] for dot in dots]
        fig = plt.figure()
        plt.plot(dots, results, 'ro')
        fig.suptitle('Task 5, Var 2', fontsize=20)
        plt.grid(True)
        plt.show()

    # print(f(1, -1, 1))
    import numpy as np
    plot(np.arange(-10., 10., 0.05))


var_2()
