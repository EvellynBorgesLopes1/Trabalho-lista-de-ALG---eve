# 6. Faça uma função que recebe por parâmetro o tempo de duração de
# uma fábrica expressa em segundos e imprima esse tempo em horas,
# minutos e segundos.

def tempo_fabrica(segundos):
    horas = segundos // 3600
    minutos = (segundos % 3600) // 60
    segundos_restantes = segundos % 60
    print(f"{horas} horas {minutos} minutos e {segundos_restantes} segundos")
tempo = int(input("tempo de duração da fabrica em segundos: "))
tempo_fabrica(tempo)