""" Solicite um número inteiro positivo e apresente todos os números de 1 até o valor informado.

Exemplo:

Digite um número: 5

1
2
3
4
5 """

import os

clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')

while True:

    clear()
    numero = int(input("Digite um número inteiro positivo: "))
    if numero <= 0:
        print("Por favor, digite um número inteiro positivo.")
    else:
        numero_atual = 1
        while numero_atual <= numero:
            clear()
            print(numero_atual)
            numero_atual += 1
            input("Pressione Enter para continuar...")
        
    break
    print("Entrada inválida. Por favor, digite um número inteiro.")