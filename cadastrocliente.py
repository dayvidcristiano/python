print ("1 - cadastrar cliente")
print ("2 - Exibir cliente")
print ("3 - Buscar cliente")
print ("4 - Atualizar cliente")
print ("5 - Excluir cliente")
print ("6 - sair")

opcao = int(input("Escolha uma opção:"))

match(opcao):
    case 1: 
        print("Cadastrando um cliente")
    case 2: 
        print("Exibindo os dados de um cliente")
    case 3:
        print("Exibindo os dados de todos os clientes")
    case 4:
        print("Atualizando cliente")
    case 5:
        print("Excluindo cliente")
    case 6:
        print("Saindo do sistema")
    case __:
        print("Opção inválida")