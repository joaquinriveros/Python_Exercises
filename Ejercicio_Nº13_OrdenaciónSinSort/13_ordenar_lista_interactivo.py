import os
import time
import random

# Colores ANSI
CYAN   = "\033[96m"
YELLOW = "\033[93m"
GREEN  = "\033[92m"
RED    = "\033[91m"
RESET  = "\033[0m"

def limpiar_consola():
    """Limpia la pantalla en Windows/Unix."""
    os.system('cls' if os.name == 'nt' else 'clear')

def pedir_lista_usuario():
    """
    Pide al usuario una lista de números separados por comas.
    Valida que haya al menos dos números y que todos sean enteros.
    Devuelve lista de ints.
    """
    while True:
        entrada = input(f"{CYAN}Ingresa números separados por comas (ej: 5,3,8,1): {RESET}").strip()
        if not entrada:
            print(f"{RED}❌ No ingresaste nada. Por favor intentá de nuevo.{RESET}")
            continue

        if ',' not in entrada:
            print(f"{RED}❌ Debés ingresar números separados por comas.{RESET}")
            continue

        partes = entrada.split(",")
        if len(partes) < 2:
            print(f"{RED}❌ Debés ingresar números separados por comas.{RESET}")
            continue

        nums = []
        error = False
        for p in partes:
            p = p.strip()
            if p == '':
                print(f"{RED}❌ No pueden quedar elementos vacíos entre las comas.{RESET}")
                error = True
                break
            if not (p.lstrip('-').isdigit()):
                print(f"{RED}❌ '{p}' no es un número entero válido.{RESET}")
                error = True
                break
            nums.append(int(p))
        if error:
            continue
        return nums

def generar_lista_aleatoria():
    """
    Genera una lista aleatoria de enteros para prueba.
    """
    tamaño = random.randint(5, 10)
    return random.sample(range(1, 100), tamaño)

def ordenar_sin_sort(lista):
    """
    Ordena una copia de 'lista' usando insertion sort,
    mostrando cada paso de la inserción.
    """
    arr = lista[:]  # clonamos
    n = len(arr)
    for i in range(1, n):
        clave = arr[i]
        j = i - 1
        # Animar el valor que vamos a insertar
        print(f"\n{YELLOW}→ Insertando {clave} en la sublista{RESET} {arr[:i]}")
        time.sleep(0.5)

        # Desplazar los elementos mayores que la clave
        while j >= 0 and arr[j] > clave:
            arr[j+1] = arr[j]
            j -= 1
            print(f"   {arr}  (moviendo {arr[j+1]} hacia la derecha)")
            time.sleep(0.3)

        arr[j+1] = clave
        print(f"{GREEN}  Sublista ordenada:{RESET} {arr[:i+1]}")
        time.sleep(0.5)

    return arr

def pedir_opcion_menu():
    """
    Pide una opción válida del menú: 1, 2 o 3.
    """
    while True:
        opc = input("Elige una opción (1/2/3): ").strip()
        if opc in ('1', '2', '3'):
            return opc
        print(f"{RED}❌ Opción inválida. Por favor ingresa 1, 2 o 3.{RESET}")

def menu_ordenamiento():
    """
    Menú interactivo para que el usuario elija:
     - Ingresar su lista manualmente
     - Usar lista aleatoria
    Luego muestra el proceso de ordenamiento.
    """
    while True:
        limpiar_consola()
        print(f"{CYAN}🔢 ORDENAMIENTO SIN sort() 🔢{RESET}")
        print("1) Ingresar lista manualmente")
        print("2) Usar lista aleatoria")
        print("3) Salir\n")

        opc = pedir_opcion_menu()

        if opc == '3':
            print(f"\n{CYAN}👋 ¡Hasta la próxima!{RESET}\n")
            break

        if opc == '1':
            lista = pedir_lista_usuario()
        elif opc == '2':
            lista = generar_lista_aleatoria()
            print(f"\n{YELLOW}Lista generada:{RESET} {lista}\n")
            time.sleep(1)

        print(f"\n{CYAN}Lista original:{RESET} {lista}")
        input(f"\nPresiona ENTER para ver el proceso de ordenamiento...")

        ordenada = ordenar_sin_sort(lista)
        print(f"\n{GREEN}✔ Lista ordenada:{RESET} {ordenada}\n")

        input("🔁 Presiona ENTER para volver al menú...")

if __name__ == "__main__":
    menu_ordenamiento()
