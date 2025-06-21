import os
import random
import time

# Colores ANSI
RED    = "\033[91m"
GREEN  = "\033[92m"
YELLOW = "\033[93m"
CYAN   = "\033[96m"
RESET  = "\033[0m"

def limpiar_consola():
    """Limpia la pantalla en Windows o Unix."""
    os.system('cls' if os.name == 'nt' else 'clear')

def pedir_int(mensaje, min_val=None, max_val=None):
    """
    Pide un entero al usuario:
     - Retorna None si ingresa 'salir'
     - Valida que esté dentro de [min_val, max_val] si se pasan
    """
    while True:
        entrada = input(f"{CYAN}{mensaje}{RESET} ").strip().lower()
        if entrada == 'salir':
            return None
        if not entrada.lstrip('-').isdigit():
            print(f"{RED}❌ Debes ingresar un número entero válido (o 'salir').{RESET}")
            continue
        valor = int(entrada)
        if min_val is not None and valor < min_val:
            print(f"{RED}❌ El número debe ser ≥ {min_val}.{RESET}")
            continue
        if max_val is not None and valor > max_val:
            print(f"{RED}❌ El número debe ser ≤ {max_val}.{RESET}")
            continue
        return valor

def pedir_si_no(pregunta):
    """
    Pide 's' o 'n'. Retorna True para sí, False para no.
    """
    while True:
        r = input(f"{YELLOW}{pregunta} (s/n){RESET} ").strip().lower()
        if r in ('s','si'):
            return True
        if r in ('n','no'):
            return False
        print(f"{RED}❌ Solo 's' o 'n'.{RESET}")

def mostrar_bienvenida():
    """Presentación inicial del juego."""
    limpiar_consola()
    print(f"{CYAN}🎲  JUEGO DE ADIVINANZA CON PISTAS  🎲{RESET}\n")
    print("Definí tu rango y la cantidad de intentos.")
    print("Escribí 'salir' en cualquier momento para abandonar.\n")

def jugar():
    """
    Lógica de una partida con:
     - Rango definido por el usuario
     - Límite de intentos
     - Historial y puntuación
    """
    mostrar_bienvenida()

    minimo = pedir_int("👉 Valor mínimo del rango:")
    if minimo is None:
        return False

    maximo = pedir_int(f"👉 Valor máximo del rango (≥ {minimo + 1}):", min_val=minimo+1)
    if maximo is None:
        return False

    max_intentos = pedir_int("👉 ¿Cuántos intentos querés tener?", min_val=1)
    if max_intentos is None:
        return False

    secreto = random.randint(minimo, maximo)
    intentos = 0
    historial = []
    rango_min, rango_max = minimo, maximo

    print(f"\n{YELLOW}🎯 ¡He elegido un número entre {minimo} y {maximo}!{RESET}")
    print(f"🧠 Tenés {max_intentos} intento{'s' if max_intentos != 1 else ''}. ¡Mucha suerte!\n")
    time.sleep(1)

    while intentos < max_intentos:
        restante = max_intentos - intentos
        guess = pedir_int(
            f"🔍 Adiviná el número ({restante} intento{'s' if restante != 1 else ''} restante):",
            min_val=rango_min, max_val=rango_max
        )
        if guess is None:
            print(f"\n{CYAN}👋 ¡Abandonaste la partida! El número era {secreto}.{RESET}")
            return False

        intentos += 1
        historial.append(guess)

        if guess < secreto:
            print(f"{RED}⬇️  Muy bajo.{RESET}")
            rango_min = max(rango_min, guess + 1)
        elif guess > secreto:
            print(f"{RED}⬆️  Muy alto.{RESET}")
            rango_max = min(rango_max, guess - 1)
        else:
            print(f"\n{GREEN}🎉 ¡Correcto! El número era {secreto}.{RESET}")
            print(f"{GREEN}🔢 Lo lograste en {intentos} intento{'s' if intentos > 1 else ''}.{RESET}")
            puntos = max_intentos - intentos + 1
            print(f"{GREEN}🏅 Puntos obtenidos: {puntos}{RESET}")
            print(f"{CYAN}📜 Tus intentos: {historial}{RESET}\n")
            return True

        print(f"{YELLOW}💡 Pista: está entre {rango_min} y {rango_max}.{RESET}\n")
        time.sleep(0.5)

    # Si se acaban los intentos
    print(f"{RED}❌ ¡Te quedaste sin intentos! El número era {secreto}.{RESET}")
    print(f"{CYAN}📜 Tus intentos: {historial}{RESET}\n")
    return False

def main():
    """Bucle principal del juego."""
    while True:
        jugar()
        if not pedir_si_no("🔁 ¿Querés jugar otra partida?"):
            print(f"\n{CYAN}👋 ¡Gracias por jugar! Hasta luego.{RESET}\n")
            break

if __name__ == "__main__":
    main()
