import numpy as np


epsilon = 10 ** -12

def bisection(f, a, b, k_max):
    
    table = []

    k = 0
    x_k = (a + b) / 2

    while k < k_max and np.sign(f(x_k)) > epsilon :
        if f(a) * f(x_k) < 0 :
            b = x_k
        else :
            a = x_k

        table.append([k, x_k, f(a), f(x_k)])

        k= k + 1
        x_k = (a + b) / 2


    return table


def derivable_function(x) :
    return x ** 2 + np.e ** x


def main():
    print(bisection(derivable_function, 0, 1, 10))