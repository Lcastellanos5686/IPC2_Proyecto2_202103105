from xml.dom import minidom
from tkinter.filedialog import askopenfilename
from PrintColores import*
import ListaDoble
import Elemento
import Pin
import Maquina
import Compuesto
from tkinter import *
import tkinter.messagebox
import Analizador
import webbrowser
import subprocess


class Menu:
    def __init__(self):
        self.listaMaquinas = ListaDoble.ListaDoble()
        self.listaElementos = ListaDoble.ListaDoble()
        self.listaCompuestos = ListaDoble.ListaDoble()

    def leerXML(self, archivoXml : minidom.Document):
        listaMaquinas = archivoXml.getElementsByTagName('listaMaquinas')
        listaElementos = archivoXml.getElementsByTagName('listaElementos')
        listaCompuestos = archivoXml.getElementsByTagName('listaCompuestos')

        for i in listaElementos[0].getElementsByTagName('elemento'):
            numeroAtomico = i.getElementsByTagName('numeroAtomico')
            simbolo = i.getElementsByTagName('simbolo')
            nombreElemento = i.getElementsByTagName('nombreElemento')

            self.listaElementos.append(Elemento.Elemento(int(numeroAtomico[0].firstChild.data), simbolo[0].firstChild.data, nombreElemento[0].firstChild.data))

        ######################################################################################################################################################################################3

        for i in listaMaquinas[0].getElementsByTagName('Maquina'):
            nombre = i.getElementsByTagName('nombre')
            numeroPines = i.getElementsByTagName('numeroPines')
            numeroElementos = i.getElementsByTagName('numeroElementos')
            listaPinesTemporal = ListaDoble.ListaDoble()

            contador = 1
            for j in i.getElementsByTagName('pin'):##aqui se va a crear lista de elementos para pin
                ##print('pin ' + str(contador))
                listaElementosTemporal = Pin.Pin(contador)
                
                for k in j.getElementsByTagName('elemento'):
                    ##print(' ' + k.firstChild.data)
                    a = self.listaElementos.head
                    elementoAnadido = False
                    while a:
                        if a.data.simbolo == k.firstChild.data:
                            ##prRed('entro al if')
                            elementoAnadido = True
                            listaElementosTemporal.anadirElemento(a.data)
                        a = a.next
                    if elementoAnadido == False:
                        listaElementosTemporal.anadirElemento(Elemento.Elemento(0,k.firstChild.data,k.firstChild.data))

                listaPinesTemporal.append(listaElementosTemporal)
                    
                contador +=1
            self.listaMaquinas.append(Maquina.Maquina(nombre[0].firstChild.data, numeroPines[0].firstChild.data, numeroElementos[0].firstChild.data, listaPinesTemporal))
            ##listaPinesTemporal.print_pines()
            #############################################################################################################################
        for i in listaCompuestos[0].getElementsByTagName('compuesto'):
            nombreCompuesto = i.getElementsByTagName('nombre')
            listaCompuestosTemporal = ListaDoble.ListaDoble()
            for j in i.getElementsByTagName('elemento'):
                listaCompuestosTemporal.append(j.firstChild.data)
            self.listaCompuestos.append(Compuesto.Compuesto(nombreCompuesto[0].firstChild.data, listaCompuestosTemporal))

        prCyan('Imprimiendo lista de Elementos!!!')
        a = self.listaElementos.head
        while a:
            a.data.print_elemento()
            a = a.next

        prCyan('Imprimiendo lista de Maquinas!!!')
        a = self.listaMaquinas.head
        while a:
            a.data.listaPines.print_pines()
            a = a.next

        prCyan('Imprimiendo lista de Compuestos!!!')
        a = self.listaCompuestos.head
        while a:
            print(a.data.nombreCompuesto)
            a.data.listaCompuesto.print_list()

            a = a.next

datos = Menu()

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
    ObjetoXML = minidom.parse(archivo)
    datos.leerXML(ObjetoXML)

