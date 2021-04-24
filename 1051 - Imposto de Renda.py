def imposto(salario_cliente):
    salario_cliente = float(salario_cliente)
    if salario_cliente >= 4500:
        return (salario_cliente - 4500 * 0.28) + imposto(salario_cliente - (salario_cliente-4500))
    elif 3000.01 <= salario_cliente <= 4500:
        return (salario_cliente - 3000 * 0.18) + imposto(salario_cliente - (salario_cliente - 3000))
    elif 2000.01 <= salario_cliente <= 3000:
        return (salario_cliente - 2000 * 0.08) + imposto(salario_cliente - (salario_cliente - 2000))
    elif salario_cliente < 2000:
        return 0


salario = input()
resultado = imposto(salario)
print(resultado)
