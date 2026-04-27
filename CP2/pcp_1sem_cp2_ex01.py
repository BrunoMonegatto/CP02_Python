estado = int(input("Digite o código do estado (de 1 a 5): "))
peso_ton = float(input("Digite o peso da carga (em toneladas): "))
codigo = int(input("Digite o código da carga (10 a 40): "))

peso_kg = peso_ton * 1000

if codigo >= 10 and codigo <= 20:
    preco_kg = 100

elif codigo >= 21 and codigo <= 30:
    preco_kg = 250

else:
    preco_kg = 340

preco_carga = peso_kg * preco_kg

if estado == 1:
    imposto_percentual = 35

elif estado == 2:
    imposto_percentual = 25

elif estado == 3:
    imposto_percentual = 15

elif estado == 4:
    imposto_percentual = 5

else:
    imposto_percentual = 0

imposto = preco_carga * (imposto_percentual / 100)
total = preco_carga + imposto

print("Peso da carga em kg:", peso_kg)
print("Preço da carga: R$", preco_carga)
print("Valor do imposto: R$", imposto)
print("Valor total: R$", total)

