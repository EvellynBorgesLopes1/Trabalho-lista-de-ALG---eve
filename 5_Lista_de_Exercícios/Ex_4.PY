# 4. Faça uma função que recebe um valor inteiro e verifica se o valor é
# par ou ímpar. A função deve retornar um valor inteiro. 

def par_impar(num):  
    if num % 2 == 0:
        return 0
    else:
        return 1
valor = int(input("Digite um numero inteiro: "))
resultado = par_impar(valor)
if resultado == 0:
    print("par")
else:    
    print("impar")