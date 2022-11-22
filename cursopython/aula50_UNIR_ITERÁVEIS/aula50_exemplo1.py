"""
Zip - Unindo iteráveis
Zip_longest - Itertools
"""
from itertools import zip_longest

### Codigo
Cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Monte Belo', 'Outra']

# Codigo
Estados = ['SP', 'MG', 'BA']

cidade_estados = zip_longest(Estados, Cidades, fillvalue='Estado')
print(list(cidade_estados))
