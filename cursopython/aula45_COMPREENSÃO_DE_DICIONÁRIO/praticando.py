lista = [
    ('Chave1', ' valor1'),
    ('chave2', 'valor2'),
]

v1 = {x: y for x, y in lista}

print(v1)

v2 = {x: x for x in range(7)}
print(v2)
