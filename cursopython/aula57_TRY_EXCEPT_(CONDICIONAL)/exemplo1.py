def converte_numero(valor):
    try:
        valor = int(valor)
        return valor
    except ValueError:
        try:
            valor = float(valor)
            return valor
        except ValueError:
            return None


while True:
    numero = (converte_numero(input('Digite um número: ')))

    if numero is not None:
        print(numero * 7)
    else:
        print('Erro: Isso não é um número!')

