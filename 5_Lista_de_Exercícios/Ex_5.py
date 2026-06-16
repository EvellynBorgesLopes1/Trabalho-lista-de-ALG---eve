# 5. Faça uma função que receba 3 valores inteiros por parâmetro e
# imprima-os ordenados em ordem crescente. 

def ordena(a, b, c):
    if a < b and a < c:
        if b < c:
            print(a, b, c)
        else:
            print(a, c, b)
    elif b < a and b < c:
        if a < c:
            print(b, a, c)
        else:
            print(b, c, a)
    else:
        if a < b:
            print(c, a, b)
        else:
            print(c, b, a)
num1 = int(input("Digite o primeiro numero inteiro: "))
num2 = int(input("Digite o segundo numero inteiro: "))
num3 = int(input("Digite o terceiro numero inteiro: "))
ordena(num1, num2, num3)
