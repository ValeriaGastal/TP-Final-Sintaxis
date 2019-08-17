######################################################################################################
###########################################      PILA      ###########################################
######################################################################################################

class Pila:
    def __init__(self):  # Constructor
        self.lista = []

    def vacia(self):  #devuelve true si esta vacia, sino devuelve false
        if self.lista == []:
            return True
        else:
            return False

    def push(self, objeto):  # apilar
        self.lista.append(objeto)


    def popp(self):   # desapila
        if not self.vacia():
            return self.lista.pop()
