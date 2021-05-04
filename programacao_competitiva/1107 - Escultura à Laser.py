altura, comprimento = map(int, input().split())

#Lista criada para colocar
lista_resposta = []

while altura != 0 and comprimento != 0:
    maior_altura = altura
    lista_altura_input = list(map(int, input().split()))
    uso_do_laser = altura - lista_altura_input[0]
    for j in range(1, comprimento):
        if lista_altura_input[j - 1] > lista_altura_input[j]:
            uso_do_laser += lista_altura_input[j-1] - lista_altura_input[j]

    lista_resposta.append(uso_do_laser)
    altura, comprimento = map(int, input().split())

for i in lista_resposta:
    print(i)
