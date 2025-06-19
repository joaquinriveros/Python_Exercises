import time
import sys
import os
from datetime import datetime

CRT_GREEN = "\033[92m"
RESET = "\033[0m"

def clear_console():
    os.system("cls" if os.name == "nt" else "clear")

def efecto_escritura(texto, delay=0.03):
    for char in texto:
        sys.stdout.write(CRT_GREEN + char + RESET)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def beep():
    print('\a', end='')  # Sonido beep

def efecto_inicio():
    clear_console()
    efecto_escritura("Booting RetroCalc v2.0...", 0.05)
    time.sleep(0.5)
    efecto_escritura("Cargando memoria de 64KB...", 0.04)
    time.sleep(0.5)
    efecto_escritura("🧮 Bienvenido a la CALCULADORA RETRO\n", 0.04)
    time.sleep(0.2)

def registrar_operacion(operacion, a, b, resultado):
    with open("registro_retro.txt", "a") as f:
        timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
        f.write(f"{timestamp} {operacion}: {a} y {b} => {resultado}\n")

def mostrar_historial():
    try:
        with open("registro_retro.txt", "r") as f:
            efecto_escritura("\n🗂️ Historial de operaciones:\n", 0.02)
            lineas = f.readlines()
            if not lineas:
                efecto_escritura("🔍 El historial está vacío.", 0.02)
                return
            for linea in lineas:
                efecto_escritura(linea.strip(), 0.002)
    except FileNotFoundError:
        efecto_escritura("🔍 Aún no hay historial registrado.", 0.02)

def pedir_numero(mensaje):
    while True:
        try:
            entrada = input(mensaje)
            valor = float(entrada)
            return valor
        except ValueError:
            efecto_escritura("❗ Entrada inválida. Por favor ingresa un número válido.", 0.02)

def seleccionar_operacion():
    opciones = {
        "1": "Sumar",
        "2": "Restar",
        "3": "Multiplicar",
        "4": "Dividir",
        "5": "Historial",
        "6": "Ayuda",
        "7": "Salir"
    }
    efecto_escritura("Seleccioná una opción:", 0.02)
    for k, v in opciones.items():
        efecto_escritura(f" {k}. {v}", 0.01)

    while True:
        eleccion = input("> ").strip()
        if eleccion in opciones:
            return eleccion
        else:
            efecto_escritura("❗ Opción inválida, intentá de nuevo.", 0.02)

def consola_calculadora():
    efecto_inicio()
    efecto_escritura("Usá el menú para elegir la operación.\n", 0.02)

    while True:
        opcion = seleccionar_operacion()

        if opcion == "7":  # Salir
            efecto_escritura("👋 Hasta la próxima. Apagando sistema retro...", 0.04)
            break
        elif opcion == "5":  # Historial
            mostrar_historial()
            continue
        elif opcion == "6":  # Ayuda
            efecto_escritura("🧾 Comandos del menú:", 0.02)
            efecto_escritura(" 1 - Sumar dos números", 0.01)
            efecto_escritura(" 2 - Restar dos números", 0.01)
            efecto_escritura(" 3 - Multiplicar dos números", 0.01)
            efecto_escritura(" 4 - Dividir dos números", 0.01)
            efecto_escritura(" 5 - Ver historial de operaciones", 0.01)
            efecto_escritura(" 6 - Mostrar esta ayuda", 0.01)
            efecto_escritura(" 7 - Salir de la calculadora", 0.01)
            continue

        a = pedir_numero("👉 Ingresá el primer número: ")
        b = pedir_numero("👉 Ingresá el segundo número: ")

        if opcion == "1":
            resultado = a + b
            beep()
            efecto_escritura(f"🟢 Resultado: {a} + {b} = {resultado}")
            registrar_operacion("Sumar", a, b, resultado)

        elif opcion == "2":
            resultado = a - b
            beep()
            efecto_escritura(f"🟠 Resultado: {a} - {b} = {resultado}")
            registrar_operacion("Restar", a, b, resultado)

        elif opcion == "3":
            resultado = a * b
            beep()
            efecto_escritura(f"🔵 Resultado: {a} × {b} = {resultado}")
            registrar_operacion("Multiplicar", a, b, resultado)

        elif opcion == "4":
            if b == 0:
                efecto_escritura("❌ Error: División entre cero no permitida.")
                continue
            resultado = a / b
            beep()
            efecto_escritura(f"🟣 Resultado: {a} ÷ {b} = {resultado}")
            registrar_operacion("Dividir", a, b, resultado)

        efecto_escritura("-" * 40, 0.005)

if __name__ == "__main__":
    consola_calculadora()
