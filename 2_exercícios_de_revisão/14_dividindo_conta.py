""" Quatro amigos compraram uma pizza de R$ 48.00 e uma bebida de R$ 12.00. A conta será dividida igualmente.

Crie variáveis para o preço da pizza, o preço da bebida e a quantidade de amigos.
Calcule o total da conta em uma nova variável.
Calcule quanto cada amigo deverá pagar.
Mostre o total e o valor por pessoa com descrições.
Use type() para mostrar o tipo do valor por pessoa.
Para pensar: o resultado da divisão é um int ou um float, mesmo quando não há centavos? """

pizza = 48.00
bebida = 12.00
quantidade_de_amigos = 4
total_da_conta = pizza + bebida
valor_por_pessoa = total_da_conta / quantidade_de_amigos

print(f"""
Total da conta: R$ {total_da_conta:.2f}
valor por pessoa: R$ {valor_por_pessoa:.2f}
Tipo do valor por pessoa: {type(valor_por_pessoa)}
""")
