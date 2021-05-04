def new_pay(old_pay):
    if type(old_pay) is float:
        if old_pay <= 400.00:
            #     |Salário reformulado        |Valor adicionado |porcentagem adicionada
            return old_pay + (0.15 * old_pay), (0.15 * old_pay), 15
        elif 400.01 <= old_pay <= 800.00:
            return old_pay + (0.12 * old_pay), (0.12 * old_pay), 12
        elif 800.01 <= old_pay <= 1200.00:
            return old_pay + (0.10 * old_pay), (0.10 * old_pay), 10
        elif 1200.01 <= old_pay <= 2000.00:
            return old_pay + (0.07 * old_pay), (0.07 * old_pay), 7
        return old_pay + (0.04 * old_pay), (0.04 * old_pay), 4
    else:
        raise ValueError('O valor colocado NÃO é FLOAT.')


try:
    old_pay1 = float(input())
except ValueError as erra:
    print(f'O valor que foi colocado não foi FLOAT: {erra}')
else:
    new_pay1, readjustment1, as_a_percentage1 = new_pay(old_pay1)
    print(f'Novo salario: {new_pay1:.2f}')
    print(f'Reajuste ganho: {readjustment1:.2f}')
    print(f'Em percentual: {as_a_percentage1} %')
finally:
    print('O código foi executado com sucesso.')
