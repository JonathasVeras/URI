"""Entrada

A entrada contém 6 números que podem ser valores inteiros ou de
ponto flutuante. Pelo menos um destes números será positivo.

Saída

O primeiro valor de saída é a quantidade de valores positivos.
A próxima linha deve mostrar a média dos valores positivos digitados.
"""
numeros = []
contador_positivo = 0
soma_positivos = 0
for i in range(6):
    numeros.append(float(input()))
for i in numeros:
    if i >= 0:
        contador_positivo += 1
        soma_positivos += i
print(f'{contador_positivo} valores positivos\n{(soma_positivos/contador_positivo):.1f}')

