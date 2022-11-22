frase = 'a garra que agarra'
tamanho_frase = len(frase)
contador = 0
nova_string = ''

repeticao = 'Y'

while repeticao == 'Y':
    input_usuário = ''
    input_usuário = input('Digite a letra que ficará maiúscula: ')
    while contador < tamanho_frase:
        letra = frase[contador]
        if letra == input_usuário:
            nova_string += input_usuário.upper()
        else:
            nova_string += letra
        contador += 1
    print(nova_string)
    print('Deseja repetir a operaçao?')
    repeticao = input('Digite Y para repetir e N para encerrar: ')
    if repeticao == 'N':
        break
    else:
        while repeticao != 'Y':
            if repeticao == 'N':
                break
            else:
                print('COMANDO INCORRETO!!!!!')
                repeticao = input('Digite Y para repetir e N para encerrar: ')
print('Operaçao encerrada!')
