import numpy as np
import sympy as sp

# -------------------------------------------
# FUNCIONES BASE DEL MÉTODO DE RICHARDSON
# -------------------------------------------

def derivada_central_base(F, X, H):
    """Aproximación centrada base O(h^2)."""
    return (F(X + H) - F(X - H)) / (2 * H)

def extrapolacion_richardson_derivada(F, X, H_inicial):
    """Mejora la derivada con extrapolación de Richardson."""
    A1 = derivada_central_base(F, X, H_inicial)
    H2 = H_inicial / 2
    A2 = derivada_central_base(F, X, H2)
    DERIVADA_MEJORADA = (4 * A2 - A1) / 3
    return A1, A2, DERIVADA_MEJORADA

# -------------------------------------------
# FUNCIÓN ANALÍTICA Y DERIVADA
# -------------------------------------------

def funcion_T(x):
    return np.exp(-0.5*x) * np.cos(2*x)

def derivada_verdadera(x):
    # T'(x) = d/dx ( e^{-0.5x} cos(2x) )
    # Usamos simbólico solo una vez
    X = sp.symbols('X')
    T = sp.exp(-0.5*X)*sp.cos(2*X)
    Tprime = sp.diff(T, X)
    fprime = sp.lambdify(X, Tprime, "numpy")
    return fprime(x)

# -------------------------------------------
# TABLA DE VALORES
# -------------------------------------------

def tabular_function(F, x0, xf, h):
    xs = np.arange(x0, xf + h/2, h)
    fs = F(xs)
    return xs, fs
