######################################################################################################
#########################################      ARCHIVOS      #########################################
######################################################################################################
def cerrarArchivo(archivo):
    archivo.close()


def leerCaracter(linea: str, pos: int)-> str:
    if pos < len(linea):
        return linea[pos]
    else:
        return ""       # si fin de pagina devuelve " "


def leerLineas(archivo):
    return archivo.readlines()


def abrirArchivo(archivo):
    open(archivo)