#Escrever um programa em Python que leia o número de carros por ele vendidos, o valor total de suas vendas, o salário fixo e a comissão que ele recebe por carro vendido. Calcule e escreva o salário final do vendedor.

numCarros = int(input("Digite o número de carros vendidos:"))
valorVendas = float(input("Valor total de vendas:"))
salarioFixo = float(input("Salário fixo:"))
comissaoFixa = float(input("Comissão por venda:"))

cal = (salarioFixo + comissaoFixa * numCarros + (5 * valorVendas / 100))

print("Salário final: ", cal)
