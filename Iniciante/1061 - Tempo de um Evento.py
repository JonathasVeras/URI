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
primeiro_dia = input()
hora_inicial = input()

ultimo_dia = input()
hora_final = input()

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
# A hora final não precisa ser modificada pois ela é a hora que termina
# Não a que começa
duracao_geral = [duracao_dia_1[i]+hora_final[i] if i == 0 else hora_final[i]-duracao_dia_1[i] for i in range(3)]
while duracao_geral[0] >= 24:
    dias += 1
    duracao_geral[0] -= 24
print(f'{dias} dia(s)')
print(f'{duracao_geral[0]} hora(s)')
print(f'{duracao_geral[1]} minuto(s)')
print(f'{duracao_geral[2]} segundo(s)')
