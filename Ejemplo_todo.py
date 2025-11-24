import numpy as np

def trapecio(f, a, b):
    return (b - a) * (f(a) + f(b)) / 2

def simpson(f, a, b):
    h = (b - a) / 2
    return (h / 3) * (f(a) + 4 * f(a + h) + f(b))

def exacta(f_prim, a, b):
    return f_prim(b) - f_prim(a)

a = 0
b = 2

funciones = {
    "(a) x^2": (lambda x: x**2, lambda x: x**3 / 3),
    "(b) x^4": (lambda x: x**4, lambda x: x**5 / 5),
    "(c) (x+1)^-1": (lambda x: 1/(x+1), lambda x: np.log(x+1)),
    "(d) sqrt(1+x^2)": (lambda x: np.sqrt(1+x**2), lambda x: 0.5*(x*np.sqrt(1+x**2) + np.log(x + np.sqrt(1+x**2)))),
    "(e) sin(x)": (lambda x: np.sin(x), lambda x: -np.cos(x)),
    "(f) e^x": (lambda x: np.exp(x), lambda x: np.exp(x))
}

print(f"{'Función':<15}{'Valor exacto':>15}{'Trapecio':>15}{'Simpson':>15}")
for nombre, (f, F) in funciones.items():
    exacto = exacta(F, a, b)
    trap = trapecio(f, a, b)
    simp = simpson(f, a, b)
    print(f"{nombre:<15}{exacto:>15.3f}{trap:>15.3f}{simp:>15.3f}")
