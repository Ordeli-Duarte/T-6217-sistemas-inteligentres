""" Crie um personagem contendo pelo menos:

nome
classe
nivel
vida
ataque
defesa
possui_magia
Depois calcule uma variável:

poder_total
utilizando:

ataque + defesa
Mostre uma ficha organizada no terminal.

Exemplo de formato:

========================
      PERSONAGEM
========================
Nome:
Classe:
Nível:
Vida:
Ataque:
Defesa:
Poder Total:
Possui magia:
======================== """

nome = "Arthas"
classe = "Cavaleiro"
nivel = 10
vida = 100
ataque = 20
defesa = 15
possui_magia = True
poder_total = ataque + defesa

print(f"""
========================
      PERSONAGEM
========================
Nome: {nome}
Classe: {classe}
Nível: {nivel}
Vida: {vida}
Ataque: {ataque}
Defesa: {defesa}
Poder Total: {poder_total}
Possui magia: {possui_magia}
======================== """)