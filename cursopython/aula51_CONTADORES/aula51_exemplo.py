"""
count - Itertools
"""
from itertools import count

contador = count(start=2, step=0.02)

for valor in contador:
    print(round(valor, 2))

    if valor >= 10:
        break
