
# joao papo de pescador:

# pergunte ao joao quantos kilos ele trouxe para pesar:
try: 
    peso = float(input("Insira o peso: "))
except ValueError:
    # se caso nao for numero gera uma msg de erro
    print("Deve ser digitado numericamente")
    exit()
    
# calculo do exesso de peso
multa = peso - 50

# calculo de exesso de peso * o valor da multa por kilo
calculo_multa = multa * 4

# se caso a multa ultrapasse o valor permitido de 50 kilos
if peso > 50:
    print(f"Peso excedido: {multa}KG e multa de:R${calculo_multa}")
    
    # caso contrario, o peso estiver dentro do permitido
else: 
    print("Valor dentro do permitido")

    