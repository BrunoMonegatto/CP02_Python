# entrada de dados
nome = input("Digite seu nome: ")

# validação do cargo
while True:
    cargo = int(input(f"1- Gerente\n2- Analista\n3- Assistente\n4- Estagiário\n{nome}, Digite o número referente ao seu cargo: "))
    if 1 <= cargo <= 4:
        break
    else:
        print("Digite um número entre 1 e 4 de acordo com o seu cargo")

salario_base = float(input("Digite o seu salário base: "))
hora_extra = float(input("Digite quantas horas extras foram feitas no mês: "))
total_falta = int(input("Digite o total de faltas que você teve no mês: "))

# validação do bônus
while True:
    bonus = input("Recebeu bônus por desempenho (s/n)? ").lower()
    if bonus == "s" or bonus == "n":
        break
    else:
        print("Insira uma resposta válida")


# funções de cálculo
def calcular_hora_extra(sb, hx):
    # 1.5% do salário por hora extra
    return sb * 0.015 * hx


def calcular_descontos_faltas(sb, f):
    # 2% de desconto por falta
    return sb * 0.02 * f


def calcular_bonus(cargo, recebeu_bonus):
    # se não recebeu, já retorna 0 direto
    if recebeu_bonus == "n":
        return 0
    else:
        # define o valor de acordo com o cargo
        if cargo == 1:
            return 1000
        elif cargo == 2:
            return 500
        elif cargo == 3:
            return 300
        elif cargo == 4:
            return 100


# cálculos principais
valor_hora_extra = calcular_hora_extra(salario_base, hora_extra)
valor_descontos = calcular_descontos_faltas(salario_base, total_falta)
valor_bonus = calcular_bonus(cargo, bonus)

# salário bruto (salário base + extras + bônus)
salario_bruto = salario_base + valor_hora_extra + valor_bonus

# salário final (tirando os descontos)
salario_final = salario_bruto - valor_descontos


# saída
print("\nRESUMO")
print(f"Funcionário: {nome}")
print(f"Salário base: R$ {salario_base:.2f}")
print(f"Acréscimos: R$ {valor_hora_extra + valor_bonus:.2f}")
print(f"Descontos: R$ {valor_descontos:.2f}")
print(f"Salário bruto: R$ {salario_bruto:.2f}")
print(f"Salário final: R$ {salario_final:.2f}")