# 08_conversor_temperatura.py

import os
import sys
import time
import re
import logging

# ─────────────────────────────────────────────────────────────────────────────
# Configuración de logging para guardar el historial de conversiones
logging.basicConfig(
    filename='conversiones.log',
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# Colores ANSI para consola
VERDE    = "\033[92m"
ROJO     = "\033[91m"
AMARILLO = "\033[93m"
AZUL     = "\033[94m"
RESET    = "\033[0m"

def escribir_lento(texto, delay=0.035):
    """
    Efecto 'máquina de escribir' para mostrar texto pausado.
    """
    for c in texto:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def limpiar_consola():
    """
    Limpia la pantalla en Windows o Unix.
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def convertir_temperatura(valor, origen, destino):
    """
    Convierte un valor de temperatura entre:
    C (Celsius), F (Fahrenheit), K (Kelvin), R (Rankine).
    """
    origen = origen.upper()
    destino = destino.upper()

    if origen == destino:
        return valor

    # --- Paso 1: llevar todo a Celsius ---
    if origen == 'C':
        c = valor
    elif origen == 'F':
        c = (valor - 32) * 5/9
    elif origen == 'K':
        c = valor - 273.15
    elif origen == 'R':
        c = (valor - 491.67) * 5/9
    else:
        return None

    # --- Paso 2: de Celsius al destino ---
    if destino == 'C':
        return c
    if destino == 'F':
        return c * 9/5 + 32
    if destino == 'K':
        return c + 273.15
    if destino == 'R':
        return (c + 273.15) * 9/5
    return None

def pedir_si_no(pregunta):
    """
    Pide una respuesta 's' o 'n', vuelve a preguntar si no es válida.
    """
    while True:
        r = input(f"{pregunta} (s/n): ").strip().lower()
        if r in ('s','si'): return True
        if r in ('n','no'): return False
        print(f"{ROJO}❌ Solo 's' o 'n' son aceptados.{RESET}")

def mostrar_unidades():
    """
    Muestra las unidades soportadas.
    """
    print(f"{AZUL}\n🌡️ Unidades disponibles:")
    print("  C  → Celsius")
    print("  F  → Fahrenheit")
    print("  K  → Kelvin")
    print("  R  → Rankine\n" + RESET)

def parsear_entrada(entrada):
    """
    Reconoce entradas del tipo:
    '25C F', '25 C F', '25cF', '100.5K C', etc.
    Retorna (valor: float, origen: str, destino: str) o (None, None, None).
    """
    patrón = r'^\s*([0-9]+(?:\.[0-9]+)?)\s*([cCfFkKrR])\s*([cCfFkKrR])\s*$'
    m = re.match(patrón, entrada)
    if not m:
        return None, None, None
    return float(m.group(1)), m.group(2).upper(), m.group(3).upper()

def menu_convertidor():
    """
    Bucle principal: muestra instrucciones y permite convertir temperaturas
    tantas veces como el usuario quiera. Procesa errores y re-pregunta.
    """
    while True:
        limpiar_consola()
        print(AZUL + "🔄 Conversor de Temperatura Interactivo 🔄" + RESET)
        escribir_lento("💬 Convertí entre °C, °F, °K y °R de forma rápida.\n")
        mostrar_unidades()

        # --- Bucle de entrada hasta que sea válida o el usuario salga ---
        while True:
            entrada = input(
                "👉 Ingresa tu conversión en formato:\n"
                "   <valor> <origen> <destino>\n"
                "   p.ej.: 25 C F   (o escribe 'salir')\n> "
            ).strip()

            if entrada.lower() == 'salir':
                print(f"\n👋 {AMARILLO}¡Gracias por usar el conversor!{RESET}\n")
                return  # finaliza toda la aplicación

            valor, origen, destino = parsear_entrada(entrada)
            if valor is None:
                print(f"{ROJO}❌ Formato inválido. Usa, por ejemplo: 100 K C{RESET}\n")
                continue  # re-pregunta en este bucle
            break  # entrada válida, salimos del bucle de input

        # --- Animación de proceso ---
        print("\n🔢 Convirtiendo", end='', flush=True)
        for _ in range(3):
            time.sleep(0.5)
            print('.', end='', flush=True)
        print('\n')

        # --- Conversión y resultado ---
        resultado = convertir_temperatura(valor, origen, destino)
        if resultado is None:
            print(f"{ROJO}❌ No se puede convertir de {origen} a {destino}.{RESET}")
        else:
            mensaje = f"{VERDE}✅ {valor:.2f}°{origen} = {resultado:.2f}°{destino}{RESET}"
            print(mensaje)
            logging.info(f"{valor:.2f}°{origen} → {resultado:.2f}°{destino}")

        # --- ¿Otra conversión? ---
        if not pedir_si_no("\n🔁 ¿Querés convertir otra temperatura?"):
            print(f"\n👋 {AMARILLO}¡Hasta la próxima!{RESET}\n")
            break

if __name__ == '__main__':
    menu_convertidor()
