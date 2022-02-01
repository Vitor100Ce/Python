"""Detector de Palíndromo"""

text = str(input('Digite uma frase')).strip().upper().replace(" ","")
inverso = text[::-1].replace(" ","").upper()

print('O inverso de {} é {}'.format(text,inverso))

if text == inverso:
    print('É palídromo')
else:
    print('Não é palíndromo')

