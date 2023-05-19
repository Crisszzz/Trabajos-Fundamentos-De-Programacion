Algoritmo Ejercicio10
	// Área de documentación
	// Enunciado: calcular el salario de un empleado
	// Versión: 1.0
	// Desarrollado por: Cristian Vargas
	// Fecha: 03/03/23
	
	// Área de definición de variables
	Definir v_nombre Como Cadena;
	Definir v_horas_semanales Como Entero;
    Definir v_precio_hora Como Real;
    Definir v_salario_mensual Como Real;
	
	// Inicialización de variables
	v_horas_semanales = 0;
    v_precio_hora = 0.0;
    v_salario_mensual = 0.0;
	
	// Área de entradas
	Escribir "Ingrese el nombre del trabajador: ";
	Leer v_nombre;
	
	Escribir "Ingrese las horas semanales trabajadas: ";
    Leer v_horas_semanales;
	
	Escribir "Ingrese el precio por hora: ";
    Leer v_precio_hora;
	
	// Área de procesos
	Si v_horas_semanales > 40 Entonces
        v_salario_mensual = 40 * v_precio_hora + (v_horas_semanales - 40) * v_precio_hora * 1.5
    Sino
        v_salario_mensual = v_horas_semanales * v_precio_hora
    Fin Si
	
	// Área de salidas
	Escribir "El salario mensual de ", v_nombre " es de: ", v_salario_mensual
FinAlgoritmo
