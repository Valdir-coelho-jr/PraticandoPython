#  Só lembrando, Objetos Mutáveis são: Listas, Dicionários e etc.
#  Objetos imutáveis seriam: Tuplas, Strings, Numeros Int e Float, valores Boleanos, None e etc

def lista_de_clientes(clientes_iteravel, lista=None):  # Aqui fica exatamente o problema
    if lista == None:
        lista = []
    lista.extend(clientes_iteravel)
    return lista


clientes1 = lista_de_clientes(['João', 'Rogério', 'Japinha'])
clientes2 = lista_de_clientes(['Jonas', 'Luciano', 'Reginaldo'])
clientes3 = lista_de_clientes(['Fabricio'])

print(clientes1)
print(clientes2)
print(clientes3)
