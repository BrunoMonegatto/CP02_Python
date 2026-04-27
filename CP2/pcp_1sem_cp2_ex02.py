a = float(input("Digite o valor do lado A: "))
b = float(input("Digite o valor do lado B: "))
c = float(input("Digite o valor do lado C: "))

lados = sorted([a, b, c], reverse = True)
A, B, C = lados

if A >= B + C:
    print("Não forma triângulo")

else:
    if A**2 == B**2 + C**2:
        print("Triângulo Retângulo")

    elif A**2 > B**2 + C**2:
        print("Triângulo Obtusangulo")

    elif A**2 < B**2 + C**2:
        print("Triângulo Acutangulo")

    if A == B == C:
        print("Triangulo Equilatero")

    elif A == B or A == C or B == C:
        print("Triangulo Isosceles")

