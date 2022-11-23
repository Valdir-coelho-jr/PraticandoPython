from vendas.calcula_preco import aumento, reducao
from vendas.formata import preco

from vendas.calcula_preco import aumento, reducao  # -> A maneira mais fácil de reduzir Código


valor = 87.90

preco_aumentado = aumento(valor=valor, porcentagem=21, formata1=True)
print(preco_aumentado)

preco_reduzido = reducao(valor=valor, porcentagem=17, formata1=True)
print(preco_reduzido)


###  NÃO ESTÁ FUNCIONANDO E EU NÃO SEI PORQUE



