import numpy as np

def derivada_central_base(F, X, H):
    return (F(X + H) - F(X - H)) / (2 * H)

def extrapolacion_richardson_derivada(F, X, H_inicial1):
    A1 = derivada_central_base(F, X, H_inicial1)
    H_reducido = H_inicial1 / 2
    A2 = derivada_central_base(F, X, H_reducido)
    DERIVADA_MEJORADA = (4 * A2 - A1) / 3
    return DERIVADA_MEJORADA

# --- Ejemplo de Uso ---

def mi_funcion_f(x):
    return -x/(x**2+1)**3/2

punto_x = 2.5   
paso_h_inicial1 = 0.5
paso_h_inicial2 = 0.1

def extrapolacion_richardson_derivada(F, X, H_inicial2):
    A1 = derivada_central_base(F, X, H_inicial2)
    H_reducido = H_inicial2 / 2
    A2 = derivada_central_base(F, X, H_reducido)
    DERIVADA_MEJORADA = (4 * A2 - A1) / 3
    return DERIVADA_MEJORADA

derivada_mejorada1 = extrapolacion_richardson_derivada(mi_funcion_f, punto_x, paso_h_inicial1)
derivada_mejorada2 = extrapolacion_richardson_derivada(mi_funcion_f, punto_x, paso_h_inicial2)

print(f"La derivada aproximada mejorada con h inicial 0.5 es: {derivada_mejorada1}")
print(f"La derivada aproximada mejorada con h inicial 0.1 es: {derivada_mejorada2}")