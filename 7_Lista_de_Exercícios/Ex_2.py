# 2 - Um pequeno comércio quer analisar as movimentações do dia. Crie um programa
# que receba várias entradas financeiras e armazene-as em uma única lista chamada
# movimentações.
# Valores positivos representam vendas (receitas) e valores negativos representam
# pagamentos (despesas). Pare de registrar quando o usuário digitar 0.
# Cálculos exigidos: Percorra a lista para calcular o total arrecadado (soma dos
# positivos), o total gasto (soma dos negativos) e o saldo final do dia (receitas +
# despesas).
# Saída: Imprima um relatório financeiro simples mostrando esses três valores. Mostre
# também uma mensagem de "Lucro" se o saldo for positivo, ou "Prejuízo" se for
# negativo.

movimentacoes = []

valor = float(input("Digite o valor: "))

while valor != 0:
    movimentacoes.append(valor)
    valor = float(input("Digite o valor: "))

total_arrecadado = 0
total_gasto = 0

for i in range(len(movimentacoes)):
    if movimentacoes[i] > 0:
        total_arrecadado = total_arrecadado + movimentacoes[i]
    elif movimentacoes[i] < 0:
        total_gasto = total_gasto + movimentacoes[i]

saldo = total_arrecadado + total_gasto

print("Total arrecadado:", total_arrecadado)
print("Total gasto:", total_gasto)
print("Saldo final:", saldo)

if saldo > 0:
    print("Lucro")
elif saldo < 0:
    print("Prejuizo")
else:
    print("Saldo zerado")