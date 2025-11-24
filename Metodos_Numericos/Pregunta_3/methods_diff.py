import math
import sympy as sp
import numpy as np

def f_expr_to_func(expr_str):
    x = sp.symbols('x')
    expr = sp.sympify(expr_str)
    return sp.lambdify(x, expr, 'math'), expr

def derivative_analytic(expr_str):
    x = sp.symbols('x')
    expr = sp.sympify(expr_str)
    d1 = sp.diff(expr, x)
    d2 = sp.diff(expr, x, 2)
    return str(sp.simplify(d1)), str(sp.simplify(d2))

def tabulate(f, a, b, h):
    xs = []
    ys = []
    n = int(round((b - a) / h)) + 1
    for i in range(n):
        x = a + i*h
        xs.append(x)
        ys.append(f(x))
    return xs, ys

def forward_diff_3pt(f, x, h):
    return ( -3*f(x) + 4*f(x+h) - f(x+2*h) ) / (2*h)

def backward_diff_3pt(f, x, h):
    return ( 3*f(x) - 4*f(x-h) + f(x-2*h) ) / (2*h)

def central_diff_3pt(f, x, h):
    return ( f(x+h) - f(x-h) ) / (2*h)

def percent_error(true, approx):
    if true == 0:
        return float('inf')
    return abs((true - approx)/true)*100
