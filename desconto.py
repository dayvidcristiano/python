#Faça um algoritmo que receba um valor de um produto e que escreva o novo valor tendo em vista que o desconto foi de 8%

valor = float(input("Digite o valor:"))

desconto = (valor - 10) / 100 * 100
print("Você ganhou um desconto de 8%! Então sua compra ficou: ", desconto)