import random
import string
import sys
import time
import os

# Códigos ANSI para color en consola
VERDE = "\033[92m"
ROJO = "\033[91m"
RESET = "\033[0m"
AZUL = "\033[94m"
AMARILLO = "\033[93m"

def escribir_lento(texto, delay=0.04):
    for c in texto:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def limpiar_consola():
    os.system("cls" if os.name == "nt" else "clear")

def evaluar_seguridad(contraseña):
    puntaje = 0
    if any(c.islower() for c in contraseña): puntaje += 1
    if any(c.isupper() for c in contraseña): puntaje += 1
    if any(c.isdigit() for c in contraseña): puntaje += 1
    if any(c in string.punctuation for c in contraseña): puntaje += 1

    niveles = {
        1: f"{AMARILLO}🟡 Básica{RESET}",
        2: f"{AMARILLO}🟠 Moderada{RESET}",
        3: f"{VERDE}🟢 Fuerte{RESET}",
        4: f"{AZUL}🟣 Muy Fuerte{RESET}"
    }

    print(f"🔍 Nivel de seguridad: {niveles.get(puntaje, 'Desconocido')}")

def generar_contraseña(longitud=12, usar_mayusculas=True, usar_numeros=True, usar_simbolos=True):
    if not (usar_mayusculas or usar_numeros or usar_simbolos):
        print(f"{ROJO}❌ Error: Debes seleccionar al menos un tipo de carácter además de minúsculas.{RESET}")
        return None

    base = list(string.ascii_lowercase)
    if usar_mayusculas:
        base += list(string.ascii_uppercase)
    if usar_numeros:
        base += list(string.digits)
    if usar_simbolos:
        base += list(string.punctuation)

    contraseña = []

    if usar_mayusculas:
        contraseña.append(random.choice(string.ascii_uppercase))
    if usar_numeros:
        contraseña.append(random.choice(string.digits))
    if usar_simbolos:
        contraseña.append(random.choice(string.punctuation))

    resto = longitud - len(contraseña)
    contraseña += random.choices(base, k=resto)

    random.shuffle(contraseña)
    return ''.join(contraseña)

def pedir_si_no(pregunta):
    """
    Pide al usuario una respuesta de tipo sí/no válida.
    Acepta 's', 'n', 'si', 'no' (insensible a mayúsculas).
    """
    while True:
        respuesta = input(pregunta + " (s/n): ").strip().lower()
        if respuesta in ['s', 'si']:
            return True
        elif respuesta in ['n', 'no']:
            return False
        else:
            print(f"{ROJO}❌ Por favor respondé solo con 's' o 'n'.{RESET}")

def pedir_longitud():
    """
    Solicita una longitud válida entre 8 y 64, y no permite continuar hasta lograrlo.
    """
    while True:
        try:
            longitud = int(input("👉 ¿Cuántos caracteres querés que tenga tu contraseña? (8-64): "))
            if 8 <= longitud <= 64:
                return longitud
            else:
                print(f"{AMARILLO}⚠️ La longitud debe estar entre 8 y 64 caracteres.{RESET}")
        except ValueError:
            print(f"{ROJO}❌ Error: Ingresá un número entero válido.{RESET}")

def menu_generador():
    limpiar_consola()
    print(f"{AZUL}🔐 Bienvenido al Generador de Contraseñas Seguras v2.1 🔐{RESET}")
    print("🤖 ¡Protegé tus cuentas con estilo!\n")

    modo_auto = pedir_si_no("¿Querés activar el modo automático?")

    if modo_auto:
        longitud = random.randint(12, 20)
        usar_mayus = usar_nums = usar_syms = True
        print(f"\n🔧 Modo automático activado: longitud = {longitud}, todo activado.\n")
    else:
        longitud = pedir_longitud()
        usar_mayus = pedir_si_no("¿Incluir MAYÚSCULAS?")
        usar_nums = pedir_si_no("¿Incluir NÚMEROS?")
        usar_syms = pedir_si_no("¿Incluir SÍMBOLOS (!@#)?")

    contraseña = generar_contraseña(
        longitud=longitud,
        usar_mayusculas=usar_mayus,
        usar_numeros=usar_nums,
        usar_simbolos=usar_syms
    )

    if contraseña:
        print("\n🔑 Tu nueva contraseña es:")
        escribir_lento(f"{VERDE}{contraseña}{RESET}")
        evaluar_seguridad(contraseña)
        print()

def main():
    while True:
        menu_generador()
        otra = pedir_si_no("¿Querés generar otra contraseña?")
        if not otra:
            print(f"\n👋 ¡Gracias por usar el generador! Hasta pronto.\n")
            break

if __name__ == '__main__':
    main()
