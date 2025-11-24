import tkinter as tk
from tkinter import filedialog, messagebox
import matplotlib.pyplot as plt
import numpy as np
from methods_irregular import derivada_irregular, build_table

# --------------------------------------------------------------------------------
# CALCULAR
# --------------------------------------------------------------------------------
def ejecutar():
    try:
        # Lectura de datos escritos
        x_vals = [float(v) for v in entrada_x.get().split(",")]
        y_vals = [float(v) for v in entrada_y.get().split(",")]

        resultados = derivada_irregular(x_vals, y_vals)

        salida.delete("1.0", tk.END)
        salida.insert(tk.END, "=== TABLA DE DATOS ===\n")
        salida.insert(tk.END, build_table(x_vals, y_vals))
        salida.insert(tk.END, "\n=== DERIVADAS APROXIMADAS ===\n\n")

        for t, d in resultados:
            salida.insert(tk.END, f"t = {t} min  ---> dC/dt ≈ {d:.6f} mol/L·min\n")

        salida.insert(tk.END, "\nSólo se calculan derivadas en los puntos internos.\n")

    except Exception as e:
        messagebox.showerror("Error", str(e))

# --------------------------------------------------------------------------------
# GRAFICAR
# --------------------------------------------------------------------------------
def graficar():
    try:
        x_vals = [float(v) for v in entrada_x.get().split(",")]
        y_vals = [float(v) for v in entrada_y.get().split(",")]

        plt.plot(x_vals, y_vals, marker='o')
        plt.title("Concentración vs Tiempo")
        plt.xlabel("t (min)")
        plt.ylabel("[C] (mol/L)")
        plt.grid(True)
        plt.show()

    except Exception as e:
        messagebox.showerror("Error", str(e))

# --------------------------------------------------------------------------------
# CARGAR ARCHIVO
# --------------------------------------------------------------------------------
def cargar_archivo():
    try:
        ruta = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if not ruta:
            return
        
        with open(ruta, "r") as f:
            data = f.read().strip().split("\n")
        
        x_line = data[0].replace("t=", "").strip()
        y_line = data[1].replace("C=", "").strip()

        entrada_x.delete(0, tk.END); entrada_x.insert(0, x_line)
        entrada_y.delete(0, tk.END); entrada_y.insert(0, y_line)

        messagebox.showinfo("Cargado", "Archivo cargado correctamente.")

    except:
        messagebox.showerror("Error", "Formato inválido.")

# --------------------------------------------------------------------------------
# GUARDAR
# --------------------------------------------------------------------------------
def guardar():
    txt = salida.get("1.0", tk.END)
    if not txt.strip():
        return messagebox.showinfo("Info", "Nada que guardar.")
    
    ruta = filedialog.asksaveasfilename(defaultextension=".txt")
    if ruta:
        with open(ruta, "w") as f:
            f.write(txt)
        messagebox.showinfo("Guardado", "Archivo guardado.")

# --------------------------------------------------------------------------------
# GUI
# --------------------------------------------------------------------------------
root = tk.Tk()
root.title("Derivadas — Datos Irregulares")
root.geometry("700x450")

frame = tk.Frame(root); frame.pack(pady=10)

tk.Label(frame, text="Valores de t (separados por coma):").grid(row=0, column=0)
entrada_x = tk.Entry(frame, width=50)
entrada_x.grid(row=0, column=1)
entrada_x.insert(0, "1.0,1.2,1.5,1.9")

tk.Label(frame, text="Valores de C (separados por coma):").grid(row=1, column=0)
entrada_y = tk.Entry(frame, width=50)
entrada_y.grid(row=1, column=1)
entrada_y.insert(0, "2.0000,1.8012,1.5032,1.1070")

btns = tk.Frame(root); btns.pack(pady=5)

tk.Button(btns, text="Calcular", command=ejecutar).grid(row=0, column=0, padx=5)
tk.Button(btns, text="Graficar", command=graficar).grid(row=0, column=1, padx=5)
tk.Button(btns, text="Cargar archivo", command=cargar_archivo).grid(row=0, column=2, padx=5)
tk.Button(btns, text="Guardar resultados", command=guardar).grid(row=0, column=3, padx=5)

salida = tk.Text(root, width=85, height=18)
salida.pack(pady=5)

root.mainloop()
