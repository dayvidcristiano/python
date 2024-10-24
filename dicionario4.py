veiculo = {}

while True:
    marca = input("Qual a marca do carro: ")
    ano = int(input("Qual o ano do carro? "))
    
    op = input("Você deseja adcionar mais carros? (S/N)")
    veiculo[marca]=ano
    print(veiculo)

    if op == 'N' or op == "n":
        print("Encerrado")
        break
    
    print(veiculo)