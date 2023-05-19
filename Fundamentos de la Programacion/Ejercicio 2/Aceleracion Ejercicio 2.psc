Proceso Hallar_aceleracion
	//Descripcion: hallar la aceleracion de un formula 1//
	//Version:1.0//
	//Programador:Cristian Vargas//
	//ultima modificacion: 25/02/2023
	
	//area de conversion//
	definir v_final_kilHor como real;//variable de entrada que almacena la velocidad final//
	definir c_facCon como real;//constante que almacena el factor de conversion de kilometros por hora a metros por segundo//
	//inicializacion de conversion//
	v_final_kilHor=216
	c_facCon=0.27
	//area de procesos//
	v_final_metseg= v_final_kilHor*c_facCon
	//area de salida//
	Escribir " la conversion es:",v_final_metseg;
	//area de definir aceleracion//
	definir v_inicial_metseg como real//variable de entrada que almacena la velocidad inicial//
	definir tiempo_s como real//variable de entrada que almacena el tiempo en el que se da la aceleracion//
	//proceso de hallar aceleracion//
	v_inicial_metseg=0
	tiempo_s=10
	//area de procesos//
	aceleracion= (v_final_metseg-v_inicial_metseg)/tiempo_s
	//area de salida de aceleracion//
	Escribir "la aceleracion es:",aceleracion;
	
FinProceso

