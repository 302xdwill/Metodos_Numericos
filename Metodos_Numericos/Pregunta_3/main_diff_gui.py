import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import matplotlib.pyplot as plt
import numpy as np
from methods_diff import *

def ejecutar():
    try:
        mode = combo.get()
        if mode == "Problema (examen)":
            expr = "5 + 4/x**3"
            entry_func.delete(0, tk.END); entry_func.insert(0, expr)
            a = float(entry_a.get()); b = float(entry_b.get()); h = float(entry_h.get())
        elif mode == "Ingresar manualmente":
            expr = entry_func.get().strip()
            a = float(entry_a.get()); b = float(entry_b.get()); h = float(entry_h.get())
        else:
            if archivo_path.get()=="":
                messagebox.showerror("Error","Seleccione archivo primero")
                return
            expr,a,b,h = cargar_problema_file(archivo_path.get())
            entry_func.delete(0, tk.END); entry_func.insert(0, expr)
            entry_a.delete(0, tk.END); entry_a.insert(0, str(a))
            entry_b.delete(0, tk.END); entry_b.insert(0, str(b))
            entry_h.delete(0, tk.END); entry_h.insert(0, str(h))

        f_func, expr_sym = f_expr_to_func(expr)
        d1_str, d2_str = derivative_analytic(expr)
        xs, ys = tabulate(f_func, a, b, h)
        x0 = 2.0
        x = __import__('sympy').symbols('x')
        true_d1 = float(__import__('sympy').diff(__import__('sympy').sympify(expr), x).subs(x, x0))
        f = f_func
        vf = forward_diff_3pt(f, x0, h)
        vb = backward_diff_3pt(f, x0, h)
        vc = central_diff_3pt(f, x0, h)
        ef = percent_error(true_d1, vf)
        eb = percent_error(true_d1, vb)
        ec = percent_error(true_d1, vc)
        text_result.delete("1.0", tk.END)
        text_result.insert(tk.END, "=== RESULTADOS ===\n")
        text_result.insert(tk.END, f"Función: {expr}\n")
        text_result.insert(tk.END, f"Dérivadas analíticas:\n  f' = {d1_str}\n  f'' = {d2_str}\n\n")
        text_result.insert(tk.END, "Tabla f(x):\n")
        for xi, yi in zip(xs, ys):
            text_result.insert(tk.END, f"{xi:>6.3f}    {yi:>12.6f}\n")
        text_result.insert(tk.END, "\nValor verdadero f'(2): {:.6f}\n".format(true_d1))
        text_result.insert(tk.END, "Aproximaciones con h={:.5f}:\n".format(h))
        text_result.insert(tk.END, "Forward 3-pt: {:.6f}, Error%: {:.4f}\n".format(vf, ef))
        text_result.insert(tk.END, "Backward 3-pt: {:.6f}, Error%: {:.4f}\n".format(vb, eb))
        text_result.insert(tk.END, "Central 3-pt: {:.6f}, Error%: {:.4f}\n".format(vc, ec))
    except Exception as e:
        messagebox.showerror("Error", str(e))

def cargar_problema_file(path):
    func=None;a=None;b=None;h=None
    with open(path,'r',encoding='utf-8') as f:
        txt=f.read().strip()
    if ',' in txt and txt.count(',')>=3:
        parts=[p.strip() for p in txt.split(',')]
        return parts[0], float(parts[1]), float(parts[2]), float(parts[3])
    for line in txt.splitlines():
        if '=' not in line: continue
        k,v=line.split('=',1)
        k=k.strip().lower(); v=v.strip()
        if k in ('funcion','func','f'): func=v
        elif k=='a': a=float(v)
        elif k=='b': b=float(v)
        elif k=='h': h=float(v)
    if func is None or a is None or b is None or h is None:
        raise ValueError("Archivo incompleto")
    return func,a,b,h

def graficar():
    try:
        expr=entry_func.get().strip()
        f,_ = f_expr_to_func(expr)
        a=float(entry_a.get()); b=float(entry_b.get())
        xs=np.linspace(a,b,300); ys=[f(xx) for xx in xs]
        plt.plot(xs,ys); plt.grid(True); plt.title("f(x)"); plt.show()
    except Exception as e:
        messagebox.showerror("Error", str(e))

def guardar():
    txt=text_result.get("1.0",tk.END)
    if not txt.strip():
        messagebox.showinfo("Info","No hay resultados")
        return
    p = filedialog.asksaveasfilename(defaultextension=".txt")
    if p:
        with open(p,'w',encoding='utf-8') as f:
            f.write(txt)
        messagebox.showinfo("Guardado","Archivo guardado")

def limpiar_campos():
    entry_func.delete(0, tk.END)
    entry_a.delete(0, tk.END)
    entry_b.delete(0, tk.END)
    entry_h.delete(0, tk.END)
    archivo_path.set("")
    text_result.delete("1.0", tk.END)


root=tk.Tk(); root.title("Diferenciacion alta exactitud"); root.geometry("820x560")
tk.Label(root,text="Modo:").pack()
combo=ttk.Combobox(root, values=["Problema (examen)","Ingresar manualmente","Cargar archivo"])
combo.current(0); combo.pack()
frm=tk.Frame(root); frm.pack(pady=8)
tk.Label(frm,text="Función f(x):").grid(row=0,column=0)
entry_func=tk.Entry(frm,width=50); entry_func.grid(row=0,column=1)
tk.Label(frm,text="a:").grid(row=1,column=0); entry_a=tk.Entry(frm,width=12); entry_a.grid(row=1,column=1,sticky='w')
tk.Label(frm,text="b:").grid(row=2,column=0); entry_b=tk.Entry(frm,width=12); entry_b.grid(row=2,column=1,sticky='w')
tk.Label(frm,text="h:").grid(row=3,column=0); entry_h=tk.Entry(frm,width=12); entry_h.grid(row=3,column=1,sticky='w')
entry_func.insert(0,"5+4/x**3"); entry_a.insert(0,"1.85"); entry_b.insert(0,"2.15"); entry_h.insert(0,"0.05")
archivo_path=tk.StringVar(); tk.Button(root,text="Seleccionar archivo",command=lambda: archivo_path.set(filedialog.askopenfilename(filetypes=[('txt','*.txt')] ))).pack()
tk.Label(root,textvariable=archivo_path).pack()
btns=tk.Frame(root); btns.pack(pady=6)
tk.Button(btns,text="Calcular",command=ejecutar).grid(row=0,column=0,padx=6)
tk.Button(btns,text="Graficar",command=graficar).grid(row=0,column=1,padx=6)
tk.Button(btns,text="Guardar resultados",command=guardar).grid(row=0,column=2,padx=6)
tk.Button(btns, text="Limpiar", command=limpiar_campos).grid(row=0, column=3, padx=6)

text_result=tk.Text(root,width=100,height=20); text_result.pack(pady=8)
root.mainloop()
