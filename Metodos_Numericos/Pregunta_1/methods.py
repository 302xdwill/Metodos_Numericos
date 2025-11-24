import numpy as np
import sympy as sp
import math

# ============================================================
#  FUNCIÓN BASE PARA EL PROBLEMA DEL EXAMEN
# ============================================================

def f_examen(x):
    return 3 * (x**2) * math.sin(x)

# ============================================================
#  FUNCIÓN MANUAL DEFINIDA POR EL USUARIO
# ============================================================

def build_function(expr_str):
    x = sp.symbols('x')
    expr = sp.sympify(expr_str)
    return sp.lambdify(x, expr, 'math')

# ============================================================
#  MÉTODO DEL TRAPECIO COMPUESTO
# ============================================================

def metodo_trapezoidal_compuesto(f, a, b, n):
    h = (b - a) / n
    suma = f(a) + f(b)
    for i in range(1, n):
        xi = a + h * i
        suma += 2 * f(xi)
    return (h / 2) * suma, h

# ============================================================
#  VALOR EXACTO DE LA INTEGRAL
# ============================================================

def integral_exacta(expr_str, a, b):
    x = sp.symbols('x')
    expr = sp.sympify(expr_str)
    return float(sp.integrate(expr, (x, a, b)))

# ============================================================
#  CARGAR PROBLEMA DESDE ARCHIVO — CORREGIDO Y ROBUSTO
# ============================================================

def cargar_problema(path):

    funcion = None
    a = None
    b = None
    n = None

    with open(path, "r", encoding="utf-8") as file:
        for linea in file:
            linea = linea.strip()
            if "=" not in linea:
                continue

            clave, valor = linea.split("=", 1)
            clave = clave.strip().lower()
            valor = valor.strip()

            if clave == "funcion":
                funcion = valor
            elif clave == "a":
                a = float(valor)
            elif clave == "b":
                b = float(valor)
            elif clave == "n":
                n = int(valor)

    if funcion is None or a is None or b is None or n is None:
        raise ValueError("Error: el archivo no contiene todos los campos requeridos.")

    return funcion, a, b, n
