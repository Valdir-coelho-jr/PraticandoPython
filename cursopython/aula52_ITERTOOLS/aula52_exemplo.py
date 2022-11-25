"""
Combinations, Permutations e Product - Itertools
Combinação - Ordem não importa
Permutação - Ordem importa
Ambos não repetem valores únicos
Produto - Ordem importa e repete valores únicos
"""
from itertools import combinations, permutations, product

pessoas = ['Luiz', 'André', 'Eduardo', 'Letícia', 'Fabrício', 'Rose']

while True:
    escolha = input('[1] Combinations [2] Permutations e [3] product: ')
    escolha = int(escolha)


    if escolha == 1:
        for grupo in combinations(pessoas, 2):
            print(grupo)
    elif escolha == 2:
        for grupo in permutations(pessoas, 2):
            print(grupo)
    elif escolha == 3:
        for grupo in product(pessoas, repeat=2):
            print(grupo)
    else:
        break

