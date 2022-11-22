Lista = [
    ['P1', 14],
    ['P2', 4],
    ['P3', 7],
    ['P4', 8],
    ['P5', 2],

]

# Lista.sort(key=lambda item: item[1])
print(sorted(Lista, key=lambda i: i[1], reverse=True))
