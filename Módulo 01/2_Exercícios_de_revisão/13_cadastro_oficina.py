"""
Uma escola oferece uma oficina de robótica. Crie variáveis para armazenar:

nome da oficina: "Robótica para iniciantes";
sala: "Laboratório 2";
quantidade de vagas: 24;
duração em horas: 2.5;
inscrições abertas: True.
Mostre uma ficha com um título e uma informação por linha. Em seguida, mostre o tipo de cada variável com type() e escreva comentários explicando o que str, int, float e bool representam nesse cadastro.
"""

nome_da_oficina = "Robótica para iniciantes"
sala = "Laboratório 2"
quantidade_de_vagas = 24
duração_em_horas = 2.5
inscrições_abertas = True

print(f"""
======= ficha de cadastro =======
Oficina: {nome_da_oficina}
Sala: {sala}
Quantidade de vagas: {quantidade_de_vagas}
Duração em horas: {duração_em_horas}
Inscrições abertas: {inscrições_abertas}

======= tipos de dados =======
Oficina: {type(nome_da_oficina)}
Sala: {type(sala)}
Quantidade de vagas: {type(quantidade_de_vagas)}
Duração em horas: {type(duração_em_horas)}
Inscrições abertas: {type(inscrições_abertas)}
""")

# str: representa uma sequência de caracteres, usado para armazenar textos.
# int: representa um número inteiro, usado para armazenar valores numéricos sem casas decimais.
# float: representa um número, usado para armazenar valores numéricos com casas decimais.
# bool: representa um valor booleano, usado para armazenar dois tipos de valores (True ou False).1