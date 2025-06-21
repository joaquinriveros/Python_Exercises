import os
import re
import sys
import time

# Colores ANSI
RED    = "\033[91m"
GREEN  = "\033[92m"
YELLOW = "\033[93m"
CYAN   = "\033[96m"
RESET  = "\033[0m"

historial = []

def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')

def escribir_lento(texto, delay=0.02):
    for c in texto:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def validar_email(email):
    """
    Valida emails con un patrón mejorado y chequeos adicionales.
    """
    patrón = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$"
    if '..' in email or email.count('@') != 1:
        return False
    return bool(re.match(patrón, email))

def pedir_email():
    while True:
        entrada = input(f"{CYAN}📧 Ingresá un correo (o 'salir' para terminar): {RESET}").strip()
        if entrada.lower() == 'salir':
            return None
        if validar_email(entrada):
            historial.append(entrada)
            return entrada
        print(f"{RED}❌ Formato inválido. Ejemplo válido: usuario@dominio.com{RESET}")

def pedir_si_no(pregunta):
    while True:
        resp = input(f"{YELLOW}{pregunta} (s/n): {RESET}").strip().lower()
        if resp in ('s', 'si'):
            return True
        if resp in ('n', 'no'):
            return False
        print(f"{RED}❌ Solo se acepta 's' o 'n'.{RESET}")

def menu_validar_email():
    while True:
        limpiar_consola()
        escribir_lento(f"{CYAN}🔍 VALIDADOR DE EMAIL 🔍{RESET}\n")
        email = pedir_email()
        if email is None:
            break

        print(f"\n{GREEN}✅ ¡El correo '{email}' es válido!{RESET}\n")

        if not pedir_si_no("¿Querés validar otro correo?"):
            break

    print(f"\n{CYAN}👋 Gracias por usar el validador de email.{RESET}")

    if historial and pedir_si_no("¿Querés ver los correos validados en esta sesión?"):
        print(f"\n{GREEN}📋 Correos validados:{RESET}")
        for i, e in enumerate(historial, 1):
            print(f"{i}. {e}")
        input(f"\n{CYAN}Presioná ENTER para salir...{RESET}")

if __name__ == "__main__":
    menu_validar_email()
