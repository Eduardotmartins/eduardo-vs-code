# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

# peça para o promp inserir quanto ganha por hora e a quantidade total de horas trabalhadas no mes
salario = int(input("Qual o valor do salário por hora: "))
horas = int(input("Numero de horas trabalhadas por mês: "))

#formula para calcular o valor hora
x =(horas // 30)
mes = (x * salario) * 30

# mostre o resultado ao promp
print(f"Salario do mês é R$:{mes}")
