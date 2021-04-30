valores = [float(input()) for numeros in range(6)]
print(f'{len((list(filter(lambda x: x > 0, valores))))} valores positivos')
