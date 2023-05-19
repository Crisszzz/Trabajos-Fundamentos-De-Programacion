Algoritmo CalcularMedia
	//Descripcion: Calcular la media de una serie de números positivos
	//Programador: Cristian Vargas
	//Version: 1.0
	//Fecha: 03/03/2023
	// Declaración de variables
	Definir num Como Entero
	Definir suma Como Real
	Definir contador Como Entero
	Definir media Como Real
	
	// Inicialización de variables
	suma <- 0
	contador <- 0
	
	// Lectura de números y cálculo de la suma y el contador
	Escribir "Introduce una serie de números positivos (introduce 0 para terminar):"
	Leer num
	Mientras num <> 0 Hacer
		Si num > 0 Entonces
			suma <- suma + num
			contador <- contador + 1
		FinSi
		Leer num
	FinMientras
	
	// Cálculo de la media
	Si contador > 0 Entonces
		media <- suma / contador
		Escribir "La media de la serie de números positivos es:", media
	Sino
		Escribir "No se introdujo ningún número positivo."
	FinSi
FinAlgoritmo
