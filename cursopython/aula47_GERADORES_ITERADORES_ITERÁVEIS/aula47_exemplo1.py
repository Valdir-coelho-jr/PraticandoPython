"""
Uma iterável é um objeto que pode ser iterar sobre ele, mas ele não é necessáriamente um iterador
"""

lista = [1, 2, 3, 4, 5, 6, 7]

print(hasattr(lista, '__iter__'))
