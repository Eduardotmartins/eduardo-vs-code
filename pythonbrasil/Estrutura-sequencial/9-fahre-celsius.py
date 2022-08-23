# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.

# Solicitar a temperatura em Fahrenheit 
x = float(input("Temperatura em Fahrenheigh: "))

#formula usada para conversao da temperatura de fahren para celcius
c = 5 * ((x - 32) / 9)

#imprimir o valor de conversao para celcius
print(f"Temperatura em Celcius:{c:.2f}")
