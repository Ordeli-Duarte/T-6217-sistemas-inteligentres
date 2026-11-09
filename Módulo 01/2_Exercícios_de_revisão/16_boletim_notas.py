# Um aluno recebeu as notas 7.5, 8.0 e 9.5 em três atividades de mesmo peso.

# Guarde o nome do aluno e cada nota em variáveis separadas.
# Calcule a soma das notas em uma variável soma_notas.
# Calcule a média dividindo a soma pela quantidade de atividades.
# Mostre o nome, as três notas e a média.
# Troque apenas a segunda nota por 6.5 no código e execute novamente.
# O programa deve recalcular a média a partir das variáveis. Não escreva a média pronta no código. Não é necessário informar aprovação ou reprovação.

nome_aluno = "João"
nota1 = 7.5 
nota2 = 8.0
nota3 = 9.5
soma_notas = nota1 + nota2 + nota3
media = soma_notas / 3

print(f"""O aluno {nome_aluno} obteve as seguintes notas: {nota1}, {nota2} e {nota3}. A média das notas é: {media}""")

nota2 = 6.5
soma_notas = nota1 + nota2 + nota3
media = soma_notas / 3

print(f"""O aluno {nome_aluno} obteve as seguintes notas: {nota1}, {nota2} e {nota3}. A média das notas é: {media}""")
