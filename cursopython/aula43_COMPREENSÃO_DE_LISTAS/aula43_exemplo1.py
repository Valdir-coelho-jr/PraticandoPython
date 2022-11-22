l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
exemplo1 = [variavel for variavel in l1]

exemplo2 = [v * 2 for v in l1]
exemplo3 = [(v, v2) for v in l1 for v2 in range(3)]

l2 = ['Rogerio', 'Etemon', 'Japinha']
exemplo4 = [v.replace('a', '@').replace('e', '3').upper() for v in l2]

tupla = (
    ('chave', 'valor'),
    ('chave2', 'valor2'),
)

exemplo5 = [(y, x) for x, y in tupla]
exemplo5 = dict(exemplo5)

l3 = list(range(100))
exemplo6 = [v for v in l3 if v % 3 == 0 if v % 8 == 0]

exemplo7 = [v if v % 3 == 0 and v % 8 == 0 else 0 for v in l3]

print(exemplo7)
