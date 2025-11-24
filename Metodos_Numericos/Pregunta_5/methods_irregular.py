import numpy as np

# -------------------------------------------------------------
# FUNCIÓN PRINCIPAL PARA DERIVADAS IRREGULARES
# -------------------------------------------------------------

def derivada_irregular(x, y):
    """
    Calcula derivadas numéricas para datos con espaciado irregular.
    Retorna una lista con las derivadas aproximadas para cada punto
    excepto los extremos (que no tienen fórmula válida de 3 puntos).
    """
    n = len(x)
    resultados = []

    for i in range(1, n - 1):
        x_prev, x_i, x_next = x[i-1], x[i], x[i+1]
        y_prev, y_i, y_next = y[i-1], y[i], y[i+1]

        dx1 = x_i - x_prev
        dx2 = x_next - x_i
        dx_total = x_next - x_prev

        deriv = ((dx1**2) * (y_next - y_i) + (dx2**2) * (y_i - y_prev)) / (dx1 * dx2 * dx_total)

        resultados.append((x_i, deriv))

    return resultados

# -------------------------------------------------------------
# TABLA
# -------------------------------------------------------------

def build_table(x, y):
    tabla = " t (min)      C (mol/L)\n"
    tabla += "-------------------------\n"
    for i in range(len(x)):
        tabla += f"{x[i]:<10}   {y[i]:<10}\n"
    return tabla
