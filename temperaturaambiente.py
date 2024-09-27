temperatura = int(input("Qual a temperatura ambiente atual?"))

if temperatura >= 25 and temperatura <= 30:
    print("Clima agradável")
elif temperatura >= 31 and temperatura <= 35:
    print("O clima está quente")
elif temperatura >= 36:
    print("O clima está SUPER quente!")
else:
    print("O clima está frio")