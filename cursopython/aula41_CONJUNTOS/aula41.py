# add (adiciona), update (atualiza), clear, discard
# union | (une)
# intersection & (todos os elementos presentes nos dois sets)
# difference - (elementos apenas no set da esquerda)
# symmetric_difference ^ (Elementos que estão nos dois sets, mas não em ambos)

s1 = set()
s1.add(1)
s1.add(2)
print(s1)
s1.discard(2)
print(s1)

print()

s1.update('Rogério')
print(s1)