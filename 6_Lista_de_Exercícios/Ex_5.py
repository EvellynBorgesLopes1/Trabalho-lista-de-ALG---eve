# 5. Dado as listas A e B de tamanho 6 e do tipo float faça um programa em C que,
# utilizando um laço de repetição, e, utilizando outro laço, inicialize os valores de ambas
# as listas, some os valores posição por posição e guarde o novo valor na lista A.

A = []
B = []

for i in range(6):
    valor = float(input("Digite um valor para a lista A: "))
    A.append(valor)

for i in range(6):
    valor = float(input("Digite um valor para a lista B: "))
    B.append(valor)

for i in range(6):
    A[i] = A[i] + B[i]

print("Lista A depois da soma:")

for i in range(6):
    print(A[i])