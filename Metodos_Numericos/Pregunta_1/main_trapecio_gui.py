import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import matplotlib.pyplot as plt
import numpy as np
from methods import *

# ============================================================
#   FUNCIÓN PRINCIPAL DE CÁLCULO
# ============================================================

def ejecutar():
    opcion = combo.get()

    try:
        # =======================================================
        #  OPCIÓN 1: PROBLEMA DEL EXAMEN
        # =======================================================
        if opcion == "Problema 1 del examen":
            f_expr = "3*x**2*sin(x)"
            f = f_examen
            a = float(entry_a.get())
            b = float(entry_b.get())
            n = int(entry_n.get())

        # =======================================================
        #  OPCIÓN 2: MANUAL
        # =======================================================
        elif opcion == "Ingresar manualmente":
            f_expr = entry_func.get()
            f = build_function(f_expr)
            a = float(entry_a.get())
            b = float(entry_b.get())
            n = int(entry_n.get())

        # =======================================================
        #  OPCIÓN 3: ARCHIVO TXT
        # =======================================================
        elif opcion == "Cargar archivo":
            if archivo_path.get() == "":
                messagebox.showerror("Error", "Seleccione un archivo primero")
                return
            f_expr, a, b, n = cargar_problema(archivo_path.get())

            # Mostrar en GUI
            entry_func.delete(0, tk.END)
            entry_func.insert(0, f_expr)
            entry_a.delete(0, tk.END)
            entry_a.insert(0, str(a))
            entry_b.delete(0, tk.END)
            entry_b.insert(0, str(b))
            entry_n.delete(0, tk.END)
            entry_n.insert(0, str(n))

            f = build_function(f_expr)

        else:
            messagebox.showerror("Error", "Seleccione una opción válida")
            return


        # =======================================================
        #  CÁLCULOS
        # =======================================================
        I_aprox, h = metodo_trapezoidal_compuesto(f, a, b, n)
        I_exacta = integral_exacta(f_expr, a, b)
        error_real = abs(I_exacta - I_aprox)
        error_estimado = (b - a) / 12 * h**2

        # Mostrar resultados
        text_result.delete("1.0", tk.END)
        text_result.insert(tk.END, "=== RESULTADOS ===\n")
        text_result.insert(tk.END, f"Valor exacto: {I_exacta}\n")
        text_result.insert(tk.END, f"Valor aproximado (Trapecio): {I_aprox}\n")
        text_result.insert(tk.END, f"Error real: {error_real}\n")
        text_result.insert(tk.END, f"Error estimado: {error_estimado}\n")
        text_result.insert(tk.END, f"h = {h}\n")

    except Exception as e:
        messagebox.showerror("Error", str(e))

# ============================================================
#   GRAFICAR FUNCIÓN
# ============================================================

def graficar():
    try:
        f_expr = entry_func.get()
        f = build_function(f_expr)
        a = float(entry_a.get())
        b = float(entry_b.get())

        xs = np.linspace(a, b, 400)
        ys = [f(x) for x in xs]

        plt.plot(xs, ys)
        plt.title("Gráfica de la función")
        plt.grid(True)
        plt.show()

    except Exception as e:
        messagebox.showerror("Error", str(e))

# ============================================================
#   GUARDAR RESULTADOS
# ============================================================

def guardar():
    contenido = text_result.get("1.0", tk.END)
    if contenido.strip() == "":
        messagebox.showinfo("Aviso", "No hay resultados para guardar")
        return

    archivo = filedialog.asksaveasfilename(defaultextension=".txt")
    if archivo:
        with open(archivo, "w") as f:
            f.write(contenido)
        messagebox.showinfo("Guardado", "Archivo guardado correctamente")

# ============================================================
#   SELECCIONAR ARCHIVO TXT
# ============================================================

def seleccionar_archivo():
    path = filedialog.askopenfilename(filetypes=[("TXT", "*.txt")])
    archivo_path.set(path)

# ============================================================
#   GUI
# ============================================================

root = tk.Tk()
root.title("Método del Trapecio — GUI Completa")
root.geometry("800x600")

# Opción
tk.Label(root, text="Seleccione modo:").pack()
combo = ttk.Combobox(root, values=[
    "Problema 1 del examen",
    "Ingresar manualmente",
    "Cargar archivo"
])
combo.current(0)
combo.pack()

# Panel de entrada
frame_in = tk.Frame(root)
frame_in.pack(pady=10)

tk.Label(frame_in, text="Función f(x):").grid(row=0, column=0)
entry_func = tk.Entry(frame_in, width=40)
entry_func.grid(row=0, column=1)

tk.Label(frame_in, text="a:").grid(row=1, column=0)
entry_a = tk.Entry(frame_in, width=25)
entry_a.grid(row=1, column=1)

tk.Label(frame_in, text="b:").grid(row=2, column=0)
entry_b = tk.Entry(frame_in, width=25)
entry_b.grid(row=2, column=1)

tk.Label(frame_in, text="n:").grid(row=3, column=0)
entry_n = tk.Entry(frame_in, width=25)
entry_n.grid(row=3, column=1)

# Cargar archivo
archivo_path = tk.StringVar()
tk.Button(root, text="Seleccionar archivo", command=seleccionar_archivo).pack()
tk.Label(root, textvariable=archivo_path).pack()

# Botones
frame_btn = tk.Frame(root)
frame_btn.pack(pady=10)

tk.Button(frame_btn, text="Calcular", command=ejecutar).grid(row=0, column=0, padx=5)
tk.Button(frame_btn, text="Graficar", command=graficar).grid(row=0, column=1, padx=5)
tk.Button(frame_btn, text="Guardar", command=guardar).grid(row=0, column=2, padx=5)

# Resultados
text_result = tk.Text(root, width=80, height=20)
text_result.pack()

root.mainloop()
