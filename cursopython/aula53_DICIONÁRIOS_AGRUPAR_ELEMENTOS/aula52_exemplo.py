from itertools import groupby, tee
alunos = [
    {'nome': 'Luiz', 'Nota': 'A'},
    {'nome': 'Letícia', 'Nota': 'B'},
    {'nome': 'Fabrício', 'Nota': 'A'},
    {'nome': 'Rosemary', 'Nota': 'C'},
    {'nome': 'Joana', 'Nota': 'D'},
    {'nome': 'João', 'Nota': 'A'},
    {'nome': 'Eduardo', 'Nota': 'B'},
    {'nome': 'André', 'Nota': 'A'},
    {'nome': 'Anderson', 'Nota': 'C'},
    {'nome': 'José', 'Nota': 'B'},
]
ordena = lambda item: item['Nota']

alunos.sort(key=ordena)
alunos_agrupados = groupby(alunos, ordena)

for agrupamento, valores_agrupados in alunos_agrupados:
    va1, va2 = tee(valores_agrupados)
    print(f'Agrupamento: {agrupamento}')

    for aluno in va1:
        print(f'\t{aluno}')

    quantidade = len(list(va2))

    print(f'\t{quantidade} Alunos tiraram nota {agrupamento}')

