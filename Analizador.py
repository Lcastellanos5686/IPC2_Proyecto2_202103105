import ListaDoble
import Pin
import Elemento
from PrintColores import*
import time
import os
import subprocess

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

listaElementosCompuesto = ListaDoble.ListaDoble()
listaElementosCompuesto.append('Li')
listaElementosCompuesto.append('Li')
listaElementosCompuesto.append('Be')
listaElementosCompuesto.append('He')
listaElementosCompuesto.append('Be')
listaElementosCompuesto.append('Li')

print('############################################')

def TiempoParaCrearCompuesto(listaMaquina : ListaDoble.ListaDoble , listaCompuesto : ListaDoble.ListaDoble, generarTabla, generarXML):
    ElementoBuscado = listaCompuesto.head
    pinActual = listaMaquina.head
    tiempoTranscurrido = 0
    pinPrioridad = 0

    listaCompuesto2 = ListaDoble.ListaDoble()

    a = listaCompuesto.head
    while a:
        listaCompuesto2.append(a.data)
        a = a.next


    listaAuxiliar = ListaDoble.ListaDoble()
    crearLista = listaCompuesto2.head

    while crearLista:
        if listaAuxiliar.se_encuentra_en_lista(crearLista.data):
            pass
        else:
            listaAuxiliar.append(crearLista.data)
        crearLista = crearLista.next

    listaAuxiliar.print_list()
    
    ##listaAuxiliar.print_list()
    detenerDeEmergencia = 0
    while ElementoBuscado:
        ##time.sleep(1)
        if detenerDeEmergencia == 500:
            return('NO SE PUDO CREAR')
        
        detenerDeEmergencia += 1
        print(detenerDeEmergencia)

        pinActual = listaMaquina.head
        while pinActual:
            pinActual.data.bloqueado=False
            pinActual = pinActual.next
        prGreen(ElementoBuscado.data)
        pinActual = listaMaquina.head

        while pinActual:
            if pinActual.data.se_encuentra_en_pin(ElementoBuscado.data):
                pinPrioridad = pinActual.data.numeroPin
                prCyan(pinActual.data.numeroPin)
                if pinActual.data.enElemento == None: ## OPCION 1
                    print('Entro en caso mover adelante')
                    pinActual.data.listaAcciones.append('<td>Mover Adelante</td>')
                    pinActual.data.listaAccionesXML.append('Mover Adelante')
                    pinActual.data.enElemento = pinActual.data.listaElementos.head
                    tiempoTranscurrido += 1
                elif pinActual.data.enElemento.data.simbolo == ElementoBuscado.data: ## OPCION 2
                    print('Entro en caso fusionar')
                    pinActual.data.listaAcciones.append('<td>Fusionar ' + ElementoBuscado.data + '</td>')
                    pinActual.data.listaAccionesXML.append('Fusionar '  + ElementoBuscado.data)
                    ElementoBuscado = ElementoBuscado.next
                    tiempoTranscurrido += 1

                    listaCompuesto2.delete_first()
                    listaCompuesto2.print_list()
                    listaAuxiliar = ListaDoble.ListaDoble()
                    crearLista = listaCompuesto2.head

                    while crearLista:
                        if listaAuxiliar.se_encuentra_en_lista(crearLista.data):
                            pass
                        else:
                            listaAuxiliar.append(crearLista.data)
                        crearLista = crearLista.next

                    listaAuxiliar.print_list()

                    break
                elif pinActual.data.movimientos_entre_dos(ElementoBuscado.data, pinActual.data.enElemento.data.simbolo) > 0: ## OPCION 3 
                    print('Entro en caso mover adelante')
                    pinActual.data.listaAcciones.append('<td>Mover Adelante</td>')
                    pinActual.data.listaAccionesXML.append('Mover Adelante')
                    pinActual.data.enElemento = pinActual.data.enElemento.next
                    tiempoTranscurrido += 1
                elif pinActual.data.movimientos_entre_dos(ElementoBuscado.data, pinActual.data.enElemento.data.simbolo) < 0: ## OPCION 4
                    print('Entro en caso mover atras')
                    pinActual.data.listaAcciones.append('<td>Mover Atras</td>')
                    pinActual.data.listaAccionesXML.append('Mover Atras')
                    pinActual.data.enElemento = pinActual.data.enElemento.prev
                    tiempoTranscurrido += 1
                else:
                    print('nada')
            pinActual = pinActual.next
        
        ElementoAuxiliar = listaAuxiliar.head
        pinActual = listaMaquina.head

        while ElementoAuxiliar:
            prYellow(ElementoAuxiliar.data)
            pinActual = listaMaquina.head
            while pinActual:
                if pinActual.data.numeroPin == pinPrioridad:
                    prYellow('pin con prioridad ' + str(pinActual.data.numeroPin))
                    pass
                elif pinActual.data.se_encuentra_en_pin(ElementoAuxiliar.data):
                    
                    if pinActual.data.enElemento == None and pinActual.data.bloqueado == False: ## OPCION 1
                        prYellow('Entro en caso mover adelante')
                        pinActual.data.listaAcciones.append('<td>Mover Adelante</td>')
                        pinActual.data.listaAccionesXML.append('Mover Adelante')
                        pinActual.data.enElemento = pinActual.data.listaElementos.head
                        pinActual.data.bloqueado = True
                    elif pinActual.data.enElemento.data.simbolo == ElementoAuxiliar.data  and pinActual.data.bloqueado == False: ## OPCION 2
                        prYellow('Entro en caso Esperar')
                        pinActual.data.listaAcciones.append('<td>Esperar</td>')
                        pinActual.data.listaAccionesXML.append('Esperar')
                        pinActual.data.bloqueado = True
                        break   
                    elif pinActual.data.movimientos_entre_dos(ElementoAuxiliar.data, pinActual.data.enElemento.data.simbolo) > 0  and pinActual.data.bloqueado == False: ## OPCION 3 
                        prYellow('Entro en caso mover adelante')
                        pinActual.data.listaAcciones.append('<td>Mover Adelante</td>')
                        pinActual.data.listaAccionesXML.append('Mover Adelante')
                        pinActual.data.enElemento = pinActual.data.enElemento.next
                        pinActual.data.bloqueado = True
                        
                    elif pinActual.data.movimientos_entre_dos(ElementoAuxiliar.data, pinActual.data.enElemento.data.simbolo) < 0  and pinActual.data.bloqueado == False: ## OPCION 4
                        prYellow('Entro en caso mover atras')
                        pinActual.data.listaAcciones.append('<td>Mover Atras</td>')
                        pinActual.data.listaAccionesXML.append('Mover Atras')
                        pinActual.data.enElemento = pinActual.data.enElemento.prev
                        pinActual.data.bloqueado = True
                pinActual = pinActual.next
            ElementoAuxiliar = ElementoAuxiliar.next
                    
        
        prLightPurple('######################################  '+ str(tiempoTranscurrido))
    print('Tiempo total!! ' + str(tiempoTranscurrido))

    TextoXML = ''
    TextoXML += '            <tiempoOptimo>' + str(tiempoTranscurrido) + '</tiempoOptimo>\n'
    TextoXML += '            <instrucciones>\n'
    
    a = listaMaquina.head
    while a:
        a.data.completarXML(tiempoTranscurrido)
        a = a.next

    
    for i in range(tiempoTranscurrido):
        contador = 0
        TextoXML += '                <tiempo>\n'
        TextoXML += '                <numeroSegundo>' + str(i+1) + '</numeroSegundo>\n'
        TextoXML += '                    <acciones>\n'
        a = listaMaquina.head
        while a:
            b = a.data.listaAccionesXML.head
            contador =0
            while b:
                if contador == i:
                    TextoXML += '                        <accionPin>\n'
                    TextoXML += '                            <numeroPin>' + str(a.data.numeroPin) + '</numeroPin>\n'
                    TextoXML += '                            <accion>' + str(b.data) + '</accion>\n'
                    TextoXML += '                        </accionPin>\n'
                    break
                contador +=1
                b = b.next
            a = a.next
        TextoXML += '                    </acciones>\n'
        TextoXML += '                </tiempo>\n'
        
    TextoXML += '            </instrucciones>\n'
    

    
    


    textoGraphviz = '''digraph {
        node [ shape=none fontname=Helvetica ]
        n1 [ label = <
        <table>
        <tr><td></td>'''
    for i in range(tiempoTranscurrido):
        textoGraphviz += '<td> Segundo ' + str(i+1) + '</td>' 
    textoGraphviz += '</tr>\n'

    a = listaMaquina.head
    while a:
        a.data.enElemento = None
        a.data.bloqueado = False
        textoGraphviz += a.data.generarTablaAcciones(tiempoTranscurrido) + '\n'
        a.data.listaAcciones = ListaDoble.ListaDoble()
        a.data.listaAccionesXML = ListaDoble.ListaDoble()
        a = a.next
    textoGraphviz += '''</table>
                    > ]}'''
    print(textoGraphviz)

    if generarXML:
        
        return TextoXML

    if generarTabla:
        archivo = open('Resultados.dot','w')
        archivo.write(textoGraphviz)
        archivo.close()
        os.system("dot.exe -Tpng Resultados.dot -o Tabla.png")
        subprocess.Popen("Tabla.png", shell=True)

    return tiempoTranscurrido

        
        
    



prRed('#######################################################################################')
TiempoParaCrearCompuesto(listaPines,listaElementosCompuesto, True, True)
