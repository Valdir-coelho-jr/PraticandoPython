"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada. Ex.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23
"""

horario = input('Digite o horário atual: ')

try:
    horario = int(horario)
    if horario < 0 or horario > 23:
        print('O horário deve estar entre 0 e 23')
    elif horario <= 11:
        print('Bom dia!')
    elif 12 <= horario <= 17:
        print('Boa tarde!')
    elif 18 <= horario <= 23:
        print('Boa noite!')
except:
    try:
        horario = float(horario)
        print(f'{horario} não é uma digitação válida')
        print('Por favor, tente digitar o horário com números inteiros.')
        print('Exemplos:')
        print('Horário de manhã: 0 a 11')
        print('Horário de tarde: 12 a 17')
        print('Horário de noite: 18 a 23')
    except:
        print('ERRO')
