# 14. Faça um algoritmo que receba três notas, calcule e mostre a média e o conceito
# que segue a tabela abaixo:
# Média Ponderada Conceito
# 8,0 |⎯| 10,0 A
# 7,0 |⎯ 8,0 B
# 6,0 |⎯ 7,0 C
# 5,0 |⎯ 6,0 D
# 0,0 |⎯ 5,0 E


Nota1 = int(input("Digite a primeira nota: "))
Nota2 = int(input("Digite a segunda nota: "))
Nota3 = int(input("Digite a terceira nota: "))
Media = (Nota1 + Nota2 + Nota3) / 3

if Media >= 8 and Media <= 10:
    Conceito = "A"
elif Media >= 7 and Media < 8:
    Conceito = "B"
elif Media >= 6 and Media < 7:
    Conceito = "C"
elif Media >= 5 and Media < 6:
    Conceito = "D"
else:
    Conceito = "E"

print("A média é: ", Media)
print("O conceito é: ", Conceito)