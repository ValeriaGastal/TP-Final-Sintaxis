# ###############################################################################################
####################################     ANALIZADOR SINTACTICO       #################################
######################################################################################################

import scanner as lex
import TAS as tas
import Arbol as ar
import Pila as p
import TabladeSimbolos as ts


Terminal = lex.Terminal
Variables = lex.Variables


class AnalizadorSintactico():
    def __init__(self, archivoAEjecutar):
        self.tablaSimbolos = ts.crearTS() #crea la tabla de simbolos
        self.arbol = ar.Nodo(lex.S) #crea el arbol con raiz S
        self.pila = p.Pila() #crea pila para apilar lo que contiene un vector de la tas
        self.pila2= p.Pila() #crea pila para apilar el nodo del arbol en el que se encuentra un elemento apilado de la primer pila
        self.pila.push(lex.peso)  # apilamos el simbolo final
        self.pila.push(lex.S) # apilamos primer Variable
        self.pila2.push(self.arbol)  #apilamos raiz
        self.nodoActual = self.arbol  # el nodo inicial es la raiz
        self.archivo = open(archivoAEjecutar)
        self.Lexico = lex.Lexico(self.archivo)  # creacion del analizador Lexico


    def analizarSintactico(self):
        a = self.Lexico.siguienteComponenteLexico(self.tablaSimbolos)  #a es un vector con el componente lexico y el lexema en este orden
        resultado = 0 # resultado =0 indica que el analizador Sintactico debe seguir analizando
        while resultado == 0:
            X = self.pila.popp()  #desapila

            if X != lex.peso :
                self.nodoActual = self.pila2.popp()  #desapila segunda pila y lo asigna a nodo actual

            if X ==  a[0] == lex.peso:
                resultado = 1 #proceso terminado con exito
            elif X in Terminal: #si X es terminal
                if X == a[0]: #y es el componente lexico leido
                    self.nodoActual.agregarHijo(ar.Nodo(a[1])) #se agrega como hijo al nodo actual
                    a = self.Lexico.siguienteComponenteLexico(self.tablaSimbolos) #y se obtiene el siguiente componente
                else:
                    resultado = -1 #error
            elif X in Variables: #si X es variable
                v = tas.tas(X[0], a[0]) #se obtiene el vector con la variable y el componente correspondiente
                if tas.tVecTASVacio(v): #si esta v vacio
                    print("Error sintactico")
                    resultado = -1 #error
                else:
                    i = 0
                    auxPila = p.Pila() #se crea dos auxiliares pila
                    auxPila2 = p.Pila()
                    while i < len(v) and v[i] != []: #mientras no se pase de rango y no quede vacio
                        self.nodoActual.agregarHijo(ar.Nodo(v[i])) # se agrega el hijo ial arbol
                        nodo = self.nodoActual.getHijos()[-1] #se obtiene su nodo
                        auxPila.push(v[i]) #se apila en la primera pila auxiliar el elemento
                        auxPila2.push(nodo) # se apila en la segunda pila auxiliar el nodo
                        i += 1 #se suma al contador
                    while i >= 0: #mientras sea mayor igual a cero, como un for de i..0
                        aux = auxPila.popp()  #se desapilan en auxiliares las pilas auxiliares
                        aux2 = auxPila2.popp()
                        if aux != None and aux != lex.epsilon :  #no se apila epsilon
                            self.pila.push(aux) # se apilar los auxiliares de forma que quedan apiladas de manera invertida
                        if aux2 != None and aux != lex.epsilon:
                            self.pila2.push(aux2)
                        i -= 1 #se descuenta contador
        return self.arbol #se devuelve el arbol