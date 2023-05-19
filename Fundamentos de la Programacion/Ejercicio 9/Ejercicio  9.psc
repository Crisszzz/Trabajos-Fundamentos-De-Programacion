Algoritmo Sintitulo
	//Descripcion: Suma de los números pares comprendidos entre 2 y 100
	//Programador: Cristian Vargas
	//Version: 1.0
	//Fecha: 03/23/2023

	// Declaración de variables
	Definir num Como Entero
	Definir suma Como Entero
	
	// Inicialización de variables
	suma <- 0
	
	// Cálculo de la suma de los pares entre 2 y 100
	Para num <- 2 Hasta 100 Con Paso 2 Hacer
		suma <- suma + num
	FinPara
	
	// Mostrar resultado por pantalla
	Escribir "La suma de los números pares entre 2 y 100 es:", suma
FinAlgoritmo
