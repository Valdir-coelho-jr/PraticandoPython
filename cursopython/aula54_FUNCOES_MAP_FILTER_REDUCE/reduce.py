from dados import produtos, pessoas, lista
from functools import reduce
# - LISTA
"""
soma_lista = reduce(lambda ac, i: i + ac, lista, 0)

print(soma_lista)
"""

# - PRODUTOS
"""
soma_precos = reduce(lambda ac, p: p['preco'] + ac, produtos, 0)
print(round(soma_precos, 2))
media_precos = soma_precos / len(produtos)
print(f'Média: {round(media_precos, 2)}')
"""

# - PESSOAS

media_idade = reduce(lambda ac, p: ac + p['idade'], pessoas, 0)
print(f'Média de idade dos clientes: {round(media_idade / len(pessoas))} anos')

