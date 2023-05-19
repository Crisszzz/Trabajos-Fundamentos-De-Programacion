Algoritmo CalcularMedia
	//Descripcion: Calcular la media de una serie de n�meros positivos
	//Programador: Cristian Vargas
	//Version: 1.0
	//Fecha: 03/03/2023
	// Declaraci�n de variables
	Definir num Como Entero
	Definir suma Como Real
	Definir contador Como Entero
	Definir media Como Real
	
	// Inicializaci�n de variables
	suma <- 0
	contador <- 0
	
	// Lectura de n�meros y c�lculo de la suma y el contador
	Escribir "Introduce una serie de n�meros positivos (introduce 0 para terminar):"
	Leer num
	Mientras num <> 0 Hacer
		Si num > 0 Entonces
			suma <- suma + num
			contador <- contador + 1
		FinSi
		Leer num
	FinMientras
	
	// C�lculo de la media
	Si contador > 0 Entonces
		media <- suma / contador
		Escribir "La media de la serie de n�meros positivos es:", media
	Sino
		Escribir "No se introdujo ning�n n�mero positivo."
	FinSi
FinAlgoritmo
