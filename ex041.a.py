from datetime import date
ano = int(input('Digite o ano de nascimento'))
idade = date.today().year - ano

if idade <= 9:
    print('Você tem {} anos. Categoria: MIRIM'.format(idade))
elif idade <= 14:
    print('Você tem {} anos. Categoria: INFANTIL'.format(idade))
elif idade <= 19:
    print('Você tem {} anos. Categoria: JÚNIOR'.format(idade))
elif idade <= 25:
    print('Você tem {} anos. Categoria: SÊNIOR'.format(idade))
else:
    print('Você tem {} anos. Categoria: ,MASTER'.format(idade))
    