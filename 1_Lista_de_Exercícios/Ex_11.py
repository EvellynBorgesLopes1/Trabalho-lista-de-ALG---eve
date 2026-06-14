# 11. Elabore um algoritmo para fazer a conversão de graus fahrenheit (º F) para graus celsius (º C). 
# A fórmula para conversão é: c= 5/9 * (f-32)

fahrenheit = float(input("digite graus em fahrenheit: "))
celsius = (5/9) * (fahrenheit - 32)

print ("sua corversão de fahrenheit (º F) para celsius (º C) é: ",celsius)
