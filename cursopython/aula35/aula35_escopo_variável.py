variavel = 'valor'


def func():
    print(variavel)


"""
def func2():
    global variavel
    variavel = 'etemon'
    print(variavel)
"""


def func3(arg=None):
    arg = arg.replace('v', 'c')
    return arg


func()
outra_variavel = func3(arg=variavel)

print(outra_variavel)
