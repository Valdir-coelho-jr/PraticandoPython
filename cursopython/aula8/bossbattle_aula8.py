"""
* Criar variáveis para nome (str), idade (int),
* altura (float) e peso (float) de uma pessoa
* Criar variável com o ano atual (int)
* Obter o ano de nascimento da pessoa (baseado na idade e no ano atual)
* Obter o imc da pessoa com 2 casas decimais (peso e na altura da pessoa)
* Exibir um texto com todos os valores na tela usando F-Strings (com as chaves)
"""

nome = 'Valdir'
idade = 28
altura = 1.83
peso = 79
data_atual = 2022
data_nascimento = data_atual - idade
imc = peso / (altura ** 2)

print(f'Seu nome é {nome} e sua idade é de {idade} anos.')
print(f'{nome} tem {altura} cm de altura e pesa {peso} quilos.')
print(f'O imc de {nome} é de {imc:.2f}')
print(f'{nome} nasceu em {data_nascimento}')

print('- Forma de cadastro -')

print(f'Nome: {nome}')
print(f'Idade: {idade} anos')
print(f'Altura: {altura} cm')
print(f'Peso: {peso} kg')
print(f'IMC: {imc:.2f}')
print(f'Ano de nascimento: {data_nascimento}')
