import copy

d1 = {1: 'a', 2: 'b', 3: 'c', 'd': ['Rogério', 'Etemon']}
v = copy.deepcopy(d1)

v[1] = 'JAPINHA'

v['d'][0] = 'GUITARHERO'

print(v)
print(d1)
