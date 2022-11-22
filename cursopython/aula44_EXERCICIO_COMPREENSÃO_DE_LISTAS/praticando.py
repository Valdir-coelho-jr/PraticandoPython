
string = '123456712345671234567123456712345671234567123456712345671234567123456712345671234567'
n = 7

contador = [v for v in range(0, len(string), n)]

contador2 = [(v, v + n) for v in range(0, len(string), n)]

lista = [string[v: v + n] for v in range(0, len(string), n)]

formatado = '.'.join(lista)

print(formatado)
