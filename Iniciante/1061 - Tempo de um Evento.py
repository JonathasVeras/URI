"""
Entradas:
1° Primeiro dia em formato string 'dia tal'
2° Hora em 'hora : minuto : segundo' em string também (Já ta vendo que vai usar split né?)
3° Último dia em formato string 'dia tal'
4° Hora em 'hora : minuto : segundo' em string do último dia

Processo:
Tratar os inputs recebidos
Calcular quanto tempo durou o evento

saída:
tantos dia(s)
tantas hora(s)
tantos minuto(s)
tantos segundo(s)
"""
# Entrada
primeiro_dia = str(input()) #"""'Dia 5'#"""
hora_inicial = str(input()) #"""08 : 12 : 23#"""

ultimo_dia = str(input()) #'Dia 9'#
hora_final = str(input()) #'06 : 13 : 23'#

# Tratamento
primeiro_dia = int(primeiro_dia.split()[1])
ultimo_dia = int(ultimo_dia.split()[1])
hora_inicial = list(map(lambda x: int(x), hora_inicial.split(' : ')))
hora_final = list(map(lambda x: int(x), hora_final.split(' : ')))

# Calculo

# O -1 é para compensar as horas a menos, já que o evento não é 24 nos
# dois dias (inicio-fim)
dias = ultimo_dia - primeiro_dia - 1



# Processando as horas
duracao_dia_1 = [24 - hora_inicial[0], hora_inicial[1], hora_inicial[2]]
if hora_inicial[1] != 0:
    duracao_dia_1[0] = duracao_dia_1[0] - 1
    duracao_dia_1[1] = 60 - hora_inicial[1]
if hora_inicial[2] != 0:
    duracao_dia_1[1] = duracao_dia_1[1] - 1
    duracao_dia_1[2] = 60 - hora_inicial[2]
# A hora final não precisa ser modificada pois ela é a hora que termina
# Não a que começa
duracao_geral = [duracao_dia_1[i]+hora_final[i] if i == 0 else duracao_dia_1[i] + hora_final[i] for i in range(3)]
while duracao_geral[2] >= 60:
    duracao_geral[1] += 1
    duracao_geral[2] -= 60
while duracao_geral[1] >= 60:
    duracao_geral[0] += 1
    duracao_geral[1] -= 60
while duracao_geral[0] >= 24:
    dias += 1
    duracao_geral[0] -= 24

print(f'{dias} dia(s)')
print(f'{duracao_geral[0]} hora(s)')
print(f'{duracao_geral[1]} minuto(s)')
print(f'{duracao_geral[2]} segundo(s)')
"""
24:00 - 12:01
"""