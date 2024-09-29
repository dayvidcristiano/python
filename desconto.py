#Faça um algoritmo que receba um valor de um produto e que escreva o novo valor tendo em vista que o desconto foi de 8%

Valor = float(input("Digite o valor:"));

Desconto = (Valor - 8) / 100 * 100
print("Você ganhou um desconto de 8%! Então sua compra ficou: ", Desconto); 