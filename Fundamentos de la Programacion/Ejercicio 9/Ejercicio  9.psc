Algoritmo Sintitulo
	//Descripcion: Suma de los n�meros pares comprendidos entre 2 y 100
	//Programador: Cristian Vargas
	//Version: 1.0
	//Fecha: 03/23/2023

	// Declaraci�n de variables
	Definir num Como Entero
	Definir suma Como Entero
	
	// Inicializaci�n de variables
	suma <- 0
	
	// C�lculo de la suma de los pares entre 2 y 100
	Para num <- 2 Hasta 100 Con Paso 2 Hacer
		suma <- suma + num
	FinPara
	
	// Mostrar resultado por pantalla
	Escribir "La suma de los n�meros pares entre 2 y 100 es:", suma
FinAlgoritmo
