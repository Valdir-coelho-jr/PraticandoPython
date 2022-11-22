print('==========================================')
titulo = 'VALIDADOR DE CPF'
print(f'{titulo:-^21}')
print('==========================================')
print('Digite o seu CPF para ele ser Validado')
replay = 'sim'
while replay == 'sim':
    while True:
        cpf = input('CPF [11 digitos]: ')
        if not cpf.isnumeric():
            print('Digite apenas numeros!')
            continue
        else:
            if len(cpf) > 11:
                print('O CPF digitado possui mais de 11 numeros!')
                continue
            elif len(cpf) < 11:
                print('O CPF digitado possui menos de 11 numeros!')
                continue
            else:
                break

    novo_cpf = cpf[:-2]
    reverso = 10
    total = 0
    for index in range(19):
        if index > 8:
            index -= 9

        total += int(novo_cpf[index]) * reverso

        reverso -= 1
        if reverso < 2:
            reverso = 11
            d = 11 - (total % 11)

            if d > 9:
                d = 0
            total = 0
            novo_cpf += str(d)
    if cpf == novo_cpf:
        print("Válido")
    else:
        print('Inválido')

    while True:
        replay = input('Deseja continuar? [sim] ou [nao]: ')
        if replay == 'sim':
            break
        elif replay == 'nao':
            break
        else:
            print('Resposta inválida! Digite [sim] para contiouar ou [nao] para encerrar o programa!')
            continue
