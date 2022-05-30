# importar a biblioteca
from tkinter import*
#back-end
def imprimir():
    print(entry.get())
    label1['text'] = entry1.get()

#front end
#executar a janela


# criar a janela
janela= Tk()
janela.geometry('400x200+100+500')
janela.minsize(width=100, height=50)
janela.maxsize(width=800, height=400)
#janela.config(background='black')

# criar os windgets
label1 = Label (janela, text='Ola mundo!', font='Arial 36')
entry1 = Entry(janela, text='.')
entry2 = Entry(janela, font='Arial 36')
btn1 = Button(janela, text='Sair', font='Arial 36', command=quit)
btn2 = Button(janela, text= 'Imprimir', font='Arial 36', command=imprimir)

# organizar os widgets
label1.pack(side=LEFT)
entry1.pack(side=LEFT)
btn1.pack()
btn2.pack()

#executar a janela
janela.mainloop()