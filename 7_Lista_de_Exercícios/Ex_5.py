# 5 - Uma empresa fez uma pesquisa de satisfação onde as notas possíveis eram apenas 1
# (Ruim), 2 (Bom) e 3 (Excelente). Crie uma lista longa simulando as respostas de 20
# clientes (ex: votos = [1, 2, 3, 2, 2, 1, 3, ...]).
# Cálculos exigidos: Crie uma lógica para contar quantas vezes cada nota aparece na
# lista. Em seguida, calcule o percentual que cada categoria representa em relação ao total
# de 20 votos.
# Saída: Imprima um relatório gerencial informando a quantidade absoluta de votos e a
# porcentagem para "Ruim", "Bom" e "Excelente". Indique também qual foi a avaliação
# vencedora (a que teve mais votos).

votos = [1, 2, 3, 2, 2, 1, 3, 3, 2, 1, 2, 3, 3, 2, 1, 2, 3, 2, 2, 3]

ruim = 0
bom = 0
excelente = 0

for i in range(len(votos)):
    if votos[i] == 1:
        ruim = ruim + 1
    elif votos[i] == 2:
        bom = bom + 1
    elif votos[i] == 3:
        excelente = excelente + 1

porcentagem_ruim = ruim * 100 / 20
porcentagem_bom = bom * 100 / 20
porcentagem_excelente = excelente * 100 / 20

print("Relatorio da pesquisa")
print("Ruim:", ruim, "votos -", porcentagem_ruim, "%")
print("Bom:", bom, "votos -", porcentagem_bom, "%")
print("Excelente:", excelente, "votos -", porcentagem_excelente, "%")

if ruim > bom and ruim > excelente:
    print("A avaliacao vencedora foi: Ruim")
elif bom > ruim and bom > excelente:
    print("A avaliacao vencedora foi: Bom")
elif excelente > ruim and excelente > bom:
    print("A avaliacao vencedora foi: Excelente")
else:
    print("Houve empate")