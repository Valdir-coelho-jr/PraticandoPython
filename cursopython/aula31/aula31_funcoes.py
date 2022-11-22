"""
Funções - def em Python (Parte 1)
"""


def funcao(msg='Olá!', nome='Valdir'):
    nome = nome.replace('e', '3')
    msg = msg.replace('e', '3')
    print(msg, nome)

funcao()
funcao('Olá', 'Dorme')
funcao('Flish', 'Lineage')
funcao(nome='Rogerio')
funcao(nome='Pao', msg='Hello!')
