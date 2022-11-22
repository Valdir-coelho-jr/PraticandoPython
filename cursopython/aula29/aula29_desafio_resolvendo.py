cpf = 16899535009
_str = cpf.__str__()
lista = list(_str)

n1, n2, n3, n4, n5, n6, n7, n8, n9, *_ = lista
lista = n1, n2, n3, n4, n5, n6, n7, n8, n9

total1 = 0

for v1, v2 in enumerate(lista):
    v2 = int(v2)
    v3 = 10 - v1
    print(f'{v2} * {v3} = {v2 * v3}')
    acumulo = v2 * v3
    total1 += acumulo

print('================================================')
print(f'Soma de todas as multiplicações: {total1}')

digit1 = len(_str) - (total1 % (len(_str)))
if digit1 > 9:
    digit1 = 0
print(f'Digito 1 = {digit1}')
print('================================================')

lista2 = list(_str)
n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, *_ = lista2
lista2 = n1, n2, n3, n4, n5, n6, n7, n8, n9, digit1
total2 = 0

for v1, v2 in enumerate(lista2):
    v2 = int(v2)
    v3 = 11 - v1
    if v3 >= 2:
        print(f'{v2} * {v3} = {v2 * v3}')
    acumulo = v2 * v3
    total2 = total2 + acumulo

print('================================================')
print(f'Soma de todas as multiplicações: {total2}')

digit2 = len(_str) - (total2 % (len(_str)))

print(f'Digito 2 = {digit2}')
print('================================================')

novo_cpf = ''
for n1 in cpf.__str__():
    if len(novo_cpf) <= 8:
        novo_cpf += n1
    else:
        novo_cpf += digit1.__str__()
        novo_cpf += digit2.__str__()
        break

if int(novo_cpf) == cpf:
    print('CPF VALIDADO COM SUCESSO!')
else:
    print('CPF INVALIDO!!!!!')
