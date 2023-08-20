import numpy as np
from evaluate import f, f_prime

EPSILON = 10 ** -12

def newton_raphson(function_str, x_0, k_max, epsilon=EPSILON) :

    table = []

    k = 0

    x_k = x_0 - (f(function_str, x_0)/f_prime(function_str, x_0))

    print(x_k)
    print(np.abs(f(function_str, x_k)))

    while k < k_max and np.abs(f(function_str, x_k)) > epsilon:

        table.append([k, x_k])

        x_k = x_k - (f(function_str, x_k)/f_prime(function_str, x_k))
        k = k + 1


    return table


def main():
    print(newton_raphson('2x + -e^-x', 1, 100))

