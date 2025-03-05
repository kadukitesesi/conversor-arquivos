from tkinter import *

janela = Tk()
janela.title("Conversor de arquivos")
janela.geometry("400x400")

texto = Label(janela,text="Clique aqui para selecionar um arquivo")
texto.grid(column=3, row=0, padx=10, pady=10)

botao = Button(janela, text="Selecionar arquivos")
botao.grid(column=3, row=1, padx=10, pady=10)

texto_resposta = Label(janela, text="")
texto_resposta.grid(column=0, row=2, padx=10, pady=10)


janela.mainloop()