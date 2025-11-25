### 📘 Métodos Numéricos 

Repositorio con la implementación de diversos métodos numéricos, cada uno estructurado con:

1. **Archivo del método** (lógica / algoritmo).
2. **Archivo main** (interfaz y ejecución).
3. **Archivo `.txt` del problema** para entrada manual.
4. **Archivo `.txt` para carga automática**.
5. **Manual de uso**.
6. **Algoritmo en pseudocódigo tipo libro**.

Incluye también gráficas cuando corresponde.

---

### 🛠️ Dependencias

Todos los métodos utilizan las siguientes dependencias:

pip install numpy
pip install matplotlib

Opcional (solo donde se use interfaz):

pip install tkinter

---

### ▶️ ¿Cómo Ejecutar Cualquier Método?

Cada carpeta contiene un archivo `main_xxx.py` con interfaz para:

* Cargar archivo TXT
* Editar datos manualmente
* Ejecutar el método
* Mostrar tabla
* (Cuando aplica) Generar gráfica
* Guardar resultados

Ejemplo:
python main_trapecio.py

---

### 📜 Contenido de Cada Entregable

Cada problema contiene:

✔️ 1. **Archivo del método (lógica del cálculo)**

Ej: `metodo_trapecio.py`
Incluye la implementación matemática exacta del método numérico.

---

✔️ 2. **Archivo main (interfaz gráfica o consola)**

Ej: `main_trapecio.py`
Permite cargar datos, procesarlos y mostrar resultados.

---

✔️ 3. **Problema en TXT para ingreso manual**

Ej: `problema_simpson.txt`
Contiene la descripción del ejercicio.

---

✔️ 4. **Archivo TXT para carga automática**

Ej: `carga_simpson.txt`
Formato amigable para lectura desde el programa.

---

✔️ 5. **Manual de uso**

Ej: `manual_richardson.md`
Explica dependencias, ejecución, cómo cargar archivos, etc.

---

📚 Métodos Incluidos

### 1️⃣ Método Trapezoidal Compuesto

* Valor exacto
* Aproximación con n=8
* Error real
* Gráfico de discretización

---

### 2️⃣ Método Simpson 1/3

* Integración analítica
* Aproximación con n=8
* Error real
* Error estimado

---

### 3️⃣ Diferenciación con Alta Exactitud

* Derivadas analíticas
* Tabulación
* Derivadas hacia adelante, atrás y centrada
* Errores porcentuales

---

### 4️⃣ Extrapolación de Richardson

* Derivada por fórmula central
* Extrapolación para mayor precisión
* Comparación con valor exacto

---

### 5️⃣ Derivadas con Datos Irregularmente Espaciados

* Cálculo de derivadas con fórmula general
* Gráfico de los datos
* Interpretación de variación química

