
#Gary David Trujillo Motato 1841682-2724

import time

def fib_recursivo(n):
    if n <= 1:
        return n
    else:
        return fib_recursivo(n-1) + fib_recursivo(n-2)

def fib_lista(n):
    F = [0, 1]
    for i in range(2, n+1):
        F.append(F[i-1] + F[i-2])
    return F[n]

def calcular_tiempo(funcion, n):
    start_time = time.time()
    resultado = funcion(n)
    end_time = time.time()
    return resultado, end_time - start_time

valores_n = [3, 5, 7, 10]

for n in valores_n:
    resultado_recursivo, tiempo_recursivo = calcular_tiempo(fib_recursivo, n)
    resultado_lista, tiempo_lista = calcular_tiempo(fib_lista, n)

    print(f"Para n = {n}:")
    print(f"FibRecurs({n}) = {resultado_recursivo}, Tiempo: {tiempo_recursivo} s")
    print(f"FibList({n}) = {resultado_lista}, Tiempo: {tiempo_lista} s")
    print()





import matplotlib.pyplot as plt

# Datos proporcionados
valores_n = [3, 5, 7, 10]
tiempos_recursivo = [1.5974044799804688e-05, 2.86102294921875e-06, 6.198883056640625e-06, 2.8133392333984375e-05]
tiempos_lista = [5.0067901611328125e-06, 2.1457672119140625e-06, 2.1457672119140625e-06, 2.384185791015625e-06]

# Crear la gráfica
plt.plot(valores_n, tiempos_recursivo, label='Recursivo', marker='o')
plt.plot(valores_n, tiempos_lista, label='Lista', marker='o')

# Etiquetas de los ejes y título
plt.xlabel('n')
plt.ylabel('Tiempo (s)')
plt.title('Tiempo de ejecución de Fibonacci en función de n')

# Mostrar la leyenda
plt.legend()

# Mostrar la gráfica
plt.show()