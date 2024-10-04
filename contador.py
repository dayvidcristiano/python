numero = int(input("Digite um número positivo (0 -- sair)"))
acumulador = 0; 

while (numero != 0):
    if numero < 0:
        print("Número negativo não será permitido!")
    else:
        acumulador = acumulador + numero 
    numero = int(input("Digite um número positivo (0 -- sair)"))
print("A soma dos números informados pelo usuário:", acumulador)



