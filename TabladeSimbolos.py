#######################################################################################################
#########################################  TABLA DE SIMBOLOS  #########################################
#######################################################################################################
def crearTS():  #crea la tabla de simbolo que es un diccionario
    ts = {}
    return ts

def devolverIdDato(ts, id: str): #devuelve el valor del correspondiente id en la diccionario si se encuentra
    if ts.get(id)!= None:
        return ts[id]

def actualizarTS(ts, id: str, res: str):  #modifica el valor del id en la tabla de simbolo, si no se encuentra lo crea
    ts[id] = res
    return ts
