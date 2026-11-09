""" O programa abaixo deveria mostrar o nome de um curso, o valor da mensalidade e se a matrícula está ativa, mas contém erros:

nome curso = "Python básico"
mensalidade = 89,90
matricula_ativa = true

print("Curso:", nome_curso)
print("Mensalidade:", Mensalidade)
print("Matrícula ativa:", matricula_ativa)

Reescreva o código corrigindo:

o nome da variável que contém um espaço;
a escrita do número decimal;
a escrita do valor booleano;
a diferença entre maiúsculas e minúsculas no nome da variável.
Para cada correção, escreva um comentário explicando a regra da aula que foi aplicada. Ao final, mostre também type(mensalidade) para verificar se o valor é um float. """

nome_curso = "Python básico" # Corrigido o nome da variável para não conter espaço, usando underscore para separar palavras
mensalidade = 89.90 # Corrigido a escrita do número decimal, usando ponto como separador de casa decimal
matricula_ativa = True # Corrigido a escrita do valor booleano, usando a primeira letra maiúscula

print("Curso:", nome_curso)
print("Mensalidade:", mensalidade)
print("Matrícula ativa:", matricula_ativa)
print("Tipo da mensalidade:", type(mensalidade)) # o resultado será <class 'float'>
