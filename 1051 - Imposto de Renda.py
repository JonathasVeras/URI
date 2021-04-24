def imposto(salario_cliente):
    imposto_renda = salario_cliente
    if salario_cliente <= 2000:
        return 0
    elif salario_cliente > 4500:
        imposto_renda = ((salario_cliente - 4500) * 0.28)
        return imposto_renda + imposto(salario_cliente - (salario_cliente - 4500))
    elif 3000.01 <= salario_cliente <= 4500:
        imposto_renda = ((salario_cliente - 3000) * 0.18)
        return imposto_renda + imposto(salario_cliente - (salario_cliente - 3000))
    elif 2000.01 <= salario_cliente <= 3000:
        imposto_renda = ((salario_cliente - 2000) * 0.08)
        return imposto_renda + imposto(salario_cliente - (salario_cliente - 2000))


salario = float(input())
resultado = imposto(salario)
if resultado == 0:
    print('Isento')
else:
    print(f'R$ {resultado:.2f}')
