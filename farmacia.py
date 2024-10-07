valor = float(input("Digite o valor total da compra:"))

if valor >= 100:
 desconto =  valor - (valor * 10 / 100)
print("Você recebeu um desconto de 10% na sua compra. Valor total: ", desconto)