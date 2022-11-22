import sys
import time

l1 = [x for x in range(8)]
print(f'Componentes de l1: {l1}')
print(f'l1 = {type(l1)}')
l2 = (x for x in range(8))
print(f'Componentes de l2: {next(l2),next(l2),next(l2),next(l2),next(l2),next(l2),next(l2),next(l2)}')
print(f'l2 no Bruto: {l2}')
print(f'l1 = {type(l2)}')

print()

print(f'l1 é iterável?: {hasattr(l1,"__iter__")}')
print(f'l1 é gerador?: {hasattr(l1,"__next__")}')
print()
print(f'l2 é iterável?: {hasattr(l2,"__iter__")}')
print(f'l2 é gerador?: {hasattr(l2,"__next__")}')

print()
print(f'Valor de l1 na memória: {sys.getsizeof(l1)}')
print(f'Valor de l2 na memória: {sys.getsizeof(l2)}')
