import pywhatkit as kit
from tkinter import *
from tkinter import ttk

def abrirMusica ():
    inp = inputtxt.get(1.0, "end-1c")
    kit.playonyt(inp)


janela = Tk()
janela.title("abrir musica no youtuba")
texto = Label(janela, text="Escreva o nome da música e clique no botão para abrir-la no youtube.")
texto.grid(column=0, row=0, padx=10, pady=10)

inputtxt = Text(janela, height=1, width=47)
inputtxt.grid(column=0,row=1,padx=10,pady=10)

botao = Button(janela, text="Abrir Musica no Youtube", command=abrirMusica)
botao.grid(column=0, row=2, padx=10, pady=10)

botao = Button(janela, text="Sair", command=janela.destroy)
botao.grid(column=0, row=3, padx=10, pady=10)


janela.mainloop()