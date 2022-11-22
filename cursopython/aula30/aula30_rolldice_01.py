from random import randint
espaçamento = '='
titulo = 'Rolador de Dados'
print(f'{titulo:=^35}')
replay = True

while replay:
    while True:
        print('Dados pré-definidos')
        print('D4: [1] D6: [2] D8: [3]')
        print('D10: [4] D12: [5] D20: [6]')
        print('Dado customizado: [7] ou mais')
        print()
        print('Digite o numero que corresponde ao Dado desejado')
        print(f'{espaçamento:=^35}')
        print('Exemplo: para escolher o D6, digite [2]')
        escolha = input('Resposta: ')
        if not escolha.isnumeric():
            print('Digite apenas números!')
            print(f'{espaçamento:=^35}')
            continue
        else:
            if escolha == '1':
                rolldice = randint(1, 4)
                print(f'{espaçamento:=^35}')
                print(f'ROLLDICE D4: {rolldice:^21}')
                print(f'{espaçamento:=^35}')
                break
            elif escolha == '2':
                rolldice = randint(1, 6)
                print(f'{espaçamento:=^35}')
                print(f'ROLLDICE D6: {rolldice:^21}')
                print(f'{espaçamento:=^35}')
                break
            elif escolha == '3':
                rolldice = randint(1, 8)
                print(f'{espaçamento:=^35}')
                print(f'ROLLDICE D8: {rolldice:^21}')
                print(f'{espaçamento:=^35}')
                break
            elif escolha == '4':
                rolldice = randint(1, 10)
                print(f'{espaçamento:=^35}')
                print(f'ROLLDICE D10: {rolldice:^21}')
                print(f'{espaçamento:=^35}')
                break
            elif escolha == '5':
                rolldice = randint(1, 12)
                print(f'{espaçamento:=^35}')
                print(f'ROLLDICE D12: {rolldice:^21}')
                print(f'{espaçamento:=^35}')
            elif escolha == '6':
                rolldice = randint(1, 20)
                print(f'{espaçamento:=^35}')
                print(f'ROLLDICE D20: {rolldice:^21}')
                print(f'{espaçamento:=^35}')
                break
            else:
                titulo = 'Dado Customizado selecionado'
                print(f'{espaçamento:=^35}')
                print(f'{titulo:^35}')
                print(f'{espaçamento:=^35}')
            while True:
                escolha = input('Digite a quantidade de lados do seu dado: #D')
                if not escolha.isnumeric():
                    print('Digite apenas números!')
                    print(f'{espaçamento:=^35}')
                    continue
                else:
                    rolldice = randint(1, int(escolha))
                    print(f'{espaçamento:=^35}')
                    print(f'ROLLDICE D20: {rolldice:^21}')
                    print(f'{espaçamento:=^35}')
                    break
            break
    while True:
        replay_escolha = input('Deseja rolar mais algum dado?[sim] [nao]: ')
        if replay_escolha == 'sim':
            replay = True
            break
        elif replay_escolha == 'nao':
            replay = False
            print(f'{espaçamento:=^35}')
            print('Rolador de Dados Encerrado com sucesso!')
            break
        else:
            print('Resposta Inválida!')
            print(f'{espaçamento:=^35}')
            print('Digite [sim] ou [nao] para responder a pergunta!')
            continue

