print()
print('Sistema de Perguntas com Alternativas.')
print('Escolha a alternativa correta para acertar a pergunta!')
print()

perguntas = {
    'pergunta 1': {
        'pergunta': 'Quanto é 2 x 2 ?',
        'respostas': {'a': '3', 'b': '5', 'c': '4', 'd': '9', },
        'resposta_certa': 'c'
    },
    'pergunta 2': {
        'pergunta': 'Quanto é 5 x 5 ?',
        'respostas': {'a': '25', 'b': '50', 'c': '41', 'd': '92', },
        'resposta_certa': 'a'
    },
    'pergunta 3': {
        'pergunta': 'Quanto é 10 / 2 ?',
        'respostas': {'a': '10', 'b': '22', 'c': '1', 'd': '5', },
        'resposta_certa': 'd'
    },
    'pergunta 4': {
        'pergunta': 'Quanto é 1 - 1 ?',
        'respostas': {'a': '40', 'b': '1', 'c': '0', 'd': 'rogério', },
        'resposta_certa': 'c'
    },
}

acertos = 0
for pk, pv in perguntas.items():
    print(f'{pk}: {pv["pergunta"]}')

    print('Respostas:')
    for rk, rv in pv['respostas'].items():
        print(f'[{rk}]: {rv}')

    print()

    resposta_usuario = input('Sua Resposta: ')

    if resposta_usuario == pv['resposta_certa']:
        print('Você acertou!')
        acertos += 1
    else:
        print('Resposta errada!')

qtd_acertos = len(perguntas)
porcentagem = acertos / qtd_acertos * 100
print(f'Você teve um total de {int(porcentagem)}% de acertos!')
