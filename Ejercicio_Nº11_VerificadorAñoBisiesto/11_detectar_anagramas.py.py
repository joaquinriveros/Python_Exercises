# 11_detectar_anagramas.py

def normalizar(texto):
    """
    Convierte un texto a minúsculas, elimina espacios y tildes,
    y ordena las letras para facilitar la comparación.
    """
    import unicodedata
    texto = texto.lower()
    texto = ''.join(c for c in texto if c.isalpha())  # Solo letras
    texto = unicodedata.normalize('NFD', texto).encode('ascii', 'ignore').decode('utf-8')
    return sorted(texto)

def son_anagramas(a, b):
    return normalizar(a) == normalizar(b)

def pedir_texto(mensaje):
    while True:
        texto = input(mensaje).strip()
        if texto.lower() == 'salir':
            return None
        if not texto:
            print("⚠️ No ingresaste nada. Por favor, intentá de nuevo o escribí 'salir' para terminar.")
            continue
        return texto

def pedir_confirmacion(mensaje):
    while True:
        respuesta = input(mensaje).strip().lower()
        if respuesta in ('s', 'n'):
            return respuesta
        print("⚠️ Por favor, respondé solo con 's' para sí o 'n' para no.")

def menu_anagramas():
    print("🔁 Bienvenido al Verificador de Anagramas 🔁\n")
    print("¿Sabés qué es un anagrama? 🤔")
    print("Un anagrama es una palabra o frase formada al reordenar las letras de otra palabra o frase, usando todas las letras exactamente una vez.")
    print("Por ejemplo, 'amor' y 'roma' son anagramas.\n")
    print("Podés ingresar palabras o frases para comprobar si son anagramas.")
    print("Escribí 'salir' en cualquier momento para terminar.\n")

    while True:
        a = pedir_texto(" Ingresá la primera palabra o frase: ")
        if a is None:
            print("👋 ¡Gracias por usar el verificador! Hasta luego.")
            break

        b = pedir_texto(" Ingresá la segunda palabra o frase: ")
        if b is None:
            print("👋 ¡Gracias por usar el verificador! Hasta luego.")
            break

        if son_anagramas(a, b):
            print(" ¡Genial! Son anagramas.")
        else:
            print(" Lo siento, no son anagramas.")

        print("\n----------------------------------------")
        seguir = pedir_confirmacion("¿Querés probar con otras palabras? (s/n): ")
        if seguir == 'n':
            print("👋 ¡Gracias por usar el verificador! Hasta luego.")
            break
        print()

if __name__ == '__main__':
    menu_anagramas()
