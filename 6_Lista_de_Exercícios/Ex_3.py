# 3. Uma escola deseja saber se existem alunos cursando, simultaneamente, as disciplinas
# Lógica e Linguagem de Programação. Coloque os números das matrículas dos alunos
# que cursam Lógica em uma lista, no máximo 10 alunos. Coloque os números das
# matrículas dos alunos que cursam Linguagem de Programação em outra lista, no
# máximo 8 alunos. Mostre o número de matrícula que aparece nas duas listas.

logica = []
linguagem = []

qtd_logica = int(input("Quantos alunos fazem logica: "))

while qtd_logica > 10:
    print("So pode ate 10 alunos")
    qtd_logica = int(input("Quantos alunos fazem logica: "))

for i in range(qtd_logica):
    mat = int(input("Digite a matricula: "))
    logica.append(mat)


qtd_linguagem = int(input("Quantos alunos fazem linguagem: "))

while qtd_linguagem > 8:
    print("So pode ate 8 alunos")
    qtd_linguagem = int(input("Quantos alunos fazem linguagem: "))

for i in range(qtd_linguagem):
    mat = int(input("Digite a matricula: "))
    linguagem.append(mat)


print("Matriculas que aparecem nas duas listas:")

achou = 0

for i in range(qtd_logica):
    for j in range(qtd_linguagem):
        if logica[i] == linguagem[j]:
            print(logica[i])
            achou = 1

if achou == 0:
    print("Nenhum aluno faz as duas materias")