# 5. Faça um algoritmo que leia 5 números e imprima quantos números maiores que
# 100 foram digitados.

contador_maior_que_100 = 0
for i in range(5):
    numero = float(input("Digite um número: "))
    if numero > 100:
        contador_maior_que_100 += 1

print(f"Números digitados maiores que 100: {contador_maior_que_100}")