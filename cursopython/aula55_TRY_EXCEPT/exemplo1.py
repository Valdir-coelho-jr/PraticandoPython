# Estudando Try e Catch

try:
    a = {}
    print(a[1])
    try:
        a = 1/10
    except:
        print('Erro')
except NameError as erro:
    print('Erro do desenvolvedor, fale com ele.')
except (IndexError, KeyError) as erro:
    print('Erro de indice ou de chave.')
except Exception as erro:
    print('Ocorreu um erro inesperado')
else:
    pass
finally:
    a = ''