def AnadirElemento():

    def ProcesarElemento(numero, simbolo, elemento):
        print(numero)
        print(simbolo)
        print(elemento)
        if elemento == '' or simbolo == '' or numero == '':
            prRed('retornoFalse')
            return False
            
        
        try:
            int(numero)
        except:
            prRed('retornoFalse')
            return False
            
        
        raiz3.destroy()
        datos.listaElementos.append(Elemento.Elemento(int(numero), simbolo, elemento))
        ElementoQuimico()
        prGreen('retornoTrue')
        return True

    raiz3 = Tk()
    raiz3.title('Añadir Elemento')
    LabelTitulo = Label(raiz3, text = 'Anadir Elemento', font = ("Courier New",13))
    LabelTitulo.grid(row = 0, column = 1, pady = 7, padx = 7, sticky = N)

    LabelTitulo = Label(raiz3, text = 'Número Atómico', font = ("Futura MdCn BT",13))
    LabelTitulo.grid(row = 1, column = 0, pady = 7, padx = 7, sticky = N)

    LabelTitulo = Label(raiz3, text = 'Símbolo', font = ("Futura MdCn BT",13))
    LabelTitulo.grid(row = 1, column = 1, pady = 7, padx = 7, sticky = N)

    LabelTitulo = Label(raiz3, text = 'Nombre del elemento', font = ("Futura MdCn BT",13))
    LabelTitulo.grid(row = 1, column = 2, pady = 7, padx = 7, sticky = N)

    NumeroAtomico = Entry(raiz3, text='')
    NumeroAtomico.grid(row=2, column=0, pady = 7, padx = 7)

    Simbolo = Entry(raiz3, text='')
    Simbolo.grid(row=2, column=1, pady = 7, padx = 7)

    nombreElemento = Entry(raiz3, text='')
    nombreElemento.grid(row=2, column=2, pady = 7, padx = 7)

    BotonAceptar = Button(raiz3, text = "Aceptar", command=lambda:ProcesarElemento(NumeroAtomico.get(),Simbolo.get(),nombreElemento.get()))
    BotonAceptar.grid(row = '3', column = '2' , pady = "7", padx = "7", sticky = W)
    
    BotonCancelar = Button(raiz3, text = "Cancelar", command=lambda:raiz3.destroy())
    BotonCancelar.grid(row = '3', column = '1' , pady = "7", padx = "7", sticky = W)

def ElementoQuimico():

    def EjecutarYMatar():
        raiz2.destroy()
        AnadirElemento()

    raiz2 = Tk()
    raiz2.title('Elementos Químicos')
    listaEnOrden = ListaDoble.ListaDoble()
    listaOriginalTemporal = ListaDoble.ListaDoble()

    prCyan('Se imprimen elementos')
    datos.listaElementos.print_elementos()

    c = datos.listaElementos.head
    contador = 0
    while c:
        listaOriginalTemporal.append(c.data)
        c = c.next
        contador += 1

    for i in range(contador):
        c = listaOriginalTemporal.head
        numeroMenor = 9999999
        while c: #Primero se escoje el menor
            if c.data.numeroAtomico < numeroMenor:
                numeroMenor = c.data.numeroAtomico
            c = c.next

        c = listaOriginalTemporal.head
        
        while c:
            if c.data.numeroAtomico == numeroMenor:
                listaEnOrden.append(c.data)
                listaOriginalTemporal.delete(c.data)
                break
            c = c.next
    BotonCerrar = Button(raiz2, text = "Cerrar", command=lambda:raiz2.destroy())
    BotonCerrar.grid(row = contador + 1, column = '3' , pady = "7", padx = "7", sticky = E)
    BotonCerrar = Button(raiz2, text = "Añadir Elemento", command=lambda:EjecutarYMatar())
    BotonCerrar.grid(row = contador + 1, column = '1' , pady = "7", padx = "7", sticky = E)

    a = listaEnOrden.head
    contador = 1

    b = Entry(raiz2, text='', justify=CENTER, font=("Calibri Bold",10))
    b.grid(row=0, column=0)
    b.insert(END, "Número Atómico")

    b = Entry(raiz2, text='', justify=CENTER, font=("Calibri Bold",10))
    b.grid(row=0, column=1)
    b.insert(END,'Símbolo')

    b = Entry(raiz2, text='', justify=CENTER, font=("Calibri Bold",10))
    b.grid(row=0, column=3)
    b.insert(END, "Nombre del Elemento")


    while a:
        b = Entry(raiz2, text='')
        b.grid(row=contador, column=0)
        b.insert(END, a.data.numeroAtomico)

        b = Entry(raiz2, text='')
        b.grid(row=contador, column=1)
        b.insert(END, a.data.simbolo)

        b = Entry(raiz2, text='')
        b.grid(row=contador, column=3)
        b.insert(END, a.data.elemento)

        contador +=1
        a = a.next

