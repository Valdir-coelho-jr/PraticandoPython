"""
3 - Crie uma função que receba 2 números. O primeiro é um valor e o segundo um percentual (ex. 10%).
Retorne (return) o valor do primeiro número somado do aumento do percentual do mesmo.
"""


def funcao(valor, percentual):
    return valor + ((valor / 100) * percentual)


ap = funcao(50, 10)
print(ap)
