#Elabore um algoritmo que leia do teclado uma quantidade de segundos e transforme este tempo em dias, horas e minutos. Exiba na tela os valores calculados.

segundos = int(input("Digite uma quantidade em segundos: "))

min = int(segundos / 60)
horas = int(min / 60)
dias = int(horas / 24)

print(segundos, "seg equivale a:")
print(min, "min")
print(horas, "horas")
print(dias, "dia(s)")
      