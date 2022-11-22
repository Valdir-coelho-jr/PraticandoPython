from random import randint
rolldice = randint(1, 20)
precisao = input('Precisão: ')
while True:
    if not precisao.isnumeric():
        print('Digite apenas numeros!')
        continue
    else:
        precisao = int(precisao)
        break

print(f'Rolldice: #D{rolldice} + {precisao} [{rolldice + precisao}]')
