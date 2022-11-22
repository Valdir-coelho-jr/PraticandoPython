import sys
import time


def gera():
    variável = 'valor 1'
    yield variável
    variável = 'valor 2'
    yield variável
    variável = 'valor 3'
    yield variável


g = gera()

for v in g:
    print(v)
