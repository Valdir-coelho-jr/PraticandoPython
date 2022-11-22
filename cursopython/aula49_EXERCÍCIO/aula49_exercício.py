
carrinho = []

carrinho.append(('Produto 1', 30))
carrinho.append(('Produto 2', 20))
carrinho.append(('Produto 3', 50))

total = 0

for produto in carrinho:
    total += produto[1]

print(total)

#  Segunda maneira, porém ainda ineficiente

print()

total2 = []

for produto in carrinho:
    total2.append(produto[1])

print(sum(total2))
