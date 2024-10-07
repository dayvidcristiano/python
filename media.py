#Faça um algoritmo que leia quatro números informados pelo usuário e que depois exiba a média dos 4 números.

numero1 = int(input("Digite o primeiro número:"))
numero2 = int(input("Digite o segundo número:"))
numero3 = int(input("Digite o terceiro número:"))
numero4 = int(input("Digite o quarto número:"))

media = numero1 + numero2 + numero3 + numero4/4

print("A média de: ", numero1, "+", numero2, "+", numero3, "+", numero4, "é:" "+", media)