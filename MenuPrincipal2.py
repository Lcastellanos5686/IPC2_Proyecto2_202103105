from tkinter import *
from tkinter.filedialog import*

raiz = Tk()
raiz.title('Menú Principal')
raiz.config()
raiz.resizable(0,0)

FramePrincipal = Frame()
FramePrincipal.pack(side='right')
FramePrincipal.config()
FramePrincipal.config(width='750', height = "450")

LabelTitulo = Label(FramePrincipal, text = 'Menú Principal', font = ("Courier New",15))
LabelTitulo.grid(row = 0, column = 1, pady = 7, padx = 7, sticky = W)

LabelTitulo = Label(FramePrincipal, text = 'Archivo', font = ("Futura MdCn BT",15))
LabelTitulo.grid(row = 1, column = 0, pady = 7, padx = 7, sticky = N)

LabelTitulo = Label(FramePrincipal, text = 'Gestión', font = ("Futura MdCn BT",15))
LabelTitulo.grid(row = 1, column = 1, pady = 7, padx = 7, sticky = N)

LabelTitulo = Label(FramePrincipal, text = 'Ayuda', font = ("Futura MdCn BT",15))
LabelTitulo.grid(row = 1, column = 2, pady = 7, padx = 7, sticky = N)

def Abrir():
    archivo = askopenfilename()
    ##accion

def ElementoQuimico():
    pass


################################

BotonAbrir = Button(FramePrincipal, text = "Abrir...", command=lambda:Abrir())
BotonAbrir.grid(row = '2', column = '0' , pady = "7", padx = "7", sticky = N)
BotonAbrir = Button(FramePrincipal, text = "Generar XML")
BotonAbrir.grid(row = '3', column = '0' , pady = "7", padx = "7", sticky = N)

BotonAbrir = Button(FramePrincipal, text = "Elementos Químicos")
BotonAbrir.grid(row = '2', column = '1' , pady = "7", padx = "7", sticky = N)
BotonAbrir = Button(FramePrincipal, text = "Compuesto")
BotonAbrir.grid(row = '3', column = '1' , pady = "7", padx = "7", sticky = N)
BotonAbrir = Button(FramePrincipal, text = "Máquinas")
BotonAbrir.grid(row = '4', column = '1' , pady = "7", padx = "7", sticky = N)

BotonAbrir = Button(FramePrincipal, text = "Información")
BotonAbrir.grid(row = '2', column = '2' , pady = "7", padx = "7", sticky = N)


raiz.mainloop()