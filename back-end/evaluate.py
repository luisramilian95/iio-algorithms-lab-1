import re
import sympy 

x, y, z, e = sympy.symbols("x y z e")

MULTIPLICATION_REGULAR = r'(\d+(\.\d+)?)([a-z])'

def multiplication_case(match_object):

    new_expression = ""

    for match_group in range(1, len(match_object.groups())):
        if match_object.group(match_group) is not None:
            new_expression +=  match_object.group(match_group)
    
    if match_object.group(3) is not None:
        new_expression += "*" + match_object.group(3)

    return new_expression

def evaluate_function(function_str, x_, y_ = 0, z_ = 0):

    function_parsed = function_str.replace('^', '**')
    function_parsed = re.sub(MULTIPLICATION_REGULAR, multiplication_case, function_str)

    expression = sympy.sympify(function_parsed)

    return expression.evalf(subs={x: x_, y : y_, z : z_, e : sympy.E})

def f(function_str, x):
    return evaluate_function(function_str, x)

def f_prime(function_str, x):
    delta_x = 0.00001
    return float((evaluate_function(function_str, x + delta_x) - evaluate_function(function_str,x)) / delta_x)