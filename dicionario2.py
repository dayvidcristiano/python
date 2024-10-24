agenda = {}

while True:
    nome = input("Informe seu nome:")
    tel = input("Informe seu número:")
    end = input("Informe seu endereço:")
    
    agenda[nome]=tel, end
    
    op = input("Você deseja continuar cadastrando? (S/N)")
    if op == "n" or op == "N":
        print("Encerrado:")
        break
    
print(agenda)

