#  d2 = {'chave1':'valor da chave'}

#  d1 = dict(chave1= 'valor da chave1', chave2= 'valor da chave2')
#  d1['nova_chave'] = 'valor da nova chave'

d1 = {
    'str': 'valor string',
    123: 'valor int',
    (1, 2, 3, 4, 5, 6, 7): 'tupla'
}
"""
if 'não existe' not in d1:
    d1['não existe'] = 'agora existe!'
    print(d1['não existe'])

print('Rogério')
"""

d1['nomedachave'] = 'agora existe'

if d1.get('nomedachave'):
    print(d1['nomedachave'])

print('feliz')
