# 1. Faça um programa que carregue uma lista de seis elementos numéricos inteiros e
# mostre:
# a. A quantidade de números pares;
# b. Quais são os números pares;
# c. A quantidade de números ímpares;
# d. Quais são os números ímpares.

qtd_pares = 0
qtd_impares = 0
pares = ""
impares = ""

for i in range(6):
    numero = int(input("Digite um número inteiro: "))
    if numero % 2 == 0:
        qtd_pares = qtd_pares + 1
        pares = pares + str(numero) + " "
    else:
        qtd_impares = qtd_impares + 1
        impares = impares + str(numero) + " "

print("Quantidade de pares:", qtd_pares)
print("Numeros pares:", pares)
print("Quantidade de ímpares:", qtd_impares)
print("Numeros ímpares:", impares)