"""
Funções (def) em Python - *args **kwargs -
Aula 16 (Parte 3)
"""


def func(*args, **kwargs):
    print(args)

    nome = kwargs.get('nome')
    print(nome)

    idade = kwargs.get('idade')
    if idade is not None:
        print(idade)


#  print(kwargs['nome'], kwargs['sobrenome'])


lista = [1, 2, 3, 4, 5, 6, 7]

lista2 = [10, 20, 30, 40, 50, 60, 70]

func(*lista, 'rogério', *lista2, nome='Rogerio', sobrenome='Etemon', idade=28)
