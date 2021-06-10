"""
Leia um valor inteiro X. Em seguida apresente os 6 valores ímpares consecutivos a partir de X, um valor por linha, inclusive o X ser for o caso.

Entrada
A entrada será um valor inteiro positivo.

Saída
A saída será uma sequência de seis números ímpares.

"""

valor_inicial = int(input())
contador_impar = 0

while contador_impar != 6:
    if valor_inicial % 2 != 0:
        print(valor_inicial)
        contador_impar += 1
    valor_inicial += 1
