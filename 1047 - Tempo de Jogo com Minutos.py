hora_inicial, minuto_inicial, hora_final, minuto_final = map(int, input().split())
hora_jogada = 0
minuto_jogado = 0
horas_iguais = False
if hora_inicial == hora_final and minuto_inicial == minuto_final:
    hora_jogada = 24
    minuto_jogado = 0
elif hora_inicial == hora_final and minuto_inicial < minuto_final:
    hora_jogada = 0
    minuto_jogado = minuto_final - minuto_inicial
elif hora_inicial < hora_final:
    hora_jogada = hora_final - hora_inicial
    minuto_jogado = minuto_final - minuto_inicial
    if minuto_jogado < 0:
        hora_jogada -= 1
        minuto_jogado += 60
else:
    hora_jogada = (24 - hora_inicial) + hora_final
    minuto_jogado = minuto_final - minuto_inicial
    if minuto_jogado < 0:
        hora_jogada -= 1
        minuto_jogado += 60
print(f'O JOGO DUROU {hora_jogada} HORA(S) E {minuto_jogado} MINUTO(S)')
