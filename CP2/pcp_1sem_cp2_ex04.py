nome = input("Digite seu nome: ")

while True:
    cargo = int(input(f"1- Gerente\n2- Analista\n3- Assistente\n4- Estagiário\n{nome}, Digite o número referente ao seu cargo: "))
    if cargo >= 1 and cargo <= 4:
        break
    else:
        print("Digite um número entre 1 e 4 de acordo com o seu cargo")

salario_base = float(input("Digite o seu salário base: "))

hora_extra = float(input("Digite quantas horas extras foram feitas no mês: "))

total_falta = int(input("Digite o total de faltas que você teve no mês: "))

while True:
    bonus = input("Recebeu bônus por desempenho (s/n)? ").lower()
    if bonus == "s" or bonus == "n":
        break
    else:
        print("Insira uma resposta válida")



def calcular_hora_extra(sb, hx):
    return sb * 0.015 * hx

def calcular_descontos_faltas(sb, f):
    return sb * 0.02 * f

def calcular_bonus(cargo, recebeu_bonus):
    if recebeu_bonus == "n":
        print("Não recebeu bônus")
        return 0
    else:
        if cargo == 1:
            b = 1000
        elif cargo == 2:
            b = 500
        elif cargo == 3:
            b = 300
        elif cargo == 4:
            b = 100
        return b