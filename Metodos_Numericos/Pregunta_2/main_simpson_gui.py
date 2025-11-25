# main_simpson_gui.py
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import matplotlib.pyplot as plt
import numpy as np
from methods_simpson import *

def ejecutar():
    modo = combo.get()
    try:
        if modo == "Problema (examen)":
            expr = "1/sqrt(3-2*x)"
            f = build_function(expr)
            a = float(entry_a.get())
            b = float(entry_b.get())
            n = int(entry_n.get())
            expr_used = expr

        elif modo == "Ingresar manualmente":
            expr = entry_func.get().strip()
            f = build_function(expr)
            a = float(entry_a.get())
            b = float(entry_b.get())
            n = int(entry_n.get())
            expr_used = expr

        elif modo == "Cargar archivo":
            ruta = archivo_path.get()
            if not ruta:
                messagebox.showerror("Error", "Seleccione archivo primero")
                return
            # intentar formato llave=valor primero
            try:
                expr, a, b, n = cargar_problema_txt(ruta)
            except Exception:
                expr, a, b, n = cargar_problema_coma(ruta)
            entry_func.delete(0, tk.END); entry_func.insert(0, expr)
            entry_a.delete(0, tk.END); entry_a.insert(0, str(a))
            entry_b.delete(0, tk.END); entry_b.insert(0, str(b))
            entry_n.delete(0, tk.END); entry_n.insert(0, str(n))
            f = build_function(expr)
            expr_used = expr

        else:
            messagebox.showerror("Error","Seleccione modo")
            return

        if n % 2 == 1:
            messagebox.showwarning("Aviso","n impar — Simpson 1/3 requiere n par. Se sumará 1 a n.")
            n += 1

        I_app, h = simpson_13_compuesto(f, a, b, n)
        I_exact = integral_exacta(expr_used, a, b)
        err_real = abs(I_exact - I_app)
        # estimado de Simpson (error ~ -(b-a)/180 * h^4 * f^(4)(ξ)) -> usamos forma común: (b-a)/180 * h^4 * max|f4|
        # Para estimado simple sin f4, mostramos la fórmula parcial (user can refine). We'll estimate as 0 if cannot compute.
        try:
            x = __import__("sympy").symbols('x')
            f4 = __import__("sympy").diff(__import__("sympy").sympify(expr_used), (x,4))
            # approximate maximum of |f4| in [a,b] by sampling
            f4f = __import__("sympy").lambdify(x, f4, 'math')
            xs = np.linspace(a,b,200)
            vals = [abs(f4f(xx)) for xx in xs]
            M4 = max(vals)
            err_est = (b-a)/180 * h**4 * M4
        except Exception:
            err_est = None

        text_result.delete("1.0", tk.END)
        text_result.insert(tk.END, "=== RESULTADOS (Simpson 1/3 compuesto) ===\n")
        text_result.insert(tk.END, f"Función: {expr_used}\n")
        text_result.insert(tk.END, f"Intervalo: [{a}, {b}]\n")
        text_result.insert(tk.END, f"n (usado): {n}\n")
        text_result.insert(tk.END, f"h = {h}\n\n")
        text_result.insert(tk.END, f"Valor exacto: {I_exact}\n")
        text_result.insert(tk.END, f"Valor aproximado (Simpson): {I_app}\n")
        text_result.insert(tk.END, f"Error real: {err_real}\n")
        text_result.insert(tk.END, f"Error estimado (vía M4): {err_est}\n")

    except Exception as e:
        messagebox.showerror("Error", str(e))

def seleccionar_archivo():
    p = filedialog.askopenfilename(filetypes=[("Txt","*.txt"),("All","*.*")])
    if p:
        archivo_path.set(p)

def graficar():
    try:
        expr = entry_func.get().strip()
        f = build_function(expr)
        a = float(entry_a.get()); b = float(entry_b.get())
        xs = np.linspace(a,b,400)
        ys = [f(xx) for xx in xs]
        plt.plot(xs, ys)
        plt.title("f(x)")
        plt.grid(True)
        plt.show()
    except Exception as e:
        messagebox.showerror("Error", str(e))

def guardar():
    txt = text_result.get("1.0", tk.END)
    if not txt.strip():
        messagebox.showinfo("Info","No hay resultados para guardar")
        return
    p = filedialog.asksaveasfilename(defaultextension=".txt")
    if p:
        with open(p,"w",encoding="utf-8") as f:
            f.write(txt)
        messagebox.showinfo("Guardado","Archivo guardado")

def limpiar_campos():
    entry_func.delete(0, tk.END)
    entry_a.delete(0, tk.END)
    entry_b.delete(0, tk.END)
    entry_n.delete(0, tk.END)
    archivo_path.set("")
    text_result.delete("1.0", tk.END)

root = tk.Tk()
root.title("Simpson 1/3 - GUI")
root.geometry("820x560")

tk.Label(root, text="Modo:").pack()
combo = ttk.Combobox(root, values=["Problema (examen)","Ingresar manualmente","Cargar archivo"])
combo.current(0); combo.pack()

frm = tk.Frame(root); frm.pack(pady=8)
tk.Label(frm,text="Función f(x):").grid(row=0,column=0)
entry_func = tk.Entry(frm,width=50); entry_func.grid(row=0,column=1)
tk.Label(frm,text="a:").grid(row=1,column=0); entry_a = tk.Entry(frm,width=12); entry_a.grid(row=1,column=1,sticky='w')
tk.Label(frm,text="b:").grid(row=2,column=0); entry_b = tk.Entry(frm,width=12); entry_b.grid(row=2,column=1,sticky='w')
tk.Label(frm,text="n:").grid(row=3,column=0); entry_n = tk.Entry(frm,width=12); entry_n.grid(row=3,column=1,sticky='w')

# default values for exam problem
entry_func.insert(0,"1/sqrt(3-2*x)")
entry_a.insert(0,"0")
entry_b.insert(0,"1")
entry_n.insert(0,"8")

archivo_path = tk.StringVar()
tk.Button(root,text="Seleccionar archivo",command=seleccionar_archivo).pack()
tk.Label(root,textvariable=archivo_path).pack()

btns = tk.Frame(root); btns.pack(pady=6)
tk.Button(btns,text="Calcular",command=ejecutar).grid(row=0,column=0,padx=6)
tk.Button(btns,text="Graficar",command=graficar).grid(row=0,column=1,padx=6)
tk.Button(btns,text="Guardar resultados",command=guardar).grid(row=0,column=2,padx=6)
tk.Button(btns, text="Limpiar", command=limpiar_campos).grid(row=0, column=3, padx=6)

text_result = tk.Text(root,width=100,height=18)
text_result.pack(pady=8)

root.mainloop()
