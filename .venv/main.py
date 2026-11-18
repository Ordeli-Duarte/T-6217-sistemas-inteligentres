#IMPORTE A BIBLIOTECA TKINTER COM O APELIDO DE 'TK' depois de "as" pode ser nomeado a sua escolha mas foi nomeado "tk" para facilitar o entendimento
import tkinter as tk

#A função "Tk()" vem pronta da biblioteca tkinter cria a janela principal do nosso programa
janela = tk.Tk()

"janela.title()" #Função do tkinter para dar nome a essa janela
janela.title("Minha primeira aplicação") # nome da janela

"janela.geometry(tamanho)" #Função do tkinter para dar tamanho à janela, em pixels
janela.geometry("400x300")

# vamos criar um componente de texto
texto = tk.Label(
janela, # em que tela que ele aparece
text="test", # qual o texto
font=("Brush Script MT", 100), # qual a fonte do texto e o tamanho
fg="black" # qual a cor do texto
)

# altera o local de apresentação do texto na janela
texto.pack(pady=80)

# cria um componente que permite digitar texto
entrada = tk.Entry(
janela, # em qual tela ele vai
width=30
)

entrada.pack(pady=10) # cria um componente que permite a entrada de um texto

def exibir_mensagem():
    print(f'Texto: {entrada.get()}')

botao = tk.Button(
    janela,
    text= "Clique aqui",
    command= exibir_mensagem
)

janela.mainloop() # é uma função que mantém a nossa aplicação em execução, aguardando alguma ação nossa.