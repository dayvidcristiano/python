# Faça um algoritmo que receba um valor de uma compra e a quantidade de prestações. De acordo com os valores informados, mostre o valor que vai ficar cada prestação.

Valor = float(input("Digite o valor da compra:"));
Prestacoes = int(input("Você deseja dividir em quantas vezes:"));

CalculaPrestacoes = Valor / Prestacoes

print("Valor da compra: ", Valor, "Dividido em" , Prestacoes, "x de: ", CalculaPrestacoes);