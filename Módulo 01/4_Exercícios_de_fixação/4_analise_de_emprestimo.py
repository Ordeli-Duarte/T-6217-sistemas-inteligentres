""" Um banco deseja automatizar a análise inicial de empréstimos.

Solicite as seguintes informações:

Salário mensal do cliente.
Valor solicitado para empréstimo.
Quantidade de parcelas.
O empréstimo só poderá ser aprovado se todas as condições forem atendidas:

O salário deve ser de pelo menos R$ 2.000,00.
O valor solicitado não pode ultrapassar 10 vezes o salário.
O valor de cada parcela não pode ultrapassar 30% do salário.
A quantidade de parcelas deve estar entre 1 e 48.
Caso alguma condição não seja atendida, informe que o empréstimo foi recusado.

Desafio: Apresente o motivo da recusa.

Considere um empréstimo sem juros, apenas para fins de exercício. """

import os
clear = lambda: print("\033[H\033[J", end="")  

clear()

salario = float(input("Digite o salário mensal do cliente: R$ "))
if salario < 2000:
    clear()
    print("Empréstimo recusado! Motivo: Salário inferior a R$ 2.000,00.")
else:
    valor_emprestimo = float(input("Digite o valor solicitado para empréstimo: R$ "))
    if valor_emprestimo > 10 * salario:
        clear()
        print("Empréstimo recusado! Motivo: Valor solicitado ultrapassa 10 vezes o salário.")
    else:
        parcelas = int(input("Digite a quantidade de parcelas: "))
        if parcelas < 1 or parcelas > 48:
            clear()
            print("Empréstimo recusado! Motivo: Quantidade de parcelas inválida.")
        else:
            valor_parcela = valor_emprestimo / parcelas
            if valor_parcela > 0.3 * salario:
                clear()
                print("Empréstimo recusado! Motivo: Valor da parcela ultrapassa 30% do salário.")
            else:
                clear()
                print("Empréstimo aprovado!")
