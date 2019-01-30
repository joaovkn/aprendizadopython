def imc(altura, peso):
  resultado = peso / (altura**2)
  print("Resultado: ")
  print(resultado)
  if resultado < 25:
    return resultado + " não está acima do peso."
  else:
    return resultado + " está acima do peso."

print(imc(180, 80))

