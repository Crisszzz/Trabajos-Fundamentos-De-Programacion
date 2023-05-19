Proceso sintitulo 
	Definir v_nomb Como Caracter
	//descripcion: saber si el estudiante aprueba o desaprueba la materia, viendose afectado tambien por el numero de inasistencias
	//programador: Cristian Vargas
	//Version:1.0
	//fecha:28/02/2023
	
	definir v_nomb_est Como Caracter
	definir v_parcial_1 como real;
	definir v_parcial_2 como real;
	definir v_parcial_3 como real;
	definir v_prom_1 como real;
	definir v_prom_2 como real;
	definir v_prom_3 como real;
	definir v_num_inasis como entero;
	//inicializacion de variables
	v_nomb_est=""
	v_parcial_1=0.0
	v_parcial_2=0.0
	v_parcial_3=0.0
	v_prom_1=0.25
	v_prom_2=0.35
	v_prom_3=0.40
	v_num_inasis=0
	Escribir "Materia: Matematicas";
	Escribir "Nombre del estudiante";
	Leer v_nomb_est;
	Escribir "Digite el numero de inasistencias que tuvo";
	leer v_num_inasis;
	Escribir "Digine nota del parcial 1";
	Leer v_parcial_1;
	Escribir "Digine nota del parcial 2";
	Leer v_parcial_2;
	Escribir "Digine nota del parcial 3";
	Leer v_parcial_3;
	//area de procesos
	v_prom_p1= v_parcial_1*v_prom_1;
	v_prom_p2= v_parcial_2*v_prom_2;
	v_prom_p3= v_parcial_3*v_prom_3;
	
	v_prom_final= v_prom_p1+v_prom_p2+v_prom_p3;
	
	Escribir "Su promedio Final fue de:", v_prom_final;
	
	Si v_prom_final>3.5 y v_num_inasis<12 Entonces
		Escribir "El estudiante Aprobo la materia";
	SiNo
		si v_prom_final>3.5 y v_num_inasis>=12 Entonces
			Escribir "El estudiante Reprobo la materia por multiples inasistencias";
			Sino
			Si v_prom_final<3.5 Entonces
				Escribir "El estudiante reprobo la materia por bajo prodemio";
				
			SiNo
			
			Fin Si
		Fin Si
	Fin Si

FinProceso
