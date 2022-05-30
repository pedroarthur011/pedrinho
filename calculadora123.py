#importar a biblioteca
from tkinter import *

#back-end
def imprimir():
    label1['text'] = float(entry1.get()) + float(entry2.get())

#front-end
#criar a janela
janela = Tk()
fn = 'Arial 26'

#criar os widgets
label1 = label(janela, text= 'Olá mundo!', font= 'Arial 36')
entry1 = Entry(janela, font=fn)
entry2 = Entry(janela, font=fn)
btn1 = Button(janela, text= 'soma', font=fn, command=soma)

#organizar os widgets
label1.pack()
entry1.pack()
btn1.pack()


#executar a janela
janela.mainloop()