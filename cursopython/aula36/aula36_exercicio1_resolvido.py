"""
1 - Crie uma função1 que recebe uma função2 como parâmetro e retorne o valor da função2 executada.
"""


def func_pai(arg):
    return arg


def func1():
    variavel = 'valor'
    return variavel


executar = func_pai(func1())
print(executar)
