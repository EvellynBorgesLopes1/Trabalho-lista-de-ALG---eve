# 8. Faça um algoritmo que leia o nome, salário e número de filhos de
# 100 pessoas, e calcule:
# a. O salário médio das pessoas que possuam 2 filhos
# b. O salário médio das que não possuem filhos
# c. Qual a média salarial maior, entre os que têm um e dois filhos
# d. O salário médio geral

salarios_2_filhos = 0
qtd_2_filhos = 0

salarios_sem_filhos = 0
qtd_sem_filhos = 0

salarios_1_filho = 0
qtd_1_filho = 0

salarios_total = 0

for i in range(100):
    nome = input("digite o nome: ")
    salario = float(input("digite o salario: "))
    filhos = int(input("digite o numero de filhos: "))

    slarios_total = salarios_total + salario

    if filhos == 2:
        salarios_2_filhos = salarios_2_filhos + salario
        qtd_2_filhos = qtd_2_filhos + 1
    elif filhos == 0:
        salarios_sem_filhos = salarios_sem_filhos + salario
        qtd_sem_filhos = qtd_sem_filhos + 1
    elif filhos == 1:
        salarios_1_filho = salarios_1_filho + salario
        qtd_1_filho = qtd_1_filho + 1

media_2_filhos = salarios_2_filhos / qtd_2_filhos
media_sem_filhos = salarios_sem_filhos / qtd_sem_filhos
media_1_filho = salarios_1_filho / qtd_1_filho
media_geral = salarios_total / 100
print(f"salario medio quu possuem 2 filhos: {media_2_filhos}")
print(f"salario medio que não possuem filhos: {media_sem_filhos}")
print(f"salario medio que possuem 1 filho: {media_1_filho}")
if media_1_filho > media_2_filhos:
    print("media salarial maior quem tem um filho")
elif media_2_filhos > media_1_filho:
    print("media salarial maior quem tem dois filhos")
else:    print("media salarial entre os que tem um e dois filhos é igual")
print(f"salario medio geral: {media_geral}")
