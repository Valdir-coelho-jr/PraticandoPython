l1 = list(range(10))

praticando1 = [v for v in l1]

praticando2 = [v * 4 for v in l1]

praticando3 = [(v, v2) for v in l1 for v2 in range(3)]

l2 = ['Etemon', 'Japinha', 'Rogerio']

praticando4 = [v.replace('m', "/\/|").replace('o', '0').replace('a', '4') for v in l2]
print(praticando4)
