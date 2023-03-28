import ListaDoble
from PrintColores import*

class Pin:
    def __init__(self, numeroPin):
        self.numeroPin=numeroPin
        self.listaElementos = ListaDoble.ListaDoble()
    
    def anadirElemento(self, Elemento):
        self.listaElementos.append(Elemento)
    
    def print_elementos(self):
        print('En el pin ' + str(self.numeroPin) + " se encuentran los siguientes Elementos:")
        self.listaElementos.print_elementos()

    def movimientos_desde_inicio(self, Elemento):
        self.listaElementos.movimientos_desde_inicio(Elemento)
    
    def movimientos_entre_dos(self,elemento1,elemento2): #El elemento 1 es el del cual se va a calcular el elemento mas cercano, es decir el elemento 2
        d_elemento1 = self.movimientos_desde_inicio(elemento1) #Recordatorio. Estamos calculando la distancia entre dos elementos en un pin. la distancia sera la resta de ambos. hacer eso usando metodos de esta clase

        