def Maquinaa():
    raiz4 = Tk()
    raiz4.title('Elija una máquina...')

    

    LabelTitulo = Label(raiz4, text = 'Escriba el nombre de la máquina', font = ("Futura MdCn BT",15))
    LabelTitulo.grid(row = 0, column = 0, pady = 7, padx = 7, sticky = W)

    TextoMaquina = Entry(raiz4, text='')
    TextoMaquina.grid(row=1, column=0, pady = 7, padx = 7)

    BotonAceptar = Button(raiz4, text = "Aceptar", command = lambda: TablaMaquinas(TextoMaquina.get()))
    BotonAceptar.grid(row = '2', column = '0' , pady = "7", padx = "7", sticky = N)

    BotonCancelar = Button(raiz4, text = "Cancelar", command = lambda: raiz4.destroy())
    BotonCancelar.grid(row = '3', column = '0' , pady = "7", padx = "7", sticky = N)

def TablaMaquinas():
    a = datos.listaMaquinas.head
    raiznueva = Tk()
    raiznueva.title('Maquinas')
    LabelTitulo = Label(raiznueva, text ='Maquinas', font = ("Futura MdCn BT",15))
    LabelTitulo.grid(row = 0, column = 0, pady = 7, padx = 7, sticky = W)
    contador = 1
    while a:
        b = Entry(raiznueva, text='', justify=CENTER, font=("Calibri Bold",10))
        b.grid(row=contador, column=0)
        b.insert(END, a.data.nombre)

        b = Entry(raiznueva, text='', justify=CENTER, font=("Calibri Bold",10))
        b.grid(row=contador, column=1)
        b.insert(END, "Elementos en orden")

        contador +=1

        c = a.data.listaPines.head
        while c:
            ElementosEnFila = ''
            b = Entry(raiznueva, text='', justify=CENTER)
            b.grid(row=contador, column=0)
            b.insert(END,'Pin #' + str(c.data.numeroPin))

            d = c.data.listaElementos.head
            while d:
                ElementosEnFila += d.data.simbolo + "-"
                d = d.next
            
            b = Entry(raiznueva, text='', justify=CENTER)
            b.grid(row=contador, column=1)
            b.insert(END, ElementosEnFila)

            
            c = c.next
            contador += 1
        

        a = a.next

