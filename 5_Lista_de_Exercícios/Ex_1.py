# 1. Crie um programa que exiba um menu interativo para o usuário com
# opções de conversão de medidas.
# O programa deve rodar continuamente até que o usuário escolha a
# opção de sair.
# O menu deve ter 3 opções: Converter Celsius para Fahrenheit,
# Converter Metros para Centímetros e Sair.
# Crie uma função específica para cada cálculo de conversão.
# Se o usuário digitar uma opção que não existe, o programa deve
# avisar que a opção é inválida e mostrar o menu novamente.


def C_F(celsius):
    return (celsius * 9/5) + 32

def M_C(metros):
    return metros * 100

while True:
    print("Menu:")
    print("1 - Celsius para Fahrenheit")
    print("2 - Metros para centímetros")
    print("3 - Sair")

    menu = int(input("Escolha um: "))

    match menu:
        case 1:
            celsius = float(input("Digite o grau em Celsius: "))
            print("Fahrenheit:", C_F(celsius))
        case 2:
            metros = float(input("Digite metros: "))
            print("Centímetros:", M_C(metros))
        case 3:
            print("Saindo...")
            break
        case _:        
            print("Opção inválida")
    
