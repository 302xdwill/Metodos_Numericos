import math
import numpy as np

def f(x):
    return (4*x**3)/(x**(2/5)) - (9*x**2)/(x**(4/3))

def F(x):
    return (10/9)*x**(18/5) - (27/5)*x**(5/3)

def regla_compuesta_simpson(f, a, b, n):
    h = (b - a) / n
    XI0 = f(a) + f(b)
    XI1 = 0.0
    XI2 = 0.0
    for i in range(1, n):
        X = a + i * h
        if i % 2 == 0:
            XI2 += f(X)
        else:
            XI1 += f(X)
    XI = h * (XI0 + 2 * XI2 + 4 * XI1) / 3
    return XI

def cuarta_derivada_num(f, x, h=1e-4):
    return (f(x-2*h) - 4*f(x-h) + 6*f(x) - 4*f(x+h) + f(x+2*h)) / (h**4)

a = 2.0
b = 4.0
n = 12

valor_exacto = F(b) - F(a)
valor_aprox = regla_compuesta_simpson(f, a, b, n)
error_real = abs(valor_exacto - valor_aprox)

xs = np.linspace(a, b, 1000)
max_f4 = max(abs(cuarta_derivada_num(f, xi)) for xi in xs)
h = (b - a) / n
error_estimado = ((b - a) / 180) * (h**4) * max_f4

print(f"Valor exacto: {valor_exacto:.6f}")
print(f"Valor aproximado: {valor_aprox:.6f}")
print(f"Error real: {error_real:.6f}")
print(f"Error estimado: {error_estimado:.6f}")
