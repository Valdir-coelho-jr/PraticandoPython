from formata import preco


def aumento(valor, porcentagem, formata1=False):
    r = valor + (valor * porcentagem / 100)
    if formata1:
        return preco.f_real(r)
    else:
        return r


def reducao(valor, porcentagem, formata1=False):
    r = valor - (valor * porcentagem / 100)
    if formata1:
        return valor.f_real(r)
    else:
        return r
