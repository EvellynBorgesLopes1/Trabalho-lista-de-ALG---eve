# 2. Desenvolva um programa que simule as operações básicas de um
# caixa eletrônico. O cliente começa com um saldo de R$ 0,00. O
# programa deve exibir um menu contínuo com as seguintes regras:
# • O menu deve ter 4 opções: Ver Saldo, Depositar, Sacar e Sair.
# • Crie uma função para o depósito e outra para o saque. Ambas
# devem receber o saldo atual e o valor da operação. Obs:
# devem retornar o saldo atualizado.
# • A função de saque não pode permitir que o usuário saque um
# valor maior do que ele tem na conta (deve exibir uma
# mensagem de erro).
# • Valores de depósito e saque não podem ser negativos

def depositar(saldo, valor):
    if valor < 0:
        print("Erro valor negativo")
        return saldo
    else:
        saldo = saldo + valor
        print("Depósito realizado")
        return saldo


def sacar(saldo, valor):
    if valor < 0:
        print("Erro valor negativo")
        return saldo
    elif valor > saldo:
        print("Erro saldo insuficiente")
        return saldo
    else:
        saldo = saldo - valor
        print("Saque realizado")
        return saldo


saldo = 0

while True:
    print("CAIXA ELETRÔNICO")
    print("1 - Ver saldo")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Sair")

    menu = int(input("Escolha um: "))

    match menu:
        case 1:
            print("Seu saldo é R$", saldo)

        case 2:
            valor = float(input("Digite o valor do depósito: "))
            saldo = depositar(saldo, valor)

        case 3:
            valor = float(input("Digite o valor do saque: "))
            saldo = sacar(saldo, valor)

        case 4:
            print("Saindo...")
            break

        case _:
            print("Opção inválida")