from random import randint

dado = input('Rolador de Dados: #D')

if not dado.isnumeric():
    print('Digite apenas numeros!')
else:
    if int(dado) <= 0:
        print('DADO INVÁLIDO!')
    else:
        rolldice = randint(1, int(dado))
        print(rolldice)
