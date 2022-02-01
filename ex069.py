#Cadastrar pessoas

cont_18 = 0
cont_m = 0
cont_idadef = 0

while True:
    idade = int(input('Idade'))
    if idade > 18:
        cont_18 += 1
    sexo = ' ' #Essa estrutura obriga o usuário a digitar o que está sendo pedido abaixo
    while sexo not in 'MF':
        sexo = input('Sexo [M/F]: ').strip().upper()
        if sexo == 'M':
            cont_m += 1
        elif sexo == 'F' and idade < 20:
            cont_idadef += 1
    option =  ' ' #Essa estrutura obriga o usuário a digitar o que está sendo pedido abaixo
    while option not in 'SN':
        option = input('Quer continuar? [S/N]: ').strip().upper()   
    if option == 'N':
        break

print(f'''O total de pessoas com mais de 18 anos: {cont_18}
Ao todo temos {cont_m} homens cadastrados
E temos {cont_idadef} mulheres com menos de 20 anos''')