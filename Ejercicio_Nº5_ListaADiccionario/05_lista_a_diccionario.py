import tkinter as tk
from tkinter import messagebox
import random

def lista_a_diccionario(lista):
    return {i: valor for i, valor in enumerate(lista)}

def generar_lista_aleatoria():
    palabras = ["🌞 sol", "🐶 perro", "🍎 manzana", "✈️avión", "🌳 árbol", "💡 luz", "⛰️ montaña", "🍂 hoja"]
    return random.sample(palabras, 5)

def convertir_manual():
    entrada = entrada_usuario.get()
    elementos = [item.strip() for item in entrada.split(",") if item.strip()]
    if not elementos:
        messagebox.showwarning("⚠️ Atención", "Por favor, ingresá al menos un elemento separado por comas.")
        return
    mostrar_resultado(elementos)

def convertir_aleatoria():
    elementos = generar_lista_aleatoria()
    entrada_usuario.delete(0, tk.END)
    entrada_usuario.insert(0, ", ".join(elementos))
    mostrar_resultado(elementos)

def mostrar_resultado(lista):
    diccionario = lista_a_diccionario(lista)
    salida_text.delete("1.0", tk.END)
    salida_text.insert(tk.END, "🧠 Resultado: Diccionario generado a partir de tu lista:\n\n")
    for k, v in diccionario.items():
        salida_text.insert(tk.END, f"🔹 Índice {k} → {v}\n")

# Crear ventana principal
ventana = tk.Tk()
ventana.title("🔁 Conversor de Lista a Diccionario")
ventana.geometry("500x430")
ventana.configure(bg="#f7f7f7")

# Título
titulo = tk.Label(ventana, text="🔁 Conversor de Lista a Diccionario 🔁", font=("Arial", 16, "bold"), bg="#f7f7f7")
titulo.pack(pady=10)

# Instrucciones
instrucciones = tk.Label(ventana, text="📝 Ingresá una lista separada por comas. Ejemplo: gato, luna, casa", 
                         font=("Arial", 10), bg="#f7f7f7", fg="#333")
instrucciones.pack(pady=5)

# Entrada
entrada_usuario = tk.Entry(ventana, font=("Arial", 12), width=50)
entrada_usuario.pack(pady=10)
entrada_usuario.insert(0, "gato, luna, casa")

# Botones
boton_manual = tk.Button(ventana, text="✍️ Convertir mi lista", font=("Arial", 11), bg="#cce5ff", command=convertir_manual)
boton_manual.pack(pady=5)

boton_aleatoria = tk.Button(ventana, text="🎲 Usar lista aleatoria", font=("Arial", 11), bg="#d4edda", command=convertir_aleatoria)
boton_aleatoria.pack(pady=5)

# Resultado
salida_text = tk.Text(ventana, height=12, font=("Consolas", 11), bg="#ffffff", wrap="word")
salida_text.pack(pady=10)

ventana.mainloop()
