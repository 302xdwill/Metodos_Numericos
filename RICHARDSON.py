import numpy as np

def derivada_central_base(F, X, H):
    return (F(X + H) - F(X - H)) / (2 * H)

def extrapolacion_richardson_derivada(F, X, H_inicial):
    A1 = derivada_central_base(F, X, H_inicial)
    H_reducido = H_inicial / 2
    A2 = derivada_central_base(F, X, H_reducido)
    DERIVADA_MEJORADA = (4 * A2 - A1) / 3
    return DERIVADA_MEJORADA

# --- Ejemplo de Uso ---

def mi_funcion_f(x):
    return -0.1*x**4 - 0.15*x**3 - 0.5*x**2 - 0.25*x + 1.2

punto_x = 0.5   
paso_h_inicial = 0.5

derivada_mejorada = extrapolacion_richardson_derivada(mi_funcion_f, punto_x, paso_h_inicial)

print(f"La derivada aproximada mejorada es: {derivada_mejorada}")