zenit, polar = 'zenit', 'polar'
mensagem_final = ''
mensagem = input('Digite a frase: ')
n = 0
for i in range(len(mensagem)):
    x = mensagem[n]
    if x in zenit:
        x = int(zenit.find(mensagem[n]))
        mensagem_final += polar[x]
    elif x in polar:
        x = int(polar.find(mensagem[n]))
        mensagem_final += zenit[x]
    else:
        mensagem_final += mensagem[n]
    n += 1

print(mensagem_final)