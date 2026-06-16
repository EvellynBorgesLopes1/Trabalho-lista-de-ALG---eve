# 1 - Crie duas listas vazias: nomes e medias. Escreva um programa que peça ao usuário
# para digitar o nome de 5 alunos e a média final de cada um. Guarde os nomes na
# primeira lista e as médias na segunda lista.
# Cálculos exigidos: Após o cadastro, o programa deve percorrer as listas e calcular a
# média geral da turma.
# Saída: Imprima o nome de cada aluno ao lado de sua nota e, ao final, informe quantos
# alunos ficaram acima da média geral da turma

nomes = []
medias = []

soma = 0
acima_media = 0

for i in range(5):
    nome = input("Digite o nome do aluno: ")
    media = float(input("Digite a media final: "))

    nomes.append(nome)
    medias.append(media)

    soma = soma + media

media_geral = soma / 5

print("Alunos e médias:")

for i in range(5):
    print(nomes[i], "-", medias[i])

    if medias[i] > media_geral:
        acima_media = acima_media + 1

print("Media geral ", media_geral)
print("alunos acima da media geral:", acima_media)