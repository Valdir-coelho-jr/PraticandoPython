"""
Funções (def) em Python - return - Parte 2
"""


def divisao(n1, n2):
    if n1 or n2 == 0:
        return

    return n1 / 2


dividir = divisao(7, 9)

if dividir:
    print(dividir)
else:
    print('Conta invalida!')
