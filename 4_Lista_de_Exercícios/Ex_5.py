# 5. Faça uma função que verifique se um valor é perfeito ou não. Um valor é dito perfeito
# quando ele é igual a soma dos seus divisores excetuando ele próprio. (Ex: 6 é perfeito,
# 6 = 1 + 2 + 3, que são seus divisores). A função deve retornar o valor inteiro 1 para
# verdadeiro e 0 caso contrário.

def perfeito(numero):
    soma = 0

    for i in range(1, numero):
        if numero % i == 0:
            soma = soma + i

    if soma == numero:
        return 1
    else:
        return 0


print(perfeito(6))
print(perfeito(11))