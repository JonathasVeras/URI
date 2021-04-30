def binario_decimal(binario: str):
    somatorio = 0
    for i in range(len(binario)):
        somatorio += int(binario[len(binario)-1 - i]) * (2 ** i)
    return somatorio


def corvo_translate(string):
    lista = []
    somatorio = 0
    for i in range(len(string)):
        if string[i] != "caw":
            somatorio += binario_decimal(string[i])
        else:
            lista.append(somatorio)
            somatorio = 0
    return lista

x = input()
corvo_input = [x]
for i in range(3):
    x = input()
    corvo_input.append(x)
    while x != "caw caw":
        x = input()
        corvo_input.append(x)

# corvo_input = input()
corvo_input = ' '.join(corvo_input)
corvo_input = corvo_input.replace("*", "1")
corvo_input = corvo_input.replace("-", "0")
corvo_input = corvo_input.replace("caw caw", "caw")
corvo_input = corvo_input.split(" ")
corvo_traduzido = corvo_translate(corvo_input)

for i in corvo_traduzido:
    print(i)
