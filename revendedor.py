NumCarros = float(input("Digite o número de carros vendidos:"))
ValorVendas = float(input("Valor total de vendas:"))
SalarioFixo = float(input("Salário fixo:"))
ComissaoFixa = float(input("Comissão por venda:"))

Cal = (SalarioFixo + ComissaoFixa * NumCarros + (5*ValorVendas/100))

print("Salário final: ", Cal)
