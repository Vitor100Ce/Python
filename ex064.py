#

n = 0
cont = 0
total = 0

n = int(input('Digite um número [999 para parar] '))

while n != 999:
    cont += 1
    total = total + n
    n = int(input('Digite um número [999 para parar] '))
print('Você digitou {} números e a soma entre eles é {}'.format(cont, total))


