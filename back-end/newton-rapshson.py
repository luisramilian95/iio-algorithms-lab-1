import numpy as np
from evaluate import f, f_prime
import pandas as pd

EPSILON = 10 ** -12

def newton_raphson(function_str, x_0, k_max, epsilon=EPSILON) :

    table = []

    k = 0

    x_k = x_0 - (f(function_str, x_0)/f_prime(function_str, x_0))

    while k < k_max and np.abs(f(function_str, x_k)) > epsilon:

        table.append([k, float(x_k)])

        x_k = x_k - (f(function_str, x_k)/f_prime(function_str, x_k))
        k = k + 1


    print(pd.DataFrame(table, columns=["x_k", "k"]))
    return pd.DataFrame(table, columns=["x_k", "k"])
