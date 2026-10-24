""" Intermediário
Uma aplicação possui um sistema simples de autenticação.

Considere as credenciais cadastradas:

usuario_correto = "admin"senha_correta = "python123"
Solicite que a pessoa informe seu usuário e sua senha.

O programa deverá apresentar uma das seguintes mensagens:

Acesso autorizado! — quando ambos estiverem corretos.
Senha incorreta! — quando o usuário estiver correto, mas a senha errada.
Usuário não encontrado! — quando o usuário não existir.
Desafio: Utilize condições aninhadas para verificar primeiro o usuário e depois a senha. """                  

import os
clear = lambda: print("\033[H\033[J", end="")

clear()

usuario_correto = "eu"
senha_correta = "sla"

usuario = input("Digite o usuário: ")
if usuario == usuario_correto:
    senha = input("Digite a senha: ")
    if senha == senha_correta:
        clear()
        print("Acesso autorizado!")
    else:
        clear()
        print("Senha incorreta!")
else:
    clear()
    print("Usuário não encontrado!")
