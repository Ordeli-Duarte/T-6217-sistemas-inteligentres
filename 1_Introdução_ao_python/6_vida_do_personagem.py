""" Um personagem possui inicialmente:

200 pontos de vida
Durante uma batalha:

recebe 45 de dano
recebe 30 de dano
recupera 20 pontos de vida
Crie uma variável vida e atualize seu valor depois de cada acontecimento.

Mostre somente a quantidade final de vida. """

vida = 200
vida -= 45
vida -= 30
vida += 20
print(f"Quantidade final de vida: {vida}")