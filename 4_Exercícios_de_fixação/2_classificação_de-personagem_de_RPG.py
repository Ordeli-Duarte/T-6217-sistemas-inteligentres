""" Um jogo de RPG classifica seus aventureiros de acordo com o nível alcançado.

Solicite o nome e o nível de um personagem e determine sua classificação:

Nível	Classificação
1 a 5	Aprendiz
6 a 15	Guerreiro
16 a 30	Veterano
31 ou superior	Lendário
Requisitos:

Não permita níveis menores que 1.
Mostre o nome do personagem e sua classificação.
Utilize if, elif e else. """

import os
clear = lambda: print("\033[H\033[J", end="")
clear()

nome = input("Digite o nome do personagem: ")
nivel = int(input("Digite o nível do personagem: "))

if nivel < 1:
    print("Nível inválido. O nível deve ser maior ou igual a 1.")
else:
    if 1 <= nivel <= 5:
        classificacao = "Aprendiz"
    elif 6 <= nivel <= 15:
        classificacao = "Guerreiro"
    elif 16 <= nivel <= 30:
        classificacao = "Veterano"
    else:
        classificacao = "Lendário"
    clear()
    print(f"Personagem: {nome}")
    print(f"Classificação: {classificacao}")