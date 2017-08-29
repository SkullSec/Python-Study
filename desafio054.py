frutas = ['morango', 'maca', 'abacate', 'laranja', 'manga']

amigos_fruta = frutas[:]

frutas.append('banana')
amigos_fruta.append('abacaxi')


print('Frutas que eu gosto:')

for fruta in frutas:
    print(fruta)

print('Frutas que meus amigos gostam:')

for amigos in amigos_fruta:
    print(amigos)