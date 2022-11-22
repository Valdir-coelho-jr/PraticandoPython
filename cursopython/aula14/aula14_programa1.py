"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

num1 = input('Digite um numero inteiro: ')

try:
    num1 = int(num1)
    if num1 % 2 == 0:
        print(f'O número {num1} é um número inteiro par')
    else:
        print(f'O número {num1} é um número inteiro impar')
except:
    try:
        num1 = float(num1)
        print(f'O numero {num1} não é um número inteiro')
        print('Por favor, digite um número inteiro.')
    except:
        print("ERRO")
