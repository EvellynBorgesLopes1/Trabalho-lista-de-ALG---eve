# 2. Faça um programa que carregue uma lista com oito números inteiros e mostre:
# a. Os números múltiplos de dois;
# b. Os números múltiplos de três;

multiplos_2 = ""
multiplos_3 = ""

for i in range(8):
    numero = int(input("Digite um numero inteiro: "))

    if numero % 2 == 0:
        multiplos_2 = multiplos_2 + str(numero) + " "

    if numero % 3 == 0:
        multiplos_3 = multiplos_3 + str(numero) + " "


print("multiplos de 2:", multiplos_2)
print("multiplos de 3:", multiplos_3)