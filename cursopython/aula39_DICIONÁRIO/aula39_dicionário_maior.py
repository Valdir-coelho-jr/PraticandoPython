clientes = {
    'cliente1': {
        'nome': 'rogério',
        'sobrenome': 'da silva',
    },
    'cliente2': {
        'nome': 'etemon',
        'sobrenome': 'feliz',
    },
    'cliente3': {
        'nome': 'valdir',
        'sobrenome': 'coelho jr',
    },
    'cliente4': {
        'nome': 'japinha',
        'sobrenome': 'dinamico',
    },
}

for clientes_k, clientes_v in clientes.items():
    print(f'Exibindo {clientes_k}')
    for dados_k, dados_v in clientes_v.items():
        print(f'\t{dados_k} = {dados_v}')
