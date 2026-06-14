# 8. Dados n e uma sequência de n números inteiros positivos, determinar a soma dos
# números pares, dos ímpares e as respectivas quantidades de cada um dos
# subconjuntos.

n = int(input("Digite a quantidade de numeros: "))
soma_pares = 0
soma_impares = 0
quantidade_pares = 0
quantidade_impares = 0
for i in range(n):
    numero = int(input("Digite um numero inteiro positivo: "))
    if numero % 2 == 0:
        soma_pares += numero
        quantidade_pares += 1
    else:
        soma_impares += numero
        quantidade_impares += 1 
print("Soma dos pares:", soma_pares)
print("Quantidade de pares:", quantidade_pares)
print("Soma dos impares:", soma_impares)
print("Quantidade de impares:", quantidade_impares)
