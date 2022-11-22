carrinho = []

carrinho.append(('Produto 1', 30))
carrinho.append(('Produto 2', 20))
carrinho.append(('Produto 3', 50))

total = []
produto = [(p, total.append(p[1])) for p in carrinho]

print(sum(total))
