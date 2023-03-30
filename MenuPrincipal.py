from tkinter import *
from tkinter.filedialog import*
import subprocess
import tkinter.messagebox

raiz = Tk()
raiz.title('Menu Principal')
raiz.config()
raiz.resizable(0,0)

FramePrincipal = Frame()
FramePrincipal.pack(side='right')
FramePrincipal.config()
FramePrincipal.config(width='750', height = "450")

CuadroTextoGrande=Text(FramePrincipal, height='20', width='70') ##Cuadro de texto grande, necesita scroll
CuadroTextoGrande.grid(row = '5', column = '0' , pady = "7", padx = "7",columnspan=3)

ScrollV= Scrollbar(FramePrincipal, command=CuadroTextoGrande.yview) ##barra de scroll, el command indica a quien va  a escrolear
ScrollV.grid(row = '5', column = '4' , pady = "7", sticky = 'nwse')
CuadroTextoGrande.config(yscrollcommand=ScrollV.set) ##corrige comportamiento del scroll

LabelTitulo = Label(FramePrincipal, text = 'Menu Principal', font = ("Courier New",15))
LabelArchivo = Label(FramePrincipal, text = 'Archivo', font = ("Century Gothic",10))
LabelEditar = Label(FramePrincipal, text = 'Editar', font = ("Century Gothic",10))
LabelAyuda = Label(FramePrincipal, text = 'Ayuda', font = ("Century Gothic",10))

LabelTitulo.grid(row = 0, column = 1, pady = 7, padx = 7, sticky = W)
LabelArchivo.grid(row = 1, column = 0, pady = 7, padx = 7, sticky = W)
LabelEditar.grid(row = 1, column = 1, pady = 7, padx = 7, sticky = S)
LabelAyuda.grid(row = 1, column = 2, pady = 7, padx = 7, sticky = W)

BotonAbrir = Button(FramePrincipal, text = "Abrir") ##Anadir ", command = funcion"
BotonGuardar = Button(FramePrincipal, text = "Generar reporte") ##Anadir ", command = funcion"
BotonGuardarComo = Button(FramePrincipal, text = "Ver Elementos Quimicos") ##Anadir ", command = funcion"
BotonAnalizar = Button(FramePrincipal, text = "Analizar") ##Anadir ", command = funcion"
BotonErrores = Button(FramePrincipal, text = "Errores") ##Anadir ", command = funcion"
BotonSalir = Button(FramePrincipal, text = "Salir") ##Anadir ", command = funcion"

BotonMusuario = Button(FramePrincipal, text = "Manual de Usuario") ##Anadir ", command = funcion"
BotonMTecnico = Button(FramePrincipal, text = "Manual Técnico") ##Anadir ", command = funcion"
BotonTemasAyuda = Button(FramePrincipal, text = "Temas de ayuda") ##Anadir ", command = funcion"



BotonAbrir.grid(row = '2', column = '0' , pady = "7", padx = "7", sticky = W)
BotonGuardar.grid(row = '3', column = '0' , pady = "7", padx = "7", sticky = W)
BotonGuardarComo.grid(row = '3', column = '1' , pady = "7", padx = "7", sticky = W)
BotonAnalizar.grid(row = '2', column = '1' , pady = "7", padx = "7", sticky = S)

BotonErrores.grid(row = '4', column = '1' , pady = "7", padx = "7", sticky = S)

BotonMusuario.grid(row = '2', column = '2' , pady = "7", padx = "7", sticky = W)
BotonMTecnico.grid(row = '3', column = '2' , pady = "7", padx = "7", sticky = W)
BotonTemasAyuda.grid(row = '4', column = '2' , pady = "7", padx = "7", sticky = W)




raiz.mainloop()