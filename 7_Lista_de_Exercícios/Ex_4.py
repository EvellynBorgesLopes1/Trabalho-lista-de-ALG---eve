# 4 - Crie um programa onde o usuário vai digitando os preços dos produtos que está
# colocando no carrinho de supermercado. Armazene todos os preços em uma lista. O
# cadastro termina quando o usuário digitar um valor negativo.
# Cálculos exigidos: Calcule o valor total da compra. Se o cliente comprou mais de 10
# itens no total, ele ganha um desconto fixo de 5% sobre o valor bruto.
# Saída: Exiba a quantidade total de produtos comprados, o valor bruto, o valor do
# desconto calculado e o valor final a ser pago.

precos = []

preco = float(input("Digite o preço do produto: "))

while preco >= 0:
    precos.append(preco)
    preco = float(input("Digite o preço do produto: "))

total = 0

for i in range(len(precos)):
    total = total + precos[i]

quantidade = len(precos)

if quantidade > 10:
    desconto = total * 5 / 100
else:
    desconto = 0

valor_final = total - desconto

print("Quantidade de produtos:", quantidade)
print("Valor bruto:", total)
print("Desconto:", desconto)
print("Valor final:", valor_final)