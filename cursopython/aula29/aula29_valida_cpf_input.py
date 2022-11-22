print('==========================================')
titulo = 'VALIDADOR DE CPF'
print(f'{titulo:-^21}')
print('==========================================')
print('Digite o seu CPF para ele ser Validado')
replay = 'sim'
while replay == 'sim':
    while True:
        cpf = input('CPF: ')

        if not cpf.isnumeric():
            print('Por favor, digite apenas numeros!')
        else:
            if len(cpf) > 11:
                print('O valor digitado contém mais de 11 números!')
                print('Por favor, digite o seu CPF corretamente (11 Digitos)')
                continue
            elif len(cpf) < 11:
                print('O valor digitado contém menos de 11 números!')
                print('Por favor, digite o seu CPF corretamente (11 Digitos)')
                continue
            else:
                break

    cpf = int(cpf)
    _str = cpf.__str__()
    lista = list(_str)

    n1, n2, n3, n4, n5, n6, n7, n8, n9, *_ = lista
    lista = n1, n2, n3, n4, n5, n6, n7, n8, n9

    total1 = 0

    for v1, v2 in enumerate(lista):
        v2 = int(v2)
        v3 = 10 - v1
        acumulo = v2 * v3
        total1 += acumulo

    digit1 = len(_str) - (total1 % (len(_str)))
    if digit1 > 9:
        digit1 = 0

    lista2 = list(_str)
    n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, *_ = lista2
    lista2 = n1, n2, n3, n4, n5, n6, n7, n8, n9, digit1
    total2 = 0

    for v1, v2 in enumerate(lista2):
        v2 = int(v2)
        v3 = 11 - v1
        acumulo = v2 * v3
        total2 = total2 + acumulo

    digit2 = len(_str) - (total2 % (len(_str)))

    novo_cpf = ''
    for n1 in cpf.__str__():
        if len(novo_cpf) <= 8:
            novo_cpf += n1
        else:
            novo_cpf += digit1.__str__()
            novo_cpf += digit2.__str__()
            break

    if int(novo_cpf) == cpf:
        print('================================================')
        print('CPF VALIDADO COM SUCESSO!')
    else:
        print('================================================')
        print('CPF INVALIDO!!!!!')

    print('Deseja validar outro CPF?')
    while True:
        replay = input('Digite [sim] ou [nao]: ')
        if replay == 'sim':
            break
        elif replay == 'nao':
            break
        else:
            print('Resposta Inválida!')
            continue

print('================================================')
print('Validador de CPF Encerrado!')
print('================================================')
