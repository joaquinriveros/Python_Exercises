import os
import time

# Colores ANSI
RED    = "\033[91m"
GREEN  = "\033[92m"
YELLOW = "\033[93m"
CYAN   = "\033[96m"
RESET  = "\033[0m"

# Almacenará todas las mediciones de la sesión
historial = []

def limpiar_consola():
    """Limpia la pantalla para mantener la interfaz ordenada."""
    os.system('cls' if os.name == 'nt' else 'clear')

def escribir_lento(texto, delay=0.02):
    """Efecto máquina de escribir para mostrar textos explicativos."""
    for c in texto:
        print(c, end='', flush=True)
        time.sleep(delay)
    print()

def mostrar_introduccion():
    """Explica al usuario qué es el IMC y para qué sirve."""
    limpiar_consola()
    escribir_lento(f"{CYAN}Bienvenido a la Calculadora de Índice de Masa Corporal (IMC){RESET}\n")
    texto = (
        "El IMC es una medida que relaciona tu peso con tu altura\n"
        "y sirve para estimar si tu peso está en un rango saludable.\n"
        "Categorías según la OMS:\n"
        "  - Bajo peso      (< 18.5)\n"
        "  - Peso normal    (18.5 – 24.9)\n"
        "  - Sobrepeso      (25 – 29.9)\n"
        "  - Obesidad       (>= 30)\n"
    )
    escribir_lento(texto)
    input(f"{YELLOW}Presiona ENTER para comenzar a calcular tu IMC...{RESET}")

def calcular_imc(peso, altura):
    """Devuelve el IMC redondeado a dos decimales."""
    return round(peso / (altura ** 2), 2)

def clasificar_imc(imc):
    """Según el IMC, devuelve la categoría y un mensaje explicativo."""
    if imc < 18.5:
        return "🔵 Bajo peso — Podrías necesitar ganar algo de masa muscular o grasa para mejorar tu salud."
    elif imc < 25:
        return "🟢 Peso normal — Tu peso está dentro del rango saludable. ¡Mantén tus hábitos!"
    elif imc < 30:
        return "🟠 Sobrepeso — Considerá ajustar tu dieta y aumentar tu actividad física."
    else:
        return "🔴 Obesidad — Te recomendamos consultar con un profesional de la salud."

def pedir_float(mensaje):
    """
    Solicita un número positivo. 
    Si el usuario escribe 'salir', retorna None para terminar la sesión.
    """
    while True:
        entrada = input(mensaje).strip().lower()
        if entrada == 'salir':
            return None
        try:
            valor = float(entrada)
            if valor <= 0:
                print(f"{RED}❌ El valor debe ser mayor que cero.{RESET}")
                continue
            return valor
        except ValueError:
            print(f"{RED}❌ Entrada inválida. Ingresá un número válido (o 'salir').{RESET}")

def mostrar_grafico(imc):
    """
    Dibuja una barra ASCII para visualizar en qué zona del IMC caes.
    """
    print(f"\n{CYAN}Visualización de tu rango de IMC{RESET}")
    categorias = [
        ("Bajo peso", 0,   18.5, "🔵"),
        ("Peso normal", 18.5, 25, "🟢"),
        ("Sobrepeso", 25,   30, "🟠"),
        ("Obesidad", 30,   40, "🔴")
    ]
    # Construcción de la barra: 20 caracteres
    barra = ""
    for nombre, min_v, max_v, icono in categorias:
        if min_v <= imc < max_v:
            barra += icono * 5
        else:
            barra += "─" * 5

    print("  0      18.5     25       30       40")
    print(f"  │{barra}│")
    print(f"     {YELLOW}↑ Aquí se encuentra tu IMC: {imc}{RESET}")

def mostrar_resumen():
    """Imprime al final un resumen de todas las mediciones hechas."""
    if not historial:
        return
    print(f"\n{CYAN}📊 Resumen de tu sesión:{RESET}")
    escribir_lento("A continuación, todas tus mediciones:\n")
    for i, dato in enumerate(historial, start=1):
        línea = (
            f"{i}. Peso: {dato['peso']} kg - Altura: {dato['altura']} m -> "
            f"IMC: {dato['imc']} - {dato['categoria'].split('—')[0].strip()}"
        )
        print(línea)
    print()

def menu_imc():
    """Bucle principal: guía al usuario a través del cálculo interactivo."""
    mostrar_introduccion()

    while True:
        limpiar_consola()
        print(f"{CYAN}⚖️  CALCULADORA DE IMC  ⚖️{RESET}")
        print("Escribe 'salir' en cualquier momento para finalizar.\n")

        peso = pedir_float("💪 Ingresá tu peso en kilogramos: ")
        if peso is None:
            break

        altura = pedir_float("📏 Ingresá tu altura en metros: ")
        if altura is None:
            break

        print(f"\n{YELLOW}Calculando tu IMC", end="", flush=True)
        for _ in range(3):
            time.sleep(0.5)
            print(".", end="", flush=True)
        print(RESET)

        imc = calcular_imc(peso, altura)
        categoria = clasificar_imc(imc)
        historial.append({
            "peso": peso,
            "altura": altura,
            "imc": imc,
            "categoria": categoria
        })

        # Resultados al usuario con explicaciones
        print(f"\n{GREEN}✅ Tu IMC es: {imc}{RESET}")
        print(f"{YELLOW}{categoria}{RESET}")

        mostrar_grafico(imc)

        input(f"\n{YELLOW}Presioná ENTER para otro cálculo o escribe 'salir' en la siguiente pantalla.{RESET}")

    # Final de sesión: despedida y resumen
    limpiar_consola()
    print(f"{CYAN}👋 ¡Gracias por usar la calculadora de IMC!{RESET}")
    mostrar_resumen()

if __name__ == "__main__":
    menu_imc()

