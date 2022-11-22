"""
For in em Python
Iterando strings com for
Função range(start=0, stop, step=1)
"""

for n in range(0, 100, 8):
    print(n)

print("===========================")

for n in range(100):
    if n % 8 == 0:
        print(n)