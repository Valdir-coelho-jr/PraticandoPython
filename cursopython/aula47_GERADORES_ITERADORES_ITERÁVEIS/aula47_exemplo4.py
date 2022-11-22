import sys
import time

l1 = [x for x in range(100000)]
print(f'l1 = {type(l1)}')
l2 = (x for x in range(100000))
print(f'l2 = {type(l2)}')

print()

print('Diferença entre uma lista normal e um gerador')
print(f'Tamanho de l1 (Lista) na memória: {sys.getsizeof(l1)}')
print(f'Tamanho de l2 (Gerador) na memória: {sys.getsizeof(l2)}')
