# Usando o comando len()

string1 = input('Digite alguma coisa: ')
string2 = input('Digite outra coisa: ')

print(f'O numero de caracteres total é de: {len(string1 + string2)}')
print('================================')
print(len(string1))
print(string1.__len__())