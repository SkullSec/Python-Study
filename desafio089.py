pedido = ['milho','molho', 'catupiry', 'frango']

ingredientes = ['milho', 'tomate', 'catupiry', 'frango']

for elemento in pedido:
    if elemento in ingredientes:
        print('Adicionando ' + elemento + '.')
    else:
        print('Nao temos o ingrediente no momento.')