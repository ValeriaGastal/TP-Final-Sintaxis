######################################################################################################
###########################################      ARBOL      ##########################################
######################################################################################################
class Nodo:

    def __init__(self, dato):
        self.dato = dato
        self.hijos = []
        self.padre = None

    def agregarHijo(self, hijo):
        hijo.padre = self
        self.hijos.append(hijo)

            # Devuelve True si el nodo es una hoja, False si no lo es
    def esHoja(self):
        if self.hijos == []:
            return True
        else:
            return False

    # Devuuelve True si el nodo es la raiz, False si no lo es
    def esRaiz(self):
        if self.padre == None:
            return True
        else:
            return False

            # Metodos Getters
            # --------------------------------------------------------
            # Devuelve su correspondiente Nodo padre.
    def getPadre(self):
        return self.padre

            # Devuelve un array con todos los hijos del nodo
    def getHijos(self):
        return self.hijos

            # Devuelve el dato del nodo en crudo
            # Como siempre usamos strings como dato, devuelve String
    def getDato(self):
        return self.dato

            # Representador (solo para debugging)
            # Representa el arbol en una estructura tabulada
            # se llama solo con escribir el nombre del objeto


    def __repr__(self, mem=''):
        dato = self.getDato()
        ret = dato + '\n'
        if self.esRaiz():
            ret = '\n' + dato + '\n'
        esp = ''
        esq = ''
        hijos = self.getHijos()
        if self.esRaiz():
            for hijo in hijos:
                if hijo != hijos[-1]:
                    esq = '╠═'
                    esp = '║ '
                else:
                    esq = '╚═'
                    esp = '  '
                ret += mem + esq + hijo.__repr__(esp)
        else:
            if not self.esHoja():  # si tengo hijos
                if self == self.getPadre().getHijos()[-1]:
                    esp = '  '
                else:
                    esp = '║ '
                for hijo in hijos:
                    if hijo == hijos[-1]:
                        esq = '╚═'
                        esp = '  '
                    else:
                        esq = '╠═'
                        esp = '║ '
                    ret += mem + esq + hijo.__repr__(mem + esp)
        return ret

    def mostrar(self,espacios= ''):
        print(espacios,self.dato,"\n")
        espacios =espacios+'  '
        for h in self.hijos:
            h.mostrar(espacios)


