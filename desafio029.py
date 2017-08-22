carros = ['corolla', 'punto', 'opala', 'civic', 'new fiesta', 'focus', 's10']

comprador = 'comprador'
vendedor = 'vendedor'

print( vendedor.title() + ' diz: \nSeja bem vindo!')
print(comprador.title() + ' diz: \nQuantos carros vocces tem?')
print(vendedor.title() + ' diz: \n' + str(len(carros)) + ' carros')
print(comprador.title() + ' diz: \nQuais sao os carros?')
print(vendedor.title() + ' diz:\n' +  carros[0].title() + ', ' + carros[1].title() + ', ' + carros[2].title()  + '...' )
print('E ainda temos: \n' + carros[3].title() + ', ' + carros[4].title() + ', ' + carros[5].title() + ' e ' + carros[6].title() + '!')
print(comprador.title() + ' diz: \nGostei do ' + carros[5].title() + '! \nQuanto custa?')
print(vendedor.title() + ' diz: \nO valor do ' + carros[5].title() + ' e de 45 mil.')
print(comprador.title() + ' diz: \nHAHAHAHA... esta barato, vou levar!')