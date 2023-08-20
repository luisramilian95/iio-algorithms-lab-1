import numpy as np
from evaluate import f, f_prime


EPSILON = 10 ** -12


def bisection(function_str, a, b, k_max, epsilon = EPSILON):
    
    table = []

    k = 0
    x_k = (a + b) / 2

    while k < k_max and np.abs(f(function_str,x_k)) > epsilon :
        if f(function_str, a) * f(function_str,x_k) < 0 :
            b = x_k
        else :
            a = x_k

        table.append([k, x_k, f(function_str,a), f(function_str,x_k)])

        k= k + 1
        x_k = (a + b) / 2


    return table


def main():
    print(bisection('2x + -e^-x', 0, 1, 100))
