# Faça um algoritmo que receba um valor de uma compra e a quantidade de prestações. De acordo com os valores informados, mostre o valor que vai ficar cada prestação.

valor = float(input("Digite o valor da compra:"))
prestacoes = int(input("Você deseja dividir em quantas vezes:"))

calculaPrestacoes = valor / prestacoes

print("Valor da compra: ", valor, "Dividido em" , prestacoes, "x de: ", calculaPrestacoes)