Proceso Hallar_aceleracion
	//Descripcion: hallar la aceleracion de un camion//
	//Version:1.0//
	//Programador:Cristian Vargas//
	//ultima modificacion: 25/02/2023
	
	//area de definicion de variables//
	definir v_inicial_metseg como real;//variable de entrada que almacena la velocidad inicial//
	definir v_final_metseg como real;//variable de entrada que almacena la velocidad final//
	definir tiempo_s como real;//variable de entrada que almacena el tiempo en el que se da la aceleracion//
	//inicializacion de variables//
	v_inicial_metseg=20
	v_final_metseg=25
	tiempo_s=5
	//Area de procesos//
	aceleracion_metseg= (v_final_metseg-v_inicial_metseg)/tiempo_s
	
	//area de salida//
	escribir "la aceleracion es: ", aceleracion_metseg;
	
FinProceso
