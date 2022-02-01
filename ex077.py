
palavras = ('Teste', 'Ola', 'Programar', 'Ofuscar', 'Computador')

for c in palavras:
    print(f'|\nA palavra {c} temos as vogais', end=' ')
for letra in c:
    if letra.lower() in 'aeiou':
        print(letra, end=' ')
