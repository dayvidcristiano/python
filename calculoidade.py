#Faça um algoritmo que receba o ano de nascimento de uma pessoa e o ano atual, calcule e mostre: A idade dessa pessoa e, quantos anos ela terá em 2028.

AnoNascimento = int(input("Digite o ano em que você nasceu:"));
AnoAtual = int(input("Digite o ano em que você está:"));

Idade = AnoAtual - AnoNascimento
Futuro = 2028 - AnoNascimento

print("Você tem: ", Idade, "anos");
print("Em 2028 você terá: ", Futuro);
