from time import sleep
from random import randint

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('''Suas opções
[0] PEDRA
[1] PAPEL
[2] TESOURA
''')

jogador = int(input('Qual é a sua jogada?'))
if jogador != 0 and jogador != 1 and jogador !=2:
    print('Opção inválida! Escolha entre 0 e 2')
else:
    print('-='*10)
    print('Computador jogou {}'.format(itens[computador]))
    print('Jogador jogou {}'.format(itens[jogador]))
    print('-='*10)

    sleep(0.3)
    print('JO')
    sleep(0.3)
    print('KEN')
    sleep(0.3)
    print('PÔ')

if computador == 0:

    if jogador == 0:
        print('EMPATE')

    elif jogador == 1:
        print('JOGADOR GANHOU')

    elif jogador == 2:
        print('COMPUTADOR GANHOU')
    
if computador == 1:

    if jogador == 0:
        print('COMPUTADOR GANHOU')

    elif jogador == 1:
        print('EMPATE')

    elif jogador == 2:
        print('JOGADOR GANHOU')

if computador == 2:

    if jogador == 0:
        print('JOGADOR GANHOU')

    elif jogador == 1:
        print('COMPUTADOR GANHOU')

    elif jogador == 2:
        print('EMPATE')