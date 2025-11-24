import numpy as np
import math

def metodo_trapezoidal_simple(f, a, b):
    return (b - a) * (f(a) + f(b)) / 2

def metodo_simpson_simple(f, a, b):
    h = (b - a) / 2
    return (h / 3) * (f(a) + 4 * f(a + h) + f(b))

def exacta(f_prim, a, b):
    return f_prim(b) - f_prim(a)

a = 0
b = 2

def f1(x): return x**2
def F1(x): return x**3 / 3

def f2(x): return x**4
def F2(x): return x**5 / 5

def f3(x): return 1 / (x + 1)
def F3(x): return np.log(x + 1)

def f4(x): return np.sqrt(1 + x**2)
def F4(x): return 0.5 * (x * np.sqrt(1 + x**2) + np.log(x + np.sqrt(1 + x**2)))

def f5(x): return np.sin(x)
def F5(x): return -np.cos(x)

def f6(x): return np.exp(x)
def F6(x): return np.exp(x)

funciones = [
    ("(a) x^2", f1, F1),
    ("(b) x^4", f2, F2),
    ("(c) (x+1)^-1", f3, F3),
    ("(d) sqrt(1+x^2)", f4, F4),
    ("(e) sin(x)", f5, F5),
    ("(f) e^x", f6, F6)
]

print("Función\t\tValor exacto\tTrapecio\tSimpson")
for nombre, f, F in funciones:
    exacto = exacta(F, a, b)
    trap = metodo_trapezoidal_simple(f, a, b)
    simp = metodo_simpson_simple(f, a, b)
    print(f"{nombre}\t{exacto:.3f}\t\t{trap:.3f}\t\t{simp:.3f}")
