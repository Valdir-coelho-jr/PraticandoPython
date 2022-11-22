#  Comparação NOT: O operador NOT precisa apenas de uma expressão.
#  Ele é Verdadeiro se a expressão for Falsa, sendo assim um INVERSOR
#  Falso = Verdadeiro
#  if not comparacao1
# =========================== #

print("Comparação NOT: Tem que ser falso para ser verdadeiro")

valor_1 = ''

valor_1 = input("Insira um valor numérico: ")
print(f"O Valor inserido na memória é: {valor_1}")

if not valor_1:
    print("Não há nenhum valor preenchido, tente novamente.")