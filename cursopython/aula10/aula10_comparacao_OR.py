# Comparação OR: É verdadeiro se qualquer uma das duas comparações retornar verdadeiro
# Verdadeiro OU Verdadeiro = Verdadeiro
# Verdadeiro OU Falso      = Verdadeiro
#      comp1 or comp2
# =========================== #

valor_1 = 'A'
valor_2 = 'B'

print("Comparação OR: Uma letra correta")
print(f"Primeira letra correta: {valor_1}")
print(f"Segunda letra correta: {valor_2}")


valor_A = input("Digite a primeira letra: ")
valor_B = input("Digite a segunda letra: ")

if valor_1 == valor_A or valor_2 == valor_B:
    print("Aprovado!")
else:
    print("Reprovado, tente novamente.")