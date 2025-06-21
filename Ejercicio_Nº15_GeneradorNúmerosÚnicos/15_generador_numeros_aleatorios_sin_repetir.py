import os
import random

# Colores ANSI
RED    = "\033[91m"
GREEN  = "\033[92m"
YELLOW = "\033[93m"
CYAN   = "\033[96m"
RESET  = "\033[0m"

def limpiar_consola():
    """Limpia la consola para mejorar la legibilidad."""
    os.system('cls' if os.name == 'nt' else 'clear')

def pedir_int(mensaje, min_val=None, max_val=None):
    """
    Solicita un entero al usuario, lo valida y lo retorna.
    Si escribe 'salir', retorna None.
    """
    while True:
        entrada = input(f"{CYAN}{mensaje}{RESET} ").strip().lower()
        if entrada == 'salir':
            return None
        if not entrada.isdigit() and not (entrada.startswith('-') and entrada[1:].isdigit()):
            print(f"{RED}❌ Debes ingresar un número entero (o 'salir').{RESET}")
            continue
        valor = int(entrada)
        if min_val is not None and valor < min_val:
            print(f"{RED}❌ El valor debe ser ≥ {min_val}.{RESET}")
            continue
        if max_val is not None and valor > max_val:
            print(f"{RED}❌ El valor debe ser ≤ {max_val}.{RESET}")
            continue
        return valor

def pedir_si_no(pregunta):
    """
    Solicita 's' o 'n' al usuario, devuelve True para sí, False para no.
    """
    while True:
        entrada = input(f"{YELLOW}{pregunta} (s/n){RESET} ").strip().lower()
        if entrada in ('s','si'):
            return True
        if entrada in ('n','no'):
            return False
        print(f"{RED}❌ Solo 's' o 'n' son respuestas válidas.{RESET}")

def menu_generador():
    """
    Permite al usuario generar listas de números aleatorios sin repetir,
    indicando rango y cantidad, con validación en cada paso.
    """
    while True:
        limpiar_consola()
        print(f"{CYAN}🔢 Generador de Números Aleatorios Sin Repetir 🔢{RESET}")
        print("Escribe 'salir' en cualquier input para terminar.\n")

        # Límite inferior
        inferior = pedir_int("Ingresa el límite inferior del rango:", min_val=None)
        if inferior is None:
            break

        # Límite superior (must be > inferior)
        superior = pedir_int(
            f"Ingresa el límite superior del rango (≥ {inferior + 1}):",
            min_val=inferior + 1
        )
        if superior is None:
            break

        # Cantidad de números a generar
        max_cant = superior - inferior + 1
        cantidad = pedir_int(
            f"¿Cuántos números quieres? (1–{max_cant}):",
            min_val=1,
            max_val=max_cant
        )
        if cantidad is None:
            break

        # Generación y presentación
        resultado = random.sample(range(inferior, superior + 1), cantidad)
        print(f"\n{GREEN}✅ Números generados (sin repetir):{RESET} {resultado}\n")

        # ¿Otra vez?
        if not pedir_si_no("¿Querés generar otra lista?"):
            print(f"\n{CYAN}👋 ¡Gracias por usar el generador!{RESET}\n")
            break

if __name__ == "__main__":
    menu_generador()
