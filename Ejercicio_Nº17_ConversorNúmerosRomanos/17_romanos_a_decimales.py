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

# Patrón para validar numerales romanos clásicos (hasta 3999)
ROMAN_PATTERN = re.compile(
    r'^M{0,3}(CM|CD|D?C{0,3})'
    r'(XC|XL|L?X{0,3})'
    r'(IX|IV|V?I{0,3})$',
    re.IGNORECASE
)

def limpiar_consola():
    """Limpia la pantalla en Windows o Unix."""
    os.system('cls' if os.name == 'nt' else 'clear')

def escribir_lento(texto, delay=0.02):
    """Efecto máquina de escribir para mensajes explicativos."""
    for c in texto:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def validar_romano(s):
    """
    Verifica si la cadena s es un numeral romano válido
    (entre I y MMMCMXCIX, es decir 1–3999).
    """
    return bool(ROMAN_PATTERN.match(s))

def romano_a_decimal(s):
    """
    Convierte un numeral romano (válido) a su valor decimal.
    Uso del método sustractivo.
    """
    s = s.upper()
    valores = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
               'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev = 0
    for ch in reversed(s):
        curr = valores[ch]
        if curr < prev:
            total -= curr
        else:
            total += curr
            prev = curr
    return total

def pedir_romano():
    """
    Pide al usuario un numeral romano no vacío.
    Repite hasta recibir uno válido o 'salir'.
    Retorna la cadena o None si decide salir.
    """
    while True:
        entrada = input(f"{CYAN}🔢 Ingresa un numeral romano (o 'salir'): {RESET}").strip()
        if entrada.lower() == 'salir':
            return None
        if entrada == '':
            print(f"{RED}❌ No puede estar vacío.{RESET}")
            continue
        if not validar_romano(entrada):
            print(f"{RED}❌ '{entrada}' no es un numeral romano válido.{RESET}")
            continue
        return entrada

def pedir_si_no(pregunta):
    """
    Solicita 's' o 'n', devuelve True/False.
    """
    while True:
        resp = input(f"{YELLOW}{pregunta} (s/n): {RESET}").strip().lower()
        if resp in ('s', 'si'):
            return True
        if resp in ('n', 'no'):
            return False
        print(f"{RED}❌ Solo 's' o 'n'.{RESET}")

def menu_romanos():
    """
    Menú interactivo para convertir romanos a decimales.
    """
    limpiar_consola()
    escribir_lento(f"{CYAN}📜 Convertidor de Números Romanos a Decimales 📜{RESET}\n")
    escribir_lento("Escribe 'salir' si deseas terminar la aplicación.\n")

    while True:
        romano = pedir_romano()
        if romano is None:
            print(f"\n{CYAN}👋 ¡Hasta luego!{RESET}\n")
            break

        # Animación de cálculo
        print(f"\n{YELLOW}Calculando el valor de {romano.upper()}", end='', flush=True)
        for _ in range(3):
            time.sleep(0.4)
            print('.', end='', flush=True)
        print(RESET)

        decimal = romano_a_decimal(romano)
        print(f"\n{GREEN}✅ {romano.upper()}  →  {decimal}{RESET}\n")

        if not pedir_si_no("🔁 ¿Querés convertir otro numeral?"):
            print(f"\n{CYAN}👋 ¡Gracias por usar el conversor!{RESET}\n")
            break

if __name__ == "__main__":
    menu_romanos()
