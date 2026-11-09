""" Solicite um número inteiro positivo e faça uma contagem regressiva até zero.

Ao terminar, mostre Lançamento realizado!. """

import os

clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')

clear()

num = int(input('Digite um número inteiro positivo: '))

while num >= 0:
    print(num)
    num -= 1