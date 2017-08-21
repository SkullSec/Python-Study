linguagens = ['python', 'java', 'c#', 'c', 'c++', 'assembly']

print(linguagens)
#017
pop = linguagens.pop()


print(pop.title() + ' eh uma linguagem de baixo nivel')

#018
print(linguagens)

pop2 = linguagens.pop(0)


print(pop2.title() + ' eh uma linguagem de alto nivel e de facil aprendizado')

#019

''' O del se usa quando simplesmente deseja excluir um elemento da lista, e o pop se usa quando deseja deletar o elemento
da lista e utiliza-lo depois.'''
