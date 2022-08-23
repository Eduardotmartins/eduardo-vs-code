# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

#faça o promp pedir o raio de um circulo
x = float(input("Insira o medida do raio do circulo: "))

# formula da area do circulo
area = 3.14 * (x * x)

#imprima os valores para o promp
print("A area do circulo é: {:.2f}".format (area))
