# 🔐 Cifrado César Interactivo en Python

Una herramienta en consola que permite cifrar y descifrar textos usando el método clásico del **Cifrado César**. Incluye explicación educativa, validaciones estrictas, normalización de acentos y opciones para guardar resultados, ideal para estudiantes y docentes interesados en criptografía básica y programación interactiva.

---

## ✨ Características principales

- ✅ Interfaz en consola con colores y efectos de texto para mejor experiencia  
- ✅ Validación rigurosa en cada entrada (no permite vacíos ni valores inválidos)  
- ✅ Normalización automática para eliminar tildes y acentos  
- ✅ Opción para ver una breve explicación educativa del cifrado César  
- ✅ Opción para ejecutar un ejemplo rápido predefinido  
- ✅ Permite guardar el resultado en un archivo `.txt`  
- ✅ Fácil de usar, con opción de salir escribiendo `salir` en cualquier momento  

---

## 🧠 ¿Qué es el Cifrado César?

El cifrado César es un método de encriptación clásico donde cada letra del texto se reemplaza por otra que está desplazada un número fijo de posiciones en el alfabeto.

Por ejemplo, con desplazamiento 3:  
- A → D  
- B → E  
- C → F  

El cifrado no modifica signos, números ni espacios, solo las letras.

---

## 🚀 Cómo usar

1. **Descargá el archivo:**  
   `16_cifrado_cesar.py`

2. **Ejecutalo desde la terminal o consola:**  

```bash
python 16_cifrado_cesar.py
Seguí las instrucciones en pantalla:

Elegí ver explicación, ejemplo, cifrar o descifrar

Ingresá el texto (se normalizarán los acentos)

Indicá el desplazamiento (entero no negativo)

Visualizá el resultado y elegí si querés guardarlo

Decidí si querés continuar o salir

Podés escribir "salir" en cualquier momento para terminar.
```

---

## 🧪 Ejemplo de ejecución

```plaintext
🔐 Cifrado César interactivo 🔐

¿Querés ver una breve explicación del cifrado César? (s/n) s

🧠 ¿Qué es el Cifrado César?
Es un método de encriptación donde cada letra se reemplaza por otra,
desplazada un número fijo de posiciones en el alfabeto.
Por ejemplo, con desplazamiento 3: A → D, B → E, C → F, etc.
No afecta los signos ni los números. Solo letras.

Elige una opción:
  0) Ver ejemplo automático
  1) Cifrar texto
  2) Descifrar texto
> 1

✍️ Ingresa el texto a procesar: ¡Hola, Mundo!

🔢 Ingresa el desplazamiento (ej: 3): 3

Procesando...

✅ Cifrado completo:
Krod, Pxqgr!

💾 ¿Querés guardar el resultado en un archivo? (s/n) n

🔁 ¿Querés procesar otro texto? (s/n) n

👋 ¡Hasta luego!
```
---

## 💡 Mejoras futuras posibles

- Implementar soporte para otros alfabetos o idiomas
- Añadir interfaz gráfica para mejor usabilidad
- Incorporar cifrados más avanzados y métodos de desencriptación
- Crear un historial de resultados para facilitar revisiones

---

## ✍️ Autor
Proyecto desarrollado por Joaquín Riveros con fines educativos y prácticos para aprender criptografía básica y programación en Python.

---
