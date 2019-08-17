import Archivos as arc
import TabladeSimbolos as tsim
import string   #se utiliza para agrupar las letrar (minusculas y mayusculas) y agrupar digitos


######################################################################################################
#################################     TIPOS COMPONENTES LEXICOS     ##################################
######################################################################################################

igual = "igual"
mas = "mas"
menos = "menos"
por = "por"
dividido = "dividido"
puntoycoma= "puntoycoma"
coma = "coma"
punto = "punto"
parentesisAbre = "parentesisAbre"
parentesisCierra = "parentesisCierra"
cadena = "cadena"
LEER = "leer"
ESCRIBIR = "escribir"
real = "real"
id = "id"
ErrorLexico = "ErrorLexico"
Z = "Z"
A = "A"
epsilon = "epsilon"
Q = "Q"
H = "H"
N = "N"
peso = "peso"
S= "S"

Terminal = [ESCRIBIR, LEER, parentesisAbre, parentesisCierra, mas, menos, por, dividido, cadena, coma, puntoycoma, id, punto, real, igual, ErrorLexico, epsilon, peso]
Variables = [S, A, Q, Z, H, N]
######################################################################################################
###########################################     LEXICO     ###########################################
######################################################################################################



class Lexico():
    def __init__(self, archivo):   #se ejecuta solo al crear el Lexico (constructor)
        self.posNueva = 0 #guarda la posicion actual en la linea
        self.lineas = arc.leerLineas(archivo) #lee todas las lineas poniendo cada linea en un vector
        self.l = 0 #guarda la linea actual

    def siguienteComponenteLexico(self,ts): #devuelve componente lexico, y lexema
        compLexico = ErrorLexico
        linea = self.lineas[self.l]
        while self.l < len(self.lineas) and self.posNueva < len(self.lineas[self.l]) and self.lineas[self.l][self.posNueva] == " "  : #mientras sea espacio o salto de pagina avanza uno, sin salirse del rang
            self.posNueva += 1
        while self.l < (len(self.lineas)-1) and linea[self.posNueva] == "\n" : #avanza de linea cuando el control se encuentra en un salto de pagina
            self.l += 1
            linea = self.lineas[self.l]
            self.posNueva = 0

        if not (self.l < (len(self.lineas)-1))and not(self.posNueva < len(self.lineas[self.l]) ) :   #si el numero de linea es mayor y la posicion es mayor al tamaño de la linea devuelve peso
            vector= [peso, "$"]
            return vector

        lexema = esConstReal(linea, self.posNueva)
        if lexema != "":
            self.posNueva += len(lexema) #suma a la posicion el tamaño del lexema
            compLexico = real
        else:
            lexema = esESCRIBIR(linea, self.posNueva)
            if lexema != "":
                self.posNueva += len(lexema)
                compLexico = ESCRIBIR
                    #lexema = ESCRIBIR
            else:
                if simbolo(linea, self.posNueva):
                    compLexico = esSimbolo(linea, self.posNueva)
                    lexema = linea[self.posNueva]
                    self.posNueva += 1
                else:
                    lexema = esLEER(linea, self.posNueva)
                    if lexema != "":
                        self.posNueva += len(lexema)
                        compLexico= LEER
                            #lexema=LEER
                    else:
                        lexema = esID(linea, self.posNueva)
                        if lexema != "":
                            ts = tsim.actualizarTS(ts, lexema, "0")
                            self.posNueva += + len(lexema)
                            compLexico = id
                        else:
                            lexema = esCADENA(linea, self.posNueva)
                            if lexema != "":
                                self.posNueva += len(lexema)
                                compLexico = cadena
        vector = [compLexico, lexema]
        if compLexico == ErrorLexico:
            print("En la linea:", self.l," Posición:",self.posNueva, "se encuentra un error lexico.")
        return vector







######################################################################################################
#########################################      AUTOMATAS      ########################################
######################################################################################################


