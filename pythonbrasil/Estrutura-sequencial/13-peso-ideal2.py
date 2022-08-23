# Solicitar ao promp a altura:
tamanho = float(input("Seu tamanho: "))

# Solicitar ao promp o sexo:
try:
    sexo = int(input("Digite seu sexo: (1) Para Homem (2) Para mulher: "))
# caso o promp digite Masc ou Fem, enviar msg de erro pedindo o correto
except ValueError:
    print("Deve ser digitado ou 1 ou 2")
    exit()

# de acordo com o resultado 1 ou 2 imprimir a formula com o peso ideal
if sexo == 1:
    peso_h = (72.7 * tamanho) - 58
    print(f"Seu peso ideal é:{peso_h}")
    exit()

elif sexo == 2:
    peso_m = (62.1 * tamanho) - 44.7
    print(f"Seu peso ideal é:{peso_m}")
    exit()