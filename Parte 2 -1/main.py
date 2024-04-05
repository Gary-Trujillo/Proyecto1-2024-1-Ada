#Gary David Trujillo Motato 1841682-2724

def valor_coincide_con_indice(vector, inicio, fin):
  # Caso base: cuando el inicio supera al fin
  if inicio > fin:
      return False

  # Calculamos el índice medio
  medio = (inicio + fin) // 2

  # Si el valor en el índice medio es igual a su índice, retornamos True
  if vector[medio] == medio:
      return True

  # Si el valor en el índice medio es mayor que su índice, buscamos en la mitad izquierda del vector
  elif vector[medio] > medio:
      return valor_coincide_con_indice(vector, medio + 1, fin)

  # Si el valor en el índice medio es menor que su índice, buscamos en la mitad derecha del vector
  else:
      return valor_coincide_con_indice(vector, inicio, medio - 1)

# Pruebas
vector = [5, 4, 3, 2, 1, 0]  # Vector ordenado decrecientemente
resultado = valor_coincide_con_indice(vector, 0, len(vector) - 1)
print("¿Algún valor coincide con su índice?", resultado)

#  Valor único que coincide con su índice
vector1 = [4, 3, 2, 1, 0, -1]
resultado1 = valor_coincide_con_indice(vector1, 0, len(vector1) - 1)
print("¿Algún valor coincide con su índice?", resultado1)  # Esperado: True

# Como el vector no tiene ningún otro valor que coincida con su índice, la función devuelve False
vector2 = [5, 4, 4, 1, 0, 0]
resultado2 = valor_coincide_con_indice(vector2, 0, len(vector2) - 1)
print("¿Algún valor coincide con su índice?", resultado2)  # Esperado: False
