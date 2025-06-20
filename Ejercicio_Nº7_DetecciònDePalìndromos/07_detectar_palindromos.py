import time
import unicodedata
import os
import sys

# Colores
VERDE = "\033[92m"
ROJO = "\033[91m"
AMARILLO = "\033[93m"
AZUL = "\033[94m"
RESET = "\033[0m"

def escribir_lento(texto, delay=0.04):
    for c in texto:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')

def quitar_tildes(texto):
    """
    Elimina tildes de las letras.
    """
    return ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )

def es_alfabetica(cadena):
    """
    Verifica que la cadena contenga solo letras (sin espacios, números ni símbolos).
    """
    cadena_sin_tildes = quitar_tildes(cadena)
    return cadena_sin_tildes.isalpha()

def es_palindromo(cadena, mostrar_proceso=True):
    limpio = quitar_tildes(cadena)
    texto = ''.join(c.lower() for c in limpio if c.isalpha())
    invertido = texto[::-1]

    if mostrar_proceso:
        escribir_lento("\n🔍 Comparando letra por letra...\n", 0.03)
        for original, reflejo in zip(texto, invertido):
            print(f"   {AZUL}{original}{RESET}  <-->  {AZUL}{reflejo}{RESET}")
            time.sleep(0.08)

    return texto == invertido

def pedir_si_no(pregunta):
    while True:
        respuesta = input(f"{pregunta} (s/n): ").strip().lower()
        if respuesta in ['s', 'si']:
            return True
        elif respuesta in ['n', 'no']:
            return False
        else:
            print(f"{ROJO}❌ Por favor respondé solo con 's' o 'n'.{RESET}")

def menu_palindromos():
    limpiar_consola()
    print(f"{AMARILLO}🔁 Bienvenido al Detector de Palíndromos Interactivo 🔁{RESET}")
    print("💬 Ingresá una palabra sin espacios, números ni símbolos.\n")

    while True:
        frase = input("📝 Ingresá una palabra (o escribí 'salir' para terminar):\n> ").strip()

        if frase.lower() == 'salir':
            print(f"\n👋 {VERDE}¡Gracias por usar el detector! Hasta pronto.{RESET}")
            break

        if not es_alfabetica(frase):
            print(f"{ROJO}❌ Error: Solo se permiten letras. No uses espacios, números ni símbolos.{RESET}")
            continue

        modo_lento = pedir_si_no("¿Querés ver el proceso paso a paso?")
        resultado = es_palindromo(frase, mostrar_proceso=modo_lento)

        if resultado:
            print(f"\n{VERDE}✅ ¡Es un palíndromo!{RESET} 🤩")
        else:
            print(f"\n{ROJO}❌ No es un palíndromo.{RESET} 😕")

        if not pedir_si_no("\n¿Querés probar otra palabra?"):
            print(f"\n🎉 {VERDE}¡Hasta la próxima!{RESET} 👋")
            break
        else:
            limpiar_consola()
            print(f"{AZUL}🔁 Nuevo intento...{RESET}\n")

if __name__ == '__main__':
    menu_palindromos()
