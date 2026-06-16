# 10.Suponha que serão digitados 100 números inteiros via teclado, faça
# um algoritmo para:
# a. Somar os números positivos
# b. Contar os números negativos.
# c. A média dos números negativos e a média dos números
# positivos.
# d. A diferença entre o total de números positivos e negativos.

soma_positivos = 0
contador_positivos = 0
soma_negativos = 0
contador_negativos = 0

for i in range(100):
    numero = int(input("Digite um numero inteiro: "))

    if numero > 0:
        soma_positivos = soma_positivos + numero
        contador_positivos = contador_positivos + 1

    elif numero < 0:
        soma_negativos = soma_negativos + numero
        contador_negativos = contador_negativos + 1

if contador_positivos > 0:
    media_positivos = soma_positivos / contador_positivos
else:
    media_positivos = 0

if contador_negativos > 0:
    media_negativos = soma_negativos / contador_negativos
else:
    media_negativos = 0

diferenca = contador_positivos - contador_negativos

print(f"Soma dos positivos: {soma_positivos}")
print(f"Contagem dos negativos: {contador_negativos}")
print(f"Média dos positivos: {media_positivos}")
print(f"Média dos negativos: {media_negativos}")
print(f"Diferença entre o total de positivos e negativos: {diferenca}")