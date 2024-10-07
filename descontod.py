#Faça um algoritmo que receba um valor de uma compra e a quantidade de prestações. De acordo com os valores informados, mostre o valor que vai ficar cada prestação

valor = float(input("Digite o valor do produto:"))
vlrDesconto = int(input("Quantos porcento de desconto?"))

desconto = (valor - vlrDesconto) / 100 * 100

print("O produto custa R$", valor, ".", "O valor com desconto será de R$", desconto)

