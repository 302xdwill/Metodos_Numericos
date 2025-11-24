import tkinter as tk
from tkinter import filedialog, messagebox
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

from methods_richardson import (
    funcion_T,
    derivada_verdadera,
    tabular_function,
    extrapolacion_richardson_derivada
)

def ejecutar():
    try:
        X = float(entrada_x.get())
        H = float(entrada_h.get())

        valor_real = derivada_verdadera(X)
        A1, A2, Richardson = extrapolacion_richardson_derivada(funcion_T, X, H)
        error_pct = abs((valor_real - Richardson)/valor_real)*100 if valor_real != 0 else float('inf')

        salida.delete(1.0, tk.END)
        salida.insert(tk.END, f"Valor verdadero T'(x): {valor_real:.8f}\n")
        salida.insert(tk.END, f"Aproximación centrada base A1: {A1:.8f}\n")
        salida.insert(tk.END, f"Aproximación centrada h/2 A2: {A2:.8f}\n")
        salida.insert(tk.END, f"Richardson mejorado: {Richardson:.8f}\n")
        salida.insert(tk.END, f"Error porcentual: {error_pct:.6f} %\n")

    except Exception as e:
        messagebox.showerror("Error", str(e))

def cargar_archivo():
    try:
        ruta = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if not ruta:
            return
        with open(ruta, "r", encoding="utf-8") as f:
            txt = f.read().strip()
        # acepta formato simple "x = 0.5\nh = 0.1" o "0.5,0.1"
        if ',' in txt:
            parts = [p.strip() for p in txt.split(',') if p.strip()]
            entrada_x.delete(0, tk.END); entrada_x.insert(0, parts[0])
            entrada_h.delete(0, tk.END); entrada_h.insert(0, parts[1])
        else:
            for line in txt.splitlines():
                if '=' in line:
                    k,v = line.split('=',1)
                    k=k.strip().lower(); v=v.strip()
                    if k=='x':
                        entrada_x.delete(0, tk.END); entrada_x.insert(0, v)
                    elif k=='h':
                        entrada_h.delete(0, tk.END); entrada_h.insert(0, v)
        messagebox.showinfo("Info", "Archivo cargado.")
    except Exception as e:
        messagebox.showerror("Error", "Formato de archivo inválido.")

def graficar():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        X = float(entrada_x.get())

        # preparar funciones simbólicas para derivada analítica (más preciso en graf)
        x = sp.symbols('x')
        Texpr = sp.exp(-0.5*x)*sp.cos(2*x)
        Tprime_expr = sp.diff(Texpr, x)
        T = sp.lambdify(x, Texpr, "numpy")
        Tp = sp.lambdify(x, Tprime_expr, "numpy")

        xs = np.linspace(a, b, 400)
        ys = T(xs)
        yps = Tp(xs)

        plt.figure(figsize=(8,4.5))
        plt.plot(xs, ys, label="T(x)")
        plt.plot(xs, yps, label="T'(x) (analítica)", linestyle='--')
        # marcar punto X
        TX = T(X)
        TPX = Tp(X)
        plt.scatter([X], [TX], color='red', zorder=5, label=f"T({X})")
        plt.scatter([X], [TPX], color='green', zorder=5, label=f"T'({X})")
        plt.axvline(X, color='gray', linewidth=0.7, linestyle=':')
        plt.title("T(x) y su derivada analítica")
        plt.xlabel("x")
        plt.grid(True)
        plt.legend()
        plt.show()

    except Exception as e:
        messagebox.showerror("Error", str(e))

def guardar():
    txt = salida.get("1.0", tk.END)
    if not txt.strip():
        messagebox.showinfo("Info", "No hay resultados para guardar.")
        return
    ruta = filedialog.asksaveasfilename(defaultextension=".txt")
    if ruta:
        with open(ruta, "w", encoding="utf-8") as f:
            f.write(txt)
        messagebox.showinfo("Guardado", "Archivo guardado correctamente.")

# VENTANA PRINCIPAL
root = tk.Tk()
root.title("Extrapolación de Richardson - GUI")
root.geometry("700x420")

# Entradas de control
frame = tk.Frame(root); frame.pack(padx=8, pady=8, fill='x')

tk.Label(frame, text="x (punto):").grid(row=0, column=0, sticky='e')
entrada_x = tk.Entry(frame, width=12); entrada_x.grid(row=0, column=1, sticky='w')
entrada_x.insert(0, "0.5")

tk.Label(frame, text="h inicial:").grid(row=0, column=2, sticky='e')
entrada_h = tk.Entry(frame, width=12); entrada_h.grid(row=0, column=3, sticky='w')
entrada_h.insert(0, "0.1")

tk.Label(frame, text="a (graf min):").grid(row=1, column=0, sticky='e')
entry_a = tk.Entry(frame, width=12); entry_a.grid(row=1, column=1, sticky='w')
entry_a.insert(0, "0.3")

tk.Label(frame, text="b (graf max):").grid(row=1, column=2, sticky='e')
entry_b = tk.Entry(frame, width=12); entry_b.grid(row=1, column=3, sticky='w')
entry_b.insert(0, "0.7")

btn_frame = tk.Frame(root); btn_frame.pack(pady=6)
tk.Button(btn_frame, text="Cargar archivo", command=cargar_archivo).grid(row=0, column=0, padx=6)
tk.Button(btn_frame, text="Resolver", command=ejecutar).grid(row=0, column=1, padx=6)
tk.Button(btn_frame, text="Graficar", command=graficar).grid(row=0, column=2, padx=6)
tk.Button(btn_frame, text="Guardar resultados", command=guardar).grid(row=0, column=3, padx=6)

# Salida
salida = tk.Text(root, width=86, height=16)
salida.pack(padx=8, pady=6)

root.mainloop()
