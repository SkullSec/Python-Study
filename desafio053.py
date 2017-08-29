lista = [num for num in range(1,11)]

#sem o fatiamento o 'lista2' vira uma variavel onde ela se iguala a lista e vice versa
lista2 = lista

print(lista)
print(lista2)

lista.append(15)
lista2.append(8)

print(lista)
print(lista2)