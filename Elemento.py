from PrintColores import*

class Elemento:
    def __init__(self, numeroAtomico, simbolo, elemento):
        self.numeroAtomico = numeroAtomico
        self.simbolo = simbolo
        self.elemento = elemento

    def print_elemento(self):
        print('')
        prGreen(self.numeroAtomico)
        prGreen(self.simbolo)
        prGreen(self.elemento)
        print('')
        