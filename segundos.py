#Elabore um algoritmo que leia do teclado uma quantidade de segundos e transforme este tempo em dias, horas e minutos. Exiba na tela os valores calculados.

Segundos = int(input("Digite uma quantidade em segundos: "));

Min = int(Segundos / 60);
Horas = int(Min / 60);
Dias = int(Horas / 24);

print(Segundos, "seg equivale a:");
print(Min, "min");
print(Horas, "horas");
print(Dias, "dia(s)");
      