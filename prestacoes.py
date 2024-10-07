#Um produto está sendo negociado em 5 (cinco) prestações sem juros. Faça um algoritmo que receba um valor de uma compra e mostre o valor das prestações.

valor = float(input("Digite o valor da compra:"))
prestacoes = valor / 5

print("Valor da compra: ", valor, "Dividido em 5x de: ", prestacoes)