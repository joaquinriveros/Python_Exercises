# Detector de Palíndromos Interactivo 🔁🧠

Este proyecto permite verificar si una palabra es un **palíndromo**, es decir, si se lee igual de izquierda a derecha que de derecha a izquierda.  
A través de un menú interactivo, el usuario puede ingresar palabras, ver paso a paso cómo se comparan los caracteres, y repetir el proceso cuantas veces quiera.

El programa incluye validaciones para evitar errores y una presentación visual llamativa, ideal para hacerlo más didáctico y dinámico en prácticas universitarias.

---

## 📌 Objetivo

Ofrecer una herramienta interactiva para practicar y visualizar:

- El análisis de cadenas en Python.
- La comparación de caracteres.
- El uso de estructuras de control como `if`, `while`, `for`, etc.
- La validación de entrada del usuario.
- El uso de funciones auxiliares y efectos visuales para una mejor experiencia.

---

## 🧠 ¿Qué se aprende con este ejercicio?

Este programa es ideal para fortalecer conceptos fundamentales:

- ✅ *Cadenas y manipulación de texto*: normalización, comparación, inversión de texto.
- ✅ *Funciones bien estructuradas*: reutilizables, claras y documentadas.
- ✅ *Validación de entradas*: permite solo palabras con letras (sin números, símbolos ni espacios).
- ✅ *Animaciones en consola*: con impresión lenta tipo máquina de escribir.
- ✅ *Flujo de control amigable*: menús claros y decisiones del usuario con “sí” o “no”.

---

## 🚀 Cómo usarlo

1. Asegurate de tener **Python 3.x** instalado.
2. Ejecutá el archivo `palindromo_interactivo.py`.
3. Ingresá una palabra (ej: `reconocer`, `radar`, `oso`).
4. El programa verificará si es un palíndromo y mostrará el proceso letra por letra (si así lo elegís).
5. Podés probar cuantas veces quieras o salir cuando lo desees.

---

## 🧪 Ejemplo de salida

```bash
🔁 Bienvenido al Detector de Palíndromos Interactivo 🔁
💬 Ingresá una palabra sin espacios, números ni símbolos.

📝 Ingresá una palabra (o escribí 'salir' para terminar):
> reconocer

¿Querés ver el proceso paso a paso? (s/n): s

🔍 Comparando letra por letra...

   r  <-->  r
   e  <-->  e
   c  <-->  c
   o  <-->  o
   n  <-->  n
   o  <-->  o
   c  <-->  c
   e  <-->  e
   r  <-->  r

✅ ¡Es un palíndromo! 🤩
```
---

## ⚠️ Consideraciones

- El programa solo acepta letras. Si ingresás números, espacios o símbolos, mostrará un mensaje de error.
- Letras con tildes se limpian automáticamente (por ejemplo, "cívico" se considera válida).
- Las respuestas “sí” o “no” se validan correctamente (solo se acepta s, si, n, no).
- El proceso puede ser paso a paso o directo, según prefiera el usuario.

---

## 🎯 Preguntas sugeridas para acompañar el ejercicio
1. **¿Por qué usamos .isalpha() en la validación de entrada?**
Para asegurarnos de que la cadena solo contiene letras, sin espacios ni otros caracteres.

2. **¿Qué ventajas tiene mostrar el proceso paso a paso al usuario?**
Ayuda a comprender visualmente cómo se compara cada letra, ideal para aprender o enseñar.

3. **¿Cómo podríamos modificar el programa para aceptar frases completas?**
Quitando la restricción de solo letras y adaptando la lógica para ignorar espacios y signos de puntuación.

4. **¿Cómo podrías implementar una interfaz gráfica (GUI) para este programa?**
Usando tkinter, PyQt o cualquier otra librería visual, agregando botones, campos de texto y animaciones gráficas.

---

## 📜 Autor
Este código fue creado por Joaquín Riveros como parte de sus prácticas en la facultad.
¡Gracias por probarlo! 💻✨

---