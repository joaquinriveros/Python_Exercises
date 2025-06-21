# 🎯 Juego de Adivinanza con Pistas – Interactivo y Personalizable

Un divertido juego de consola en Python donde el jugador debe adivinar un número secreto dentro de un rango definido. Cada intento fallido brinda una pista que acorta el rango posible. ¡Ideal para ejercitar la lógica y divertirse al mismo tiempo!

---

## ✨ Características principales

✅ El usuario define el rango y la cantidad de intentos  
✅ Valida que los datos ingresados sean correctos o permite salir  
✅ Pistas automáticas que actualizan el rango luego de cada intento  
✅ Historial de intentos al finalizar la partida  
✅ Sistema de puntaje según intentos usados  
✅ Permite volver a jugar cuantas veces se desee  
✅ Interfaz amigable con colores y mensajes motivadores  

---

## 🧠 ¿Cómo funciona?

1. El usuario define un **valor mínimo** y un **valor máximo** para el número secreto  
2. También elige cuántos **intentos** desea tener  
3. El programa genera un número secreto aleatorio en ese rango  
4. Por cada intento:
   - Se indica si el número es muy alto o muy bajo  
   - Se muestra un nuevo rango más reducido como pista  
5. Si adivinás, ¡ganás puntos!  
6. Si se te acaban los intentos, se muestra el número secreto y tus intentos  
7. Siempre podés escribir `"salir"` para abandonar en cualquier momento  

---

## 🚀 Cómo usar

1. **Descargá el archivo:**  
   `adivinanza_con_pistas.py`

2. **Ejecutalo desde la terminal o consola:**  
```bash
python adivinanza_con_pistas.py
Seguí las instrucciones en pantalla
```
---

## 🧪 Ejemplo de ejecución

```plaintext
🎲  JUEGO DE ADIVINANZA CON PISTAS  🎲

Definí tu rango y la cantidad de intentos.
Escribí 'salir' en cualquier momento para abandonar.

👉 Valor mínimo del rango: 10
👉 Valor máximo del rango (≥ 11): 50
👉 ¿Cuántos intentos querés tener?: 5

🎯 ¡He elegido un número entre 10 y 50!
🧠 Tenés 5 intentos. ¡Mucha suerte!

🔍 Adiviná el número (5 intentos restante): 30
⬆️  Muy alto.
💡 Pista: está entre 10 y 29.

🔍 Adiviná el número (4 intentos restante): 20
⬇️  Muy bajo.
💡 Pista: está entre 21 y 29.

🔍 Adiviná el número (3 intentos restante): 25

🎉 ¡Correcto! El número era 25.
🔢 Lo lograste en 3 intentos.
🏅 Puntos obtenidos: 3
📜 Tus intentos: [30, 20, 25]

🔁 ¿Querés jugar otra partida? (s/n): n

👋 ¡Gracias por jugar! Hasta luego.
```
---

## 💡 Ideas de mejora futuras

- Modo difícil (sin mostrar pistas)
- Ranking de puntajes
- Niveles con rangos predefinidos
- Interfaz gráfica con Tkinter o PyQt

---

## ✍️ Autor
Este proyecto fue desarrollado por Joaquín Riveros con fines educativos y recreativos, buscando mejorar la interacción hombre-máquina en proyectos simples con Python.

---