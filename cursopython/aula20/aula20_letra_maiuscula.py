texto = "Python"
nova_string = ""

# Continue - pula para o proximo laço
# Break - termina o laço

for letra in texto:
    if letra == 't':
        nova_string = nova_string + letra.upper()
    elif letra == "h":
        nova_string = nova_string + letra.upper()
    else:
        nova_string += letra

print(nova_string)
