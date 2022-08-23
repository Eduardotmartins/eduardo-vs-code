# pedir numero inteiro ao promp
try:# se caso nao for numero gera uma msg de erro
    num_inteiro_1 = int(input("Numero inteiro(1): "))
    num_inteiro_2 = int(input("Numero inteiro(2): "))
except ValueError:
    print("deve ser digitado um numero inteiro")
    exit()
# pedir numero real ao promp
try:# se caso nao for numero real gera uma msg de erro
    num_real = float(input("Numero real: "))
except ValueError:
    print("Deve ser digitado um numero real")
    exit()

# elaboração dos calculos a serem efetuados para situação a,b,c
calc_a1 = (num_inteiro_1 * 2)
calc_a2 = (num_inteiro_1 * 3)
calc_b2 = (num_inteiro_2 / 2)
calc_c3 = (num_real ** 3)

# montar as situações pedidas no problema a,b,c:
a = (calc_a1) * (calc_b2)
b = (calc_a2) + (num_real)
c = (calc_c3) 

# mostre ao promp o resultado de a , b , c:
print(f"valores a:{a}")
print(f"Valores b:{b}")
print(f"Valores c:{c}")