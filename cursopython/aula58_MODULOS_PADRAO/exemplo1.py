# Módulos padrão do Python:
# Módulos são arquivos .py (que contém código python) e servem para expandir
# as funcionalidades padrão da linguagem.
# Veja todos os módulos padrão do Python em:
# https://docs.python.org/3/py-modindex.html

# from sys import platform as so -> Testando esquema de import e from import para importar uma unica funcao
# print(so)


#  from random import randint as randomic -> Para não preescrever randint com a def randint

#  from random import * -> Para importar tudo

import random  # Para garantir que nada vai ser preescrevida


def randint(*args):
    return 'Hahahaha'


for i in range(10):
    print(random.randint(0, 10))
