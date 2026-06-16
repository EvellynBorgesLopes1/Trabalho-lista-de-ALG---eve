# 3. Faça uma função que recebe um valor inteiro e verifica se o valor é
# positivo ou negativo. A função deve retornar um valor inteiro. 

def verificar(valor):
    if valor < 0:
        return -1
    else: 
        return 1

valor = int(input("Digite um numero inteiro: "))
resultado = verificar(valor)
if resultado == -1:
    print("negativo")
elif resultado == 1:
    print("positivo")
