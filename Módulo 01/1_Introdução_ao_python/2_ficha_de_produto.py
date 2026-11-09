""" Crie variáveis que representem um produto:

nome
preço
quantidade em estoque
disponível
Depois mostre todas as informações na tela.

Utilize tipos de dados adequados para cada informação """

nome_produto = "Notebook"
preco = 3500.00
quantidade_estoque = 10
disponivel = True

print(f"""
  ===== FICHA DE PRODUTO =====
  Nome: {nome_produto}
  Preço: R${preco:.2f}
  Quantidade em estoque: {quantidade_estoque}
  Disponível: {disponivel}
""")
