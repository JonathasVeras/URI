def binario_decimal(binario: str):
    somatorio = 0
    for i in range(len(binario)):
        somatorio += binario[len(binario)-1] * 2**i
