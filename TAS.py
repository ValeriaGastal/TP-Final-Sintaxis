import scanner as s

igual = s.igual
mas = s.mas
menos = s.menos
por = s.por
dividido = s.dividido
puntoycoma= s.puntoycoma
coma = s.coma
punto = s.punto
parentesisAbre = s.parentesisAbre
parentesisCierra = s.parentesisCierra
cadena = s.cadena
LEER = s.LEER
ESCRIBIR = s.ESCRIBIR
real = s.real
id = s.id
ErrorLexico = s.ErrorLexico
Z = s.Z
A = s.A
epsilon = s.epsilon
Q = s.Q
H = s.H
N = s.N
peso = s.peso
S= s.S


######################################################################################################
###########################################       TAS       ##########################################
######################################################################################################

cTAS = [None] * 6
for i in range(6):
    cTAS[i] = [None] * 12
cTAS[0][0] =[Z, A]
cTAS[0][1] = [Z, A]
cTAS[0][2] = []
cTAS[0][3] = []
cTAS[0][4] = []
cTAS[0][5] = []
cTAS[0][6] = []
cTAS[0][7] = []
cTAS[0][8] = []
cTAS[0][9] = [Z, A]
cTAS[0][10] = []
cTAS[0][11] = []
cTAS[1][0] = []
cTAS[1][1] = []
cTAS[1][2] = [puntoycoma, Z, A]
cTAS[1][3] = []
cTAS[1][4] = []
cTAS[1][5] = []
cTAS[1][6] = []
cTAS[1][7] = []
cTAS[1][8] = []
cTAS[1][9] = []
cTAS[1][10] = []
cTAS[1][11] = [epsilon]  #no sale este epsilon
cTAS[2][0] = [LEER, parentesisAbre, cadena, coma, id, parentesisCierra]
cTAS[2][1] = [ESCRIBIR, parentesisAbre, cadena, coma, Q, H, N, parentesisCierra]
cTAS[2][2] = []
cTAS[2][3] = []
cTAS[2][4] = []
cTAS[2][5] = []
cTAS[2][6] = []
cTAS[2][7] = []
cTAS[2][8] = []
cTAS[2][9] = [id, igual, Q, H, N]
cTAS[2][10] = []
cTAS[2][11] = []
cTAS[3][0] = []
cTAS[3][1] = []
cTAS[3][2] = [epsilon]
cTAS[3][3] = []
cTAS[3][4] = [epsilon]
cTAS[3][5] = [mas, Q, H, N]
cTAS[3][6] = [menos, Q, H, N]
cTAS[3][7] = []
cTAS[3][8] = []
cTAS[3][9] = []
cTAS[3][10] = []
cTAS[3][11] = [epsilon]
cTAS[4][0] = []
cTAS[4][1] = []
cTAS[4][2] = [epsilon]
cTAS[4][3] = []
cTAS[4][4] = [epsilon]
cTAS[4][5] = [epsilon]
cTAS[4][6] = [epsilon]
cTAS[4][7] = [por, Q, H]
cTAS[4][8] = [dividido, Q, H]
cTAS[4][9] = []
cTAS[4][10] = []
cTAS[4][11] = [epsilon]
cTAS[5][0] = []
cTAS[5][1] = []
cTAS[5][2] = []
cTAS[5][3] = [parentesisAbre, Q, H, N, parentesisCierra]
cTAS[5][4] = []
cTAS[5][5] = []
cTAS[5][6] = []
cTAS[5][7] = []
cTAS[5][8] = []
cTAS[5][9] = [id]
cTAS[5][10] = [real]
cTAS[5][11] = []


def tVecTASVacio(x): #controla si el vector que devuelve la tas esta vacio
    if x != []:
        return False
    else:
        return True

def tas(produccion, simbolo): # devuelve el vector que se encuentra en la posicion de la tas, produccion son variables y simbolo son tipos de componentes lexicos
  i = 0
  j = 0
  if simbolo == LEER:
      j = 0
  elif simbolo == ESCRIBIR:
      j = 1
  elif simbolo == puntoycoma:
      j = 2
  elif simbolo == parentesisAbre:
      j = 3
  elif simbolo == parentesisCierra:
      j = 4
  elif simbolo == mas:
      j = 5
  elif simbolo == menos:
      j = 6
  elif simbolo == por:
      j = 7
  elif simbolo == dividido:
      j = 8
  elif simbolo == id:
      j = 9
  elif simbolo == real:
      j = 10
  elif simbolo == peso:
      j = 11
  if produccion == S:
      i = 0
  elif produccion == A:
      i = 1
  elif produccion == Z:
      i = 2
  elif produccion == N:
      i = 3
  elif produccion == H:
      i = 4
  elif produccion == Q:
      i = 5
  resul = cTAS[i][j]
  return resul

#######