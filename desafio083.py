idade = 12


if idade < 4:
    price = 0
elif idade < 18:
    price = 5
elif idade <65:
    price = 10
elif idade >= 65:
    price = 5

print("Seu valor de admissao eh RS$" + str(price))