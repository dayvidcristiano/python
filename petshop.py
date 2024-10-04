print("1 - banho")
print("2 - tosa")
print("3 - banho e tosa")
print("4 - outros")

cp = int(input("Informe o código desejado:"))

for i in range (5):
    match (cp):
        case 1: 
            banho = 1
        case 2: 
            tosa = 2
        case 3:
            banhoetosa = 3
        case 4:
            outros = 4

print("Banho", banho)
print("Tosa: ", tosa)
print("Banho e tosa:", banhoetosa)
print("Outros: ", outros)


