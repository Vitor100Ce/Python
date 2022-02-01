#Programa que lê dois números e tem um menu para ação desses valores

import time

n1 = int(input('Digite o primeiro valor'))
n2 = int(input('Digite o segundo valor'))
menu = 0
while menu != 5:
    menu = int(input("""
    Escolha uma das opções abaixo
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa

    """))

    if menu == 1:
        print('O resultado da soma de {} + {} é = {}'.format(n1, n2, n1+n2))
    elif menu == 2:
        print('O resultado da multiplicação de {} x {} é = {}'.format(n1, n2, n1*n2))
    elif menu == 3:
            if n1 > n2:
                print('Entre {} e {} o maior valor foi {}'.format(n1, n2, n1))
            elif n1 < n2:
                print('Entre {} e {} o maior valor foi {}'.format(n1, n2, n2))
            elif n1 == n2:
                print('Os valores {} e {} são iguais!'.format(n1, n2))
    elif menu == 4:
        print('Digite os valores novamente')
        n1 = int(input('Digite o primeiro valor'))
        n2 = int(input('Digite o segundo valor'))
    else:
        print('Opção errada, escolha entre 1 e 5')

print('Finalizando o programa')
time.sleep(.5)
print('...')
time.sleep(.5)
print('Finalizado')
