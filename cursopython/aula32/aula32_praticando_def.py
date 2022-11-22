def verif(num):
    num = input('Digite um numero: ')
    if not num.isnumeric():
        print('Digite apenas numeros!!!!')
    else:
        num = int(num)
    return verif(num)


