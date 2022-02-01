velocidade = int(input('Digite a velocidade'))

multa = (velocidade - 80) * 7

if velocidade <= 80:
    print('Está dentro da velocidade permitidade, tenha um bom dia')
else:
    print('Está acima da velocidade, deverá pagar uma multa de {:.2f}'.format(multa))