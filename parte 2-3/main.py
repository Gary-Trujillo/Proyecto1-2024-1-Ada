#Gary David Trujillo Motato 1841682-2724

def super_digit(x):
  # Si x tiene solo un dígito, su superdígito es x
  if x < 10:
      return x
  else:
      # Sumar los dígitos de x de forma recursiva
      suma_digitos = sum(int(digito) for digito in str(x))
      return super_digit(suma_digitos)

# Ejemplos
numeros = [9875, 123, 4567]

for numero in numeros:
  superdigito = super_digit(numero)
  print("Superdígito de", numero, "es:", superdigito)



