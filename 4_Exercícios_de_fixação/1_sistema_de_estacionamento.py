""" Um estacionamento precisa calcular o valor cobrado de seus clientes de acordo com o tempo de permanência.

Desenvolva um programa que solicite a quantidade de horas que um veículo permaneceu estacionado.

As regras são:

Tempo de permanência        Valor
Até 2 horas	               R$ 10,00
Mais de 2 até 5 horas      R$ 20,00
Mais de 5 horas	           R$ 30,00

Requisitos:

A quantidade de horas deve ser maior que zero.
Caso seja informado um valor inválido, apresente uma mensagem.
Exiba o valor total a pagar. """

import os
os.system("cls")
clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')
horas = int(input("Digite a quantidade de horas que o veículo permaneceu estacionado: "))

if horas <= 0:
    print("Valor inválido. A quantidade de horas deve ser maior que zero.")
else:
    if horas <= 2:
        valor = 10
    elif horas <= 5:
        valor = 20
    else:
        valor = 30
    clear()
    print(f"O valor total a pagar é: R$ {valor:.2f}")