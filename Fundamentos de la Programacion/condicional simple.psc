
Proceso condicional
	//Leer 2 numeros e imprimir cual es el mayor de ellos//
	//Programador: Cristian Vargas//
	//Fecha: 27/02/2023//
	//Version:1.0//
	
	//Area de definicion de variables//
	Definir v_numUno como entero;
	Definir v_numDos como entero;
	
	//Inicializar variables//
	v_numUno<-0.0;
	v_numDos<-0.0;
	
	//Entradas//
	Escribir "Digite el numero 1";
	Leer v_numUno;
	Escribir "Digite el numero 2";
	Leer v_numDos;
	
	//Procesos//
	si (v_numUno>v_numDos) Entonces
		escribir "El mayor es:", v_numUno;
		finsi
		si (v_numDos>v_numUno) entonces
			escribir " El mayor es:", v_numDos
		FinSi
		si (v_numUno=v_numDos) Entonces
			escribir " No hay mayor, los numeros son iguales";
		FinSi
FinProceso

	

