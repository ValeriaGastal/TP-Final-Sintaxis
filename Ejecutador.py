import Parser as p
import scanner as s
import TabladeSimbolos as tsim
#Semantica

#< S >::= < sentencia > < A >
def evaluarS(arbol, ts):
    evaluarSentencia(arbol.hijos[0], ts)   # pasandose la el subarbol cuya raiz es el primer nodo que sera < sentencia > --> "Z"
    evaluarA(arbol.hijos[1], ts)  #el segundo hijo --> "A"

#< A >::= 	 ; < sentencia> <A> | ε
def evaluarA(arbol ,ts):
    if len(arbol.hijos)>1 and  arbol.hijos[0].getDato()==s.puntoycoma:  #si la produccion es la primera:  ; < sentencia> <A>, es decir tiene hijos puntoycoma, Z, A respectivamente
        evaluarSentencia(arbol.hijos[1] ,ts)  #porque el primer hijo es punto y coma
        evaluarA(arbol.hijos[2] ,ts)
    #Si no es la primera produccion quiere decir que es epsilon, por lo que no se realiza nada.

#<sentencia> ::=        leer(cadena, id) | escribir(texto, < expr_arit_c > < H > < N > ) | id = < expr_arit_c > < H > < N >
def evaluarSentencia(arbol, ts):
    if len(arbol.hijos)>=1 and  arbol.hijos[0].getDato()== s.LEER: #Si es leer
        #if len(arbol.hijos[2].hijos) == 1:
        print(arbol.hijos[2].hijos[0].getDato())                #muestra la cadena
        aux = input()                                           #lee en un auxiliar
        tsim.actualizarTS(ts,arbol.hijos[4].hijos[0].getDato(), aux) #asigna en la tabla de simbolos el valor leido al id
    elif len(arbol.hijos)>=1 and  arbol.hijos[0].getDato() == s.ESCRIBIR: #Si es escribir
        #if len(arbol.hijos[2].hijos) == 1:
        print(arbol.hijos[2].hijos[0].getDato())                #escribe el contenido del hijo del tercer hijo porque contiene la cadena (el texto)
        res = evaluarExprArit(arbol.hijos[4], ts)               #evalua expresion aritmetica (Q) en el 5to hijo
        res = evaluarH(arbol.hijos[5], ts, res)                 #evalua H con el 6to hijo y lo obtenido en Q
        res = evaluarN(arbol.hijos[6], ts, res)                 #evalua N con el 7mo hijo y lo obtenido en H
        print(res)
    else:                                                       #Si no, es una asignacion
        res = evaluarExprArit(arbol.hijos[2], ts)
        res = evaluarH(arbol.hijos[3], ts, res)
        res = evaluarN(arbol.hijos[4], ts, res)
        tsim.actualizarTS(ts,arbol.hijos[0].hijos[0].getDato(), str(res))   # al resultado se lo guarda en la tabla de simbolos

#< N >::=        + < expr_arit_c > < H > < N > | - < expr_arit_c > < H > < N > | ε

def evaluarN(arbol, ts, res):
    if len(arbol.hijos)>=1 and arbol.hijos[0].getDato() == s.mas:   #Si es una suma
        res1 = evaluarExprArit(arbol.hijos[1], ts)
        res2 = evaluarH(arbol.hijos[2], ts, res1)
        res = res + evaluarN(arbol.hijos[3], ts, res2)
    elif len(arbol.hijos)>=1 and  arbol.hijos[0].getDato() == s.menos:   #Si es una resta
        res1 = evaluarExprArit(arbol.hijos[1], ts)
        res2 = evaluarH(arbol.hijos[2], ts, res1)
        res = res - evaluarN(arbol.hijos[3], ts, res2)
    return res

#< H >::= * < expr_arit_c > < H > | / < expr_ar1it_c > < H > | ε

def evaluarH(arbol, ts, res: int):
    if len(arbol.hijos)>=1 and arbol.hijos[0].getDato() == s.por:
        res1 = evaluarExprArit(arbol.hijos[1], ts)
        res = res * evaluarH(arbol.hijos[2], ts, res1)
    elif len(arbol.hijos)>=1  and arbol.hijos[0].getDato() == s.dividido:
        res2 = evaluarExprArit(arbol.hijos[1], ts)
        res = res /evaluarH(arbol.hijos[2], ts, res2)
    return res

#< expr_arit_c >::=    id | const | ( < expr_arit_c > < H > < N >)
def evaluarExprArit(arbol, ts):
    if len(arbol.hijos)>=1 and arbol.hijos[0].getDato() == s.id:
        return float(tsim.devolverIdDato(ts, arbol.hijos[0].hijos[0].getDato()))
    elif len(arbol.hijos)>=1 and arbol.hijos[0].getDato() == s.real:
        return float(arbol.hijos[0].hijos[0].getDato())
    elif len(arbol.hijos)>=1 and arbol.hijos[0].getDato() == s.parentesisAbre:
        res = evaluarExprArit(arbol.hijos[1], ts)
        res = evaluarH(arbol.hijos[2], ts, res)
        res = evaluarN(arbol.hijos[3], ts, res)
        return res


archivoAEjecutar = input("Ingrese direccion del archivo a ejecutar: \n")
sint = p.AnalizadorSintactico(archivoAEjecutar) #crea el Analizador Sintactico
arb = sint.analizarSintactico() #Analiza sintacticamente obteniendo un arbol
evaluarS(arb,sint.tablaSimbolos)  #evalua la raiz con el arbol obtenido y la tabla de simbolos del Analizador Sintactico