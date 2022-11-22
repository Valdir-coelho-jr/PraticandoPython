"""
Um iterador sempre será uma iterável
"""

import sys
import time


def gera():
    for n in range(100):
        yield n
        time.sleep(0.1)


g = gera()

print(hasattr(g, '__next__'))
print(hasattr(g, '__iter__'))
