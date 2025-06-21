import os
import random
import time
import sys

# Colores ANSI
RED    = "\033[91m"
GREEN  = "\033[92m"
YELLOW = "\033[93m"
CYAN   = "\033[96m"
RESET  = "\033[0m"

def limpiar_consola():
    """Limpia la pantalla en Windows o Unix."""
    os.system('cls' if os.name == 'nt' else 'clear')

def escribir_lento(texto, delay=0.02):
    """Escribe texto con efecto máquina de escribir."""
    for c in texto:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def pedir_int(mensaje, min_val=None, max_val=None):
    """
    Pide un número entero al usuario con validaciones.
    Retorna None si el usuario escribe 'salir'.
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
            print(f"{RED}❌ El número debe ser como mínimo {min_val}.{RESET}")
            continue
        if max_val is not None and valor > max_val:
            print(f"{RED}❌ El número debe ser como máximo {max_val}.{RESET}")
            continue
        return valor

def pedir_si_no(pregunta):
    """
    Pide una respuesta sí o no al usuario.
    Retorna True para 's', False para 'n'.
    """
    while True:
        r = input(f"{YELLOW}{pregunta} (s/n):{RESET} ").strip().lower()
        if r in ('s', 'si'):
            return True
        elif r in ('n', 'no'):
            return False
        else:
            print(f"{RED}❌ Solo se permite 's' o 'n'.{RESET}")

def simular_tiradas(lados, dados, repeticiones):
    """
    Simula el lanzamiento de múltiples dados por cierta cantidad de veces.
    Retorna lista con los resultados individuales y suma total de cada tirada.
    """
    resultados = []
    for _ in range(repeticiones):
        tirada = [random.randint(1, lados) for _ in range(dados)]
        total = sum(tirada)
        resultados.append((tirada, total))
    return resultados

def mostrar_histograma(resultados, lados):
    """
    Muestra la frecuencia de aparición de cada cara en formato histograma.
    """
    conteo = {cara: 0 for cara in range(1, lados + 1)}
    for tirada, _ in resultados:
        for valor in tirada:
            conteo[valor] += 1

    print(f"\n{CYAN}📊 Frecuencia de cada cara:{RESET}")
    for cara in range(1, lados + 1):
        cantidad = conteo[cara]
        barra = '▇' * (cantidad * 100 // max(conteo.values(), default=1) // 2)
        print(f"  {cara:>2}: {barra} ({cantidad})")

def menu_dado():
    """
    Menú principal del simulador de lanzamiento de dados.
    """
    while True:
        limpiar_consola()
        escribir_lento(f"{YELLOW}🎲 SIMULADOR DE LANZAMIENTO DE DADO 🎲{RESET}")
        print("Podés escribir 'salir' en cualquier momento para terminar.\n")

        lados = pedir_int("👉 ¿Cuántas caras tiene el dado? (mínimo 2, máximo 100):", min_val=2, max_val=100)
        if lados is None:
            break

        dados = pedir_int("👉 ¿Cuántos dados querés lanzar a la vez? (mínimo 1):", min_val=1)
        if dados is None:
            break

        repeticiones = pedir_int("👉 ¿Cuántas tiradas querés hacer? (mínimo 1):", min_val=1)
        if repeticiones is None:
            break

        print(f"\n{YELLOW}Simulando lanzamientos", end='', flush=True)
        for _ in range(3):
            time.sleep(0.4)
            print('.', end='', flush=True)
        print(RESET)

        resultados = simular_tiradas(lados, dados, repeticiones)

        # Mostrar resultados de cada tirada
        print(f"\n{GREEN}✅ Resultados:{RESET}")
        for i, (tirada, total) in enumerate(resultados, start=1):
            print(f"  Tirada {i:>2}: {tirada} → suma = {total}")
            time.sleep(0.05)

        # Mostrar estadísticas
        totales = [suma for _, suma in resultados]
        suma_total = sum(totales)
        promedio = suma_total / len(totales)
        print(f"\n{CYAN}📈 Estadísticas generales:{RESET}")
        print(f"  • Total de tiradas:   {len(totales)}")
        print(f"  • Suma acumulada:     {suma_total}")
        print(f"  • Promedio por tirada:{promedio:.2f}")

        mostrar_histograma(resultados, lados)

        if not pedir_si_no("\n🔁 ¿Querés realizar otra simulación?"):
            print(f"\n{CYAN}👋 ¡Gracias por usar el simulador! Hasta la próxima.{RESET}\n")
            break

if __name__ == "__main__":
    menu_dado()
