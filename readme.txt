##############################################################################
######################## Intérprete Última Hora (IUH) ########################
##############################################################################

Ayuda y Documentación para el Lenguaje de Programación de Última Hora (LPUH).



#########################    Instalación y uso    #########################

El Intérprete de Última Hora es el intérprete oficial del Lenguaje de Programación de Última Hora. No requiere instalación, puesto que es distribuido en formato portable (standalone) y tiene un uso sencillo.

Una vez llamado, IUH comenzará y continuará la ejecución del programa LPUH hasta finalizar el archivo fuente, terminando el proceso de ejecución.

Funciona llamándolo desde la consola con la dirección completa de donde se encuentra Ejecutador, donde al ejecutarse solicita la dirección del archivo de texto con el código a interpretar.


#########################  Conceptos fundamentales  #########################

Cada línea en LPUH debe finalizar con ; si le sigue una nueva línea.

El intérprete reconoce tanto leer como LeEr, etc. sucede lo mismo con escribir.

Las cadenas se comienzan y terminan con comilla simple.


#########################       Asignaciones       #########################

LPUH permite la asignación de variables con la forma:
	id = constante | identificador | expresión aritmética
Ejemplos:
	pi = 3.14;
	suma = (1 + 2) * 3;
	expresion_aritmetica = (1 + 2) / 3;
	elevado = 5E-2

#########################  Operaciones aritméticas  #########################

Se permite suma, resta, producto o cociente de variables y constantes, permitiendo paréntesis.

Se respetan las prioridades usuales de los operadores (primero lo que esté dentro de paréntesis, seguido de cocientes y productos, y por último sumas y restas).


###################### Escribir una cadena en pantalla ######################

Para imprimir en pantalla se hace uso de la instrucción escribir(), que permite la salida de una cadena y el contenido de un identificador provisto.
	escribir(cadena, identificador)
Ejemplos:
	escribir(‘Su nombre es: ’, nombre);

#########################     Leer una cadena     #########################

En LPUH la lectura se realiza mediante la instrucción leer(), la cual imprime en pantalla una cadena provista en su primer argumento y guarda en el identificador dado como segundo argumento el texto ingresado por el usuario. Su sintaxis es la siguiente:
	leer(cadena, identificador)
Ejemplos:
	leer(‘Ingrese su nombre: ’, nombre);



#########################         Autores         #########################


	GASTAL, Valeria Noemi Elisa
	
	LEIVA, Maria Ayelen
	
	MIRET, Giuliana Dariela
	
	PASTORINI, Sandro Leon


#########################           2015          #########################		