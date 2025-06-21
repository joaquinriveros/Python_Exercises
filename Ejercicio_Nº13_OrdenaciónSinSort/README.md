# 🔢 Ordenamiento sin sort() - Interactivo y Visual

Un programa en Python que permite ordenar listas de números enteros sin usar la función `sort()`, mostrando paso a paso cómo se realiza el ordenamiento por inserción (insertion sort).  
Incluye validaciones para entrada manual, opción de lista aleatoria y mensajes claros para guiar al usuario.

---

## ✨ Características principales

✅ Validación robusta para ingresar listas manuales con números enteros separados por comas  
✅ Requiere al menos dos números para ordenar  
✅ Genera listas aleatorias para probar el algoritmo automáticamente  
✅ Visualización paso a paso del algoritmo insertion sort con pausas para mejor comprensión  
✅ Menú interactivo con opciones claras y validaciones en cada paso  
✅ Compatible con Windows, macOS y Linux (limpia consola automáticamente)  
✅ Uso de colores ANSI para destacar mensajes y pasos importantes  

---

## 🧠 ¿Qué es el ordenamiento por inserción?

El ordenamiento por inserción es un algoritmo sencillo que ordena una lista construyendo la lista final de manera incremental.  
Toma un elemento de la lista y lo inserta en su posición correcta respecto a los ya ordenados, repitiendo el proceso hasta ordenar toda la lista.  

Este método es intuitivo y fácil de entender, ideal para aprender conceptos básicos de algoritmos de ordenamiento.

---

## 🚀 Cómo usar

1. **Descargá el archivo:**  
   `ordenamiento_sin_sort.py` (o el nombre que le hayas dado)

2. **Ejecutalo desde la terminal:**  

```bash
python ordenamiento_sin_sort.py
Seguí las instrucciones en pantalla:

Elegí si querés ingresar la lista manualmente o usar una lista aleatoria

Si elegís manual, ingresá números separados por comas (ej: 5,3,8,1). Debés ingresar al menos dos números.

Verás paso a paso cómo el programa ordena la lista usando insertion sort

Podés repetir el proceso tantas veces como quieras hasta elegir salir

```

---

## 🧪 Ejemplo de ejecución

```plaintext

🔢 ORDENAMIENTO SIN sort() 🔢
1) Ingresar lista manualmente
2) Usar lista aleatoria
3) Salir

Elige una opción (1/2/3): 1
Ingresa números separados por comas (ej: 5,3,8,1): 7, 3, 9, 1

Lista original: [7, 3, 9, 1]

Presiona ENTER para ver el proceso de ordenamiento...

→ Insertando 3 en la sublista [7]
   [7, 7, 9, 1]  (moviendo 7 hacia la derecha)
  Sublista ordenada: [3, 7]

→ Insertando 9 en la sublista [3, 7]
  Sublista ordenada: [3, 7, 9]

→ Insertando 1 en la sublista [3, 7, 9]
   [3, 7, 9, 9]  (moviendo 9 hacia la derecha)
   [3, 7, 7, 9]  (moviendo 7 hacia la derecha)
   [3, 3, 7, 9]  (moviendo 3 hacia la derecha)
  Sublista ordenada: [1, 3, 7, 9]

✔ Lista ordenada: [1, 3, 7, 9]

🔁 Presiona ENTER para volver al menú...
```
---

## ✍️ Autor
Proyecto desarrollado por Joaquín Riveros con el objetivo de enseñar el funcionamiento de un algoritmo clásico de ordenamiento mediante una experiencia visual e interactiva.

---