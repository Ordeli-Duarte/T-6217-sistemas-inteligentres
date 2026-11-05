""" Solicite quantos alunos existem em uma turma.

Em seguida, leia a nota de cada aluno e calcule a média geral.

A quantidade de alunos deve ser maior que zero. """

import os

clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')

clear()

quantidade_alunos = int(input("Digite a quantidade de alunos: "))
contador = 1
soma = 0

if quantidade_alunos < 1:
    print("a quantidade deve ser maior que zero")
else:  
    while contador <= quantidade_alunos:
        nota = float(input(f"Digite a nota do {contador}º aluno: "))    
        soma = soma = nota
        contador += 1
    print(f"Nota total: {soma / quantidade_alunos}")