# Leia vários números inteiros e mostre a quantidade de número digitados, a média e o maior e o menor valor
resp = 'S'
cont = 0
total = 0
lts_idades = []


while resp == 'S':
    n = int(input('Digite um número: '))
    cont += 1
    total += n
    media = total / cont
    lts_idades += [n]

    resp = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
print('Você digitou {} e a media foi {:.2f}'.format(cont, media))

#maior e menor número
maior = max(lts_idades)
menor = min(lts_idades)
print('O maior valor digitado foi {} e o menor {}'.format(maior, menor))