def Compuestos():
    raiz6 = Tk()
    raiz6.title('Listado Compuestos')

    LabelTitulo = Label(raiz6, text = 'Lista de compuestos', font = ("Futura MdCn BT",15))
    LabelTitulo.grid(row = 0, column = 0, pady = 7, padx = 7, sticky = W)

    Ventana = Entry(raiz6, text='', justify=CENTER, font=("Calibri Bold",10))
    Ventana.grid(row=1, column=0)
    Ventana.insert(END, "Nombre del Compuesto")

    Ventana = Entry(raiz6, text='', justify=CENTER, font=("Calibri Bold",10))
    Ventana.grid(row=1, column=1)
    Ventana.insert(END, "Componentes")

    a = datos.listaCompuestos.head
    contador = 2
    while a:
        TextoCompuestoTemporal = ''

        Ventana = Entry(raiz6, text='', justify=CENTER)
        Ventana.grid(row=contador, column=0)
        Ventana.insert(END, a.data.nombreCompuesto)


        b = a.data.listaCompuesto.head
        while b:
            TextoCompuestoTemporal += b.data
            b = b.next

        Ventana = Entry(raiz6, text='', justify=CENTER)
        Ventana.grid(row=contador, column=1)
        Ventana.insert(END, TextoCompuestoTemporal)
        
        contador +=1
        a = a.next

    BotonAceptar = Button(raiz6, text = "Ver tiempos", command=lambda: VentanaBuscarCompuesto())
    BotonAceptar.grid(row = contador, column = '2' , pady = "7", padx = "7", sticky = N)

    BotonCancelar = Button(raiz6, text = "Cancelar", command = lambda: raiz6.destroy())
    BotonCancelar.grid(row = contador, column = '1' , pady = "7", padx = "7", sticky = N)

    BotonTabla = Button(raiz6, text = "Generar Tabla", command = lambda: GenerarGraphviz())
    BotonTabla.grid(row = contador+1, column = '1' , pady = "7", padx = "7", sticky = N)
    
def VentanaBuscarCompuesto():
    raiz7 = Tk()

    LabelTitulo = Label(raiz7, text = 'Escriba el nombre del compuesto', font = ("Futura MdCn BT",15))
    LabelTitulo.grid(row = 0, column = 0, pady = 7, padx = 7, sticky = W)

    TextoCompuesto = Entry(raiz7, text='')
    TextoCompuesto.grid(row=1, column=0, pady = 7, padx = 7)

    BotonAceptar = Button(raiz7, text = "Aceptar", command = lambda: TiemposCompuesto(TextoCompuesto.get()))
    BotonAceptar.grid(row = '2', column = '0' , pady = "7", padx = "7", sticky = N)

    BotonCancelar = Button(raiz7, text = "Cancelar", command = lambda: raiz7.destroy())
    BotonCancelar.grid(row = '3', column = '0' , pady = "7", padx = "7", sticky = N)

def TiemposCompuesto(Nombre):
    raiz8 = Tk()
    raiz8.title(Nombre) 

    LabelTitulo = Label(raiz8, text =Nombre, font = ("Futura MdCn BT",15))
    LabelTitulo.grid(row = 0, column = 0, pady = 7, padx = 7, sticky = W)
    
    a = datos.listaCompuestos.head
    contador = 1
    while a:
        
        if a.data.nombreCompuesto == Nombre:
            b = datos.listaMaquinas.head
            while b:

                celda = Entry(raiz8, text='', justify=CENTER)
                celda.grid(row=contador, column=0)
                celda.insert(END, b.data.nombre)

                celda = Entry(raiz8, text='', justify=CENTER)
                celda.grid(row=contador, column=1)
                celda.insert(END, str(Analizador.TiempoParaCrearCompuesto(b.data.listaPines,a.data.listaCompuesto, FALSE, FALSE)) + '-')

                contador +=1
                b = b.next
        a = a.next

