"""
While em Python
utilizado para realizar ações enquanto
uma condição for verdadeira

Requisitos: Entender condições e operadores
"""

x = 0  # coluna
y = 0  # linha

while x < 10:
    y = 0
    while y < 5:
        print(f'X:{x}, Y:{y}')
        y += 1
    x += 1  # x = x + 1

print('Acabou!')
