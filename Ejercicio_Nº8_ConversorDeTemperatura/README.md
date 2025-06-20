# Conversor de Temperatura Interactivo 🌡️🔁

Este proyecto permite convertir temperaturas entre **Celsius (°C)**, **Fahrenheit (°F)**, **Kelvin (°K)** y **Rankine (°R)** de forma dinámica e interactiva.  
Incluye una interfaz por consola con animaciones, validaciones inteligentes y registro de historial en un archivo `.log`.

Ideal para prácticas de programación en Python, ya que combina lógica matemática, interacción con el usuario y manejo de archivos.

---

## 📌 Objetivo

Desarrollar una aplicación que permita:

- Convertir entre 4 unidades de temperatura física.
- Brindar una experiencia de usuario clara, animada y validada.
- Registrar automáticamente el historial de conversiones en un archivo.
- Aplicar buenas prácticas de modularidad y estructura de código.

---

## 🧠 ¿Qué se aprende con este ejercicio?

- ✅ *Conversión de unidades físicas* con fórmulas matemáticas aplicadas.
- ✅ *Validación de entradas* usando expresiones regulares (`re`).
- ✅ *Efectos visuales en consola* con animación tipo "máquina de escribir".
- ✅ *Manejo de errores y flujos controlados* con estructuras `while`, `try`, etc.
- ✅ *Registro en archivo de texto (`.log`)* usando el módulo `logging`.

---

## 🚀 Cómo usarlo

1. Asegurate de tener **Python 3.x** instalado.
2. Descargá el archivo `08_conversor_temperatura.py`.
3. Abrí la terminal y ejecutalo con:

```bash
python 08_conversor_temperatura.py
```
4. Ingresá conversiones como:

```bash

100 C F     → convierte 100°C a Fahrenheit
25K R       → convierte 25 Kelvin a Rankine
212 F C     → convierte 212°F a Celsius
Escribí salir para cerrar el programa.

```

---

## 🧪 Ejemplo de salida

```bash

🔄 Conversor de Temperatura Interactivo 🔄
💬 Convertí entre °C, °F, °K y °R de forma rápida.

🌡️ Unidades disponibles:
  C  → Celsius
  F  → Fahrenheit
  K  → Kelvin
  R  → Rankine

👉 Ingresa tu conversión en formato:
   <valor> <origen> <destino>
   p.ej.: 25 C F   (o escribe 'salir')
> 100 C F

🔢 Convirtiendo...

✅ 100.00°C = 212.00°F

```

---

## 📂 Historial de conversiones
Todas las conversiones exitosas se guardan automáticamente en un archivo llamado:

```lua

conversiones.log

```

---

## Ejemplo de entrada en el archivo:

```r

2025-06-20 09:45:12 - 100.00°C → 212.00°F

```

---

## ⚠️ Consideraciones

- Solo se permiten unidades: C, F, K, R (no distingue mayúsculas/minúsculas).
- El formato debe ser: valor unidad_origen unidad_destino.
- ✅ Ej: 100 C F o 25k c
- ❌ Inválido: c 100 f, 100C->F, cien grados

- El resultado se muestra con 2 decimales.
- El programa tiene controles para evitar errores y no se cae ante entradas inválidas.

---

## 🎯 Preguntas sugeridas para acompañar el ejercicio

1. **¿Cómo funciona cada fórmula de conversión entre las unidades?**

Las conversiones se hacen en dos pasos:
- Se convierte la unidad de origen a Celsius.
- Luego se convierte desde Celsius a la unidad destino.

Fórmulas:
- °F → °C:       (F - 32) × 5/9
- K → °C:        K - 273.15
- R → °C:        (R - 491.67) × 5/9
- °C → °F:       C × 9/5 + 32
- °C → K:        C + 273.15
- °C → R:        (C + 273.15) × 9/5

2. **¿Por qué usamos expresiones regulares para validar la entrada?**

Porque con una sola expresión regular podemos validar de forma compacta si el usuario ingresó bien el formato:
   número + espacio + letra de unidad origen + espacio + letra de unidad destino

- Ejemplo: 100 C F

Esto previene errores como símbolos mal puestos, espacios incorrectos o letras inválidas.

3. **¿Cómo se podría convertir este programa en una aplicación con interfaz gráfica (GUI)?**

Podemos usar bibliotecas como:
- tkinter
- PyQt5 / PySide
- customtkinter

El usuario ingresaría el número en un Entry, y elegiría las unidades en ComboBoxes. 
El botón “Convertir” mostraría el resultado en una Label.
Incluso se podría exportar el historial como archivo de texto.

4. **¿Cómo permitir conversiones encadenadas (de C a F y luego a R)?**

Podrías permitirle al usuario ingresar solo el valor y unidad origen, 
y luego mostrar un menú con múltiples unidades destino para elegir más de una.

- Por ejemplo: ingresar “100 C” → seleccionar: F, K, R → el programa hace todas las conversiones automáticamente.

5. **¿Qué otras magnitudes físicas podrías agregar usando la misma estructura?**

Podrías adaptar el mismo menú y lógica para:
- Longitud: metros, pies, pulgadas, km, millas
- Peso: kg, g, lb, oz
- Tiempo: segundos, minutos, horas, días
- Velocidad: km/h, m/s, mph

Solo hay que cambiar la función de conversión y las fórmulas según cada magnitud.

---

## 📜 Autor
Este código fue creado y mejorado por Joaquín Riveros como parte de sus prácticas en la facultad.
💻 ¡Gracias por probarlo y feliz programación!

---