# devuelve true si es simbolo sino devuelve false
def simbolo (linea: str, posicion: int)-> bool:
    simb = False
    aux = arc.leerCaracter(linea,posicion)
    if aux in {'=', '+', '-', '*', '/', ';', ',', '.', '(', ')'}:
        simb = True
    return simb

# devuelve el tipo de componente lexico del simbolo
def esSimbolo (linea: str, posicion: int)-> str:
    aux = linea[posicion]
    if aux == '=':
        return igual
    elif aux == '+':
        return mas
    elif aux == '-':
        return menos
    elif aux == '*':
        return por
    elif aux == '/':
        return dividido
    elif aux == ";":
        return puntoycoma
    elif aux == ",":
        return coma
    elif aux == '.':
        return punto
    elif aux == "(":
        return parentesisAbre
    elif aux == ")":
        return parentesisCierra
    else:
        return ""


# se usa dentro de EsID para el automata
def simboloID(aux: str)-> int:
    if aux in string.ascii_letters:
        return 0
    elif aux in string.digits:
        return 1
    elif aux == "_":
        return 2
    else:
        return 3

# devuelve el id si es un id, sino devuelve cadena vacia
def esID (linea: str, posicion: int)-> str:
    q0 = 0
    F = {0, 1}
   # Q = (0,1,2)
   # sigma=[(letra, digito, guionBajo, otro)]   #letra = 0ra columna, digito = 1da columna, guionBajo = 2ra columna, otro= 3ta columna)
    delta = [None] * 3
    for i in range(3):
        delta[i] = [None] * 4
    delta[0][0] = 1
    delta[0][1] = 2
    delta[0][2] = 2
    delta[0][3] = 2
    delta[1][0] = 1
    delta[1][1] = 1
    delta[1][2] = 1
    delta[1][3] = 2
    delta[2][0] = 2
    delta[2][1] = 2
    delta[2][2] = 2
    delta[2][3] = 2
    lexema = ""
    auxControl = posicion
    T = arc.leerCaracter(linea, auxControl)
    estado = q0
    while (estado != 2) and auxControl < len(linea) and (T != " ") and (T != "\n") and not simbolo(linea, auxControl):
        estado = delta[estado][simboloID(T)]
        lexema = lexema + T
        auxControl = auxControl + 1
        T = arc.leerCaracter(linea, auxControl)
    if estado in F:
        return lexema
    else:
        return ""


# lo usa en sigma esConstReal para el automata
def simbCONS(Car: str)-> int:
    if Car in string.digits:
        return 0
    elif Car == '-':
        return 1
    elif Car == '.':
        return 2
    elif Car in ('e', 'E'):
        return 3
    else:
        return 4

#lo usa esConstReal (como simbolo pero sin el menos ni el punto)
def simbolo1(linea: str, posicion: int) -> bool:
    simb = False
    aux = arc.leerCaracter(linea, posicion)
    if aux in {'=', '+', '*', '/', ';', ',', '(', ')'}:
        simb = True
    return simb


# Automata para un numero real
def esConstReal(linea: str, pos: int)-> str:
  q0=0
  F={4, 2, 7}
  #Q=range(1,9)
  #sigma=(D, menos, punto, E, O)
  delta = [None] * 9
  for i in range(9):
      delta[i] = [None] * 5
  estado = q0
  auxControl = pos
  delta[0][0] = 2
  delta[0][1] = 1
  delta[0][2] = 8      # 8=muerto
  delta[0][3] = 8
  delta[0][4] = 8
  delta[1][0] = 2
  delta[1][1] = 8
  delta[1][2] = 8
  delta[1][3] = 8
  delta[1][4] = 8
  delta[2][0] = 2
  delta[2][1] = 8
  delta[2][2] = 3
  delta[2][3] = 5
  delta[2][4] = 8
  delta[3][0] = 4
  delta[3][1] = 8
  delta[3][2] = 8
  delta[3][3] = 8
  delta[3][4] = 8
  delta[4][0] = 4
  delta[4][1] = 8
  delta[4][2] = 8
  delta[4][3] = 5
  delta[4][4] = 8
  delta[5][0] = 7
  delta[5][1] = 6
  delta[5][2] = 8
  delta[5][3] = 8
  delta[5][4] = 8
  delta[6][0] = 7
  delta[6][1] = 8
  delta[6][2] = 8
  delta[6][3] = 8
  delta[6][4] = 8
  delta[7][0] = 7
  delta[7][1] = 8
  delta[7][2] = 8
  delta[7][3] = 8
  delta[7][4] = 8
  delta[8][0] = 8
  delta[8][1] = 8
  delta[8][2] = 8
  delta[8][3] = 8
  delta[8][4] = 8
  lexema = ""
  T = arc.leerCaracter(linea, auxControl)
  while estado != 8 and auxControl < len(linea) and T != " " and T != "\n" and (not simbolo1(linea, auxControl)):
      estado = delta[estado][simbCONS(T)]
      if estado != 8:
          lexema = lexema + T
          auxControl = auxControl+1
          T = arc.leerCaracter(linea, auxControl)
  if estado in F:
      return lexema
  else:
      return ""


