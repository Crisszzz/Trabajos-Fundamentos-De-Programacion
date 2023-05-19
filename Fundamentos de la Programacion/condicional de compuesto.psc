
	Proceso condicional
		//Leer 2 numeros e imprimir cual es el mayor de ellos//
		//Programador: Cristian Vargas//
		//Fecha: 27/02/2023//
		//Version:1.0//
		
		//Area de definicion de variables//
		Definir v_numUno como entero;
		Definir v_numDos como entero;
		Definir v_numMay como entero;
		
		//Inicializar variables//
		v_numUno<-0;
		v_numDos<-0;
		v_numMay<-0;
		
		//Entradas//
		Escribir "Digite el numero 1";
		Leer v_numUno;
		Escribir "Digite el numero 2";
		Leer v_numDos;
		
		//Procesos//
		Si v_numUno=v_numDos Entonces
			Escribir " No hay numero mayor, los dos son iguales";
		SiNo
			Si v_numUno>v_numDos Entonces
				v_numMay= v_numUno;
			SiNo
				v_numMay=v_numDos;
			Fin Si
			Escribir "El numero mayor es:", v_numMay;
		Fin Si
		
FinProceso

