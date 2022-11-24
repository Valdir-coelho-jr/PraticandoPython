"""
try:
    file = open('dfg.txt', '+w')
    file.write('Linha')
    file.seek(0, 0)
    print(file.read())
finally:
    file.close()
"""
"""
with open('dfg.txt', 'w+')as file: -> ['w+'] = Write / Escrever. Apaga tudo que estiver no arquivo antes de escrever
    file.write('Linha 1\n')
    file.write('Linha 2\n')
    file.write('Linha 3\n')

    file.seek(0)
    print(file.read())

with open('dfg.txt', 'r')as file: ['r'] = Read / Ler
    print(file.read())
"""

with open('dfg.txt', 'a+')as file:
    file.write('Outra linha\n')
    file.seek(0, 0)
    print(file.read())
