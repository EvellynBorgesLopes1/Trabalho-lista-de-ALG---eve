# 4. Faça um procedimento que recebe por parâmetro os valores necessários para o
# cálculo da fórmula de báskara e imprima as suas raízes, caso seja possível calcular.

def bhaskara(a, b, c):
    delta = b**2-4*a*c

    if delta < 0:
        print("Nao tem raiz")
    elif delta == 0:
        raiz = -b / (2*a)
        print(f"raiz: {raiz}")
    else:
        raiz1 = (-b + delta**0.5) / (2*a)
        raiz2 = (-b - delta**0.5) / (2*a)
        print(f" as raizes sao: {raiz1} e {raiz2}")  
