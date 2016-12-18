def binary_activation(value):
    if value > 0:
        return 1
    elif value < 0:
        return 0
    else:
        raise Exception("0 passed to binary activation")


def binary_activation_reversed(value):
    if value > 0:
        return 0
    elif value < 0:
        return 1
    else:
        raise Exception("0 passed to binary activation")


def binary_activation_bipolar(value):
    if value > 0:
        return 1
    elif value < 0:
        return -1
    else:
        raise Exception("0 passed to binary activation")


def linear_activation(value):
    return value


def linear_activation_double(value):
    return value * 2


def linear_activation_double_plus_one(value):
    return 2 * value + 1


def one_to_one_activation(value):
    if value <= -1:
        return 0
    elif -1 < value < 1:
        return value
    else:
        return 0


def modular_activation(value):
    if value < 0:
        return -1 * value
    else:
        return value


def sqrt_activation(value):
    return value ** 2


class Neuron:
    def __init__(self, modifier_list, b, activation_function=binary_activation):
        self.activation = activation_function
        self.modifier = modifier_list
        self.b = b

    def calc(self, value_list, log=False):
        if len(value_list) != len(self.modifier):
            raise Exception("Value length don't match")
        res = self.activation(sum([value_list[i] * self.modifier[i] for i in range(len(value_list))]) - self.b)
        if log:
            print('Calculating ' + str(value_list) + " * " + str(self.modifier) + " - " + str(
                self.b) + " with activation function '" + self.activation.__name__ + "'")
            summ = 0
            for i in range(len(value_list)):
                cur_res = value_list[i] * self.modifier[i]
                print(str(value_list[i]) + " * " + str(self.modifier[i]) + " = " + str(cur_res))
                summ += cur_res
                print("Summ is now " + str(summ))

            summ_without_b = summ - self.b
            print("Summ " + str(summ) + " - b (" + str(self.b) + ") = " + str(summ_without_b))
            activated_res = self.activation(summ_without_b)
            print("After activation - " + str(activated_res))
        return res


def test_data(dimensions):
    if dimensions == 2:
        return [
            [0, 0],
            [0, 1],
            [1, 0],
            [1, 1]
        ]
    elif dimensions == 3:
        return [
            [0, 0, 0],
            [0, 0, 1],

            [0, 1, 0],
            [0, 1, 1],

            [1, 0, 0],
            [1, 0, 1],

            [1, 1, 0],
            [1, 1, 1]
        ]
    elif dimensions == 4:
        return [
            [0, 0, 0, 0],
            [0, 0, 0, 1],
            [0, 0, 1, 0],
            [0, 0, 1, 1],

            [0, 1, 0, 0],
            [0, 1, 0, 1],
            [0, 1, 1, 0],
            [0, 1, 1, 1],

            [1, 0, 0, 0],
            [1, 0, 0, 1],
            [1, 0, 1, 0],
            [1, 0, 1, 1],

            [1, 1, 0, 0],
            [1, 1, 0, 1],
            [1, 1, 1, 0],
            [1, 1, 1, 0]
        ]


def test_data_bipolar(dimensions):
    if dimensions == 2:
        return [
            [-1, -1],
            [-1, 1],
            [1, -1],
            [1, 1]
        ]
    elif dimensions == 3:
        return [
            [-1, -1, -1],
            [-1, -1, 1],

            [-1, 1, -1],
            [-1, 1, 1],

            [1, -1, -1],
            [1, -1, 1],

            [1, 1, -1],
            [1, 1, 1]
        ]
    elif dimensions == 4:
        return [
            [-1, -1, -1, -1],
            [-1, -1, -1, 1],
            [-1, -1, 1, -1],
            [-1, -1, 1, 1],

            [-1, 1, -1, -1],
            [-1, 1, -1, 1],
            [-1, 1, 1, -1],
            [-1, 1, 1, 1],

            [1, -1, -1, -1],
            [1, -1, -1, 1],
            [1, -1, 1, -1],
            [1, -1, 1, 1],

            [1, 1, -1, -1],
            [1, 1, -1, 1],
            [1, 1, 1, -1],
            [1, 1, 1, -1]
        ]


def dimension_test(dim, res_func, bipolar=False):
    print("|", end='')
    for i in range(1, dim + 1):
        print(" x" + str(i) + " ", end='')
        print("|", end='')
    print(" y |")

    data = test_data(dim) if not bipolar else test_data_bipolar(dim)
    for i in data:
        print("|", end='')
        for j in i:
            if j < 0:
                print("  " + str(j) + "|", end='')
            else:
                print("  " + str(j) + " |", end='')
        print(" " + str(res_func(i)) + " |", end='')
        print()
