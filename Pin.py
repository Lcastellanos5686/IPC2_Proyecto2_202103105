import ListaDoble
from PrintColores import*

class Pin:
    def __init__(self, numeroPin):
        self.numeroPin=numeroPin
        self.listaElementos = ListaDoble.ListaDoble()
        self.enElemento = None
        self.bloqueado = False
        self.listaAcciones = ListaDoble.ListaDoble()
        self.listaAccionesXML = ListaDoble.ListaDoble()
    
    def anadirElemento(self, Elemento):
        self.listaElementos.append(Elemento)
    
    def print_elementos(self):
        print('En el pin ' + str(self.numeroPin) + " se encuentran los siguientes Elementos:")
        self.listaElementos.print_elementos()

    def movimientos_desde_inicio(self, Elemento):
        return self.listaElementos.movimientos_desde_inicio(Elemento)
    
    def movimientos_entre_dos(self,elemento1,elemento2): #El elemento 1 es el del cual se va a calcular el elemento mas cercano, es decir el elemento 2
        d_elemento1 = self.movimientos_desde_inicio(elemento1) 
        d_elemento2 = self.movimientos_desde_inicio(elemento2)

        if d_elemento1 == None or d_elemento2 == None:
            prRed('No se encontro un elemento')
            return

        ##prCyan('El elemento ' + elemento1 + ' se encuentra a ' + str(abs(d_elemento1-d_elemento2)) + " del elemento " + elemento2)
        ##print('')
        return d_elemento1-d_elemento2

    def se_encuentra_en_pin(self, Elemento):
        return self.listaElementos.se_encuentra_en_pin(Elemento)

    def movimientos_entre_actual(self, Elemento2):
        if self.enElemento == None:
            return self.movimientos_desde_inicio(Elemento2)
        else:
            return self.movimientos_entre_dos(self.enElemento, Elemento2)
    
    def restaurar_bloqueo(self):
        self.bloqueado = False

    def generarTablaAcciones(self,tiempo):
        TextoTabla = "<tr>"
        TextoTabla += '<td>Pin ' + str(self.numeroPin) + "</td>"
        f = self.listaAcciones.head
        while f:
            TextoTabla += f.data
            tiempo -= 1
            f= f.next
        
        if tiempo > 0:
            for i in range(tiempo):
                TextoTabla += "<td>Esperar</td>"
            TextoTabla += "</tr>"
            return TextoTabla
        TextoTabla += "</tr>"
        return TextoTabla

    def completarXML(self,tiempo):
        a = self.listaAccionesXML.head

        while a:
            tiempo -= 1
            a=a.next

        if tiempo > 0:
            for i in range(tiempo):
                self.listaAccionesXML.append('Esperar')
        




        
        