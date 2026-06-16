# 4. Dado uma lista A de tamanho 8 e do tipo inteiro faça um programa em Python que,
# utilizando um laço de repetição, receba os valores de entrada e, utilizando outro laço
# de repetição, verifique qual o maior valor da lista e apresente esse valor.

A = []

for i in range(8):
    valor = int(input("Digite um valor: "))
    A.append(valor)

maior = A[0]

for i in range(8):
    if A[i] > maior:
        maior = A[i]

print("Maior valor da lista:", maior)