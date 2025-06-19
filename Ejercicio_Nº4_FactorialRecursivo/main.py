import time

# Variable global para contar llamadas recursivas
contador_llamadas = 0

def factorial_recursivo(n):
    """
    Calcula el factorial de forma recursiva.
    """
    global contador_llamadas
    contador_llamadas += 1

    # Caso base
    if n == 0 or n == 1:
        return 1

    # Llamada recursiva
    return n * factorial_recursivo(n - 1)

def factorial_iterativo(n):
    """
    Calcula el factorial de forma iterativa.
    """
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

def main():
    print("///////////// Comparador de Factorial Recursivo vs Iterativo /////////////")
    print("--------------------------------------------------------------------------\n")

    try:
        # Entrada del usuario
        n = int(input(" _ Ingresa un número entero no negativo (recomendación: menor que 997): "))

        if n < 0:
            print("❌ El factorial no está definido para números negativos.")

        global contador_llamadas
        contador_llamadas = 0

        # Cálculo recursivo
        try:
            inicio_rec = time.perf_counter()
            resultado_rec = factorial_recursivo(n)
            fin_rec = time.perf_counter()
        except RecursionError:
            print("❌ Error: se superó la profundidad máxima de recursión.")
            return

        # Mostrar resultados recursivos
        print(f"\n✅ Resultado Recursivo: {resultado_rec}")
        print(f"📈 Llamadas recursivas: {contador_llamadas}")
        print(f"⏱️ Tiempo recursivo: {fin_rec - inicio_rec:.8f} segundos")

        # Cálculo iterativo
        inicio_it = time.perf_counter()
        resultado_it = factorial_iterativo(n)
        fin_it = time.perf_counter()

        # Mostrar resultados iterativos
        print(f"\n✅ Resultado Iterativo: {resultado_it}")
        print(f"⏱️ Tiempo iterativo: {fin_it - inicio_it:.8f} segundos")

        # Comparación final
        if resultado_it == resultado_rec:
            print(f"\n🎉 Ambos métodos dieron el mismo resultado ✅")
        else:
            print(f"\n⚠️ Los resultados difieren ❌")

    except ValueError:
        print("❗ Entrada inválida. Por favor, ingresa un número entero.")

if __name__ == "__main__":
    main()
