#Jogo do ímpar ou par

from random import randint
cont = 0
print('VAMOS JOGAR PAR OU ÍMPAR')
while True:
    n = int(input('Digite um valor: '))
    computador = randint(1, 10)
    result = n + computador
    option = ' '  #Essa estrutura obriga o usuário a digitar 'P' ou 'I'
    while option not in 'PI':
        option = input('Par ou Ímpar [P/I]: ').strip().upper()[0]

    if result % 2 == 0:
        print(f'Você jogou {n} e o computador jogou {computador}. O total foi {result} que deu PAR')
    else:
        print(f'Você jogou {n} e o computador jogou {computador}. O total foi {result} que deu ÍMPAR')

    if option == 'P' and result % 2 == 0:
        print('Você venceu...Vamos jogar novamente')
        cont += 1
    elif option == 'I' and result % 2 == 1:
        print('Você venceu...Vamos jogar novamente')
    else:
        print('Você perdeu')
        break
print(f' FIM DE JOGO Você venceu {cont} vezes')

        