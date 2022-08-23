# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

# perguntar ao promp a temperatura em Celcius para fazer a conversao para fahrenheig
try:
    x = float(input("Insira a temperatura em Celcius: "))
except ValueError:
    # Caso o promp não digite valor numerico é enviado uma mensagem de erro
    print("Deve ser inserido valor numérico")
    exit()
    
#formula de conversao de fahrenheig to celcius
f = (x * 1.8 ) + 32

# imprimir a temperatura em fahrenheig
print(f"Temperatura em Fahrenheig:{f}")