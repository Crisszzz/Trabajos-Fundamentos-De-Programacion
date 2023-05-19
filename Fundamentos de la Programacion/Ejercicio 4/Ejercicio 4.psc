Proceso Hallar_tiempo
	//Descripcion: hallar la aceleracion de un formula 1//
	//Version:1.0//
	//Programador:Cristian Vargas//
	//ultima modificacion: 25/02/2023
	
	//area de conversion//
	definir v_final_kilHor como real;//variable de entrada que almacena la velocidad final//
	//inicializacion de conversion//
	v_final_kilHor=144
	//area de procesos//
	v_final_metseg= v_final_kilHor* 1000/3600
	//area de salida//
	Escribir " la conversion es:",v_final_metseg;
	//area de definir aceleracion//
	definir v_inicial_metseg como real//variable de entrada que almacena la velocidad inicial//
	definir v_aceleracion como real//variable de entrada que almacena la acelaracion//
	//proceso de hallar tiempo//
	v_inicial_metseg=12
	v_aceleracion=2
	//area de procesos//
	v_tiempo= (v_final_metseg-v_inicial_metseg)/v_aceleracion
	//area de salida de aceleracion//
	Escribir "el tiempo que tarda en adquirir esa velocidad es:",v_tiempo;
	
FinProceso