print('-- Calculadora de Soma de numeros inteiros --')
num1 = input('Digite o primeiro numero: ')
num2 = input('Digite o segundo numero: ')
print()
if num1.isdigit() and num2.isdigit():
    num1 = int(num1)
    num2 = int(num2)
    print(num1 + num2)
else:
    print('Não foi possivel realizar a soma')
