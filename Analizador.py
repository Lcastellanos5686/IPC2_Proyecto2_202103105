import ListaDoble
import Pin
import Elemento

listaPines = ListaDoble.ListaDoble()

Pin1 = Pin.Pin(1)
Pin1.anadirElemento(Elemento.Elemento(3, "Li", 'Litio'))
Pin1.anadirElemento(Elemento.Elemento(2, "He", 'Helio'))
Pin1.anadirElemento(Elemento.Elemento(7, "N", 'Nitrogeno'))

Pin2 = Pin.Pin(2)
Pin2.anadirElemento(Elemento.Elemento(6, "C", 'Carbono'))
Pin2.anadirElemento(Elemento.Elemento(4, "Be", 'Berilio'))
Pin2.anadirElemento(Elemento.Elemento(1, "H", 'Hidrogeno'))

listaPines.append(Pin1)
listaPines.append(Pin2)

listaPines.print_pines()

Pin1.movimientos_desde_inicio('N')

