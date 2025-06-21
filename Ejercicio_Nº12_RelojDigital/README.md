
# 🕒 Reloj Digital en Consola - Interactivo, Sonoro y Personalizable

Una aplicación en Python que muestra un **reloj digital en tiempo real**, con opción de formato 12h o 24h, visualización de la fecha y sonido de tic configurable. Diseñado con una interfaz de texto clara y validaciones que aseguran una excelente experiencia de usuario. Ideal para aprender sobre control del tiempo, entrada del usuario, ciclos y manejo de interrupciones.

---

## ✨ Características principales

✅ Interfaz limpia con estilo visual retro y colores personalizados  
✅ Formato de hora personalizable: 24h o 12h (AM/PM)  
✅ Opción para mostrar la fecha actual junto al reloj  
✅ Sonido de "tic" activable cada segundo (compatible con Windows/Linux)  
✅ Validaciones robustas de entradas del usuario  
✅ Manejo elegante de interrupciones (Ctrl+C) para volver al menú  
✅ Instrucciones claras y amigables para una experiencia intuitiva

---

## 🧠 ¿Qué se puede aprender?

Este reloj es un proyecto ideal para practicar:
- Manipulación de fechas y horas (`time`, `strftime`)
- Control de flujo (`while`, `if`, `try/except`)
- Limpieza de pantalla y manejo de consola
- Estilo visual con caracteres ASCII y colores ANSI
- Funcionalidades del sistema operativo (como `winsound.Beep()` en Windows)

---

## 🚀 Cómo usar

1. **Descargá el archivo:**  
   `reloj_digital.py`

2. **Ejecutalo desde la terminal o consola:**  

```bash
python reloj_digital.py
```

3. **Seguí las instrucciones en pantalla:**  
   - Elegí el formato de hora
   - Activá o desactivá el sonido de tic
   - Decidí si querés mostrar también la fecha

4. **Presioná `Ctrl+C` para volver al menú en cualquier momento.**

---

## 🧪 Ejemplo de ejecución

```plaintext
🕒  RELOJ DIGITAL EN CONSOLA  🕒

Elegí una opción:
1) Formato 24 horas
2) Formato 12 horas (AM/PM)
3) Formato 24h con fecha
4) Salir

Seleccioná una opción (1/2/3/4): 3
¿Querés que el reloj haga un tic cada segundo? (s/n): s

╔════════════════════════════╗
║  Viernes 21 de junio del 2025  ║
║          16:42:07           ║
╚════════════════════════════╝

Presioná Ctrl+C para volver al menú.
```

---

## 🎯 Sugerencias de mejora

- Agregar funciones como **cronómetro**, **temporizador** o **alarma personalizada**
- Crear un **archivo de configuración** para recordar la última elección del usuario
- Hacer una **versión GUI** con `tkinter` o `PyQt`

---

## ✍️ Autor

Proyecto desarrollado por **Joaquín Riveros** con fines educativos y prácticos, pensado para ofrecer una herramienta útil, visualmente atractiva y con múltiples funcionalidades para aprender y experimentar con Python en consola.
