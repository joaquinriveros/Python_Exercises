import os

# Colores ANSI
RED    = "\033[91m"
GREEN  = "\033[92m"
YELLOW = "\033[93m"
CYAN   = "\033[96m"
RESET  = "\033[0m"

# Matriz de ejemplo (10×10)
MATRIZ = [
    list("C A S A D E C U A M".split()),
    list("O B O L A R Z B R A".split()),
    list("L A P I Z P O M A R".split()),
    list("A R B O L E S C A S".split()),
    list("R A M A S C A J A S".split()),
    list("E S O P A L E T R A".split()),
    list("O M U M E L E F A N".split()),
    list("N I Ñ O S T O R I N".split()),
    list("S T A D I O M U N O".split()),
    list("M O T O C I C L E T".split()),
]

# Todas las direcciones posibles: horizontal, vertical, diagonales
DIRECCIONES = [
    (-1,  0), (1,  0), (0, -1), (0,  1),
    (-1, -1), (-1, 1), (1, -1), (1,  1),
]

def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')

def imprimir_matriz_con_resaltado(coords=[]):
    """
    Muestra la matriz y resalta las coordenadas encontradas.
    """
    print(f"\n{CYAN}🔎 Sopa de Letras{RESET}")
    for i, fila in enumerate(MATRIZ):
        for j, letra in enumerate(fila):
            if (i, j) in coords:
                print(f"{GREEN}{letra}{RESET}", end=" ")
            else:
                print(letra, end=" ")
        print()
    print()

def pedir_palabra(buscadas):
    """
    Pide una palabra válida al usuario. Valida que:
    - Sea solo letras
    - No haya sido buscada antes
    - Tenga mínimo 2 letras
    """
    while True:
        entrada = input(f"{YELLOW}🔤 Ingresa la palabra a buscar (o 'salir'): {RESET}").strip()
        if entrada.lower() == 'salir':
            return None
        if not entrada.isalpha():
            print(f"{RED}❌ Solo se permiten letras. Intentá de nuevo.{RESET}")
            continue
        if len(entrada) < 2:
            print(f"{RED}❌ Ingresá al menos 2 letras.{RESET}")
            continue
        palabra = entrada.upper()
        if palabra in buscadas:
            print(f"{YELLOW}⚠ Ya buscaste esa palabra. Probá con otra.{RESET}")
            continue
        return palabra

def buscar_palabra(matriz, palabra):
    """
    Busca una palabra en todas las direcciones.
    Devuelve lista de coordenadas si la encuentra, [] si no.
    """
    filas = len(matriz)
    cols  = len(matriz[0]) if filas else 0
    L = len(palabra)

    for i in range(filas):
        for j in range(cols):
            if matriz[i][j] != palabra[0]:
                continue
            for dx, dy in DIRECCIONES:
                coords = [(i, j)]
                x, y = i, j
                for k in range(1, L):
                    x += dx
                    y += dy
                    if 0 <= x < filas and 0 <= y < cols and matriz[x][y] == palabra[k]:
                        coords.append((x, y))
                    else:
                        break
                if len(coords) == L:
                    return coords
    return []

def pedir_si_no(pregunta):
    """
    Fuerza al usuario a responder 's' o 'n'. Repite si responde mal.
    """
    while True:
        respuesta = input(f"{YELLOW}{pregunta} (s/n): {RESET}").strip().lower()
        if respuesta in ('s', 'si'):
            return True
        elif respuesta in ('n', 'no'):
            return False
        print(f"{RED}❌ Solo se acepta 's' o 'n'. Intentá de nuevo.{RESET}")

def menu_sopa_letras():
    """
    Menú principal. Muestra la sopa, pide palabras, busca y resalta.
    Guarda historial de búsquedas exitosas.
    """
    buscadas = set()
    encontradas = []

    while True:
        limpiar_consola()
        imprimir_matriz_con_resaltado()
        palabra = pedir_palabra(buscadas)
        if palabra is None:
            break
        buscadas.add(palabra)

        coords = buscar_palabra(MATRIZ, palabra)
        if coords:
            encontradas.append(palabra)
            print(f"\n{GREEN}✅ ¡'{palabra}' encontrada!{RESET}")
            print("📍 Posiciones (fila, columna):")
            for f, c in coords:
                print(f"  ({f+1}, {c+1})")
            imprimir_matriz_con_resaltado(coords)
        else:
            print(f"\n{RED}❌ '{palabra}' NO se encontró en la matriz.{RESET}")

        print(f"\n{CYAN}🔢 Palabras encontradas hasta ahora: {len(encontradas)}{RESET}")
        input(f"\n{YELLOW}Presioná ENTER para continuar...{RESET}")

    limpiar_consola()
    print(f"{CYAN}👋 Gracias por jugar a la sopa de letras.{RESET}")
    if encontradas and pedir_si_no("¿Querés ver todas las palabras que encontraste?"):
        print(f"\n{GREEN}📋 Palabras encontradas:{RESET}")
        for i, p in enumerate(encontradas, 1):
            print(f"{i}. {p}")
    print(f"\n{CYAN}¡Hasta la próxima!{RESET}\n")

if __name__ == "__main__":
    menu_sopa_letras()
