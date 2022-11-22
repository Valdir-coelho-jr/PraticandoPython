"""
Tipos de dados
str - string - textos 'Assim' ou "Assim"
int - inteiro - 123456789 0 -10 -20 -50 -100 -15000 1500
float - real/ponto flutuante - 10.50 1.5 -10.10 -50.93 0.0
bool - booleano/lógico - True/False 10 == 10 20 == 10
"""

print('Luiz', type('Luiz'))
print(77, type(77))
print(7.77, type(7.77))
print(7 == 7, type(7 == 7))
print(7.7 == 77, type(7.7 == 77))
print('L' == 'L', type('L' == 'L'))
print('l' == 'L', type('l' == 'L'))
print(bool('A'))
print(bool(''))

"""
Exercício:
"""

# string: nome
print('Valdir Coelho Junior', type('Valdir Coelho Junior'))

# int: idade
print(28, type(28))
# float: alturaprint('', type(''))

# float: altura
print(1.83, type(1.83))

# bool: É maior de idade 10 > 20
print(28 > 18, type(28 > 18))

