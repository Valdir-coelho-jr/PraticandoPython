#       Índices
#       0123456789.......................33
frase = "o rato roeu a roupa do rei de roma"  # Iterável
tamanho_frase = len(frase)
contador = 0
nova_string = ''

input_usuario = input('Digite a letra que vai ficar maiúscula: ')

# Iteração <- Iterar
while contador < tamanho_frase:
    letra = frase[contador]
    if letra == input_usuario:
        nova_string += input_usuario.upper()
    else:
        nova_string += letra
    contador += 1
