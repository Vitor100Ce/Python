n = int(input('Digite um número'))
base = int(input('''Para conversão, escolha uma das opções abaixo: 
1 para binário, 
2 para octal
3 para hexadecimal'''))

if base == 1:
    binary = bin(n)[2:]
    print('{} em binário é {}'.format(n,binary))
elif base == 2:
    octal = oct(n)[2:]
    print('{} em octal é {}'.format(n,octal))
elif base == 3:
    hexa = hex(n)[2:]
    print('{} em hexadecimal é {}'.format(n,hexa))
else:
    print('Digite a opção correta')


