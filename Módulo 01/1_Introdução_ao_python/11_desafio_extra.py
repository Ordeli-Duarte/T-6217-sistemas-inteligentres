""" Sem utilizar nenhum recurso além do que foi visto na aula, crie um pequeno sistema representando um personagem de RPG.

O personagem deve possuir:

nome
vida
ouro
nivel
Durante a aventura:

ganha ouro
recebe dano
gasta ouro
recupera vida
sobe de nível
Cada acontecimento deve alterar a variável correspondente.

No final, apresente o estado atualizado do personagem. """

nome = "gih"
vida = 100
ouro = 50
nivel = 1

ganha_ouro = 20
vida -= 30
ouro += ganha_ouro  
gasta_ouro = 10
ouro -= gasta_ouro
recupera_vida = 15
vida += recupera_vida
nivel += 1

print(f"""
========================
        PERSONAGEM
========================
Nome: {nome}
Vida: {vida}
Ouro: {ouro}
Nível: {nivel}
======================== """)