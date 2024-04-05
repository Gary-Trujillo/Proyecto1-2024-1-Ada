#Gary David Trujillo Motato 1841682-2724

def num_formas_expresarse(X, N, actual):
  # Caso base: hemos encontrado una combinación válida
  if X == 0:
      return 1
  # Caso base: hemos excedido X o no hay más números para considerar
  elif X < 0 or actual == 0:
      return 0
  else:
      # Sumar la N-ésima potencia del número actual
      suma_con_actual = num_formas_expresarse(X - actual**N, N, actual - 1)
      # No incluir la N-ésima potencia del número actual
      suma_sin_actual = num_formas_expresarse(X, N, actual - 1)
      return suma_con_actual + suma_sin_actual

# Ejemplos de uso
X = 10
N = 2
# Calcular el valor inicial de 'actual' como la raíz N-ésima de X
actual = int(X**(1/N))
resultado = num_formas_expresarse(X, N, actual)
print("Número de formas en que", X, "puede expresarse como la suma de las", N, "ésimas potencias de números:", resultado)

X = 12
N = 2
actual = int(X**(1/N))
resultado = num_formas_expresarse(X, N, actual)
print("Número de formas para X =", X, "y N =", N, "es:", resultado)

X = 10
N = 2
actual = int(X**(1/N))
resultado = num_formas_expresarse(X, N, actual)
print("Número de formas para X =", X, "y N =", N, "es:", resultado)

X = 100
N = 2
actual = int(X**(1/N))
resultado = num_formas_expresarse(X, N, actual)
print("Número de formas para X =", X, "y N =", N, "es:", resultado)
