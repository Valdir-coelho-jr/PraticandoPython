

while True:
    idade = input('Digite sua idade: ')
    if not idade.isnumeric():
        print('Digite apenas numeros!')
        continue
    else:
        idade = int(idade)
        maior_idade = (idade >= 18)
        msg = 'Acesso liberado' if maior_idade else 'Não tem acesso'

        print(msg)
        break
