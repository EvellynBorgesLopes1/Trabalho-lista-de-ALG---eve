# 7. Faça um algoritmo para ler um número até que o usuário opte por
# terminar a entrada dos dados e, mostre na tela as seguintes
# informações: a média dos números, o maior e o menor número.

soma = 0
quantidade = 0
maior = 0
menor = 0

while True:
    numero = float(input("Digite um numero: "))

    soma = soma + numero

    if quantidade == 0:
        maior = numero
        menor = numero
    else:
        if numero > maior:
            maior = numero

        if numero < menor:
            menor = numero

    quantidade = quantidade + 1

    continuar = input("Deseja continuar? S/N: ")

    if continuar == "N":
        break

media = soma / quantidade

print("Média:", media)
print("Maior número:", maior)
print("Menor número:", menor)