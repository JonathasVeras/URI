"""
Faça um programa que leia 5 valores inteiros. Conte quantos destes valores digitados são pares e mostre esta informação.
Entrada

O arquivo de entrada contém 5 valores inteiros quaisquer.
Saída

Imprima a mensagem conforme o exemplo fornecido, indicando a quantidade de valores pares lidos.
"""
valores_par = []
for i in range(5):
    x = int(input())
    if x % 2 == 0:
        valores_par.append(x)
print(f'{len(valores_par)} valores pares')
