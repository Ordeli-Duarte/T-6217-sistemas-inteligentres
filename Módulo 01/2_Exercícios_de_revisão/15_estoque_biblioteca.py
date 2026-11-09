# A biblioteca começa o dia com 40 livros disponíveis. Nesta ordem:

# recebe 12 livros novos;
# empresta 9 livros;
# recebe a devolução de 4 livros;
# empresta mais 6 livros.
# Crie uma variável livros_disponiveis e atualize essa mesma variável após cada acontecimento. Mostre a quantidade inicial e a quantidade após cada atualização, identificando a etapa.

# Antes de executar, anote em comentários suas previsões para cada etapa. Compare com o resultado do programa.

biblioteca = 40
recebe = 0
empresta = 0
devolução = 0
livros_disponiveis = biblioteca + recebe + empresta + devolução

print(f"""a quantidade de livros disponiveis é: {livros_disponiveis}""")


recebe = 12
livros_disponiveis = biblioteca + recebe + empresta + devolução
print(f"""a quantidade de livros disponiveis é: {livros_disponiveis}""")

empresta = -9
livros_disponiveis = biblioteca + recebe + empresta + devolução
print(f"""a quantidade de livros disponiveis é: {livros_disponiveis}""")

devolução = 4
livros_disponiveis = biblioteca + recebe + empresta + devolução
print(f"""a quantidade de livros disponiveis é: {livros_disponiveis}""")

empresta = empresta + (-6)
livros_disponiveis = biblioteca + recebe + empresta + devolução
print(f"""a quantidade de livros disponiveis é: {livros_disponiveis}""")

