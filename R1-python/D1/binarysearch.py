highside = int(1000)
media = int(0)
lowside = int(0)
resposta = False

input("Pense em um número de 0 a 1000 e dê enter")
while resposta == False:
    media = (highside + lowside) // 2
    ins = input("O numero é  {}? [y/n]".format(media))
    if(ins == 'y'):
        break
    else:

        ins = input("O numero é menor que {}? [y/n]".format(media))
        if(ins == 'y'):
            highside = media
        else:
            lowside = media
