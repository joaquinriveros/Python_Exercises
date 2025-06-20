# Comparador de Factorial Recursivo vs Iterativo 🧮

Este proyecto compara dos enfoques clásicos para calcular el factorial de un número entero no negativo: **recursivo** e **iterativo**. Sirve como ejercicio práctico para comprender estructuras de control, eficiencia algorítmica y el diseño de código limpio y modular.

---

## 📌 Objetivo

El objetivo es demostrar que ambos métodos producen el mismo resultado, mientras se comparan en términos de:

- Cantidad de llamadas (en el caso recursivo)
- Tiempo de ejecución
- Robustez frente a entradas inválidas o números grandes

---

## 🧠 ¿Qué se aprende con este ejercicio?

Este tipo de comparador es ideal para desarrollar habilidades esenciales en programación, como:

- ✅ *Entender funciones recursivas*: cómo funcionan y cómo se comportan en la pila de llamadas.
- ✅ *Comparar enfoques algorítmicos*: lo elegante de la recursión frente a lo estable de la iteración.
- ✅ *Evaluar eficiencia*: uso de `time.perf_counter()` para analizar tiempos reales de ejecución.
- ✅ *Manejo de errores*: entrada inválida, números negativos o casos extremos como recursión profunda.
- ✅ *Diseño limpio*: código organizado, modular y bien comentado.

---

## 🚀 Cómo usarlo

1. Ejecutá el archivo `main.py` o `factorial_comparador.py` (según cómo lo hayas nombrado).
2. Ingresá un número entero no negativo cuando se te pida.
3. Observá los resultados de ambos métodos, incluyendo tiempos y número de llamadas recursivas.

---

## 🧪 Ejemplo de salida

```bash

🧮 Comparador de Factorial Recursivo vs Iterativo
🔢 Ingresa un número entero no negativo: 5
✅ Resultado Recursivo: 120 📈 Llamadas recursivas: 5 ⏱️ Tiempo recursivo: 0.00001020 segundos
✅ Resultado Iterativo: 120 ⏱️ Tiempo iterativo: 0.00000990 segundos
🎉 Ambos métodos dieron el mismo resultado ✅

```
---

## ⚠️ Consideraciones

- Si se ingresan números muy grandes (como > 997), el enfoque recursivo puede lanzar un `RecursionError`.
- El método iterativo es más eficiente para computación pura.
- El diseño modular permite expandir fácilmente este proyecto para agregar gráficos, benchmarks o análisis de memoria.

---

## 🎯 Preguntas sugeridas para acompañar el ejercicio

1. **¿Qué limitación tiene el enfoque recursivo y cómo se puede mitigar?**  
   El enfoque recursivo puede causar un desbordamiento de pila (*stack overflow*) si el número es muy grande, ya que cada llamada consume memoria. Para mitigar esto se puede usar la versión iterativa, aplicar recursión de cola (si el lenguaje lo permite) o establecer un límite razonable para la entrada del usuario.

2. **¿Por qué el tiempo recursivo es más alto en números pequeños?**  
   Porque cada llamada recursiva implica crear un nuevo contexto de función en la pila, lo que agrega un pequeño *overhead*. En cambio, la iterativa ejecuta todo en un solo flujo de control más directo.

3. **¿En qué casos conviene usar recursividad sobre iteración?**  
   La recursividad es conveniente cuando un problema tiene una estructura naturalmente recursiva (por ejemplo, recorridos de árboles o algoritmos de backtracking), o cuando mejora la claridad del código, aunque no siempre sea más eficiente.

4. **¿Cómo podrías generalizar este comparador para otras funciones matemáticas?**  
   Se podría adaptar la estructura general para comparar versiones recursivas e iterativas de otras funciones, como la secuencia de Fibonacci, suma de elementos, potencias, etc., manteniendo la lógica de medición de tiempo y validación de resultados.

5. **¿Qué aporta la estructura modular al mantenimiento y lectura del código?**  
   Una estructura modular facilita la lectura, el testeo, la reutilización y el mantenimiento del código. Permite separar responsabilidades (cálculo, entrada/salida, validación), lo que hace más sencillo escalar o modificar el proyecto en el futuro.

---

## 📜 Autor  
Este código fue creado por Joaquín Riveros como práctica de Python. ¡Espero que lo disfrutes! 😃

---