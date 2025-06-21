import os
import time
import unicodedata

# Colores ANSI
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"

def limpiar_consola():
    """
    Limpia la consola para mantener la interfaz ordenada.
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def normalizar(texto):
    """
    Normaliza el texto eliminando acentos y tildes.
    """
    return ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )

def contar_vocales_consonantes(texto):
    """
    Cuenta vocales y consonantes en un texto normalizado.

    Parámetro:
        texto (str): Cadena a analizar.

    Retorna:
        tuple: (número de vocales, número de consonantes)
    """
    vocales = 'aeiou'
    texto = normalizar(texto.lower())

    cant_vocales = sum(1 for letra in texto if letra in vocales)
    cant_consonantes = sum(1 for letra in texto if letra.isalpha() and letra not in vocales)

    return cant_vocales, cant_consonantes

def animar_conteo(vocales, consonantes):
    """
    Muestra el conteo de vocales y consonantes con una pequeña animación.
    """
    print("\n📊 Procesando resultados", end='')
    for _ in range(3):
        print(".", end='', flush=True)
        time.sleep(0.3)

    print(f"\n\n{GREEN}🔡 Vocales encontradas:      {vocales}{RESET}")
    print(f"{CYAN}🅰️ Consonantes encontradas:  {consonantes}{RESET}")

def advertencia_si_vacio(frase):
    """
    Detecta si la frase no tiene letras válidas.
    """
    solo_letras = ''.join(c for c in frase if c.isalpha())
    return len(solo_letras) == 0

def menu_contador():
    """
    Menú principal para ingresar cadenas y contar vocales y consonantes.
    """
    while True:
        limpiar_consola()
        print(f"{YELLOW}🔠 CONTADOR DE VOCALES Y CONSONANTES 🔠{RESET}")
        frase = input("\n📝 Escribí una frase (o 'salir' para terminar): ").strip()

        if frase.lower() == 'salir':
            print(f"\n{GREEN}👋 ¡Hasta luego! Gracias por usar el contador.{RESET}")
            break

        if not frase:
            print(f"{RED}⚠️  No escribiste nada. Intentalo de nuevo.{RESET}")
            time.sleep(1.5)
            continue

        if advertencia_si_vacio(frase):
            print(f"{RED}⚠️  No hay letras válidas en esa entrada. Solo símbolos o números.{RESET}")
            time.sleep(1.5)
            continue

        v, c = contar_vocales_consonantes(frase)
        animar_conteo(v, c)

        input(f"\n{YELLOW}Presiona ENTER para analizar otra frase...{RESET}")

if __name__ == '__main__':
    menu_contador()
