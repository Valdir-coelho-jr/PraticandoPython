from dados import pessoas, produtos, lista

# nova_lista = filter(lambda x: x > 5, lista)  # Normal
# nova_lista = [x for x in lista if x > 5]  # LIST COMPREHENSION
# print(list(nova_lista))

"""
def filtra(produto):
    if produto['preco'] > 50:
        produto ['e_caro'] = True  # Não é correto, isso é imbutir uma função map junto do filter
        return True


nova_lista = filter(filtra, produtos)

for produto in nova_lista:
    print(produto)
"""


def maior_idade(pessoa):
    if pessoa['idade'] >= 18:
        return True


nova_lista = filter(maior_idade, pessoas)

for pessoa in nova_lista:
    print(pessoa)
