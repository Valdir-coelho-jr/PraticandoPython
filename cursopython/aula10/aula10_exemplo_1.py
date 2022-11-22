"""
Operadores Relacionais
== - Igualdade
 > - Maior que
>= - Maior que ou igual a
 < - Menor que
<= - Menor que ou igual a
!= - Diferente
"""

nome = input("Qual o seu nome? ")
idade = input("Qual a sua idade? ")

idade = int(idade)

# Limite para pegar empréstimo
menor_idade = 20  # Muito jovem
maior_idade = 30  # Muito velho

if menor_idade <= idade <= maior_idade:
    print(f"{nome} pode fazer um empréstimo")
else:
    print(f"{nome} não pode fazer um empréstimo")
