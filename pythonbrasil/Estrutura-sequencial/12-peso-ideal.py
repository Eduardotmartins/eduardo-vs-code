# Tendo como dados de entrada a altura de uma pessoa:

try: # float para captar numero decimal
    tamanho = float(input("Seu tamanho: "))
except ValueError:
    print("Deve ser escrito com ponto")
    exit()

# formula do peso ideal de acordo com sua altura
peso = (72.7*tamanho) - 58

# imprima o peso ideal
print(f"Seu peso ideal é:{peso}")