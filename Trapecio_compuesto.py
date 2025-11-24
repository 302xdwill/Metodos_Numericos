import numpy as np
import math

def f(x):
    return (math.sin(x))**2 * (math.cos(x))**3

def metodo_trapezoidal_compuesto(f, a, b, n):
    h = (b - a) / n
    suma = f(a) + f(b)
    for i in range(1, n):
        xi = a + i * h
        suma += 2 * f(xi)
    area = (h / 2) * suma
    return area

a = math.pi / 2
b = 3 * math.pi / 2
n = 12
h = (b - a) / n

I_aprox = metodo_trapezoidal_compuesto(f, a, b, n)
I_exacta = -0.2666
error_real = abs(I_exacta - I_aprox)
error_estimado = -((b - a) / 12) * h**2

print("=== RESULTADOS ===")
print(f"h = {h:.4f}")
print(f"Integral exacta = {I_exacta:.4f}")
print(f"Integral método del trapecio = {I_aprox:.4f}")
print(f"Error real = {error_real:.4f}")
print(f"Error estimado = {error_estimado:.4f}")
