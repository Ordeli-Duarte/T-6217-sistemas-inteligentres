import tkinter as tk
janela = tk.Tk()
janela.title("Contador de Cliques")
janela.geometry("400x300")


rotulo = tk.Label(
janela,
text="Clique no butaum",
font=("Brush Script MT", 50),
fg="blue" 
)

rotulo.pack(pady=10)

cliques = 0
def clicar():
    global cliques
    cliques += 1
    rotulo.config(text=f"Qtd. de cliques : {cliques}")

botao = tk.Button(
    janela,
    text="clique-me",
    command=clicar
)

botao.pack(pady=5)

janela.mainloop()