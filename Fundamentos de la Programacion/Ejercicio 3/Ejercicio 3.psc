Proceso titulo
	//Descripcion: hallar la acecleracion y distancia recorrida de una locomotora
	//programador: Cristian Vargas
	//fecha:27/02/2023
	//version:1.0
	
	//area de definicion de variables
	definir v_velInicial_metSeg Como Entero;
	definir v_velFinal_metSeg como entero;
	definir v_tiempo_Seg como entero;
	definir v_aceleracion como real;
	definir v_distancia_met como real;
	//inicializacion de variables
	v_velInicial_metSeg=0;
	v_velFinal_metSeg=25;
	v_tiempo_Seg=10;
	v_aceleracion=0.0;
	v_distancia_met=0.0;
	//area de procesos
	v_aceleracion= (v_velFinal_metSeg-v_velInicial_metSeg)/v_tiempo_Seg
	v_distancia_met= v_velInicial_metSeg*v_tiempo_Seg+ (1/2)*v_aceleracion*v_tiempo_Seg^2
	//area de salida de aceleracion
	Escribir "La aceleracion de la locomotora es de:",v_aceleracion;
	Escribir "La distancia que recorrio fue de:",v_distancia_met;
	
	
	
	
	
FinProceso

