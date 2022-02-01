listanum = []

while True:
    n = int(input('Digite um número'))
    if n not in listanum:
        listanum.append(n)
    else:
        print('Valor duplicado')
    option = ' '
    while option not in 'SN':
        option = input('Deseja continuar [S/N]? ').upper().strip()
    if option == 'N':
        break
listanum.sort()
print(f'Você dgitou os valores {listanum}')

   