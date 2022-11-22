"""
2 - Crie uma função1 que recebe uma função2 como parâmetro e retorne o valor da função2 executada.
Faça a função1 executar duas funções que recebam um número diferente de argumentos.
"""


def func_pai(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)


def func_oi(nome):
    return f'Oi, {nome}'


def func_saudacao(nome, saudacao):
    return f'{saudacao}, {nome}'


executar = func_pai(func_oi, 'Valdir!')
print(executar)
executar2 = func_pai(func_saudacao, 'Valdir!', saudacao='Bom dia!')
print(executar2)
