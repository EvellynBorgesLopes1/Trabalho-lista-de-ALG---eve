# 15. Faça um algoritmo que receba três notas de um aluno, calcule e mostre a média
# aritmética e a mensagem que segue a tabela abaixo. Para alunos de exame,
# calcule e mostre a nota mínima a ser tirada no exame para que o aluno obtenha
# aprovação, considerando que a média no exame é 6,0.
# Média Ponderada Conceito
# 0,0 |⎯ 3,0 Reprovado
# 3,0 |⎯ 7,0 Exame
# 7,0 |⎯| 10,0 Aprovado

nota1 = int(input("Digite a primeira nota: "))
nota2 = int(input("Digite a segunda nota: "))
nota3 = int(input("Digite a terceira nota: "))
media = (nota1 + nota2 + nota3) / 3

if media < 3:
    print("Reprovado")
elif media < 7:
    print("Exame")
    nota_exame = 6 - media
    print("Nota mínima para aprovação no exame: ", nota_exame)
elif media <= 10:
    print("Aprovado")