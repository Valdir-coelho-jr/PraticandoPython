# https://docs.python.org/3/library/exceptions.html

def divide(n1, n2):
    if n2 == 0:
        raise ValueError('n2 não pode ser divisível por 0')
    return n1 / n2

try:
    print(divide(5, 0))
except ValueError as error:
    print('VOcê está tentando dividir por 0.')
    print('Log: ', error)
