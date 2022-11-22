#  Comparação In e Not In - É verdadeiro se há alguma expressão citada em uma das comparacoes
#  ==================  #

print("Comparacao In e Not In")
nome_inserido = 'Valdir Coelho Junior'
print(f"Nome já inserido: {nome_inserido}")
print("Comparacao IN")
print()
nome = input("Insira um nome: ")

if 'Val' in nome:
    print(f"O nome inserido contem 'Val' que é uma das letras de {nome_inserido}")
else:
    print(f"O nome inserido não contém nenhuma letra do nome de {nome_inserido}")
print("==========================")
print("Comparacao NOT IN")
print()
nome_2 = input("Insira um nome: ")

if 'Jun' not in nome_2:
    print("Este nome não contém 'Jun' no nome, aprovado!")
else:
    print(f"Este nome contém 'Jun' no nome, que já é uma letra do nome de {nome_inserido}")
