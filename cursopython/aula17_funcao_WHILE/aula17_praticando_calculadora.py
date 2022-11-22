print('==========================================================')
print('App de Calculadora')
print('Tipos de Calculos: + , - , * e /')
print('==========================================================')
titulo = ''
replay = 'sim'

while replay == 'sim':
    n1 = input('Digite um número: ')
    if not n1.isnumeric():
        print('Digite um numero, não uma letra!')
        print()
        continue
    n2 = input('Digite o segundo número: ')
    if not n2.isnumeric():
        print('Digite um numero, não uma letra!')
        print()
        continue
    else:
        n1 = int(n1)
        n2 = int(n2)

    print(f'{titulo:=^40}')
    print('Operadores: [+],[-],[*] e [/]')
    print(f'{titulo:=^40}')
    while True:
        operador = input('Digite o operador: ')
        if operador == "+":
            print('Operação de Soma [+]')
            print(f'{n1} + {n2} = {n1 + n2}')
            break
        elif operador == '-':
            print('Operação de Soma [-]')
            print(f'{n1} - {n2} = {n1 - n2}')
            break
        elif operador == '*':
            print('Operação de Soma [*]')
            print(f'{n1} * {n2} = {n1 * n2}')
            break
        elif operador == '/':
            print('Operação de Soma [/]')
            print(f'{n1} / {n2} = {n1 / n2}')
            break
        else:
            print('Operador invalido! Digite um Operador Válido!')
            continue

    print('Operação concluída!')
    print('Deseja realizar mais alguma operação?')
    while True:
        print(f'{titulo:=^40}')
        print('Digite [sim] para realizar outra operação.')
        print('Digite [nao] para encerrar o programa.')
        print(f'{titulo:=^40}')
        replay_temporario = input('Resposta: ')
        if replay_temporario == 'nao':
            replay = replay_temporario
            break
        elif replay_temporario == 'sim':
            replay = replay_temporario
            break
        else:
            print('ERRO')
            print('Resposta Invalída!')
            continue

print()
print('Obrigado por Utilizar esse Programa!')

