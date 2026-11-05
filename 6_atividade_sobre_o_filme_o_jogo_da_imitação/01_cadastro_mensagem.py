""" Antes de investigar uma mensagem, a equipe precisa organizar os dados disponíveis.

Recebam pelo teclado:

o nome ou apelido do analista;
a identificação da mensagem, como texto, por exemplo MSG-007;
a quantidade de grupos de símbolos, como inteiro;
o tempo estimado para analisar cada grupo, em minutos, como decimal.
Regras:

A quantidade de grupos e o tempo por grupo devem ser maiores que zero.
Se qualquer um desses valores for inválido, mostrem Dados inválidos e não calculem o tempo total.
Se os dados forem válidos, calculem o tempo total estimado: quantidade de grupos multiplicada pelo tempo por grupo.
Apresentem uma ficha com o analista, a identificação, a quantidade de grupos e o tempo total em minutos.
Se o total for menor ou igual a 60 minutos, mostrem Análise dentro do prazo; caso contrário, mostrem Reorganizar o trabalho.
Para explicar: por que a identificação é texto mesmo quando contém algarismos? Por que é adequado usar float() para o tempo por grupo? """

codinome = input("Qual o seu nome ou apelido? ")
mensagem = input("Digite a identificação da mensagem, como texto: ")
qtd_simbolos = int(input("Quantidade de grupos de símbolos: "))
if qtd_simbolos <= 0:
    print("Esta quantidade de símbolos é inválida.")
    exit()
tempo = float(input("Qual o tempo estimado para analisar cada grupo, em minutos? "))
if tempo <= 0:
    print("Este tempo é inválido.")
    exit()

total = qtd_simbolos / tempo
if total <= 60:
    print("Análise dentro do prazo.")
elif total > 60:
    print("Reorganizar o trabalho.")
print(f"""
=== FICHA ===
Codinome: {codinome}
ID Mensagem: {mensagem}
Quantidade grupos: {qtd_simbolos}
Tempo total: {total:.2f}
""")
# A identificação continua texto pois contém texto no meio ou é para ser lido como um código, não um número em questão.
# É adequado usar float porque pode ser um tempo quebrado, como, por exemplo, um minuto e meio.