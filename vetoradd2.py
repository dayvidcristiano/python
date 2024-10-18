lista = []
op = 1
while op != 0:
    op = int(input("Informe VALORES (0 -- PARAR): "))
    if op == 0:
        break
    else:
        lista.append(op)
print(lista)