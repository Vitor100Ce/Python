#Caixa eletrônico - Cédulas de 50, 20, 10 e 1


valor = int(input('Qual o valor que deseja sacar?'))
ced = 50
totced = 0

while True:
    if valor >= ced:
        valor -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R${ced}')
        if ced == 50:
           ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if valor == 0:
            break


