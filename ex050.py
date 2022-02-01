
result = 0
cont = 0

for cont_n in range(0,6):
    num = int(input('Digite um número '))
    if num % 2 == 0:
        result = result + num
        cont += 1
print('Você digitou {} PARES e a soma deles é {}'.format(cont,result))