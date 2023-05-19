Algoritmo sin_titulo
	//area de documentacion//
	//enunciado: leer velocidad en metros sobre segundo y convertirlas a kilometros sobre hora//
	//Version:1.0//
	//Programador: Cristian Vargas//
	//Version: 1.0//
	
	//area de definicion de variables//
	definir v_metSeg como real;//variable de entrada que almacena los metros sobre segundo//
	definir v_kiLHor como real; //variable de salida que almacena los kilometros por hora//
	definir c_facCon como real;//constante que almacena el factor de conversion de metros sobre segundos a kilometros sobre hora//
	//inicializacion de variables//
	v_metSeg=0.0
	v_kiLHor=0.0
	c_facCon=3.6
	Escribir " digito metro sobre segundo:"; leer v_metSeg;
	//area de procesos//
	v_kiLHor = v_metSeg*c_facCon
	//area de salida//
	Escribir "la conversion es: ",v_kiLHor;
	
	
	
FinAlgoritmo
