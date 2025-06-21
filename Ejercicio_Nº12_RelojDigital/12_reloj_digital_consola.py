import os
import sys
import time
import platform

# ─────────────────────────────────────────────────────────────────────────────
# Colores ANSI
CYAN    = "\033[96m"
YELLOW  = "\033[93m"
GREEN   = "\033[92m"
RED     = "\033[91m"
RESET   = "\033[0m"

# ─────────────────────────────────────────────────────────────────────────────
def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')

def pedir_confirmacion(mensaje):
    while True:
        respuesta = input(f"{YELLOW}{mensaje} (s/n): {RESET}").strip().lower()
        if respuesta in ('s', 'si'): return True
        elif respuesta in ('n', 'no'): return False
        print(f"{RED}❌ Respuesta inválida. Ingresá 's' o 'n'.{RESET}")

def obtener_opcion():
    while True:
        opcion = input(f"\n{YELLOW}Seleccioná una opción (1/2/3/4): {RESET}").strip()
        if opcion in ('1', '2', '3', '4'):
            return opcion
        print(f"{RED}❌ Ingresá una opción válida (1 al 4).{RESET}")

def reproducir_tic():
    """Reproduce un sonido simple del sistema (si es compatible)."""
    if platform.system() == 'Windows':
        import winsound
        winsound.Beep(1000, 100)  # frecuencia 1000 Hz, duración 100 ms
    else:
        sys.stdout.write('\a')  # beep ASCII
        sys.stdout.flush()

def mostrar_reloj(formato_24h, mostrar_fecha=False, con_sonido=False):
    try:
        while True:
            limpiar_consola()
            ahora = time.localtime()
            colon = ':' if int(time.time()) % 2 == 0 else ' '
            hh = time.strftime("%H" if formato_24h else "%I", ahora)
            mm = time.strftime("%M", ahora)
            ss = time.strftime("%S", ahora)
            ampm = time.strftime(" %p", ahora) if not formato_24h else ""
            hora = f"{hh}{colon}{mm}{colon}{ss}{ampm}"
            fecha = time.strftime("%A %d de %B del %Y", ahora).capitalize()

            print(f"{CYAN}╔════════════════════════════╗{RESET}")
            if mostrar_fecha:
                print(f"{CYAN}║{GREEN}{fecha.center(26)}{CYAN}║{RESET}")
            print(f"{CYAN}║{GREEN}{hora.center(26)}{CYAN}║{RESET}")
            print(f"{CYAN}╚════════════════════════════╝{RESET}")
            print(f"\nPresioná {YELLOW}Ctrl+C{RESET} para volver al menú.")

            if con_sonido:
                reproducir_tic()

            time.sleep(1)
    except KeyboardInterrupt:
        print(f"\n{CYAN}← Regresando al menú principal...{RESET}")
        time.sleep(1)

def menu_reloj():
    while True:
        limpiar_consola()
        print(f"{YELLOW}🕒  RELOJ DIGITAL EN CONSOLA  🕒{RESET}")
        print("\nElegí una opción:")
        print("1) Formato 24 horas")
        print("2) Formato 12 horas (AM/PM)")
        print("3) Formato 24h con fecha")
        print("4) Salir")

        opcion = obtener_opcion()

        if opcion in ('1', '2', '3'):
            sonido = pedir_confirmacion("¿Querés que el reloj haga un tic cada segundo?")
            mostrar_fecha = (opcion == '3')
            formato_24 = (opcion != '2')
            mostrar_reloj(formato_24, mostrar_fecha, sonido)
        elif opcion == '4':
            print(f"\n{CYAN}👋 ¡Gracias por usar el reloj! Que Dios te bendiga.{RESET}")
            break

# ─────────────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    menu_reloj()
