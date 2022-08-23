# Faça um Programa que peça as 4 notas bimestrais e mostre a média.

# pedir as notas bimestrais

b1 = int(input("1º Bimestre: "))
b2 = int(input("2º Bimestre: "))
b3 = int(input("3º Bimestre: "))
b4 = int(input("4º Bimestre: "))

# formula da media dos bimestres
media = b1 + b2 + b3 + b4 / 4

#imprima o valor da media dos bimestres
print(f"Media bimestral: {media}")