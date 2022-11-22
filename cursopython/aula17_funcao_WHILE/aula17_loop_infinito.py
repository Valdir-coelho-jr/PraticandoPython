titulo = 'Calculadora Básica'
print(f'{titulo:#^40}')
replay = 'sim'
while replay == 'sim':
    num1 = input('Digite o primeiro numero: ')
    num2 = input('Digite o segundo numero: ')

    print('=== Exemplo de Operadores ===')
    print('+ , - , * , /')
    operador = input('Selecione o Operador:')

    if not num1.isnumeric() or not num2.isnumeric():
        print('Você precisa um número para realizar a operação.')
    else:
        num1 = int(num1)
        num2 = int(num2)

    if operador == '+':
        print(f'{num1} + {num2} = ', num1 + num2)
    elif operador == '-':
        print(f'{num1} - {num2} = ', num1 - num2)
    elif operador == '*':
        print(f'{num1} * {num2} = ', num1 * num2)
    elif operador == '/':
        print(f'{num1} / {num2} = ', num1 / num2)
    else:
        print(f'Operador invalido!')
    print('Deseja continuar?')
    replay = input('Digite [sim] para continuar e [nao] para encerrar: ')
    while replay != 'sim' and replay != 'nao':
        print('Digite [sim] ou [nao] para continuar ou encerrar o programa!')
        replay = input('Digite [sim] para continuar e [nao] para encerrar: ')
    if replay == 'sim':
        continue
    elif replay == 'nao':
        print('Programa de Calculadora Básica encerrado!')

