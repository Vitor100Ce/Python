from datetime import date
ano = int(input('Digite o ano. Digite 0 se quiser mostrar o ano atual'))

if ano == 0:
    ano = date.today().year

if ano % 400 == 0 and ano % 100 == 0:
    print('O ano {} é bissexto'.format(ano))
else:
    print('O ano {} não é bissexto'.format(ano))