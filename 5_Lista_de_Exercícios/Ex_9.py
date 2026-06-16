# 9. Agora repita o exercício anterior para um número indefinido de
# pessoas.

salarios_2_filhos = 0
qtd_2_filhos = 0

salarios_sem_filhos = 0
qtd_sem_filhos = 0

salarios_1_filho = 0
qtd_1_filho = 0

salarios_total = 0
qtd_total = 0

while True:
    nome = input("digite o nome: ")
    salario = float(input("digite o salario: "))
    filhos = int(input("digite o numero de filhos: "))

    salarios_total = salarios_total + salario
    qtd_total = qtd_total + 1

    if filhos == 2:
        salarios_2_filhos = salarios_2_filhos + salario
        qtd_2_filhos = qtd_2_filhos + 1
    elif filhos == 0:
        salarios_sem_filhos = salarios_sem_filhos + salario
        qtd_sem_filhos = qtd_sem_filhos + 1
    elif filhos == 1:
        salarios_1_filho = salarios_1_filho + salario
        qtd_1_filho = qtd_1_filho + 1

    resposta = input("deseja continuar? (s/n) ")
    if resposta == "n":
        break

media_2_filhos = salarios_2_filhos / qtd_2_filhos
media_sem_filhos = salarios_sem_filhos / qtd_sem_filhos
media_1_filho = salarios_1_filho / qtd_1_filho
media_geral = salarios_total / qtd_total
print(f"salario medio quu possuem 2 filhos: {media_2_filhos}")
print(f"salario medio que não possuem filhos: {media_sem_filhos}")
print(f"salario medio que possuem 1 filho: {media_1_filho}")
if media_1_filho > media_2_filhos:
    print("media salarial maior quem tem um filho")
elif media_2_filhos > media_1_filho:
    print("media salarial maior quem tem dois filhos")
else:    print("media salarial entre os que tem um e dois filhos é igual")
print(f"salario medio geral: {media_geral}")
