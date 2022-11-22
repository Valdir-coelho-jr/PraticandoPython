secreto = 'gardevoir'
digitadas = []
chances = 3

while True:
    if chances <= 0:
        print('Você Perdeu!')
        break

    letras = input('Digite uma letra: ')

    digitadas.append(letras)

    if len(letras) > 1:
        print('Não vale! Digite apenas uma letra!')
        continue

    if letras in secreto:
        print(f'Boa! a letra {letras} faz parte da palavra secreta!')
    else:
        print(f'A letra {letras} não faz parte da palavra secreta.')
        digitadas.pop()

    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'

    if secreto_temporario == secreto:
        print(f'Você ganhou! a palavra secreta é: {secreto}')
        break
    else:
        print(f'A palavra secreta está assim: {secreto_temporario}')

    if letras not in secreto:
        chances -= 1

    print(f'Você ainte tem {chances} chances!')
    print()
