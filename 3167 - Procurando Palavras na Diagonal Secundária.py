def x(matriz, n_linhas, n_colunas):
    diagonal_coordenada = []
    lista_palavras_matriz = []
    for limite in range(0, n_linhas):
        print(limite)
        j = 0
        palavra = []
        diagonal_coordenada.append(is_secundary_diagonal(limite, n_linhas))
        for lin in range(limite, -1, -1):
            palavra.append(matriz[lin][j])
            j += 1
        palavra = ''.join(palavra)
        lista_palavras_matriz.append(palavra)
    print(lista_palavras_matriz)
    print(diagonal_coordenada)


def is_secundary_diagonal(linha, numero_linhas):
    if linha == numero_linhas-2:
        return "acima da"
    elif linha == numero_linhas-1:
        return "na"
    return "abaixo da"


# input do número de palavras, linhas e colunas usando a função map.
n_palavras, n_linhas, n_colunas = map(int, input().split())

lista_palavras = []
# Colocando as palavras a serem "pesquisadas" na matriz dentro de uma liasta
for i in range(n_palavras):
    lista_palavras.append(input())
palavras = {}
palavras = palavras.fromkeys(lista_palavras, 0)

print('Coloque a matriz')

# input de matriz usando List Comprehension
matriz = [[str(input()) for j in range(n_colunas)] for i in range(n_linhas)]

x(matriz, n_linhas, n_colunas)


