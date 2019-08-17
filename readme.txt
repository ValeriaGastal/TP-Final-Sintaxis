##############################################################################
######################## Int�rprete �ltima Hora (IUH) ########################
##############################################################################

Ayuda y Documentaci�n para el Lenguaje de Programaci�n de �ltima Hora (LPUH).



#########################    Instalaci�n y uso    #########################

El Int�rprete de �ltima Hora es el int�rprete oficial del Lenguaje de Programaci�n de �ltima Hora. No requiere instalaci�n, puesto que es distribuido en formato portable (standalone) y tiene un uso sencillo.

Una vez llamado, IUH comenzar� y continuar� la ejecuci�n del programa LPUH hasta finalizar el archivo fuente, terminando el proceso de ejecuci�n.

Funciona llam�ndolo desde la consola con la direcci�n completa de donde se encuentra Ejecutador, donde al ejecutarse solicita la direcci�n del archivo de texto con el c�digo a interpretar.


#########################  Conceptos fundamentales  #########################

Cada l�nea en LPUH debe finalizar con ; si le sigue una nueva l�nea.

El int�rprete reconoce tanto leer como LeEr, etc. sucede lo mismo con escribir.

Las cadenas se comienzan y terminan con comilla simple.


#########################       Asignaciones       #########################

LPUH permite la asignaci�n de variables con la forma:
	id = constante | identificador | expresi�n aritm�tica
Ejemplos:
	pi = 3.14;
	suma = (1 + 2) * 3;
	expresion_aritmetica = (1 + 2) / 3;
	elevado = 5E-2

#########################  Operaciones aritm�ticas  #########################

Se permite suma, resta, producto o cociente de variables y constantes, permitiendo par�ntesis.

Se respetan las prioridades usuales de los operadores (primero lo que est� dentro de par�ntesis, seguido de cocientes y productos, y por �ltimo sumas y restas).


###################### Escribir una cadena en pantalla ######################

Para imprimir en pantalla se hace uso de la instrucci�n escribir(), que permite la salida de una cadena y el contenido de un identificador provisto.
	escribir(cadena, identificador)
Ejemplos:
	escribir(�Su nombre es: �, nombre);

#########################     Leer una cadena     #########################

En LPUH la lectura se realiza mediante la instrucci�n leer(), la cual imprime en pantalla una cadena provista en su primer argumento y guarda en el identificador dado como segundo argumento el texto ingresado por el usuario. Su sintaxis es la siguiente:
	leer(cadena, identificador)
Ejemplos:
	leer(�Ingrese su nombre: �, nombre);



#########################         Autores         #########################


	GASTAL, Valeria Noemi Elisa
	
	LEIVA, Maria Ayelen
	
	MIRET, Giuliana Dariela
	
	PASTORINI, Sandro Leon


#########################           2015          #########################		