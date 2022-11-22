
string = '0123456789012345678901234567890123456789'
n = 10

contador = [v for v in range(0, len(string), n)]

contador2 = [(v, v + n) for v in range(0, len(string), n)]

lista = [string[v:v + n] for v in range(0, len(string), n)]

retorno = '.'.join(lista)

print(retorno)
