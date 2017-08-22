mesa = ['mustaine', 'hetfield', 'anselmo']

nao_pagou = mesa.pop()

print(nao_pagou.title() + ' nao pagou a conta e sera expulso!')

convidado = 'belladonna'

mesa.append(convidado)

print('-Deseja se juntar a nos, ' + convidado.title() + '? \n-Claro que sim!')


print(mesa[0].title() + ' e ' + mesa[1].title() + ' curtiram na companhia de ' + mesa[2].title() + '!')