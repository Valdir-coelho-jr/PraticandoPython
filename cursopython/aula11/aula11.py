usuário = input("Digite seu usuário: ")

qtde_caracteres = len(usuário)

print(usuário, qtde_caracteres, type(qtde_caracteres))

if qtde_caracteres < 6:
    print("Você precisa digitar pelo menos 6 caracteres para se cadastrar no sistema.")
else:
    print('Você foi cadastrado no sistema.')
