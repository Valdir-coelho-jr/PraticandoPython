
usuario = input('Nome do usuário: ')
senha = input('Senha do usuário: ')

usuario_bd = 'valdircoelho'
senha_bd = 'junior123'

if usuario == usuario_bd and senha == senha_bd:
    print('Usuário logado!')
else:
    print('Usuário ou senha inválidos.')
