def ler_nota(nome):
    while True:
        nota = float(input(f"Digite a nota da {nome}: "))

        if 0 <= nota <= 10:
            return nota
        else:
            print("Nota inválida, digite um valor entre 0 e 10.")

# Leitura das notas
cp1 = ler_nota("CP 01")
cp2 = ler_nota("CP 02")
cp3 = ler_nota("CP 03")
sp1 = ler_nota("Sprint 01")
sp2 = ler_nota("Sprint 02")
gs = ler_nota("GS")

cps = [cp1, cp2, cp3]
menor = cp1
for cp in cps:
    if cp < menor:
        menor = cp


print(f"O cálculo será feito sem a menor nota de CP que é: {menor:.1f}")

media_sem = ((cp1 + cp2 + cp3 - menor + sp1 + sp2) / 4 ) * 0.4 + gs * 0.6
print(f"A sua média final do semestre é: {media_sem:.1f}")

media_peso = media_sem * 0.4
print(f"A sua média final do ano é: {media_peso:.1f}")

