# Comparação and: É verdadeiro apenas se as duas comparações forem verdadeiras
# (Verdadeiro e Verdadeiro) = Verdadeiro
# (Verdadeiro e   Falso   ) = Falso
# comparacao1 and comparacao2
# =========================== #

print("Comparação AND: Valores iguais")
valor_1 = 5
valor_2 = 3
print(f"Primeiro valor já inserido: {valor_1}")
print(f"Segundo valor já inserido: {valor_2}")
print()
valor_3 = input("Insira o terceiro valor: ")
valor_4 = input("Insira o quarto valor: ")
valor_3 = int(valor_3)
valor_4 = int(valor_4)

if valor_1 == valor_3 and valor_2 == valor_4:
    print("Os dois valores inseridos pelo usuário são iguais aos valores já inseridos pelo programa!")
else:
    print("Um ou dois valores inseridos pelo usuário são diferente dos valores já inseridos pelo programa.")
