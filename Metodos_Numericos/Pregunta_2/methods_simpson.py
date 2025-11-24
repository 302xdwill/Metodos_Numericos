# methods_simpson.py
import math
import sympy as sp
import numpy as np

def build_function(expr_str):
    x = sp.symbols('x')
    expr = sp.sympify(expr_str)
    return sp.lambdify(x, expr, 'math')

def simpson_13_compuesto(f, a, b, n):
    if n % 2 == 1:
        raise ValueError("n debe ser par para Simpson 1/3 compuesto.")
    h = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n):
        x = a + i * h
        s += 4 * f(x) if i % 2 == 1 else 2 * f(x)
    I = s * h / 3
    return I, h

def integral_exacta(expr_str, a, b):
    x = sp.symbols('x')
    expr = sp.sympify(expr_str)
    val = sp.integrate(expr, (x, a, b))
    return float(val)

def cargar_problema_txt(path):
    # formato robusto: acepta "funcion = ...", "a = ...", "b = ...", "n = ..."
    funcion = None; a = None; b = None; n = None
    with open(path, "r", encoding="utf-8") as f:
        for linea in f:
            linea = linea.strip()
            if not linea or "=" not in linea: 
                continue
            clave, valor = linea.split("=", 1)
            clave = clave.strip().lower()
            valor = valor.strip()
            if clave in ("funcion", "func", "f"):
                funcion = valor
            elif clave == "a":
                a = float(valor)
            elif clave == "b":
                b = float(valor)
            elif clave == "n":
                n = int(valor)
    if funcion is None or a is None or b is None or n is None:
        raise ValueError("Archivo incompleto: debe contener funcion, a, b y n.")
    return funcion, a, b, n

def cargar_problema_coma(path):
    # formato sencillo con comas: expr,a,b,n
    with open(path, "r", encoding="utf-8") as f:
        txt = f.read().strip()
    parts = [p.strip() for p in txt.split(",") if p.strip()!=""]
    if len(parts) < 4:
        raise ValueError("Archivo con formato coma incorrecto. Debe ser: expr,a,b,n")
    expr = parts[0]
    a = float(parts[1]); b = float(parts[2]); n = int(parts[3])
    return expr, a, b, n
