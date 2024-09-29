<<<<<<< HEAD
NumCarros = float(input("Digite o número de carros vendidos:"))
ValorVendas = float(input("Valor total de vendas:"))
SalarioFixo = float(input("Salário fixo:"))
ComissaoFixa = float(input("Comissão por venda:"))
=======
#Uma revendedora de carros oferece aos seus vendedores um salário mensal fixo além de uma comissão fixa pelos carros vendido e 5% do valor total das vendas efetuadas por eles.
>>>>>>> eb35fb8 (pull)

#Escrever um programa em Python que leia o número de carros por ele vendidos, o valor total de suas vendas, o salário fixo e a comissão que ele recebe por carro vendido. Calcule e escreva o salário final do vendedor.

NumCarros = int(input("Digite o número de carros vendidos:"));
ValorVendas = float(input("Valor total de vendas:"));
SalarioFixo = float(input("Salário fixo:"));
ComissaoFixa = float(input("Comissão por venda:"));

Cal = (SalarioFixo + ComissaoFixa * NumCarros + (5 * ValorVendas / 100));

print("Salário final: ", Cal);
