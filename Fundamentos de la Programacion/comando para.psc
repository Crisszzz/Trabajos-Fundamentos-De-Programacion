
Proceso condicional
	//enunciado: leer una cantidad de nuemeros
	//pedir por teclado cada numero
	//y calcular su promedio
	//desarrollado por: Cristian Vargas
	//version:1.0
	//fecha: 27/02/2023
	
	//declaracion de variables//
	definir v_canNum como entero;
	definir v_conCic como entero;
	definir v_num como entero;
	definir v_sumNum como entero;
	definir v_prom como real;
	//inicializacion de variables
	v_canNum=0;
	v_conCin=0;
	v_num=0;
	v_sumNum=0;
	v_prom=0.0;
	//entrada de datos
	escribir "digite cantidad de numeros a promediar:"
	leer v_canNum;
	Para v_conCic=1 Hasta v_canNum Con Paso 1 Hacer
		escribir "digite numero : ";
		leer v_num;
		v_sumNum=v_sumNum+v_num;
	Fin Para
	v_prom=v_sumNum/v_canNum
	escribir "el promedio de los numeros es :", v_prom;
FinProceso

