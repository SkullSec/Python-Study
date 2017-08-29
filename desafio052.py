lista = [num for num in range(1,11)]

#quando se usa o fatiamento, se cria outra lista copiando a lista de referencia
lista2 = lista[:4]

print(lista)
print(lista2)

lista.append(15)
lista2.append(8)

print(lista)
print(lista2)