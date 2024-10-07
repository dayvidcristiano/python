#Escreva um programa que declare uma variável real para representar uma quantia em dólares. Solicite ao usuário que insira essa quantia e, em seguida, converta-a para reais, utilizando um fator de conversão fixo. Exiba o resultado.

dolar = float(input("Digite um valor em dolar: "))
conversao = (dolar * 5.43);

print("Valor enviado: ", dolar, "\n", "Valor convertido para real: ", conversao)