#Faça um algoritmo que receba um valor de uma compra e a quantidade de prestações. De acordo com os valores informados, mostre o valor que vai ficar cada prestação

Valor = float(input("Digite o valor do produto:"));
VlrDesconto = int(input("Quantos porcento de desconto?"));

Desconto = (Valor - VlrDesconto) / 100 * 100

print("O produto custa R$", Valor, ".", "O valor com desconto será de R$", Desconto);

