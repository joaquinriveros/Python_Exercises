import time
import os

def limpiar_consola():  # Limpia la consola para que la animación se vea más ordenada.
    os.system('cls' if os.name == 'nt' else 'clear')

def invertir_animado(texto):  # Invierte un texto mostrando cada paso de la inversión.
    invertida = ''
    for letra in reversed(texto):
        invertida += letra
        print(f"Invirtiendo... {invertida}")
        time.sleep(0.15)  # Pequeña pausa para animación

def pedir_nombre():
    """
    Solicita al usuario su nombre, lo saluda y espera a que presione ENTER para continuar.
    """
    nombre = input("\n👤 Por favor, ingresa tu nombre: ").strip().capitalize()
    print(f"\n¡Hola, {nombre}! Bienvenido al inversor interactivo de texto.\n")
    input("Presiona ENTER para continuar...")  # Espera antes de limpiar la consola
    return nombre


def despedida(nombre):
    # Imprime el saludo de despedida personalizado.
    print(f"\n👋 ¡Hasta la próxima, {nombre}! Gracias por usar el inversor de cadenas.")

def menu_interactivo():  
    # Menú interactivo que permite al usuario invertir múltiples cadenas
    # y el usuario puede salir escribiendo 'salir'.
    nombre = pedir_nombre() # Se solicita el nombre al inicio

    while True:
        limpiar_consola()
        print("----------------- INVERSOR DE CADENAS DE TEXTO -----------------")
        texto = input("\n _ Escribe aquí la cadena a invertir (o 'salir' para terminar): ")

        if texto.strip().lower() == 'salir':
            despedida(nombre)  # Saludo de despedida al elegir salir
            break

        print("\n Proceso de inversión:\n")
        invertir_animado(texto)
        input("\n Presiona ENTER para continuar e invertir otra cadena...")

# Iniciar la aplicación
menu_interactivo()
