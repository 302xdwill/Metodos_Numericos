import numpy as np

def derivada_irregular(X, Y):
    N = len(X)
    derivadas = np.zeros(N)
    for i in range(1, N - 1):
        dx_izq = X[i] - X[i-1]
        dx_der = X[i+1] - X[i]
        derivadas[i] = (Y[i+1] - Y[i-1]) / (dx_izq + dx_der)
    derivadas[0] = (Y[1] - Y[0]) / (X[1] - X[0])
    derivadas[N-1] = (Y[N-1] - Y[N-2]) / (X[N-1] - X[N-2])
    return derivadas

def derivada_lagrange(X, Y, x0):
    x0_, x1_, x2_ = X[0], X[1], X[2]
    y0_, y1_, y2_ = Y[0], Y[1], Y[2]
    term1 = y0_ * (2*x0 - x1_ - x2_) / ((x0_ - x1_)*(x0_ - x2_))
    term2 = y1_ * (2*x0 - x0_ - x2_) / ((x1_ - x0_)*(x1_ - x2_))
    term3 = y2_ * (2*x0 - x0_ - x1_) / ((x2_ - x0_)*(x2_ - x1_))
    return term1 + term2 + term3

z_cm = np.array([0.0, 1.25, 3.75])  
T_C = np.array([13.5, 12.0, 10.0])  

derivadas = derivada_irregular(z_cm, T_C)
grad_central = derivadas[0]  

grad_lagrange = derivada_lagrange(z_cm, T_C, 0.0)  

grad_lagrange_m = grad_lagrange * 100

k = 3.5e-7      
rho = 1800      
C = 840        

q = -k * rho * C * grad_lagrange_m

print("=== CÁLCULO DEL FLUJO DE CALOR BAJO EL SUELO ===")
print(f"Gradiente (método irregular)     : {grad_central:.6f} °C/cm")
print(f"Gradiente (método Lagrange)      : {grad_lagrange:.6f} °C/cm")
print(f"Gradiente convertido a °C/m      : {grad_lagrange_m:.6f} °C/m")
print(f"Flujo de calor q(z=0)            : {q:.2f} W/m²")


