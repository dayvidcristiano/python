#Faça um algoritmo que receba o ano de nascimento de uma pessoa e o ano atual, calcule e mostre: A idade dessa pessoa e, quantos anos ela terá em 2028.

anoNascimento = int(input("Digite o ano em que você nasceu:"))
anoAtual = int(input("Digite o ano em que você está:"))

idade = anoAtual - anoNascimento
futuro = 2028 - anoNascimento

print("Você tem: ", idade, "anos")
print("Em 2028 você terá: ", futuro)