def simbLEER(car: str)->int:
    if car in {"l","L"}:
        return 0
    elif car in {"E","e"}:
        return 1
    elif car in {"R","r"}:
        return 2
    else:
        return 3
#devuelve la palabra si es leer, sino devuelve cadena vacia
def esLEER(linea: str, posicion: str)-> str:
  q0 = 0
  F = {4}
  #Q=0..5
  #sigma=(L, E, R, O)
  delta = [None] * 6
  for i in range(6):
      delta[i] = [None] * 4
  delta[0][0] = 1
  delta[0][1] = 5
  delta[0][2] = 5
  delta[0][3] = 5
  delta[1][0] = 5
  delta[1][1] = 2
  delta[1][2] = 5
  delta[1][3] = 5
  delta[2][0] = 5
  delta[2][1] = 3
  delta[2][2] = 5
  delta[2][3] = 5
  delta[3][0] = 5
  delta[3][1] = 5
  delta[3][2] = 4
  delta[3][3] = 5
  delta[4][0] = 5
  delta[4][1] = 5
  delta[4][2] = 5
  delta[4][3] = 5
  auxControl = posicion
  estado = q0
  lexema = ""
  T = arc.leerCaracter(linea, auxControl)
  while estado != 5 and auxControl < len(linea) and T != " " and T != "\n" and not simbolo(linea, auxControl):
      estado = delta[estado][simbLEER(T)]
      if estado!= 5:
        lexema = lexema+T
        auxControl = auxControl + 1
        T = arc.leerCaracter(linea, auxControl)
  if estado in F:
        return lexema
  else:
        return ""


def simbESCRI(car: str) -> int:
    if car in {'E', 'e'}:
        return 0
    elif car in {'S', 's'}:
        return 1
    elif car in {'C', 'c'}:
        return 2
    elif car in {'R', 'r'}:
        return 3
    elif car in {'I', 'i'}:
        return 4
    elif car in {'B', 'b'}:
        return 5
    else:
        return 6
