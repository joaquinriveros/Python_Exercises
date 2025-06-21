# 🔤 Sopa de Letras Interactiva - Visual, Educativa y Validada

Un juego de **sopa de letras en Python** totalmente interactivo, ideal para aprender programación estructurada, manipulación de matrices, validación de inputs y dirección en dos dimensiones.

Perfecto para estudiantes, docentes y entusiastas de la lógica.

---

## ✨ Características principales

✅ Muestra la sopa de letras en consola, resaltando las palabras encontradas  
✅ Soporte para búsqueda en todas las direcciones (horizontal, vertical y diagonales)  
✅ Validaciones estrictas: solo palabras válidas, sin repetir, sin números  
✅ Historial de palabras encontradas en la sesión  
✅ Colores ANSI para mejor experiencia visual  
✅ Interfaz amigable y bucles robustos que previenen errores del usuario  
✅ Compatible con Windows, macOS y Linux  

---

## 🧠 ¿Cómo funciona?

El usuario ve una matriz 10x10 de letras y debe escribir una palabra para buscar.  
El programa escanea la matriz en todas las direcciones y si encuentra la palabra:

- La resalta en color verde
- Muestra las posiciones donde fue hallada (fila y columna)
- Guarda la palabra en un historial de sesión

Si no se encuentra, lo informa claramente.

---

## 📌 Reglas de entrada

- ✅ Solo se aceptan **letras** (sin espacios, números ni símbolos)
- ⚠ La palabra debe tener **al menos 2 letras**
- 🚫 No se puede buscar dos veces la misma palabra

---

## 🚀 Cómo usar

1. **Descargá el archivo:**
   `18_sopa_letras_mejorado.py`

2. **Ejecutalo desde la terminal:**

```bash
python 18_sopa_letras_mejorado.py
```

---

## 🧪 Ejemplo de ejecución

```plaintext

🔎 Sopa de Letras
C A S A D E C U A M
O B O L A R Z B R A
L A P I Z P O M A R
A R B O L E S C A S
R A M A S C A J A S
E S O P A L E T R A
O M U M E L E F A N
N I Ñ O S T O R I N
S T A D I O M U N O
M O T O C I C L E T

🔤 Ingresa la palabra a buscar (o 'salir'): elefante

✅ 'ELEFANTE' encontrada!
📍 Posiciones (fila, columna):
  (7, 5)
  (7, 6)
  (7, 7)
  (7, 8)
  (7, 9)
  (7,10)
  (8, 1)
  (8, 2)

🔢 Palabras encontradas hasta ahora: 1
Presioná ENTER para continuar...
📋 Resumen de la sesión (al salir)
plaintext
Copiar
Editar
👋 Gracias por jugar a la sopa de letras.
¿Querés ver todas las palabras que encontraste? (s/n): s

📋 Palabras encontradas:
1. ELEFANTE
2. CASA
3. CAJA
```

---

## ✍️ Autor
Proyecto desarrollado por Joaquín Riveros, como parte de sus prácticas en lógica computacional y diseño de interfaces de consola.

---