def GenerarGraphviz():

    def BuscarYGenerar(Compuesto, Maquina):
        a = datos.listaCompuestos.head
        while a:
            if a.data.nombreCompuesto == Compuesto:
                b = datos.listaMaquinas.head
                while b:
                    if b.data.nombre == Maquina:
                        Analizador.TiempoParaCrearCompuesto(b.data.listaPines,a.data.listaCompuesto, True, False)
                        return 
                    b = b.next
            a = a.next
        
        tkinter.messagebox.showerror(title='ERROR', message='No se encontraron los parametros')
        return

    raiz9 = Tk()
    raiz9.title('GenerarTabla')

    LabelTitulo = Label(raiz9, text = 'Escriba el nombre del compuesto', font = ("Futura MdCn BT",15))
    LabelTitulo.grid(row = 0, column = 0, pady = 7, padx = 7, sticky = W)

    TextoCompuesto = Entry(raiz9, text='')
    TextoCompuesto.grid(row=1, column=0, pady = 7, padx = 7)

    LabelTitulo2 = Label(raiz9, text = 'Escriba el nombre de la maquina', font = ("Futura MdCn BT",15))
    LabelTitulo2.grid(row = 2, column = 0, pady = 7, padx = 7, sticky = W)

    TextoMaquina = Entry(raiz9, text='')
    TextoMaquina.grid(row=3, column=0, pady = 7, padx = 7)

    BotonAceptar = Button(raiz9, text = "Abrir...", command=lambda:BuscarYGenerar(TextoCompuesto.get(),TextoMaquina.get() ))
    BotonAceptar.grid(row = '4', column = '0' , pady = "7", padx = "7", sticky = N)

def GenerarSalidaXML():
    TextoXML = '<?xml version="1.0"?>\n'
    TextoXML += '<RESPUESTA>\n'
    TextoXML += '   <listaCompuestos>\n'
    a = datos.listaCompuestos.head
    while a:
        TextoXML += '       <compuesto>\n'
        
        b = datos.listaMaquinas.head
        while b:
            TextoXML += '       <nombreMaquina>' + b.data.nombre + '</nombreMaquina>\n'
            TextoXML += Analizador.TiempoParaCrearCompuesto(b.data.listaPines,a.data.listaCompuesto,False,True)
            b = b.next
        TextoXML += '       </compuesto>\n'
        a= a.next
    TextoXML += '   </listaCompuestos>\n'
    TextoXML += '</RESPUESTA>\n'

    archivo = open('Resultados.XML','w')
    archivo.write(TextoXML)
    archivo.close()

def Info():
    raizfinal = Tk()
    raizfinal.title('Información')

    LabelTitulo = Label(raizfinal, text = 'Luis Daniel Castellanos Betancourt | 202103105 | IPC2 - D | Proyecto 2', font = ("Courier New",10))
    LabelTitulo.grid(row = 0, column = 0, pady = 7, padx = 7, sticky = W)

    BotonRepo = Button(raizfinal, text = "Repositorio", command=lambda:webbrowser.open('https://github.com/Lcastellanos5686/IPC2_Proyecto2_202103105'))
    BotonRepo.grid(row = '1', column = '0' , pady = "7", padx = "7", sticky = N)

    Botoninfo = Button(raizfinal, text = "Ensayo", command=lambda:subprocess.Popen("Ensayo.pdf", shell=True))
    Botoninfo.grid(row = '2', column = '0' , pady = "7", padx = "7", sticky = N)




################################

BotonAbrir = Button(FramePrincipal, text = "Abrir...", command=lambda:Abrir())
BotonAbrir.grid(row = '2', column = '0' , pady = "7", padx = "7", sticky = N)
BotonAbrir = Button(FramePrincipal, text = "Generar XML", command = lambda: GenerarSalidaXML())
BotonAbrir.grid(row = '3', column = '0' , pady = "7", padx = "7", sticky = N)

BotonAbrir = Button(FramePrincipal, text = "Elementos Químicos", command=lambda:ElementoQuimico())
BotonAbrir.grid(row = '2', column = '1' , pady = "7", padx = "7", sticky = N)
BotonAbrir = Button(FramePrincipal, text = "Compuesto", command = lambda: Compuestos())
BotonAbrir.grid(row = '3', column = '1' , pady = "7", padx = "7", sticky = N)
BotonAbrir = Button(FramePrincipal, text = "Máquinas", command = lambda: TablaMaquinas())
BotonAbrir.grid(row = '4', column = '1' , pady = "7", padx = "7", sticky = N)

BotonAbrir = Button(FramePrincipal, text = "Información", command = lambda: Info())
BotonAbrir.grid(row = '2', column = '2' , pady = "7", padx = "7", sticky = N)




raiz.mainloop()
