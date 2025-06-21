# 📧 Validador de Emails - Interactivo, Didáctico y Seguro

Una herramienta en Python que permite verificar si un correo electrónico está bien formado, con una interfaz interactiva, mensajes explicativos, historial de validaciones y validaciones reales.

Ideal para estudiantes, docentes, programadores principiantes o cualquier persona interesada en mejorar su comprensión del formato de correos electrónicos.

---

## ✨ Características principales

✅ Validación robusta de correos electrónicos con expresiones regulares avanzadas  
✅ Prevención de errores comunes como doble punto, múltiples @, dominios sin extensión, etc.  
✅ Mensajes de error claros con ejemplos  
✅ Interfaz interactiva con efecto "máquina de escribir"  
✅ Opción para revisar el historial de correos validados  
✅ Limpieza automática de la consola (Windows, macOS, Linux)  
✅ Control completo de flujo con preguntas de sí/no  
✅ Visualmente agradable gracias a los colores ANSI  

---

## 🧠 ¿Qué se considera un email válido?

Un email válido debe tener:
- Solo **una arroba** (@)
- Nombre de usuario alfanumérico (puede incluir puntos, guiones o guiones bajos)
- Un **dominio válido**, sin caracteres especiales o vacíos
- Una extensión con al menos **dos letras**

**Ejemplos válidos:**
- usuario@gmail.com  
- nombre.apellido@empresa.org  
- contacto123@mi-dominio.net  

**Ejemplos inválidos:**
- user@@gmail.com  
- user@gmail  
- user@.com  
- user..name@correo.com  

---

## 🚀 Cómo usar

1. **Descargá el archivo:**  
   `validador_email.py`

2. **Ejecutalo desde la terminal:**

```bash
python validador_email.py
Seguí las instrucciones paso a paso:

Ingresá un correo electrónico (o escribí salir para finalizar)

Si es válido, el programa lo registrará en el historial

Después de cada verificación podés elegir si querés probar con otro

Al final, tenés la opción de ver todos los correos validados

```

---

## 🧪 Ejemplo de ejecución

```plaintext

🔍 VALIDADOR DE EMAIL 🔍

📧 Ingresá un correo (o 'salir' para terminar): contacto@gmail.com

✅ ¡El correo 'contacto@gmail.com' es válido!

¿Querés validar otro correo? (s/n): s

📧 Ingresá un correo (o 'salir' para terminar): prueba@correo

❌ Formato inválido. Ejemplo válido: usuario@dominio.com

📧 Ingresá un correo (o 'salir' para terminar): joaquin.riveros@outlook.com

✅ ¡El correo 'joaquin.riveros@outlook.com' es válido!

¿Querés validar otro correo? (s/n): n

👋 Gracias por usar el validador de email.
¿Querés ver los correos validados en esta sesión? (s/n): s

📋 Correos validados:
1. contacto@gmail.com
2. joaquin.riveros@outlook.com

```
---

## ✍️ Autor
Proyecto desarrollado por Joaquín Riveros como práctica de validaciones en Python, orientado a mejorar la interacción con el usuario, la comprensión del formato de emails y el manejo de expresiones regulares.

Con un enfoque educativo, accesible y visualmente claro. 🙌

---