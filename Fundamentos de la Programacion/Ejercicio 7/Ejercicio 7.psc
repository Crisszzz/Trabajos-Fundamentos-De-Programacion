Algoritmo Ejercicio_7
	//Descripcion: Calcular el salario de un trabajador
	//Version:1.0
	//Desarrollado: Cristian Vargas
	//Fecha: 02/03/200¿23
	
	//Definicion de variables
	Definir Nombre Como Caracter
	Definir Numero_Horas,Valor_Hora,Salario_Base,Salario_Fin Como Entero
	Definir Salario_Tasas Como Real
	
	//Declaracion de variables
	Nombre=""
	Numero_Horas=h
	Valor_Hora=n
	Tasas=0.25
	
	//Entradas y Procesos
	Escribir "Digite Nombre de Usuario: "
	Leer Nombre
	Escribir "El numro de horas trabajadas fue de: "
	Leer Numero_Horas
	Escribir "El Valor por las horas trabajadas fue de: "
	Leer Valor_Hora
	Salario_Base=(Valor_Hora*Numero_Horas)
	Escribir "El Salario Base es de: ", Salario_Base
	Salario_Tasas=(Salario_Base*Tasas)
	Escribir "El salario con la aplicacion de Tasas de Interes es de: ", Salario_Tasas
	Salario_Fin=(Salario_Base-Salario_Tasas)
	
	//Salidas
	Escribir Nombre " Su Salario Final fue de: ", Salario_Fin
	
FinAlgoritmo

	
	

