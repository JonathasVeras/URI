"""
Leia 5 valores Inteiros. A seguir mostre quantos valores digitados foram pares, quantos valores digitados foram ímpares, quantos valores digitados foram positivos e quantos valores digitados foram negativos.
Entrada

O arquivo de entrada contém 5 valores inteiros quaisquer.
Saída

Imprima a mensagem conforme o exemplo fornecido, uma mensagem por linha, não esquecendo o final de linha após cada uma.
"""
#Criação da lista onde ficarão as entradas.
valores = []
#Sistema para a entrada de 5 elementos na lista "valores".
for i in range(5):
    valores.append(int(input()))
#Dicionário onde ficam os contadores de números pares, ímpares, positivos e negativos
contadores = {"pares": 0, "impares": 0, "positivos": 0, "negativos": 0}
#For para avaliar cada número da lista "valores" e adicionarem pontos nos 
#contadores dependendo do resultado
for i in valores:
    if i % 2 == 0:
        contadores["pares"] += 1
    else:
        contadores["impares"] += 1
    if i > 0:
        contadores["positivos"] += 1
    elif i < 0:
        contadores["negativos"] += 1
#Saída dos dados
print(f'{contadores["pares"]} valor(es) par(es)')
print(f'{contadores["impares"]} valor(es) impar(es)')
print(f'{contadores["positivos"]} valor(es) positivo(s)')
print(f'{contadores["negativos"]} valor(es) negativo(s)')