#devuelve la palabra si es escribir, sino devuelve cadena vacia
def esESCRIBIR(linea: str, pos: int)->int:
    q0=0
    F={8}
    #Q=0..9;
    # #sigma=(E, S, C, R, I, B ,O) 0 para E, 1 para S, 2 para C...
    #delta = np.empty((10, 7))
    delta = [None] *10
    for i in range(10):
        delta[i] = [None] * 7
    delta[0][0]=1
    delta[0][1]=9
    delta[0][2]=9
    delta[0][3]=9
    delta[0][4]=9
    delta[0][5]=9
    delta[0][6]=9
    delta[1][0]=9
    delta[1][1]=2
    delta[1][2]=9
    delta[1][3]=9
    delta[1][4]=9
    delta[1][5]=9
    delta[1][6]=9
    delta[2][0]=9
    delta[2][1]=9
    delta[2][2]=3
    delta[2][3]=9
    delta[2][4]=9
    delta[2][5]=9
    delta[2][6]=9
    delta[3][0]=9
    delta[3][1]=9
    delta[3][2]=9
    delta[3][3]=4
    delta[3][4]=9
    delta[3][5]=9
    delta[3][6]=9
    delta[4][0]=9
    delta[4][1]=9
    delta[4][2]=9
    delta[4][3]=9
    delta[4][4]=5
    delta[4][5]=9
    delta[4][6]=9
    delta[5][0]=9
    delta[5][1]=9
    delta[5][2]=9
    delta[5][3]=9
    delta[5][4]=9
    delta[5][5]=6
    delta[5][6]=9
    delta[6][0]=9
    delta[6][1]=9
    delta[6][2]=9
    delta[6][3]=9
    delta[6][4]=7
    delta[6][5]=9
    delta[6][6]=9
    delta[7][0]=9
    delta[7][1]=9
    delta[7][2]=9
    delta[7][3]=8
    delta[7][4]=9
    delta[7][5]=9
    delta[7][6]=9
    delta[8][0]=9
    delta[8][1]=9
    delta[8][2]=9
    delta[8][3]=9
    delta[8][4]=9
    delta[8][5]=9
    delta[8][6]=9
    delta[9][0]=9
    delta[9][1]=9
    delta[9][2]=9
    delta[9][3]=9
    delta[9][4]=9
    delta[9][5]=9
    delta[9][6]=9
    auxControl = pos
    estado = q0
    lexema=""
    T = arc.leerCaracter(linea, pos)
    while estado != 9 and auxControl < len(linea) and T!= " " and T != "\n" and not simbolo(linea, auxControl):
        estado = delta[estado][simbESCRI(T)]
        if estado != 9:
            lexema = lexema+T
            auxControl = auxControl + 1
            T = arc.leerCaracter(linea, auxControl)
    if estado in F:
        posicion = auxControl
        return lexema
    else:
        return ""
    #automatas para palabras reservadas??


def simbCAD(car: str)-> int:
  if car == "'":
      return 0
  else:
      return 1

#devuelve la cadena si es cadena, si no devuelve ""
def esCADENA(linea: str, pos: int)-> str:
    q0 = 0
    F = [2]
    #Q=0..3
    # #sigma=(C,O);
    delta = [None] * 4
    for i in range(4):
        delta[i] = [None] * 2
    delta[0][0] =1
    delta[0][1] =3
    delta[1][0] =2
    delta[1][1] =1
    delta[2][0] =3
    delta[2][1] =3
    delta[3][0] =3
    delta[3][1] =3
    auxControl = pos
    estado = q0
    lexema = ''
    T = arc.leerCaracter(linea, auxControl)
    while estado != 3  and auxControl < len(linea)  and T!="\n" and (estado not in F) :
        estado= delta[estado][simbCAD(T)]
        if estado!=3:
            lexema = lexema + T
            auxControl = auxControl+1
            T = arc.leerCaracter(linea, auxControl)
    if estado in F:
        pos = auxControl
        return lexema
    else:
        return ""



#######################################################TESTING#######################################################
"""
archivo=open(r"prueba.txt")
lex=Lexico(archivo)

a = lex.siguienteComponenteLexico()
print(a)
a = lex.siguienteComponenteLexico()
print(a)
a = lex.siguienteComponenteLexico()
print(a)
a = lex.siguienteComponenteLexico()
print(a)
a = lex.siguienteComponenteLexico()
print(a)
a = lex.siguienteComponenteLexico()
print(a)
a = lex.siguienteComponenteLexico()
print(a)
a = lex.siguienteComponenteLexico()
print(a)
a = lex.siguienteComponenteLexico()
print(a)
a = lex.siguienteComponenteLexico()
print(a)
a = lex.siguienteComponenteLexico()
print(a)
a = lex.siguienteComponenteLexico()
print(a)
a = lex.siguienteComponenteLexico()
print(a)
a = lex.siguienteComponenteLexico()
print(a)
a = lex.siguienteComponenteLexico()
print(a)
"""