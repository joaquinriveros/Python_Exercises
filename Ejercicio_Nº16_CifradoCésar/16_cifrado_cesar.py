import os
import sys
import time
import unicodedata

# Colores ANSI
RED    = "\033[91m"
GREEN  = "\033[92m"
YELLOW = "\033[93m"
CYAN   = "\033[96m"
RESET  = "\033[0m"

def limpiar_consola():
    """Limpia la pantalla en Windows/Unix."""
    os.system('cls' if os.name == 'nt' else 'clear')

def escribir_lento(texto, delay=0.02):
    """Efecto máquina de escribir para dar feedback."""
    for c in texto:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def pedir_texto(mensaje):
    """
    Pide al usuario un texto no vacío.
    Retorna la cadena o None si escribe 'salir'.
    """
    while True:
        entrada = input(f"{CYAN}{mensaje}{RESET} ").rstrip()
        if entrada.lower() == 'salir':
            return None
        if entrada == '':
            print(f"{RED}❌ No puede estar vacío. Ingresa texto o 'salir'.{RESET}")
            continue
        return entrada

def normalizar_texto(texto):
    """Elimina tildes y acentos para el cifrado."""
    return ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )

def pedir_int(mensaje, min_val=None):
    """
    Pide al usuario un entero válido (desplazamiento).
    Retorna el entero o None si escribe 'salir'.
    """
    while True:
        entrada = input(f"{CYAN}{mensaje}{RESET} ").strip().lower()
        if entrada == 'salir':
            return None
        if entrada.lstrip('-').isdigit():
            valor = int(entrada)
            if min_val is not None and valor < min_val:
                print(f"{RED}❌ Debe ser ≥ {min_val}.{RESET}")
                continue
            return valor
        print(f"{RED}❌ Ingresa un número entero válido (o 'salir').{RESET}")

def pedir_opcion(mensaje, opciones):
    """
    Pide al usuario una opción de un conjunto dado.
    opciones: dict de {'clave': 'Descripción'}.
    Retorna la clave elegida o None si escribe 'salir'.
    """
    claves = list(opciones.keys())
    while True:
        print(f"{YELLOW}{mensaje}{RESET}")
        for k, desc in opciones.items():
            print(f"  {k}) {desc}")
        entrada = input("> ").strip().lower()
        if entrada == 'salir':
            return None
        if entrada in claves:
            return entrada
        print(f"{RED}❌ Opción inválida. Elige {', '.join(claves)} o 'salir'.{RESET}")

def pedir_si_no(pregunta):
    """
    Pide 's' o 'n'. Retorna True para sí, False para no.
    """
    while True:
        r = input(f"{YELLOW}{pregunta} (s/n){RESET} ").strip().lower()
        if r in ('s', 'si'): return True
        if r in ('n', 'no'): return False
        print(f"{RED}❌ Solo 's' o 'n'.{RESET}")

def cifrado_cesar(texto, shift, modo='enc'):
    """
    Aplica cifrado César. modo='enc' para cifrar, 'dec' para descifrar.
    """
    resultado = ''
    if modo == 'dec':
        shift = -shift
    for c in texto:
        if 'a' <= c <= 'z':
            base = ord('a')
            resultado += chr((ord(c) - base + shift) % 26 + base)
        elif 'A' <= c <= 'Z':
            base = ord('A')
            resultado += chr((ord(c) - base + shift) % 26 + base)
        else:
            resultado += c
    return resultado

def explicar_cifrado_cesar():
    print(f"\n{YELLOW}🧠 ¿Qué es el Cifrado César?{RESET}")
    print("Es un método de encriptación donde cada letra se reemplaza por otra,")
    print("desplazada un número fijo de posiciones en el alfabeto.")
    print("Por ejemplo, con desplazamiento 3: A → D, B → E, C → F, etc.")
    print("No afecta los signos ni los números. Solo letras.\n")

def prueba_rapida():
    print(f"\n{YELLOW}🧪 Ejemplo rápido de cifrado César:{RESET}")
    ejemplo = "Hola Mundo"
    desplazamiento = 5
    print(f"Texto original: {ejemplo}")
    cifrado = cifrado_cesar(ejemplo, desplazamiento)
    print(f"Cifrado (+{desplazamiento}): {cifrado}")
    descifrado = cifrado_cesar(cifrado, desplazamiento, modo='dec')
    print(f"Descifrado: {descifrado}\n")

def guardar_resultado(texto):
    while True:
        nombre = input("📁 Nombre del archivo para guardar (sin extensión): ").strip()
        if nombre == '':
            print(f"{RED}❌ No puede estar vacío.{RESET}")
            continue
        try:
            with open(f"{nombre}.txt", "w", encoding="utf-8") as f:
                f.write(texto)
            print(f"{GREEN}✅ Resultado guardado en '{nombre}.txt'{RESET}")
            break
        except Exception as e:
            print(f"{RED}❌ Error al guardar archivo: {e}{RESET}")

def menu_cifrado():
    limpiar_consola()
    escribir_lento(f"{CYAN}🔐 Cifrado César interactivo 🔐{RESET}\n")
    escribir_lento("Escribe 'salir' en cualquier entrada para terminar.\n")

    if pedir_si_no("¿Querés ver una breve explicación del cifrado César?"):
        explicar_cifrado_cesar()

    while True:
        opciones_menu = {
            '0': 'Ver ejemplo automático',
            '1': 'Cifrar texto',
            '2': 'Descifrar texto'
        }
        modo = pedir_opcion("Elige una opción:", opciones_menu)
        if modo is None:
            break

        if modo == '0':
            prueba_rapida()
            if not pedir_si_no("🔁 ¿Querés volver al menú principal?"):
                break
            limpiar_consola()
            continue

        texto = pedir_texto("✍️ Ingresa el texto a procesar:")
        if texto is None:
            break

        texto = normalizar_texto(texto)

        shift = pedir_int("🔢 Ingresa el desplazamiento (ej: 3):", min_val=0)
        if shift is None:
            break

        print(f"\n{YELLOW}Procesando", end='', flush=True)
        for _ in range(3):
            time.sleep(0.4)
            print('.', end='', flush=True)
        print(RESET)

        accion = 'enc' if modo == '1' else 'dec'
        resultado = cifrado_cesar(texto, shift, modo=accion)
        acción_txt = "Cifrado" if modo == '1' else "Descifrado"
        print(f"\n{GREEN}✅ {acción_txt} completo:{RESET}\n{resultado}\n")

        if pedir_si_no("💾 ¿Querés guardar el resultado en un archivo?"):
            guardar_resultado(resultado)

        if not pedir_si_no("🔁 ¿Querés procesar otro texto?"):
            break

    print(f"\n{CYAN}👋 ¡Hasta luego!{RESET}")

if __name__ == "__main__":
    menu_cifrado()
