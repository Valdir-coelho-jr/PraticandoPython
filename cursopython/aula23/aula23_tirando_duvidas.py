"""
* Enumerate - Enumerar elementos da lista # list
"""

lista = [
    ['Rogerio', 'Etemon', 'Dormecocaine'],  # Indice 0
    ['Pão', 'Toninho', 'Jony'],             # Indice 1
    ['Rogerio', 'Veerzinho', 'Lucianos']    # Indice 2
]

for v1 in enumerate(lista):
    valor_enumerado, minha_lista = v1
    nome1, nome2, nome3 = minha_lista
    print(nome1, nome3, nome2)


"""
[ <-- Enumerate

 (0, ['Rogerio', 'Etemon', 'Dormecocaine']),
 (1, ['Pão', 'Toninho', 'Jony']), 
 (2, ['Rogerio', 'Veerzinho', 'Lucianos'])
 
]
"""
