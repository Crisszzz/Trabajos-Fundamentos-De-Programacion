Algoritmo sintitulo
	//Descripcion: Producto de numeros naturales
	//Programador: Cristian Vargas
	//Version: 1.0
	//Fecha: 03/23/2023
    Escribir "Ingrese un n�mero entero positivo n: "
    Leer n
    Si n <= 0 Entonces
        Escribir "Error: n debe ser un n�mero entero positivo"
    Sino
        producto <- 1
        Para i <- 1 Hasta n Con Paso 1 Hacer
            producto <- producto * i
        FinPara
        Escribir "El producto de los primeros ", n, " n�meros naturales es: ", producto
    FinSi
FinAlgoritmo
