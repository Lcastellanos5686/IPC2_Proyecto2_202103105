class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class ListaDoble:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            curr_node = self.head
            while curr_node.next:
                curr_node = curr_node.next
            curr_node.next = new_node
            new_node.prev = curr_node

    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

    def delete(self, data):
        curr_node = self.head
        while curr_node:
            if curr_node.data == data:
                if curr_node.prev is None:
                    self.head = curr_node.next
                    if self.head:
                        self.head.prev = None
                else:
                    curr_node.prev.next = curr_node.next
                    if curr_node.next:
                        curr_node.next.prev = curr_node.prev
                del curr_node
                return
            curr_node = curr_node.next


    def print_list(self):
        curr_node = self.head
        while curr_node:
            print(curr_node.data)
            curr_node = curr_node.next

    def print_pines(self): #Esto es para la Lista de pines
        curr_node = self.head
        while curr_node:
            curr_node.data.print_elementos()
            curr_node = curr_node.next

    def print_elementos(self): #Esto es para la lista de elementos (Pin)
        curr_node = self.head
        while curr_node:
            curr_node.data.print_elemento()
            curr_node = curr_node.next
    
    def movimientos_desde_inicio(self, Elemento): #Esto es para la lista de elementos (Pin)
        curr_node = self.head #Curr node es un elemento
        contador = 0
        while curr_node:
            if curr_node.data.simbolo == Elemento:
                print('El elemento se encuentra a ' + str(contador) + " pasos del inicio")
                return contador
            contador +=1
            curr_node = curr_node.next

        


