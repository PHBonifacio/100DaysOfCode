import random
import sys
leitura = " "

while True :
    leitura = input("Rolar o dado?[y/n]")

    if (leitura == "y" or leitura == "Y"):
        dado = random.randrange(1, 6, 1)
        print("Valor sorteado: %d", dado)
    else:
        sys.exit(0)
