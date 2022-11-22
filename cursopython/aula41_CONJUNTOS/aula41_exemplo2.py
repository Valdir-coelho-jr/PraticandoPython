s1 = {1, 2, 3, 4, 5, 7}
s2 = {1, 2, 3, 4, 5, 6}
# s3 = s1 | s2
# s3 = s1 & s2
# s3 = s1 - s2
# s3 = s2 - s1 > A ordem altera o resultado
# s3 = s1 ^ s2
# print(s3)

l1 = ['Rogério', 'Japinha', 'Etemon', 'Japinha', ]
l2 = ['Rogério', 'Rogério', 'Rogério', 'Japinha', 'Etemon']

"""
l1 = list(set(l1))
l2 = list(set(l2))

print(l1, l2)
"""

if set(l1) == set(l2):
    print('L1 é igual a L2')
else:
    print('L1 não é igual a L2')
