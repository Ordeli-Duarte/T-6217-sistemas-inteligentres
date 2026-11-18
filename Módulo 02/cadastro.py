import tkinter as tk
janela = tk.Tk()
janela.title("")
janela.geometry("400x300")

texto = tk.Label(
janela,
text="Digite seu nome",
font=("Brush Script MT", 100),
fg="black" 
)

texto.pack(pady=80)

entrada = tk.Entry(
janela,
width=30
)

entrada.pack(pady=10)

def exibir_mensagem():
    print(f'Texto: {entrada.get()}')

botao = tk.Button(
    janela,
    text= "Clique aqui",
    command= exibir_mensagem
)

janela.mainloop()