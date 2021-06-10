"""
Leia 2 valores inteiros X e Y. A seguir, calcule e mostre a soma dos números impares entre eles.

Entrada
O arquivo de entrada contém dois valores inteiros.

Saída
O programa deve imprimir um valor inteiro. Este valor é a soma dos valores ímpares que estão entre os valores fornecidos na entrada que deverá caber em um inteiro.
"""

def maior_valor(num1, num2):
    return num1*(num1 > num2) + num2*(num2 > num1)


def menor_valor(num1, num2):
    return num1*(num1 < num2) + num2*(num2 < num1)

valor_1 = int(input())
valor_2 = int(input())

valores_impares = []

for i in range(menor_valor(valor_1, valor_2)+1, maior_valor(valor_1, valor_2)):
    if i % 2 != 0:
        valores_impares.append(i)


print(sum(valores_impares))
