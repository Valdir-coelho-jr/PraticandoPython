carrinho = [
    ('Produto 1', 50.20),
    ('Produto 2', 78.50),
    ('Produto 3', 84),
]

lista = sum([float(y) for x, y in carrinho])

print(f'Valor total no carrinho: R${lista}')
