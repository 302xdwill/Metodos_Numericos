import numpy as np

def f(x):
    return np.exp(x)

def f_deriv_exacta(x):
    return np.exp(x)

def derivada_adelante(f, x, h):
    return (-3*f(x) + 4*f(x + h) - f(x + 2*h)) / (2*h)

def derivada_atras(f, x, h):
    return (3*f(x) - 4*f(x - h) + f(x - 2*h)) / (2*h)

def derivada_centrada(f, x, h):
    return (f(x - 2*h) - 8*f(x - h) + 8*f(x + h) - f(x + 2*h)) / (12*h)

x = 1.0
h = 0.001
valor_real = f_deriv_exacta(x)

adelante = derivada_adelante(f, x, h)
atras = derivada_atras(f, x, h)
centrada = derivada_centrada(f, x, h)

error_adelante = (adelante - valor_real) / valor_real * 100
error_atras = (atras - valor_real) / valor_real * 100
error_centrada = (centrada - valor_real) / valor_real * 100

print(f"{'Método':<20}{'Estimación':>15}{'Error (%)':>15}")
print(f"{'Hacia adelante':<20}{adelante:>15.6f}{error_adelante:>15.3f}")
print(f"{'Hacia atrás':<20}{atras:>15.6f}{error_atras:>15.3f}")
print(f"{'Centrada':<20}{centrada:>15.6f}{error_centrada:>15.3f}")
