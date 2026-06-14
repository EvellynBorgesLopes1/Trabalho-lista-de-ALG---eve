# 10. Encontre todos os números primos entre 2 e 20.000.

for numero in range(2, 20001):
    primo = True

    for divisor in range(2, numero):
        if numero % divisor == 0:
            primo = False
            break

    if primo:
        print(numero)
