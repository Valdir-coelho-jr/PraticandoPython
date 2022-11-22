print()
print('Sample Text.')

perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quanto é 2 + 2 ?',
        'respostas': {'a': '7', 'b': '4', 'c': '5', 'd': '3', },
        'resposta_certa': 'b',
    },
    'Pergunta 2': {
        'pergunta': 'Quanto é 3 x 2 ?',
        'respostas': {'a': '23', 'b': '2', 'c': '6', 'd': '4', },
        'resposta_certa': 'c',
    },
    'Pergunta 3': {
        'pergunta': 'Quanto é 1 + 2 ?',
        'respostas': {'a': '23', 'b': '3', 'c': '6', 'd': '4', },
        'resposta_certa': 'b',
    },
    'Pergunta 4': {
        'pergunta': 'Quanto é 1 - 1 ?',
        'respostas': {'a': '0', 'b': '100', 'c': '6', 'd': '1.5', },
        'resposta_certa': 'a',
    },
    'Pergunta 5': {
        'pergunta': 'Quanto é 8 / 4 ?',
        'respostas': {'a': '20', 'b': '1', 'c': '2', 'd': '4', },
        'resposta_certa': 'c',
    },
}

acertos = 0
for pk, pv in perguntas.items():
    print(f'{pk}: {pv["pergunta"]}')

    print('Respostas:')
    for rk, rv in pv['respostas'].items():
        print(f'[{rk}]: {rv}')

    usuario_resposta = input('Sua resposta: ')

    if usuario_resposta == pv['resposta_certa']:
        print('Você acertou!')
        acertos += 1
    else:
        print('Resposta errada!')

    print()
    qtd_perguntas = len(perguntas)
    porcentagem = acertos / qtd_perguntas * 100
    print(f'Você tem um total de {int(porcentagem)}% de acertos!')

    print()
