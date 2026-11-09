""" Peça o nome, a cidade e a idade da pessoa. Mostre uma ficha e calcule quantos anos ela terá no próximo aniversário. """

import os

clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')

clear()

nome = input("Digite seu nome: ")
cidade = input("Digite sua cidade: ")
idade = int(input("Digite sua idade: "))
idade_proximo_aniversario = idade + 1

clear()

print("====== cadastro ======")
print(f"Nome: {nome}")
print(f"Cidade: {cidade}")
print(f"Idade atual: {idade}")
print(f"Idade no próximo aniversário: {idade_proximo_aniversario}")