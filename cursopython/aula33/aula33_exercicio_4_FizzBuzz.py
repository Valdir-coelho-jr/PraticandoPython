"""
4 - Fizz Buzz - Se o parâmetro da função for divisível por 3, retorne fizz, se o parâmetro da função for
divisível por 5, retorne buzz. Se o parâmetro da função for divisível por 5 e por 3,
retorne FizzBuzz, caso contrário, retorne o número enviado.
"""


def Fizz_Buzz(n1):
    n1 = int(n1)
    if n1 % 3 == 0 and n1 % 5 == 0:
        return 'FizzBuzz'
    if n1 % 5 == 0:
        return 'Buzz'
    if n1 % 3 == 0:
        return 'Fizz'
    return n1


while True:
    contador = Fizz_Buzz(n1=input(': '))
    print(contador)
