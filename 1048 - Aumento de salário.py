import math


def new_pay(old_pay):
    if old_pay <= 400.00:
        return old_pay + (0.15 * old_pay), (0.15 * old_pay), 15
    elif old_pay >= 400.01 and old_pay <= 800.00:
        return old_pay + (0.12 * old_pay), (0.12 * old_pay), 12
    elif old_pay >= 800.01 and old_pay <= 1200.00:
        return old_pay + (0.10 * old_pay), (0.10 * old_pay), 10
    elif old_pay >= 1200.01 and old_pay <= 2000.00:
        return old_pay + (0.07 * old_pay), (0.07 * old_pay), 7
    return old_pay + (0.04 * old_pay), (0.04 * old_pay), 4


old_pay1 = float(input())
new_pay1, readjustment1, as_a_percentage1 = new_pay(old_pay1)
print(f'Novo salário: {new_pay1:.2f}')
print(f'Reajuste ganho: {readjustment1:.2f}')
print(f'Em percentual: {as_a_percentage1} %')

