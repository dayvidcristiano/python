estoque = {}

while True:
    nomeproduto = input("Informe o nome do produto:")
    quant = input("Informe a qauntidade:")
    
    estoque[nomeproduto]=quant
    
    op = input("Você deseja continuar cadastrando? (S/N)")
    if op == "n" or op == "N":
        print("Encerrado:")
        break
    
print(estoque)

