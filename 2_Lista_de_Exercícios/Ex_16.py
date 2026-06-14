# 16. Fazer um algoritmo para ajudar a bilheteria do metrô. O operador deve informar
# o tipo do bilhete (unitário, duplo ou 10 viagens) e o valor pago pelo passageiro.
# O sistema deve mostrar, então, a quantidade de bilhetes possíveis e o troco que o
# passageiro deve receber.
# Considere a seguinte tabela de preço:
# Bilhete unitário ..................................... 1,30
# Bilhete duplo ........................................ 2,60
# Bilhete de 10 viagens ......................... 12,00

bilhete = float(input("escolha o bilhete (1 - unitário, 2 - duplo, 3 - 10 viagens): "))
valor = float(input("Informe o valor pago: "))

if bilhete == 1:
    preco = 1.30
elif bilhete == 2:
    preco = 2.60
elif bilhete == 3:
    preco = 12.00

quantidade = valor // preco
troco = valor - (quantidade * preco)
print("Quantidade de bilhetes possíveis:", quantidade)
print("troco: ", troco)