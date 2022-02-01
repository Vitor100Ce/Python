
from datetime import date

sexo = int(input('''Informe seu sexo
Digite 1 pra masculino
Digite 2 para feminino'''))

if sexo == 1:
    nascimento = int(input('Digite seu ano de nascimento'))
    ano = date.today().year
    idade = ano - nascimento

    if idade <= 17:
        print('Você tem {} e deve se alistar em {}'.format(idade, ano + (18 - idade)))
    elif idade == 18:
        print('Você tem {} anos! Está na hora de se alistar'.format(idade))
    elif idade > 18:
        print('Você tem {}, já passou da hora de se alistar! O alistamento deveria ter ocorrido em {}'.format(idade, ano -(idade - 18)))
elif sexo == 2:
    print('Não há necessida de se alistar! Obrigado!')





