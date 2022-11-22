"""
lista = [
    ['c1', 1],
    ['c2', 2],
    ['c3', 3],
    ('c4', 4),
]

d1 = dict(lista)

print(d1)
"""

d1 = {
    1: 2,
    2: 3,
    3: 4,
    4: 5,
}

#  d1.pop(4)
#  d1.popitem()

d2 = {
    'a': 'b',
    'c': 'd',
}
d1.update(d2)
print(d1)
