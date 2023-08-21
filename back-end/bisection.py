import numpy as np
from evaluate import f

import pandas as pd


EPSILON = 10 ** -12


def bisection(function_str, a, b, k_max, epsilon = EPSILON):
    
    table = []

    k = 0
    x_k = (a + b) / 2

    while k < k_max and np.abs(f(function_str,x_k)) > epsilon :

        f_a = f(function_str, a)
        f_x_k = f(function_str,x_k)

        if f_a * f_x_k < 0 :
            b = x_k
        else :
            a = x_k

        table.append([k, x_k, float(f_x_k)])

        k= k + 1
        x_k = (a + b) / 2

    return pd.DataFrame(table, columns=["k", "x_k", "error"])
