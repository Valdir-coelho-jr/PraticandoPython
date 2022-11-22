encontra_duple = [1, 2, 3, 4, 5, 6, 7]

numeros_checados = set(encontra_duple)
primeiro_duplicado = -1

for numero in encontra_duple:
    if numero in numeros_checados:
        primeiro_duplicado = numero
        break

    numeros_checados.add(numero)

    print(primeiro_duplicado)
