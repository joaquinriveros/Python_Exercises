# Generador de Contraseñas Seguras 🔐💡

Este proyecto permite al usuario generar contraseñas seguras y personalizadas desde la consola. A través de un menú interactivo, se pueden seleccionar las características de la contraseña (longitud, uso de mayúsculas, números y símbolos). El programa también incluye un **modo automático**, una presentación atractiva con colores y efectos, y una evaluación del nivel de seguridad de la contraseña.

---

## 📌 Objetivo

Ofrecer una herramienta práctica y divertida para:

- Explorar la generación aleatoria de datos en Python.
- Reforzar estructuras de control y validaciones.
- Comprender los fundamentos de la seguridad en contraseñas.
- Aplicar lógica interactiva para una experiencia más realista.

---

## 🧠 ¿Qué se aprende con este ejercicio?

Este proyecto permite ejercitar varios conceptos fundamentales:

- ✅ *Uso de módulos estándar* como `random`, `string`, `os`, `time` y `sys`.
- ✅ *Validación de entrada del usuario* con ciclos `while` y excepciones.
- ✅ *Funciones bien separadas* y reutilizables (`generar_contraseña`, `evaluar_seguridad`, etc.).
- ✅ *Estética en consola*: uso de colores ANSI y efectos visuales.
- ✅ *Buenas prácticas de programación*: claridad, documentación, control de errores.

---

## 🚀 Cómo usarlo

1. Asegurate de tener **Python 3.x** instalado.
2. Ejecutá el archivo `generador_contraseñas.py`.
3. Elegí entre usar el **modo automático** o configurar tu contraseña paso a paso.
4. Si elegís configurarla manualmente, el programa te pedirá:
   - Longitud (entre 8 y 64 caracteres).
   - Si querés incluir mayúsculas.
   - Si querés incluir números.
   - Si querés incluir símbolos.

5. El programa generará tu contraseña y evaluará su nivel de seguridad.

---

## 🧪 Ejemplo de salida

```bash
🔐 Bienvenido al Generador de Contraseñas Seguras v2.1 🔐
🤖 ¡Protegé tus cuentas con estilo!

👉 ¿Cuántos caracteres querés que tenga tu contraseña? (8-64): 16
¿Incluir MAYÚSCULAS? (s/n): s
¿Incluir NÚMEROS? (s/n): s
¿Incluir SÍMBOLOS (!@#)? (s/n): s

🔑 Tu nueva contraseña es:
rU7!pkv#Q8tLw@zA

🔍 Nivel de seguridad: 🟣 Muy Fuerte
```
---

## ⚠️ Consideraciones

- Si la longitud es menor a 8 o mayor a 64, el programa no continúa hasta que ingreses un valor válido.
- Si no seleccionás ningún tipo de carácter (además de las minúsculas), se mostrará un error.
- Las contraseñas generadas siempre incluyen al menos un carácter de cada tipo seleccionado para mayor seguridad.
- El programa evita errores al aceptar únicamente "s", "n", "si" o "no" como respuestas válidas.

---

## 🎯 Preguntas sugeridas para acompañar el ejercicio

1. **¿Por qué es importante incluir diferentes tipos de caracteres en una contraseña?**
Porque aumenta la entropía y hace más difícil que sea adivinada por fuerza bruta.

2. **¿Qué ventaja tiene asegurar al menos un carácter de cada tipo seleccionado?**
Garantiza que la contraseña cumpla realmente con las políticas de seguridad.

3. **¿Cómo podrías guardar la contraseña en un archivo de texto cifrado?**
Usando el módulo cryptography o simplemente base64 + open() para escribirla en un archivo.

4. **¿Cómo podrías llevar este generador a una interfaz gráfica (GUI)?**
Utilizando bibliotecas como tkinter o PyQt para hacerlo más accesible a todo público.

---

## 📜 Autor
Este código fue creado por Joaquín Riveros como parte de sus prácticas en la facultad.
💻 ¡Gracias por probarlo y recordá mantener tus contraseñas seguras! 🔐✨

---