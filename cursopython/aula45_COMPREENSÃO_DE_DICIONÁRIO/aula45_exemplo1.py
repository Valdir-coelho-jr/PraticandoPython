lista = [
    ('chave', 'valor1'),
    ('chave2', 'valor2'),
]

d1 = {x: y for x, y in lista}

d2 = {x: x for x in range(5)}

print(d2)
