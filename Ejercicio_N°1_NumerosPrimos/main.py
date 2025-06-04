import random
import time

def es_primo(n):
    if n <= 1:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

# Bienvenida y reglas del juego
print("--------------------------------- ¡Bienvenido al juego de los números primos! ---------------------------------")
print("_ Responde correctamente si el número es primo o no y ganá puntos!")
print("_ Responde con 'sí' o 'no'. También puedes usar 's' o 'n'.")
print("_ Si aciertas rápido, ganarás más puntos. ¡Buena suerte!")

puntaje = 0

for _ in range(5):
    numero = random.randint(1, 50)
    print(f"\n ¿El número {numero} es primo? (sí/no)")

    inicio = time.time()
    respuesta = input("Tu respuesta: ").strip().lower().replace("si", "sí")  # Convierte "si" en "sí"
    fin = time.time()

    correcto = es_primo(numero)
    respuesta_correcta = "sí" if correcto else "no"

    if respuesta in ["sí", "s", "No", "n"]:  # Solo acepta respuestas válidas
        if respuesta == respuesta_correcta:
            puntaje += 2 if fin - inicio < 5 else 1
            print("¡Correcto y rápido! +2 puntos")
        else:
            puntaje += 1
            print("¡Correcto! +1 punto")
    else:
        print(f"Incorrecto. La respuesta correcta era '{respuesta_correcta}'.")
    
print(f"\n🏆 ¡Juego terminado! Tu puntaje final es: {puntaje} puntos.")

