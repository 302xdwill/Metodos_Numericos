import numpy as np
import matplotlib.pyplot as plt

def derivada_central_base(F, X, H):
    return (F(X + H) - F(X - H)) / (2 * H)

def extrapolacion_richardson_derivada(F, X, H_inicial):
    A1 = derivada_central_base(F, X, H_inicial)
    H_reducido = H_inicial / 2
    A2 = derivada_central_base(F, X, H_reducido)
    DERIVADA_MEJORADA = (4 * A2 - A1) / 3
    return DERIVADA_MEJORADA

def f(x):
    return 1 / (1 + 25 * x**2)

a = -0.5
b = 0.5
h_inicial = 0.05
valores_x = np.linspace(a, b, 41)

derivadas = []
for x in valores_x:
    d = extrapolacion_richardson_derivada(f, x, h_inicial)
    derivadas.append(d)

indice_cercano_cero = np.argmin(np.abs(derivadas))
x_optimo = valores_x[indice_cercano_cero]

print(f"{'x':>10}{'f(x)':>15}{'f\'(x)':>15}")
for i in range(len(valores_x)):
    print(f"{valores_x[i]:>10.3f}{f(valores_x[i]):>15.6f}{derivadas[i]:>15.6f}")

print(f"\nEl valor de x donde la derivada se aproxima más a cero es: x = {x_optimo:.4f}")
print(f"f(x) en ese punto: {f(x_optimo):.6f}")

# --- Gráfica ---
plt.figure(figsize=(8,5))
plt.plot(valores_x, [f(x) for x in valores_x], label='f(x)', color='blue')
plt.plot(valores_x, derivadas, label="f'(x) (derivada numérica)", color='red')
plt.axhline(0, color='black', linestyle='--', linewidth=1)
plt.scatter(x_optimo, f(x_optimo), color='green', s=80, zorder=5, label=f'Máximo en x={x_optimo:.3f}')
plt.title('Optimización Numérica - Función de Runge')
plt.xlabel('x')
plt.ylabel('Valor')
plt.legend()
plt.grid(True)
plt.show()
